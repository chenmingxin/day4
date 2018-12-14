def click_element(self, location, location_vlaue):
    # location: 定位类型
    # location_vlaue: 定位元素属性值
    self.find_element(location, location_vlaue).click()

# 输入内容
def input_element(self, location, location_vlaue, text):
    # text: 需要输入的值
    self.find_element(location, location_vlaue).send_keys(text)


