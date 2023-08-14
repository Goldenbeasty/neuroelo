import os
import sys
import json
import time
import subprocess

OUTPUT_BASE_DIR = "neuroelo_web"
NUMBER_OF_TOP_SPOTS = 20
DEBUG = False

# not being in the root dir thing
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

import main

def get_git_commit_hash():
    try:
        commit_hash = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode("utf-8").strip()
        return commit_hash
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

def check_dir(dir: str) -> None:
    if not os.path.exists(dir):
        os.makedirs(dir)

def generate_api():
    ### Load the chat logs into memory
    chatlist = os.listdir(main.chatpath)
    chatlog = []
    elolist = {}
    for file in chatlist:
        with open(os.path.join(main.chatpath, file)) as f:
            this = f.readlines()
        for line in this:
            chatlog.append(line.strip())

    ## time to assign elos
    for message in chatlog:
        grade = main.grade_elo(message)
        if grade:
            user, elo_delta = grade
            user = user.capitalize()
            if user in elolist:
                elolist[user]["elo"] += elo_delta
                elolist[user]["messages"].append([message, elo_delta])
            else:
                elolist[user] = {}
                elolist[user]["elo"] = elo_delta
                elolist[user]["messages"] = [[message, elo_delta]]

    # Check and create the directories
    web_root_dir = os.path.join(current_dir, OUTPUT_BASE_DIR)
    api_dir = os.path.join(current_dir, OUTPUT_BASE_DIR, "api")
    user_dir = os.path.join(api_dir, "user")
    check_dir(web_root_dir)
    check_dir(api_dir)
    check_dir(user_dir)

    # Create the dataset for the ranking table
    ranking = {name: data["elo"] for name, data in elolist.items()}
    ranking = dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))
    ranking_spot = list(ranking.keys())

    # Create the /api/user/{username} data
    for user, data in elolist.items():
        data["messages"] = sorted(data["messages"], key=lambda item: item [1], reverse=True)
        data["ranking"] = ranking_spot.index(user) + 1
        if DEBUG:
            json.dump(data, open(os.path.join(user_dir, user), "w"), indent=4)
            continue
        json.dump(data, open(os.path.join(user_dir, user), "w"))

    # Dump the ranking table dataset
    elolist = ranking
    json.dump(elolist, open(os.path.join(api_dir, "user_list"), "w"))

    # And grab the top NUMBER_OF_TOP_SPORTS of the ranking table
    toplist = dict(list(elolist.items())[:NUMBER_OF_TOP_SPOTS])
    json.dump(toplist, open(os.path.join(api_dir, "top_list"), "w"))

    # Create the info data for the website
    commit_hash = get_git_commit_hash()
    if commit_hash:
        print("Current commit hash:", commit_hash)
    else:
        print("Failed to retrieve commit hash.")

    sysinfo = {
        "Debug": DEBUG,
        "generated at": int(time.time()),
        "message count": len(chatlog),
        "tracked users": len(elolist),
        "git hash": commit_hash
    }
    json.dump(sysinfo, open(os.path.join(api_dir, "info"), "w"))
    json.dump(chatlist, open(os.path.join(api_dir, "log_list"), "w"))

if __name__ == "__main__":
    generate_api()
