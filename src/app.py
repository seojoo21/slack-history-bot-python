import json
from history import SlackChannelConversationsHistory
from chatgpt import ChatGPTAnalyzer
from config import SLACK_API_TOKEN, SLACK_CHANNEL_ID, INITIAL_PROMPT

def lambda_handler(event, context):
    # Initialize Slack history fetcher
    slack_history = SlackChannelConversationsHistory(SLACK_API_TOKEN)
    duration_in_days = 1  # Assuming you want the past day's messages

    # Fetch messages from Slack
    messages = slack_history.fetch_all_messages(SLACK_CHANNEL_ID, duration_in_days)

    # Convert messages to a format suitable for analysis
    conversation_text = "\n".join([msg.get("text", "") for msg in messages])

    # Initialize ChatGPT analyzer
    chatgpt_analyzer = ChatGPTAnalyzer()

    # Define the initial prompt for GPT
    initial_prompt = INITIAL_PROMPT

    # Analyze the conversation
    analysis_result = chatgpt_analyzer.analyze_conversation(conversation_text, initial_prompt)

    # Handle the analysis result
    # This can be logging, saving to a database, sending an email, etc.
    print("========분석 결과 시작=========")
    print(analysis_result)
    print("========분석 결과 끝==========")
    

    # Return a response
    return {
        "statusCode": 200,
        "body": json.dumps("Analysis completed successfully.")
    }

# For local testing, you can call lambda_handler directly
if __name__ == "__main__":
    print(lambda_handler({}, {}))
