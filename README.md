# Groupme stat
Most comprehensive Groupme Groupchat csv generator

This project allows you to download the entire groupme group chat into a csv file, which includes Name, Date, Message, Like Count, User Id, Time, Liked by (list of user_id(s)), and Attachments (```export_groupme_stat.py```)

I also provided some examples on how you can use the csv file to get the stats 

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

### Get group id: 

```
curl -s -H "X-Access-Token: YOUR_ACCESS_TOKEN" "https://api.groupme.com/v3/groups" | jq '.response[] | select(.name=="Group_Name") | .id'
```

### Get Access Token:

[Developer Portal](https://dev.groupme.com/)

### File description

```export_groupme_stat.py``` download the entire group converation into a csv file which includes Name, Date, Message, Like Count, User Id, Time, Liked by (list of user_id(s)), and Attachments

### Example Stats

```total_message.py``` give top 30 people who have the most message sent

```total_likes_received.py ``` give top 30 people who were given the most likes

```self_liked.py ``` give the top 30 who self-liked the most

```likes_per_message.py ``` give the ratio of likes per message and give top 30 people who have the most likes per message

```like_sent.py ``` give top 30 people who have given the most likes

```aver_char.py``` give the top 30 people who has the highest average character per message 

```GraphicalData.ipynb``` Make the graph for all these data in google colab and jupyter notebook

```moreStat.py``` give the percentage of messages that have 0 likes and the message that has the most likes

```NickNameChangeAndDate.py``` Shows top 10 most changed nickname and give total messages for each month and year

```removed_user.py``` Shows the top 10 users got removed from the groupchat the most

```LateTexter.py``` Shows the top 10 late texters (from 2am to 4am)

```mostEmojiAttachment.py``` Most emojis and attachements sent

Create a pull request or an issue to request more/diff stats
