import pandas as pd
import requests
from ast import literal_eval

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

def safe_parse(x):
    try:
        result = literal_eval(x)
        if isinstance(result, int): 
            return [result]
        return result
    except:
        return []  
df['Liked By'] = df['Liked By'].apply(lambda x: safe_parse(x) if pd.notnull(x) and x.strip() != '' else [])

likes_given = {}

for liked_by in df['Liked By']:
    for user_id in liked_by:
        if user_id in likes_given:
            likes_given[user_id] += 1
        else:
            likes_given[user_id] = 1

likes_given_df = pd.DataFrame(likes_given.items(), columns=['User ID', 'Likes Given'])

sorted_likes_given = likes_given_df.sort_values(by='Likes Given', ascending=False).reset_index(drop=True)


for index, row in sorted_likes_given.head(30).iterrows():
    user_id = row['User ID']
    likes_given = row['Likes Given']
    nickname = get_nickname(user_id)
    print(f"{nickname}: {likes_given} likes given")
