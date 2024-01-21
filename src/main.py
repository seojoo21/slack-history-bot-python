import json
from chatlytics.history import SlackChannelHistory
from chatlytics.chatgpt import ChatGPTAnalyzer
from config import SLACK_API_TOKEN, CHATGPT_API_URL

def lambda_handler(event, context):
    # Initialize Slack history fetcher
    slack_history = SlackChannelHistory(SLACK_API_TOKEN)
    channel_id = "your-channel-id"  # Replace with your Slack channel ID
    duration_in_days = 1  # Assuming you want the past day's messages

    # Fetch messages from Slack
    messages = slack_history.fetch_all_messages(channel_id, duration_in_days)

    # Convert messages to a format suitable for analysis
    # This might need customization based on how you want to analyze the data
    conversation_text = "\n".join([msg.get("text", "") for msg in messages])

    # Initialize ChatGPT analyzer
    chatgpt_analyzer = ChatGPTAnalyzer(CHATGPT_API_URL)

    # Analyze the conversation
    analysis_result = chatgpt_analyzer.analyze_conversation(conversation_text)

    # Handle the analysis result
    # This can be logging, saving to a database, sending an email, etc.
    print(analysis_result)

    # Return a response
    return {
        "statusCode": 200,
        "body": json.dumps("Analysis completed successfully.")
    }

# For local testing, you can call lambda_handler directly
if __name__ == "__main__":
    print(lambda_handler({}, {}))
