#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：华能项目角色划分
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class initDriver:
	u'''web驱动初始化'''
	def open_driver(self,ipAdd):
		driver = webdriver.Chrome()
		#窗口最大化
		driver.maximize_window()
		#打开IP地址对应的网页
		driver.get("https://" + ipAdd + "/fort/login")
		return driver

class comElement(object):
	def __init__(self,driver):
		self.driver = driver

	u'''等待元素出现后再定位元素EC
		parameter:
			- type:定位的类型，如id,name,tag name,class name,css,xpath等
			- value：页面的元素值
			- timeout:超时前等待的时间
		return：定位元素并点击该元素
	'''
	def find_element_with_wait_EC(self,type,value,timeout=10):
		if type == "id":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value)))
		elif type == "xpath":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value)))
		elif type == "name":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value)))
		elif type == "tagname":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value)))
		elif type == "classname":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
		elif type == "css":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
		elif type == "link":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
		elif type == "plt":
			return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))

	u'''等待元素出现后再定位元素并点击EC
		parameter:
			- type:定位的类型，如id,name,tag name,class name,css,xpath等
			- value：页面的元素值
			- timeout:超时前等待的时间
		return：定位元素并点击该元素
	'''
	def find_element_wait_and_click_EC(self,type,value,timeout=10):
		if type == "id":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).click()
		elif type == "xpath":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).click()
		elif type == "name":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).click()
		elif type == "tagname":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).click()
		elif type == "classname":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).click()
		elif type == "css":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).click()
		elif type == "link":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).click()
		elif type == "plt":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).click()

	u'''填写文本框的内容
		parameter:
			- type:定位的类型，如id,name,tag name,class name,css,xpath等
			- value：页面的元素值
			- key:文本框内容
			- timeout:超时前等待的时间
	'''
	def find_element_sendkyes_EC(self, type, value, key, timeout=10):
		if type == "id":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).send_keys(key)
		elif type == "xpath":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).send_keys(key)
		elif type == "name":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).send_keys(key)
		elif type == "tagname":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).send_keys(key)
		elif type == "classname":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).send_keys(key)
		elif type == "css":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).send_keys(key)
		elif type == "link":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).send_keys(key)
		elif type == "plt":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).send_keys(key)

	u'''清空文本框的内容
		parameter:
			- type:定位的类型，如id,name,tag name,class name,css,xpath等
			- value：页面的元素值
			- timeout:超时前等待的时间
	'''
	def find_element_wait_and_clear_EC(self, type, value, timeout=10):
		if type == "id":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).clear()
		elif type == "xpath":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).clear()
		elif type == "name":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).clear()
		elif type == "tagname":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).clear()
		elif type == "classname":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).clear()
		elif type == "css":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).clear()
		elif type == "link":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).clear()
		elif type == "plt":
			WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).clear()

	u'''元素是否存在
		parameter:
			- type:定位的类型，如id,name,tag name,class name,css,xpath等
			- value：页面的元素值
			- timeout:超时前等待的时间
		return:true代表元素出现，false代表找不到元素
	'''
	def is_element_exsit(self,type,value):
		isExsit = False

		try:
			element = self.find_element_with_wait_EC(type,value)
			if element != False:
				isExsit = True
		except Exception as e:
			print("element is not exsit:",value)
		return isExsit

	u'''根据text选择
		Parameters:
			- selem:定位带的Select元素
			- text:select选项中的文本值
	'''
	def select_element_by_visible_text(self,selem,text):
		return Select(selem).select_by_visible_text(text)

	u'''定位到topFrame'''
	def switch_to_top(self):
		if self.is_element_exsit("id","content1"):
			self.driver.switch_to_frame("content1")

		if self.is_element_exsit("id","topFrame"):
			self.driver.switch_to_frame("topFrame")

	u'''定位到mainFrame'''
	def switch_to_main(self):
		if self.is_element_exsit("id","content1"):
			self.driver.switch_to_frame("content1")
		if self.is_element_exsit("id","mainFrame"):
			self.driver.switch_to_frame("mainFrame")

	u'''定位到leftFrame'''
	def switch_to_left(self):
		self.switch_to_main()
		if self.is_element_exsit("id","leftFrame"):
			self.driver.switch_to_frame("leftFrame")

	u'''定位到rightFrame'''
	def switch_to_right(self):
		self.switch_to_main()
		if self.is_element_exsit("id","rightFrame"):
			self.driver.switch_to_frame("rightFrame")

	u'''定位到rigthFrame'''
	def switch_to_rigth(self):
		self.switch_to_main()
		if self.is_element_exsit("id","rigthFrame"):
			self.driver.switch_to_frame("rigthFrame")

	u'''定位到bottomFrame'''
	def switch_to_bottom(self):
		if self.is_element_exsit("id","content1"):
			self.driver.switch_to_frame("content1")
		if self.is_element_exsit("id","bottomFrame"):
			self.driver.switch_to_frame("bottomFrame")

	u'''返回上级frame'''
	def switch_to_content(self):
		self.driver.switch_to_default_content()

	u'''定位到artIframe'''
	def switch_to_artIframe(self):
		self.switch_to_content()
		if self.is_element_exsit("id","artIframe"):
			self.driver.switch_to_frame("artIframe")

	u'''从一个frame跳转到其他frame
		Parameters:
			- frameName:要跳转到的frame的名字
	'''
	def from_frame_to_otherFrame(self,frameName):
		time.sleep(2)
		self.switch_to_content()
		time.sleep(1)
		if frameName == "mainFrame":
			#定位到mainFrame
			self.switch_to_main()
		elif frameName == "bottomFrame":
		#定位到bottomFrame
			self.switch_to_bottom()
		elif frameName == "topFrame":
		#定位到topFrame
			self.switch_to_top()
		elif frameName == "leftFrame":
		#定位到leftFrame
			self.switch_to_left()
		elif frameName == "rightFrame":
		#定位到rightFrame
			self.switch_to_right()
		elif frameName == "rigthFrame":
		#定位到rightFrame
			self.switch_to_rigth()
		elif frameName == "artIframe":
			self.switch_to_artIframe()

	u'''菜单选择
		Parameters:
			- levelText1：1级菜单文本
			- levelText2：2级菜单文本
			- levelText3：3级菜单文本
	'''
	def select_menu(self,levelText1,levelText2='no',levelText3='no'):

		self.from_frame_to_otherFrame("topFrame")

		#点击一级菜单
		WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,levelText1))).click()

		#如果有2级菜单，再点击2级菜单
		if levelText2 != 'no':
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,levelText2))).click()

		#如果有3级菜单，根据名称点击3级菜单
		if levelText3 != 'no':
			self.from_frame_to_otherFrame("leftFrame")
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,levelText3))).click()

	u'''弹窗类检查点
		Parameters:
			- type：定位弹窗中元素的类型
			- elem：弹窗元素的名字或者路径
			- data：excel一行的数据
			- flag:没有检查点的测试项通过标识。Ture为通过，False为未通过
	'''
	def click_login_msg_button(self):
		#确定按钮
		self.driver.switch_to_default_content()
		OKBTN = "//div[@id='aui_buttons']/button[1]"
		return self.find_element_wait_and_click_EC('xpath',OKBTN)

	u'''切换模块
		parameter:
			levelText1 : 一级模块名称
			levelText2 : 二级模块名称
	'''
	def switch_to_moudle(self,levelText1,levelText2):
		time.sleep(2)
		self.from_frame_to_otherFrame("topFrame")

		self.select_menu(levelText1)
		self.select_menu(levelText1,levelText2)

