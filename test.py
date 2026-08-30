import requests

url = "http://localhost:11434/api/chat"
# 保存完整对话上下文，实现对话记忆
messages = [
    {"role": "system", "content": "你是幽默的中药学学长，擅长使用比喻。"}
]

print("====中药AI对话（带记忆，输入exit退出）====")
while True:
    user_input = input("\n请输入问题：")
    if user_input.strip().lower() == "exit":
        print("结束程序")
        break
    messages.append({"role":"user","content":user_input})

    data = {
        "model":"deepseek-r1",
        "stream":False,
        "messages":messages,
        "timeout":240
    }
    print("🧠思考中……")
    try:
        resp = requests.post(url,json=data,timeout=240)
        resp.raise_for_status()
        res = resp.json()
        reply = res["message"]["content"]
        print(f"\n回答：{reply}")
        # 将AI回答存入记忆
        messages.append({"role":"assistant","content":reply})
    except Exception as e:
        print("错误：",e)