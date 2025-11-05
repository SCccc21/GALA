import re
import time

def generate_response(client, model, messages, max_tokens=2048, temperature=1.0, top_p=0.9, frequency_penalty=0, presence_penalty=0):
    """
    Generates a response from an OpenAI-compatible API with retry logic.
    """
    while True:
        try:
            params = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "frequency_penalty": frequency_penalty,
                "presence_penalty": presence_penalty
            }
            if top_p is not None:
                params["top_p"] = top_p

            response = client.chat.completions.create(**params)
            return response.choices[0].message.content
        except Exception as err:
            print(f'Exception occurs when calling {model}: {err}')
            print('Will sleep for ten seconds before retry...')
            print(messages)
            time.sleep(10)


def extract_dict(model_output):
    start = model_output.find('{')
    if start == -1:
        # No '{' found at all
        return None
    
    end = model_output.rfind('}')
    if end == -1 or end < start:
        # No closing '}' after start, return everything from '{' to the end and add '}'
        return model_output[start:] + '}'
    else:
        # Found a complete block
        return model_output[start:end+1]

def shorten_conversation(conv_list):
    
    shortened_conversation = []
    
    for turn in conv_list:
        if turn['role'] == 'assistant':
            # Split the content into sentences
            sentences = re.split(r'(?<=[.!?]) +', turn['content'])
            # Keep only the first 3 sentences and add "..." if there are more sentences
            shortened_content = ' '.join(sentences[:3]) + (' ...' if len(sentences) > 3 else '')
            shortened_conversation.append({'role': 'assistant', 'content': shortened_content})
        else:
            # Add user turns unchanged
            shortened_conversation.append(turn)
    return shortened_conversation