u'''添加角色'''
class AddRole(object):
	def __init__(self,driver):
		self.driver = driver
		self.comEle = comElement(driver)

	u'''点击角色添加按钮'''
	def role_add_button(self):
		time.sleep(1)
		self.comEle.from_frame_to_otherFrame('mainFrame')
		self.comEle.find_element_wait_and_click_EC('id','add_role')

	u'''设置角色名称和简写
		parameter:
			- roleName：角色名称
			- abbrName：角色简称
	'''
	def set_role_name(self,roleName,abbrName):
		self.comEle.from_frame_to_otherFrame('mainFrame')
		self.comEle.find_element_sendkyes_EC('id','fortRoleName',roleName)
		self.comEle.find_element_sendkyes_EC('id','fortRoleShortName',abbrName)
		time.sleep(1)

	u'''展开角色树(三角形)；
		parameter:
		- treeDemo_switch:角色演示树
	'''
	def set_tree_demo_switch(self,treeDemo_switch):
		self.comEle.find_element_wait_and_click_EC('id',treeDemo_switch)
		time.sleep(1)

	u'''勾选一层角色;
		parameter:
			- treeDemo_check:角色树勾选框
	'''
	def set_tree_demo_check(self,treeDemo_check):
		self.comEle.find_element_wait_and_click_EC('id',treeDemo_check)
		time.sleep(1)

	u'''勾选角色框;
		parameter:
			- inputName:底层角色勾选框
	'''
	def set_bottom_click(self,inputName):
		self.comEle.find_element_wait_and_click_EC('name',inputName)
		time.sleep(1)

	u'''选择其他角色；
		parameter:
			- roleName：角色名称
	'''
	def set_other_role(self,roleName):
		time.sleep(1)
		sele = self.comEle.find_element_with_wait_EC('id','allOtherPrivileges')
		time.sleep(1)
		self.comEle.select_element_by_visible_text(sele,roleName)
		self.comEle.find_element_wait_and_click_EC('id','add_privileges')
		time.sleep(1)

	#保存角色
	def save_role_button(self):
		time.sleep(1)
		self.comEle.find_element_wait_and_click_EC('id','save_role')
		self.comEle.click_login_msg_button()
		time.sleep(1)
		self.comEle.switch_to_main()
		self.comEle.find_element_wait_and_click_EC('id','history_skip')
		time.sleep(1)

	#添加日志管理者角色
	def set_logAdmin_role(self):
		self.role_add_button()
		self.set_role_name(u'日志管理者',u'日志管理')
		#勾选访问记录和配置记录
		self.set_tree_demo_switch('treeDemo_17_switch')
		self.set_tree_demo_check('treeDemo_18_check')
		self.set_tree_demo_check('treeDemo_19_check')
		#勾选报表管理
		self.set_tree_demo_check('treeDemo_31_check')
		#保存角色
		self.save_role_button()

	#添加审批者角色
	def set_appr_role(self):
		self.role_add_button()
		self.set_role_name(u'审批者',u'审批者')
		#勾选流程控制
		self.set_tree_demo_check('treeDemo_21_check')
		self.set_other_role(u"审批人")
		#保存角色
		self.save_role_button()

	#添加权限持有者角色
	def set_holder_role(self):
		self.role_add_button()
		self.set_role_name(u'权限持有者',u'权限持有')
		#勾选资源账号的增删改
		self.set_tree_demo_switch('treeDemo_3_switch')
		self.set_tree_demo_check('treeDemo_9_check')
		self.set_bottom_click("1002030000001")
		self.set_bottom_click("1002030000002")
		self.set_bottom_click("1002030000003")
		self.set_bottom_click("1002030000004")
		self.set_bottom_click("1002030000005")
		self.set_bottom_click("1002030000006")
		self.set_bottom_click("1002030000007")
		self.set_bottom_click("1002030000008")
		self.set_bottom_click("1002030000012")
		self.set_bottom_click("1002030000013")
		self.set_bottom_click("1002030000016")
		#勾选流程控制（不包含全部历史）
		self.set_tree_demo_switch('treeDemo_21_switch')
		self.set_tree_demo_check('treeDemo_21_check')
		self.set_tree_demo_check('treeDemo_25_check')
		#保存角色
		self.save_role_button()

	#添加用户管理员角色
	def set_userAdmin_role(self):
		self.role_add_button()
		self.set_role_name(u'用户管理员',u'用户管理')
		#勾选资源、用户、授权、审批规则
		self.set_tree_demo_switch('treeDemo_3_switch')
		self.set_tree_demo_check('treeDemo_3_check')
		self.set_tree_demo_check('treeDemo_4_check')
		self.set_tree_demo_check('treeDemo_11_check')
		#去掉用户中不需要的功能
		self.set_bottom_click("1002020000004")
		self.set_bottom_click("1002020000005")
		self.set_bottom_click("1002020000006")
		self.set_bottom_click("1002020000007")
		#去掉资源中不需要的功能
		self.set_bottom_click("1002030000004")
		self.set_bottom_click("1002030000005")
		self.set_bottom_click("1002030000006")
		self.set_bottom_click("1002030000007")
		self.set_bottom_click("1002030000008")
		self.set_bottom_click("1002030000009")
		self.set_bottom_click("1002030000010")
		self.set_bottom_click("1002030000011")
		self.set_bottom_click("1002030000012")
		self.set_bottom_click("1002030000013")
		self.set_bottom_click("1002030000014")
		self.set_bottom_click("1002030000015")
		self.set_bottom_click("1002030000016")
		#去掉授权中不需要的功能
		self.set_bottom_click("1002040000002")
		self.set_bottom_click("1002040000003")
		self.set_bottom_click("1002040000007")
		self.set_bottom_click("1002040000008")
		self.set_bottom_click("1002040000009")
		#保存角色
		self.save_role_button()

	#添加系统配置管理员角色
	def set_sysAdmin_role(self):
		self.role_add_button()
		self.set_role_name(u'系统配置管理员',u'系统管理')
		#勾选组织定义和规则定义
		self.set_tree_demo_switch('treeDemo_3_switch')
		self.set_tree_demo_check('treeDemo_4_check')
		self.set_tree_demo_check('treeDemo_11_check')

		#勾选流程控制（不包含全部历史）
		self.set_tree_demo_switch('treeDemo_21_switch')
		self.set_tree_demo_check('treeDemo_21_check')
		self.set_tree_demo_check('treeDemo_25_check')

		#勾选系统配置
		self.set_tree_demo_switch('treeDemo_39_switch')
		self.set_tree_demo_check('treeDemo_39_check')
		self.set_tree_demo_check('treeDemo_58_check')
		self.set_tree_demo_check('treeDemo_62_check')
		self.set_tree_demo_check('treeDemo_64_check')
		self.set_tree_demo_switch('treeDemo_40_switch')
		self.set_tree_demo_check('treeDemo_44_check')
		self.set_tree_demo_check('treeDemo_46_check')

		#勾选策略配置
		self.set_tree_demo_switch('treeDemo_65_switch')
		self.set_tree_demo_check('treeDemo_65_check')
		self.set_tree_demo_check('treeDemo_67_check')

		#保存角色
		self.save_role_button()

