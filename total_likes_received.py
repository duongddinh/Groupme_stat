import pandas as pd
import requests
import json

# Your GroupMe access token and group ID
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

df['Like Count'] = df['Like Count'].astype(int)

likes_per_user = df.groupby('User ID')['Like Count'].sum()

sorted_likes = likes_per_user.sort_values(ascending=False)

for user_id in sorted_likes.head(30).index:
    nickname = get_nickname(user_id)
    like_count = sorted_likes[user_id]
    print(f"{nickname}: {like_count} likes")
