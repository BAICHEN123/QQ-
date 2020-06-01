import time,json
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys#模拟按键


def gundong(browser):
	#回到父布局滚动加载元素
	browser.switch_to.parent_frame()
	browser.find_element_by_css_selector("iframe.app_canvas_frame").send_keys(Keys.HOME)
	browser.switch_to.frame(browser.find_element_by_css_selector("iframe.app_canvas_frame"))
	ffi=browser.find_elements_by_css_selector('ol#msgList>li')
	time.sleep(0.2)
	#ifm=browser.find_element_by_css_selector("iframe.app_canvas_frame")
	for i in ffi:
		try:
			browser.execute_script("arguments[0].scrollIntoView()",i)
			time.sleep(0.5)
		except:
			print("滑动失败")
			continue
	
	browser.switch_to.parent_frame()
	return browser

list_delzd=[]
try:
	f=open("删除字典.txt",'r',encoding="utf-8")
	str1=f.readline()
	while str1!="":
		str1=str1.strip()
		if str1!="":
			list_delzd.append(str(str1))
		str1=f.readline()
	f.close()
except:
	print("字典读取失败")
	exit(0)

print("下面是字典")
print(list_delzd)
print("如果误删，请联系作者")


options=webdriver.ChromeOptions()
options.add_argument('--disable-gpu')#禁用gpu加速
options.add_argument('--start-maximized')
prefs={'profile.default_content_setting_values':{'notifications':2}}
options.add_experimental_option('prefs',prefs)#2行禁止弹窗
#options.add_argument('--proxy-server='+ipwork)
browser=webdriver.Chrome(chrome_options=options)
'''
	for cookie in listcookies:
		print(cookie['domain'])
		browser.add_cookie({'domain':cookie['domain'],
						'expiry':cookie['expiry'],
						'httpOnly':cookie['httpOnly'],
						'name':cookie['name'],
						'path':cookie['path'],
						'secure':cookie['secure'],
						'value':cookie['value']})#
	browser.get("https://user.qzone.qq.com/3575679970/infocenter")
	cookies=browser.get_cookies()
		jscookie=json.dumps(cookies)
		fcookie=open("cookie",'w')
		fcookie.write(jscookie)
		fcookie.close()
'''
browser.get("https://user.qzone.qq.com")
input("登录之后点击回车")
kkk=5
qqurl=browser.current_url

def del_sspl(browser):
	global kkk
	kkk=kkk-1
	#input("登录之后点击回车1")
	browser.get(qqurl)
	browser.implicitly_wait(10)
	shuoshuo=browser.find_element_by_css_selector('div[class="layout-shop-item"]>div[class="shop-item cs"]>div[class="head-nav"]>ul[class="head-nav-menu"]>li[class="menu_item_311"]>a')
	browser.execute_script("arguments[0].click();",shuoshuo)
	#input("123")
	browser.implicitly_wait(10)
	browser.switch_to.parent_frame()
	browser.switch_to.frame(browser.find_element_by_css_selector("iframe.app_canvas_frame"))

	ifm=browser.find_elements_by_css_selector('div[class="mod_wrap bg mod-wrap"]')
	
	#for list_ss_i in list_ss:
	#list_str=browser.find_elements_by_css_selector('li[data-tid="'+list_ss_i.get_attribute('data-tid')+'"]>div[class="box bgr3"]>div[class="box_extra bor3 "]>div[class="mod_comment"]>div[class="mod_comments"]>div[class="comments_list"]>ul>li[class="comments_item bor3"]>div[class="comments_item_bd"]>div>div[class="comments_content"]>span')
	#print(list_str[0].get_attribute('textContent'))
	#browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	#ffi=len(browser.find_elements_by_css_selector('ol#msgList>li'))
	ffi=browser.find_elements_by_css_selector('ol#msgList>li')
	#回到父布局滚动加载元素
	#browser.switch_to.parent_frame()
	#ifm=browser.find_element_by_css_selector("iframe.app_canvas_frame")
	time.sleep(1)
	for ff_i in ffi:
		try:
			#ifm.send_keys(Keys.PAGE_DOWN)
			browser.execute_script("arguments[0].scrollIntoView()",ff_i)
			time.sleep(0.1)
		except:
			print("滑动失败")
			continue
	#进入说说布局，提取内容和按键
	browser.switch_to.parent_frame()
	browser.switch_to.frame(browser.find_element_by_css_selector("iframe.app_canvas_frame"))
	list_str=browser.find_elements_by_css_selector('div[class="comments_list"]>ul>li[class="comments_item bor3"]>div[class="comments_item_bd"]>div>div[class="comments_content"]>span')
	list_del=browser.find_elements_by_css_selector('a[class="c_tx mod_comment_del"]')
	
	while len(list_str)//3 !=len(list_del):
		print(str(len(list_str))+str(len(list_del)))
		browser=gundong(browser)
		browser.switch_to.frame(browser.find_element_by_css_selector("iframe.app_canvas_frame"))
		list_str=browser.find_elements_by_css_selector('div[class="comments_list"]>ul>li[class="comments_item bor3"]>div[class="comments_item_bd"]>div>div[class="comments_content"]>span')
		list_del=browser.find_elements_by_css_selector('a[class="c_tx mod_comment_del"]')
	print(str(len(list_str))+str(len(list_del)))
	for i in range(0,len(list_str)):
		huifu_str=list_str[i].get_attribute('textContent')
		#print(str(i)+huifu_str)
		for del_str in list_delzd:
			if huifu_str.find(del_str)>=0:
				print("删除标记	"+str(i//3)+"内容	"+huifu_str)
				browser.execute_script("arguments[0].click();",list_del[i//3])
				browser.switch_to.parent_frame()
				browser.execute_script("arguments[0].click();",browser.find_element_by_css_selector('a[class="qz_dialog_layer_btn qz_dialog_layer_sub"]>span'))
				kkk=kkk+1
				return 1
while kkk>1:
	del_sspl(browser)	












