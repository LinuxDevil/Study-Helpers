import openai
import argparse

openai.api_key = 'YOUR_API_KEY_HERE'

def generate_answer(prompt, model, temperature):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        temperature=temperature,
    )
    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description='Ask a Question and Get an Answer')
    parser.add_argument('prompt', metavar='prompt', type=str, help='The prompt for the question')
    parser.add_argument('--model', metavar='model', type=str, help='The name of the OpenAI model to use', default='text-davinci-002')
    parser.add_argument('--temperature', metavar='temperature', type=float, help='The temperature to use for generating the answer', default=0.5)
    args = parser.parse_args()

    answer = generate_answer(args.prompt, args.model, args.temperature)
    print(answer)

if __name__ == '__main__':
    main()
