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

df['Message Length'] = df['Message'].apply(lambda x: len(str(x)))

agg_df = df.groupby('User ID')['Message Length'].mean().reset_index()

sorted_agg_df = agg_df.sort_values(by='Message Length', ascending=False)

top_10_users = sorted_agg_df.head(30)

print("Top 10 users by average characters per message:")
for index, row in top_10_users.iterrows():
    user_id = row['User ID']
    avg_length = row['Message Length']
    nickname = get_nickname(user_id)
    print(f"{nickname} (User ID: {user_id}): {avg_length:.2f} characters/message")
