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

def load_and_analyze_data(filename):
    df = pd.read_csv(filename)
    df['Time'] = df['Time'].astype(str)
    
    late_night_df = df[df['Time'].between('02:00:00', '03:59:59')]

    late_night_counts = late_night_df['User ID'].value_counts().head(10)
    
    return late_night_counts

def main():
    filename = 'groupme_chat_history.csv'
    top_late_night_users = load_and_analyze_data(filename)

    print("Top 10 users who sent the most messages from 2 AM to 4 AM:")
    for user_id, count in top_late_night_users.items():
        nickname = get_nickname(str(user_id))
        print(f"{nickname} (User ID: {user_id}): {count} messages")

if __name__ == "__main__":
    main()
