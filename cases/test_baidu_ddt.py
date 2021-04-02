import codecs
import json
import os
import time
import pytest
import yaml


def test_read_data_from_json_yaml(data_file):
    return_value = []

    data_file_path = os.path.abspath(data_file)

    print(data_file_path)

    _is_yaml_file = data_file_path.endswith((".yml", ".yaml"))

    with codecs.open(data_file_path, 'r', 'utf-8') as f:

        # 从YAML或JSON文件中加载数据

        if _is_yaml_file:

            data = yaml.safe_load(f)

        else:

            data = json.load(f)

    for i, elem in enumerate(data):

        if isinstance(data, dict):

            key, value = elem, data[elem]

            if isinstance(value, dict):

                case_data = []

                for v in value.values():
                    case_data.append(v)

                return_value.append(tuple(case_data))

            else:

                return_value.append((value,))

    return return_value


@pytest.mark.baidu
class TestBaidu:

    @pytest.mark.parametrize('search_string, expect_string',
                             test_read_data_from_json_yaml('tests_pytest_ddt/test_baidu_ddt.yaml'))
    def test_baidu_search(self, login, search_string, expect_string):
        driver, s, base_url = login

        driver.get(base_url + "/")

        driver.find_element_by_id("kw").send_keys(search_string)

        driver.find_element_by_id("su").click()

        time.sleep(2)

        search_results = driver.find_element_by_xpath('//*[@id="1"]/h3/a').get_attribute('innerHTML')

        print(search_results)

        assert (expect_string in search_results) is True


if __name__ == "__main__":
    pytest.main(['-s', '-v'])
