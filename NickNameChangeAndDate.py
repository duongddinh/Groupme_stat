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

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year
df['Count'] = 1

messages_per_month_year = df.pivot_table(index='Month', columns='Year', values='Count', aggfunc='sum', fill_value=0)

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
messages_pivot = messages_per_month_year.reindex(month_order)

messages_pivot['Total'] = messages_pivot.sum(axis=1)

messages_pivot.loc['Total'] = messages_pivot.sum()

print("Total messages per month for each year, with totals:")
print(messages_pivot)


nickname_changes = df.groupby('User ID')['Name'].nunique()

sorted_changes = nickname_changes.sort_values(ascending=False).head(10)

current_nicknames = {user_id: get_nickname(user_id) for user_id in sorted_changes.index}

results = pd.DataFrame({
    'User_ID': sorted_changes.index,
    'Current Nickname': [current_nicknames[user_id] for user_id in sorted_changes.index],
    'Nickname Changes': sorted_changes.values
})

print("\nTop 10 users by nickname changes:")
print(results)
