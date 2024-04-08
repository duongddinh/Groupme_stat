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

df['Like Count'] = pd.to_numeric(df['Like Count'], errors='coerce').fillna(0).astype(int)

total_messages = len(df)

messages_with_zero_likes = len(df[df['Like Count'] == 0])

percentage_with_zero_likes = (messages_with_zero_likes / total_messages) * 100

print(f"Percentage of messages with 0 likes: {percentage_with_zero_likes:.2f}%")

max_likes = df['Like Count'].max()
messages_with_max_likes = df[df['Like Count'] == max_likes]
print(f"\nMessage(s) with the most likes ({max_likes} likes):")
for _, row in messages_with_max_likes.iterrows():
    nickname = get_nickname(row['User ID'])  # Dynamic fetching of nickname
    print(f"Date/Time: {row['Date']}, Nickname: {nickname}, Message: {row['Message']}")

