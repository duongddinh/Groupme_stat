# Groupme stat
Most Comprehensive GroupMe Group Chat CSV Generator

This project enables you to download the entire GroupMe group chat into a CSV file. The file includes columns for Name, Date, Message, Like Count, User ID, Time, Liked By (a list of user IDs), and Attachments (via ```export_groupme_stat.py```).

I have also provided some examples of how you can use the CSV file to generate stats.

### Get group id: 

```
curl -s -H "X-Access-Token: YOUR_ACCESS_TOKEN" "https://api.groupme.com/v3/groups" | jq '.response[] | select(.name=="Group_Name") | .id'
```

### Get Access Token:

[Developer Portal](https://dev.groupme.com/)

### Run The script:

Add ```access_token = TOKEN_HERE``` and ```group_id = GROUP_ID_HERE``` to ```export_groupme_stat.py```

and run:

```python3 export_groupme_stat.py```

### File description

```export_groupme_stat.py``` downloads the entire group conversation into a CSV file, which includes Name, Date, Message, Like Count, User ID, Time, Liked By (a list of user IDs), and Attachments."

### Example Stats
```total_message.py``` gives the top 30 people who have sent the most messages.

```total_likes_received.py``` provides the top 30 people who have received the most likes.

```self_liked.py``` identifies the top 30 individuals who have self-liked their messages the most.

```likes_per_message.py``` calculates the ratio of likes per message and lists the top 30 people with the highest likes per message.

```like_sent.py``` displays the top 30 people who have given out the most likes.

```aver_char.py``` reveals the top 30 people with the highest average character count per message.

```GraphicalData.ipynb``` generates graphs for all these data points in Google Colab and Jupyter Notebook.

```moreStat.py``` provides the percentage of messages that have received 0 likes and identifies the message that has received the most likes.

```NickNameChangeAndDate.py``` shows the top 10 nicknames that have been changed the most and provides the total number of messages for each month and year.

```removed_user.py``` highlights the top 10 users who have been removed from the group chat the most.

```LateTexter.py``` identifies the top 10 late texters (from 2 am to 4 am).

```mostEmojiAttachment.py``` identifies who has sent the most emojis and attachments.

## Dependencies:

```python3```

```python
import requests
import csv
import time
import sys
from datetime import datetime
import pandas as pd
import requests
import json
from ast import literal_eval
import matplotlib.pyplot as plt
import emoji
import re

```

do ```pip3 install [Name]```

## More Stats

Create a pull request or an issue to request additional or different statistics.
