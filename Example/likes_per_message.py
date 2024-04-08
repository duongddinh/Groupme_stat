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

df['Like Count'] = df['Like Count'].astype(int)

agg_df = df.groupby('User ID').agg({'Like Count': ['sum', 'count']})
agg_df.columns = ['Total Likes Received', 'Total Messages Sent']

agg_df['Average Likes per Message'] = agg_df['Total Likes Received'] / agg_df['Total Messages Sent']

sorted_agg_df = agg_df.sort_values(by='Average Likes per Message', ascending=False).reset_index()

top_10_users = sorted_agg_df.head(10)

print("Top 10 users by average likes per message (Total messages, Total likes received):")
for index, row in top_10_users.iterrows():
    user_id = row['User ID']
    nickname = get_nickname(user_id)
    avg_likes = row['Average Likes per Message']
    total_msgs = row['Total Messages Sent']
    total_likes = row['Total Likes Received']
    print(f"{nickname} (User ID: {user_id}): Avg Likes/Msg: {avg_likes:.2f}, Total Msgs: {total_msgs}, Total Likes: {total_likes}")
