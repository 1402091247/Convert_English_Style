from openai import OpenAI

client = OpenAI(
    base_url='https://xiaoai.plus/v1',
    # sk-xxx替换为自己的key
    api_key='sk-RjDt8IuNCTsOZPvLHwErGBygww3MIjHNz7oArnzCKwiSlYA9'
)
def convert(input):
    # input = 'we want to go to supermarket next weekend'

    #Insert medical jargon into the sentences below,,,Add terms from the {} field

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an Chinese expert."},
            {"role": "user", "content": input}
        ]
    )
    # completion.choices[0].message
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content
if __name__ == '__main__':
    input1 = input("输入：")
    out = convert(input1)
    print(out)