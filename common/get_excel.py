'''
支持pytest excel数据驱动。
'''
import pytest
from xlrd import open_workbook


# 把excel sheet解析为双层列表，每一个行是一个外层元素，每个单元格是一个内层元素。
def sheet_to_list(excel_file_path, sheet_name):
    lst = []
    with open_workbook(excel_file_path) as f:
        table = f.sheet_by_name(sheet_name)
        # nrows是sheet的行数
        for row in range(0, table.nrows):
            lst.append([])
            # ncols是sheet的列数
            for col in range(0, table.ncols):
                # ctype为1是字符串，ctype为2是数值。
                cell_type = table.cell(row, col).ctype
                cell_value = table.cell_value(row, col)
                # 去掉字符串首尾空格。excel会自动去掉整数和浮点数前后的空格。
                if cell_type == 1:
                    lst[row].append(cell_value.strip())
                # xlrd读取cell时1变成1.0。如果是数值，并且原本是整数，则返回整数。
                elif cell_type == 2 and cell_value == round(cell_value):
                    lst[row].append(int(cell_value))
                # 浮点数则不用额外处理
                else:
                    lst[row].append(cell_value)
    return lst


# 从excel sheet中获取@pytest.mark.parametrize()所需要的参数名和数据
def get_data_from_sheet(excel_file_path, sheet_name):
    lst = sheet_to_list(excel_file_path, sheet_name)
    # 参数名格式化，格式为"a,b,c"
    param_name = ','.join(lst[0])
    # 去掉参数名行，剩下的就是数据
    data = lst[1:]
    return param_name, data


# 使用举例：
@pytest.mark.parametrize(*get_data_from_sheet("../data/test_data.xlsx", "add_test"))
def test_add(a, b, c):
    assert a + b == c

@pytest.mark.parametrize("a,b,c",[[1,2,3],[3,4,7]])
def test_add(a,b,c):
    assert a+b==c

if __name__ == '__main__':

    pytest.main(["-s", "get_excel.py"])


'''
运行结果如下：
>pytest pytest_ddt_excel.py -v
============================= test session starts =============================
collected 4 items
pytest_ddt_excel.py::test_add[1-2-3] PASSED                              [ 25%]
pytest_ddt_excel.py::test_add[abc-def-abcdef] PASSED                     [ 50%]
pytest_ddt_excel.py::test_add[abc-123-abc123] PASSED                     [ 75%]
pytest_ddt_excel.py::test_add[1.8-2.6-4.4] PASSED                        [100%]
========================== 4 passed in 0.11 seconds ===========================
'''

'''
执行时，将分别使用上面两组数据，执行两个test。

实际中我们经常使用excel文件来提供数据。所以实现excel数据驱动。

实现思路：

将读取出的excel文件中的标题行中各个单元格使用逗号连接成一个字符串，数据以双重列表的方式返回，作为@pytest.mark.parametrize()的参数即可。

我实现一个函数，get_data_from_sheet(excel_file_path,sheet_name)。以字符串形式返回标题栏，同时以双重列表的方式返回data。
@pytest.mark.parametrize (*get_data_from_sheet(excel_file_path,sheet_name))使用数据。具体代码和使用举例如下：

原文链接：https://blog.csdn.net/jxzdsw/article/details/106277538
'''