u'''登录'''
class UserLogin(object):
	def __init__(self,driver):
		self.driver = driver
		self.comEle = comElement(driver)

	def login(self):
		self.comEle.find_element_wait_and_clear_EC('id','username')
		self.comEle.find_element_sendkyes_EC('id','username','isomper')
		self.comEle.find_element_wait_and_clear_EC('id','pwd')
		self.comEle.find_element_sendkyes_EC('id','pwd','1')
		time.sleep(1)
		self.comEle.find_element_wait_and_click_EC('id','do_login')

u'''添加用户
	parameter:
		- account:用户账号
		- name：用户名称
		- pwd:用户密码
		- roleText:赋予用户的角色
'''
class AddUser(object):
	def __init__(self,driver):
		self.driver = driver
		self.comEle = comElement(driver)

	def add_user(self,account,name,pwd,roleText):
		time.sleep(2)
		#点击添加按钮
		self.comEle.from_frame_to_otherFrame("mainFrame")
		self.comEle.find_element_wait_and_click_EC('classname','btn_tj')
		#输入账号，名称，密码
		self.comEle.find_element_wait_and_clear_EC('id','fortUserAccount')
		self.comEle.find_element_sendkyes_EC('id','fortUserAccount',account)
		self.comEle.find_element_wait_and_clear_EC('id','fortUserName')
		self.comEle.find_element_sendkyes_EC('id','fortUserName',name)
		self.comEle.find_element_wait_and_clear_EC('id','fortUserPassword')
		self.comEle.find_element_sendkyes_EC('id','fortUserPassword',pwd)
		self.comEle.find_element_wait_and_clear_EC('id','fortUserPasswordAgain')
		self.comEle.find_element_sendkyes_EC('id','fortUserPasswordAgain',pwd)
		if roleText != 'no':
			#切换到角色页面
			self.comEle.find_element_wait_and_click_EC('id','userMessage')
			#为用户赋予角色
			selem = self.comEle.find_element_with_wait_EC('id','Roles')
			self.comEle.select_element_by_visible_text(selem,roleText)
			self.comEle.find_element_wait_and_click_EC('id','add_roles')
		#保存用户
		self.comEle.find_element_wait_and_click_EC('id','save_user')
		#点击弹框确定按钮
		self.comEle.click_login_msg_button()
		time.sleep(1)
		#点击返回
		self.comEle.switch_to_main()
		self.comEle.find_element_wait_and_click_EC('id','history_skip')

if __name__ == "__main__":
	initDriver = initDriver()
	driver = initDriver.open_driver('172.16.20.100')
	loginEle = UserLogin(driver)
	userEle = AddUser(driver)
	comEle = comElement(driver)
	roleEle = AddRole(driver)
	loginEle.login()
	comEle.switch_to_moudle(u'角色管理', u'角色定义')
	roleEle.set_logAdmin_role()
	roleEle.set_appr_role()
	roleEle.set_holder_role()
	roleEle.set_sysAdmin_role()
	roleEle.set_userAdmin_role()
	comEle.switch_to_moudle(u'操作管理', u'用户')
	userEle.add_user('logAdmin',u'日志管理者', 'admin@1234', u'日志管理者')
	userEle.add_user('appr',u'审批者', 'admin@1234', u'审批者')
	userEle.add_user('holder',u'权限持有者', 'admin@1234', u'权限持有者')
	userEle.add_user('userAdmin',u'用户管理员', 'admin@1234', u'用户管理员')
	userEle.add_user('sysAdmin',u'系统配置管理员', 'admin@1234', u'系统配置管理员')
	userEle.add_user('oper',u'操作员', 'admin@1234', 'no')
	driver.close()