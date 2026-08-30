import requests

url = "http://localhost:11434/api/chat"
data = {
    "model": "deepseek-r1",
    "stream": False,
    "messages": [
        {"role": "system", "content": "你是一个幽默的中药学学长，说话喜欢用比喻。"},
        {"role": "user", "content": "用3句话向我女朋友解释当归为什么被称为‘女科之圣药’，要让她觉得中药很浪漫。"}
    ]
}

print("🧠 正在生成你的专属浪漫科普...")
try:
    resp = requests.post(url, json=data, timeout=120)
    resp.raise_for_status()
    res = resp.json()
    print("\n输出结果：")
    print(res['message']['content'])
except Exception as e:
    print("网络/异常错误：", e)
    print("网络/异常错误：", e)