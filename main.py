import json, requests, sys

def delete_messages(auth, id, user, messages):
    count = 0
    for message in messages:
        if delete_from_all_users or message["author"]["username"] == user:
            requests.delete("http://canary.discordapp.com/api/v6/channels/"
                    + id + "/messages/" + message["id"],
                    headers={"authorization": auth})
            count += 1
    
    print(str(count) + " messages deleted")

# iteratively find and delete all messages in a channel, 100 at a time
def traverse_messages(auth, id, user, last=""):
    count = 0
    while True:
        # first method call, start from beginning (might be able to remove)
        if not last:
            messages = json.loads(requests.get(
                "http://canary.discordapp.com/api/v6/channels/"
                + id + "/messages",
                headers={"authorization": auth}, params={"limit": 100}).content)
        else:
            messages = json.loads(requests.get(
                "http://canary.discordapp.com/api/v6/channels/"
                + id + "/messages", headers={"authorization": auth},
                params={"before" : last, "limit" : 100}).content)

        count += len(messages)
        delete_messages(auth, id, user, messages);

        if len(messages) < 100:
            print("got to end of channel at " + str(count) + " messages")
            break
        else:
            last = sorted(messages, key=lambda x: x["timestamp"],
                    reverse=True)[-1]["id"]

x = """  __    __
 /' \  /' \\
/\_, \/\_, \\
\/_/\ \/_/\ \\
   \ \ \ \ \ \\
    \ \_\ \ \_\\
     \/_/  \/_/
"""

if __name__ == '__main__':
    print(x)

    print("--- 11's discord deleter thing ---")
    print("clears all of your messages in a channel")
    if len(sys.argv) > 1 and sys.argv[1] == "config":
        with open('config.json') as json_data:
            data = json.load(json_data)
        username = data["username"]
        auth_token = data["auth_token"]
        channel_id = data["channel_id"]
        delete_from_all_users = data["delete_from_all"]
    else:
        print("in order for this script to work properly the channel id, " +
                "auth token, and username is required")
        username = input("username: ")
        auth_token = input("auth token: ")
        channel_id = input("channel id: ")
        delete_from_all_users = True if input(
                "delete messages from other users (y/n): ") == "y" else False

    traverse_messages(auth_token, channel_id, username)
