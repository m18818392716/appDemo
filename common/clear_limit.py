import redis
import logging

class ClearLimit():

    def __init__(self, host, port, pwd):
        """
        连接redis
        :param host: 服务器本机
        :param port: 端口
        :param pwd: 密码
        """
        self.st = redis.StrictRedis(host=host,port=port,password=pwd)

    def get_verification_code(self,number):
        try:
            code = int(self.st.get('TNAOT_PHONE:VERIFICATION:CODE:86{}'.format(number)))
        except:
            return "redis库中没有手机号{}的短信验证码".format(number)

        return "手机号{}的短信验证码为{}".format(number, code)

    def clear_number_limit(self, number):
        """
        清除手机号每天短信限制
        :param number: 手机号
        :return:
        """
        if len("{}".format(number)) < 11:
            phone_data = "TNAOT_PHONE:VERIFICATION:NUM:855{}:2".format(number)
        else:
            phone_data = "TNAOT_PHONE:VERIFICATION:NUM:86{}:2".format(number)
        self.st.set(phone_data.encode(), 0)
        print("清除成功")

    def clear_device_limit(self, device_id):
        """
        清除设备号请求短信验证次数
        :param device_id: 设备id
        :return:
        """
        device_data = "TNAOT_REQUEST:LIMIT:DEVICEID:homeget_verify_code{}".format(device_id)
        self.st.set(device_data.encode(), 0)
        print("清除成功")



if __name__ == '__main__':
    re = ClearLimit('192.168.1.248','7379',"sadfhis$oi#vj")
    # 获取手机验证码
    print(re.get_verification_code(18800220013))

    # 清除手机号每天短信限制
    # re.clear_number_limit(18800220013)

    # 清除设备号请求短信验证次数
    # re.clear_device_limit("C8A7E8EEE480575A04D422DBC695E82026D3F7AA")