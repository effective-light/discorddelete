# discorddelete
###### a tool to delete messages from any discord channel (that you have permissions to)

## How do I get my auth token and channel id?
I currently do not have an automated way of grabbing these so I generally do it by hand in inspect element.
Press Control + Shift + i to open inspect element and select the network tab.
Filter it to XHR only in order to not get spammed by requests you dont care about.
Find either a `typing` or `messages` request and select it. The auth token is under request headers > authorization,
and the channel id is in the request url (`http://discordapp.com/api/v6/channel_id/request`)

I may look into automating this through better discord or some sort of js that you can paste into the console.
We'll see :crystal_ball:

## Usage
Either just run the script using `python main.py`
OR
Create a JSON file with the following format next to the script, and run the script with your JSON file as the single argument.
```json
{
    "username": "username#0000",
    "auth_token": "abcdefghijklmnopqrstuvwxyz123543564364576234",
    "channel_id": "12345678910123456",
    "delete_from_all": "True"
}
```

`python main.py jsonfile.json`