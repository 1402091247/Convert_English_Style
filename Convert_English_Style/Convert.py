from openai import OpenAI

# 为保证准确率，给每个风格及程度都设置特定的prompt
data = ["Enhance the formality of the following sentences to a lesser extent:",
        "Please refine the tone and language of the following sentences to be more formal and suitable for a professional audience:",
        "Enhance the formality and sophistication of the following sentences to exemplify a high degree of professionalism:",
        "Rewrite the sentence to sound more casual and informal, with a slight sense of friendliness:",
        "Enhance the sociability of the following sentence to make it more engaging and approachable without losing its original meaning:",
        "Rewrite the sentences below to make them sound exceptionally friendly and engaging, maximizing sociability:",
        "Revise the sentences below by breaking them down into simpler sentences with minimal complexity:",
        "Break down the sentences provided into shorter, more concise sentences without altering the original meaning too much. Aim to maintain clarity and improve readability by dividing the sentences into smaller units:",
        "Restructure the given text by breaking down complex sentences into simpler and more concise sentences. Aim to enhance clarity and readability by dividing the content into smaller units while maintaining the original meaning:"
        ]

index = ["Professional_Low","Professional_Medium","Professional_High",
        "Sociable_Low","Sociable_Medium","Sociable_High",
        "Summary_Low","Summary_Medium","Summary_High"
         ]
client = OpenAI(
    base_url='https://xiaoai.plus/v1',
    # sk-xxx替换为自己的key
    api_key='sk-RjDt8IuNCTsOZPvLHwErGBygww3MIjHNz7oArnzCKwiSlYA9'
)
def convert(input,degree, profession):
    # input = 'we want to go to supermarket next weekend'

    #Insert medical jargon into the sentences below,,,Add terms from the {} field
    if profession =="None":
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": "You are an English expert."},
            {"role": "user", "content": "{}{}".format(data[index.index(degree)], input)}
          ]
        )
    else:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an English expert."},
                {"role": "user", "content": "Insert {} jargon into the sentences below，and {}{}".format(profession,data[index.index(degree)], input)}
            ]
        )
    # completion.choices[0].message
    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content
if __name__ == '__main__':
    print('out')
