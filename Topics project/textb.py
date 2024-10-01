from g4f.client import Client

def request(st):
        client = Client()
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Are you ok"}],
        )
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "на основе лда модели и веса слов дай название тем, объединяющих группы следующих слов. Ответ должен быть на русском языке. " + st}],
)
        response_str = str(response.choices[0].message.content)
        return response_str