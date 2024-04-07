import requests
import csv
import time
import sys
from datetime import datetime

access_token = ''
group_id = ''
base_url = 'https://api.groupme.com/v3'

def fetch_messages(group_id, access_token):
    messages = []
    url = f"{base_url}/groups/{group_id}/messages"
    params = {'token': access_token, 'limit': 100}
    last_id = None
    total_fetched = 0  
    while True:
        if last_id:
            params['before_id'] = last_id

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Check for HTTP errors
            batch = response.json()['response']['messages']
        except requests.exceptions.HTTPError as http_err:
            # Handle common rate limiting error
            if response.status_code == 429:
                print("Rate limit exceeded. Waiting 60 seconds before retrying...")
                time.sleep(60)
                continue  
            else:
                print(f"HTTP error occurred: {http_err}")
                break
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

        if not batch:
            break  

        messages.extend(batch)
        last_id = batch[-1]['id']  
        total_fetched += len(batch)  
        print(f"Total messages fetched: {total_fetched}")  
    return messages

def save_messages_to_csv(messages, filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Date', 'Message', 'Like Count', 'User ID', 'Liked By'])

            for msg in messages:
                name = msg['name']
                # Convert timestamp to mm/dd/yyyy format
                created_at = datetime.fromtimestamp(msg['created_at']).strftime('%m/%d/%Y')
                text = msg['text']
                like_count = len(msg['favorited_by'])
                user_id = msg['user_id']
                liked_by = ','.join(msg['favorited_by'])
                writer.writerow([name, created_at, text, like_count, user_id, liked_by])
    except Exception as e:
        print(f"Failed to save messages: {e}")

try:
    messages = fetch_messages(group_id, access_token)
    save_messages_to_csv(messages, 'groupme_chat_history.csv')
    print("Messages have been successfully saved to 'groupme_chat_history.csv'.")
except Exception as e:
    print(f"An error occurred while fetching or saving messages: {e}")
    sys.exit(1)

