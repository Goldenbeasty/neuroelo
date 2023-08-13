import re

with open("final_rankings.txt") as f:
    inputlines = f.readlines()

inputlines = [line.strip() for line in inputlines]

result_dict = {}

for item in inputlines:
    match = re.match(r"^(\d+)\. (\S+|\S+ \S+) \((-?\d+)\)$", item)
    if match:
        name = match.group(2)
        elo = int(match.group(3))
        rank = int(match.group(1))
        player_info = {"elo": elo, "rank": rank, "messages": []}
        result_dict[name.capitalize()] = player_info

import json

json.dump(result_dict, open("temp_data_holder.json", "w"))

