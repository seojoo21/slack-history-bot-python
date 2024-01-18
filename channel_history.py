from typing import List, Dict
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_API_TOKEN
from datetime import datetime, timedelta
import time
import os

class SlackChannelHistory:
    def __init__(self, token: str) -> None:
        self.client = WebClient(token=token)

    def fetch_all_messages(self, channel_id: str, days: int) -> List[Dict]:
        all_messages = []
        try:
            # Calculate the start time for the given duration
            end_time = datetime.now()
            start_time = end_time - timedelta(days=days)
            start_timestamp = int(time.mktime(start_time.timetuple()))

            response = self.client.conversations_history(
                channel=channel_id,
                oldest=start_timestamp
            )
            all_messages.extend(response["messages"])

            # Handling pagination
            while response["has_more"]:
                response = self.client.conversations_history(
                    channel=channel_id,
                    cursor=response["response_metadata"]["next_cursor"],
                    oldest=start_timestamp
                )
                all_messages.extend(response["messages"])

        except SlackApiError as e:
            print(f"Error fetching conversations: {e}")
        return all_messages

# Usage
if __name__ == "__main__":
    slack_token = os.environ.get("SLACK_API_TOKEN", SLACK_API_TOKEN)
    slack_history = SlackChannelHistory(slack_token)
    channel_id = "your-channel-id"  # Replace with your channel ID
    duration_in_days = 100  # Fetch messages from the last 7 days
    messages = slack_history.fetch_all_messages(channel_id, duration_in_days)
    for message in messages:
        print(message)
