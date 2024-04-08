import pandas as pd
import requests
import emoji

# Your GroupMe access token and group ID
access_token = ''
group_id = ''

def fetch_all_nicknames(group_id, access_token):
    nicknames = {}
    url = f"https://api.groupme.com/v3/groups/{group_id}?token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        members = response.json().get('response', {}).get('members', [])
        nicknames = {str(member.get('user_id')): member.get('nickname') for member in members}
    return nicknames

def main():
    nicknames = fetch_all_nicknames(group_id, access_token)
    if not nicknames:
        print("Failed to fetch nicknames. Please check your access token and group ID.")
        return

    df = pd.read_csv('groupme_chat_history.csv')
    df['Nickname'] = df['User ID'].map(nicknames).fillna('Unknown')
    df['Message'] = df['Message'].astype(str)

    df['Emoji Count'] = df['Message'].apply(lambda x: emoji.emoji_count(x))

    df['Attachment Count'] = df['Attachments'].fillna('').apply(lambda x: x.count(';') + 1 if x else 0)
    emoji_counts_by_user = df[df['Nickname'] != 'Unknown'].groupby('Nickname')['Emoji Count'].sum()
    attachment_counts_by_user = df[df['Nickname'] != 'Unknown'].groupby('Nickname')['Attachment Count'].sum()

    top_10_emoji_users = emoji_counts_by_user.sort_values(ascending=False).head(10)
    print("Top 10 users by emoji usage:")
    print(top_10_emoji_users)

    top_10_attachment_users = attachment_counts_by_user.sort_values(ascending=False).head(10)
    print("\nTop 10 users by attachment usage:")
    print(top_10_attachment_users)

if __name__ == "__main__":
    main()
