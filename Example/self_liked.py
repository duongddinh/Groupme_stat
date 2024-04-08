import pandas as pd
import requests

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

def convert_to_list(liked_by_str):
    if pd.isnull(liked_by_str) or not liked_by_str.strip():
        return []
    return [user_id.strip() for user_id in liked_by_str.split(',')]

df['Liked By'] = df['Liked By'].apply(convert_to_list)

self_likes = {}

for _, row in df.iterrows():
    user_id = row['User ID']
    liked_by = row['Liked By']
    if str(user_id) in liked_by:  
        self_likes[user_id] = self_likes.get(user_id, 0) + 1

self_likes_df = pd.DataFrame(list(self_likes.items()), columns=['User ID', 'Self Likes'])

sorted_self_likes = self_likes_df.sort_values(by='Self Likes', ascending=False).reset_index(drop=True)

print("Top 10 users by self likes:")
for index, row in sorted_self_likes.head(30).iterrows():
    user_id = row['User ID']
    nickname = get_nickname(user_id)
    print(f"{nickname} (User ID: {user_id}): {row['Self Likes']} self likes")
