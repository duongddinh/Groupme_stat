import pandas as pd
import re

df = pd.read_csv('groupme_chat_history.csv')
df['Message'] = df['Message'].astype(str)

df_system_messages = df[df['User ID'] == 'system']

def find_names(message):
    pattern = re.compile(r"removed (.+?) from the group")
    matches = pattern.findall(message)
    return matches

df_system_messages['Removed Names'] = df_system_messages['Message'].apply(find_names)

df_exploded = df_system_messages.explode('Removed Names')

name_counts = df_exploded['Removed Names'].value_counts()

top_10_removed_names = name_counts.head(10)
print("Top 10 users removed from the group the most:")
print(top_10_removed_names)
