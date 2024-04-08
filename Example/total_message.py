import pandas as pd
import requests

access_token = ''
group_id = ''

def get_nickname(user_id):
    url = f"https://api.groupme.com/v3/groups/{group_id}?token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        members = response.json().get('response', {}).get('members', [])
        for member in members:
            if str(member.get('user_id')) == str(user_id):
                return member.get('nickname')
    return 'Unknown'

df = pd.read_csv('groupme_chat_history.csv')

message_counts = df.groupby('User ID')['User ID'].count()
sorted_message_counts = message_counts.sort_values(ascending=False)

for user_id in sorted_message_counts.head(30).index:
    nickname = get_nickname(user_id)
    message_count = sorted_message_counts[user_id]
    print(f"{nickname}: {message_count} messages sent")
