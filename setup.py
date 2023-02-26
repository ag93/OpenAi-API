import openai
import os

if __name__ == "__main__":
    #Setting up the API key as an OS environment variable
    #os.environ["OPENAI_API_KEY"] = "YOUR KEY HERE!"

    #Making sure it works :)
    #print(os.getenv("OPENAI_API_KEY"))

    #Making a test call to openai
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = "What is the standard tuning of a bass guitar",
        max_tokens = 100
    )

    print(response)

    '''
    ---------------------------- Response ----------------------------
    {
    "choices": [
        {
        "finish_reason": "stop",
        "index": 0,
        "logprobs": null,
        "text": "?\n\nThe standard tuning for a bass guitar is E-A-D-G."
        }
    ],
    "created": 1677445776,
    "id": "cmpl-6oIYyN6Ivzng1NHp5vRVEBb0QPFL8",
    "model": "text-davinci-003",
    "object": "text_completion",
    "usage": {
        "completion_tokens": 19,
        "prompt_tokens": 9,
        "total_tokens": 28
    }
    }
    ---------------------------- End Response ----------------------------
    '''