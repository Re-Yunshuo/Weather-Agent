import json
from dashscope import Generation
from weather_search import get_weather

functions = [
    {
        "name": "get_weather",
        "description": "获取指定城市的天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名"
                }
            },
            "required": ["city"]
        }
    }
]

user_question = input("你好，我是天气智能助手，请输入你的问题：")

response = Generation.call(
    model='qwen-plus', 
    messages=[{
        'role': 'user',
        'content': user_question
    }],
    functions=functions,
    result_format='message',
    temperature=0.2,
    api_key='API-KEY'  # 在此处填写API Key
)

message = response['output']['choices'][0]['message']
if message.get('function_call'):
    func_name = message['function_call']['name']
    arguments = json.loads(message['function_call']['arguments'])
    city = arguments['city']
    result = get_weather(city)

    second_response = Generation.call(
        model='qwen-plus',
        messages=[
            {'role': 'user', 'content': user_question},
            message,
            {'role': 'function', 'name': func_name, 'content': result}
        ],
        result_format='message',
        temperature=0.3,
        api_key='API-KEY'  # 在此处填写API Key
    )

    final_reply = second_response['output']['choices'][0]['message']['content']
    print(final_reply)
else:
    print("模型没有调用函数，直接回复：", message['content'])
