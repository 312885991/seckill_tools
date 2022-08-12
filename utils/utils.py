import os
import requests


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
