from selenium import webdriver as wd
import time
from selenium.webdriver.chrome.options import Options


def click_element(element, time_wait=3):
    time.sleep(time_wait)
    element.click()


class WhatsappBot:
    def __init__(self):
        self.message = 'Eae Negão'
        self.target = ["Negão Vargas"]
        self.driver = wd.Chrome(executable_path=r'./chromedriver.exe')

    def send_messages(self):

        self.drive.get("web.whatsapp.com/")

        time.sleep(10)
        for each in self.target:
            target_element = self.driver.find_element_by_xpath(f"//span[@title = '{each}']")
            click_element(target_element)

            typing_box = self.driver.find_element_by_class_name("DuUXI")
            try:
                click_element(typing_box)
                typing_box.send_keys(self.message)
                send_button = self.driver.find_element_by_xpath("//span[@data-icon = 'send']")
                click_element(send_button, 3)
            except Exception as e:
                print(e)


bot = WhatsappBot()
bot.send_messages()
