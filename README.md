# Groupme stat

This project allows you to download the entire groupme group chat into a csv file, which includes Name, Date, Message, Like Count, User Id, and Liked by (list of user_id(s)) (```export_groupme_stat.py```)

I also provided some examples on how you can use the csv file to get the stats 

### Get group id: 

```
curl -s -H "X-Access-Token: YOUR_ACCESS_TOKEN" "https://api.groupme.com/v3/groups" | jq '.response[] | select(.name=="Group_Name") | .id'
```

### Get Access Token:

[Developer Portal](https://dev.groupme.com/)

### File description

```export_groupme_stat.py``` download the entire group converation into a csv file which includes Name, Date, Message, Like Count, User Id, and Liked by (list of user_id(s))

```total_message.py``` give top 30 people who have the most message sent

```total_likes_received.py ``` give top 30 people who were given the most likes

```self_liked.py ``` give the top 30 who self-liked the most

```likes_per_message.py ``` give the ratio of likes per message and give top 30 people who have the most likes per message

```like_sent.py ``` give top 30 people who have given the most likes

```aver_char.py``` give the top 30 people who has the highest average character per message 

```GraphicalData.ipynb``` Make the graph for all these data in google colab and jupyter notebook

```moreStat.py``` give the percentage of messages that have 0 likes and the message that has the most likes

Create a pull request or an issue to request more/diff stats
