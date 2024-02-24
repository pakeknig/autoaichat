from wxauto import WeChat
from zhipuai import ZhipuAI
client = ZhipuAI(api_key=your_key)
import time
# 实例化微信对象
wx = WeChat()
# 持续监听消息，并且收到消息后回复“收到”
wait = 10  # 设置10秒查看一次是否有新消息
while True:
    msg = wx.GetNextNewMessage(savepic=True)  # 如果获取到新消息了，则回复收到
    if msg:
        name=wx.CurrentChat()
        prompt = msg[name][0][1]
        response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": prompt}
        ],
        )
        answer = response.choices[0].message.content
        wx.SendMsg(msg=answer, who=list(msg)[0])  # 回复收到
