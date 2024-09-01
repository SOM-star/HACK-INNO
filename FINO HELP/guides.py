import openai

API_key = "my_api_key"

# Set your OpenAI API key
openai.api_key = API_key


def get_chatgpt_response(prompt):
    try:
        # Make a request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access to it
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract and return the response text
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"An error occurred: {str(e)}"


print(get_chatgpt_response())
