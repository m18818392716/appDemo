from appium import webdriver
from time import sleep

class DriverConfig:

      def driver_init(self):
          self.desired_caps = {
              'platformName': 'Android',
              'deviceName': 'Samsung Galaxy S7_1',  # adb  deivces
              'platformVersion': '8.0',  # 从设置中可以获取
              'appPackage': 'com.tnaot.newspro',  # 包名
              'appActivity': 'com.tnaot.news.mctnews.detail.activity.MainActivity',  # apk的launcherActivity
              # 'skipServerInstallation': True
              # 'browserName': 'chrome',
              'chromedriverExecutable': r"C:\\Users\\23633\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\win\\chromedriver.exe"
              # 'chromeOptions': {'androidProcess', 'WEBVIEW_com.tanot.newspro'}
          }
          self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
          sleep(5)
          return self.driver