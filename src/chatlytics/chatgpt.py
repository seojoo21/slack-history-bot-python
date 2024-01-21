import requests

class ChatGPTAnalyzer:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def analyze_conversation(self, conversation: str) -> str:
        payload = {'text': conversation}
        response = requests.post(self.api_url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"ChatGPT API request failed: {response.text}")

# Example usage
if __name__ == "__main__":
    chatgpt_analyzer = ChatGPTAnalyzer("http://your-chatgpt-api-endpoint")
    analysis_result = chatgpt_analyzer.analyze_conversation("Sample conversation text")
    print(analysis_result)
