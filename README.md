ollama‑tcm‑demo
 
Python + Ollama本地大模型，中药学趣味对话Demo，无需API密钥，全部本地运行。
 
项目简介
 
基于Ollama调用deepseek‑r1模型，实现控制台多轮对话，具备上下文记忆，面向中药学知识问答，输入 exit 退出程序。
 
环境准备
 
1. 安装 Ollama
 
官网下载安装 Ollama：https://ollama.com/
 
拉取模型（终端执行）
 
bash
  
ollama pull deepseek-r1
 
 
2. Python依赖
 
bash
  
pip install requests
 
 
运行项目
 
bash
  
python test.py
 
 
- 在控制台输入问题，进行中药学问答
- 输入  exit  回车，退出程序
 
项目文件
 
-  test.py ：主程序代码
-  .gitignore ：git忽略配置
 
示例对话
 
plaintext
  
====中药AI对话（带记忆，输入exit退出）====
请输入问题：讲讲黄芪
回答：......
请输入问题：对比和当归的区别
回答：......
请输入问题：exit
结束程序
 
 
注意事项
 
1. 运行前确保Ollama软件处于打开状态
2. 多轮对话积累过多上下文会触发400错误，输入 exit 重启程序重置记忆即可
3. deepseek‑r1推理速度受电脑硬件影响，耐心等待输出
