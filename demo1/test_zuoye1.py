import pytest
from appium import webdriver

class Test_Zuoye():
	def setup(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'emulator-5554'
		desired_caps['appPackage'] = 'com.xueqiu.android'
		desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
		desired_caps['noreset'] = "true"
		# desired_caps['dontStopAppOnReset'] = 'True'
		desired_caps['skipDeviceInitialization'] = 'true'
		desired_caps['uncodeKeyBoard'] = 'true'
		desired_caps['reseKeyBoard'] = 'true'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(5)

	def teardown(self):
		self.driver.quit()