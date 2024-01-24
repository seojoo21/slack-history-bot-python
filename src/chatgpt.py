from openai import OpenAI
from config import OPENAI_API_KEY

class ChatGPTAnalyzer:
    def __init__(self, model: str = "gpt-4") -> None:
        self.model = model
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def analyze_conversation(self, conversation_history: str, initial_prompt: str) -> str:
        prompt_text = f"{initial_prompt}\n\n{conversation_history}"
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt_text}
                ],
                max_tokens=2000
            )
            
            # Accessing the response correctly
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in ChatGPT API request: {e}")
            raise

# Example usage
if __name__ == "__main__":
    initial_prompt = "Provide a summary of the following conversation:"
    conversation_history = "Person A: How are you? Person B: I'm good, thanks!"
    
    chatgpt_analyzer = ChatGPTAnalyzer()
    analysis_result = chatgpt_analyzer.analyze_conversation(conversation_history, initial_prompt)
    print(analysis_result)
