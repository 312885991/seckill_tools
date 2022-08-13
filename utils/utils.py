import os
from random import choice

import requests
from selenium import webdriver


# 获取useragent信息
def get_useragent_data(filename: str = "./useragents.txt") -> list:
    root_folder = os.path.dirname(__file__)
    user_agents_file = os.path.join(root_folder, filename)
    try:
        with open(user_agents_file, 'r', encoding='utf-8') as reader:
            data = [_.strip() for _ in reader.readlines()]
    except Exception as e:
        print(e)
        data = ["Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"]
    return data


# 配置chrome启动项
def build_chrome_options():
    """配置启动项"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.accept_untrusted_certs = True
    chrome_options.assume_untrusted_cert_issuer = True
    arguments = ['--no-sandbox', '--disable-impl-side-painting', '--disable-setuid-sandbox',
                 '--disable-seccomp-filter-sandbox',
                 '--disable-breakpad', '--disable-client-side-phishing-detection', '--disable-cast',
                 '--disable-cast-streaming-hw-encoding', '--disable-cloud-import', '--disable-popup-blocking',
                 '--ignore-certificate-errors', '--disable-session-crashed-bubble', '--disable-ipv6',
                 '--allow-http-screen-capture', '--start-maximized', '--ignore-ssl-errors']
    for arg in arguments:
        chrome_options.add_argument(arg)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    chrome_options.add_argument(f'--user-agent={choice(get_useragent_data())}')
    return chrome_options


# 消息推送
def notify_user(uuid="5d4bc588e000bfc",
                title="秒杀通知",
                text="商品抢购成功！",
                html=None,
                uids="UID_orEZQ6c54qCO3KzMkQT5CdzcWU7g_N",
                emails=""):
    """
    推送消息
    :param uuid: 账户ID
    :param title: 消息标题
    :param text: 消息内容
    :param html: 消息详情（支持html格式）
    :param uids: 推送到的微信UID，多个UID用英文逗号,分割
    :param emails: 推送到的邮箱地址，多个邮箱地址用英文逗号,分割
    :return:
    """
    # 调用接口完成信息的推送
    res = requests.post(url="https://courier.toptopn.com/api/v1/cui/notify/push", json=dict(
        uuid=uuid,
        uids=uids,
        title=title,
        text=text,
        html=html,
        emails=emails
    )).json()
    print("消息推送结果：{}".format(res))


if __name__ == '__main__':
    notify_user()
