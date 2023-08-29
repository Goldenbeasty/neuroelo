elo_mappings = [
    { ### The 0th object in this list MUST be the std message token weight
        "name": "stdmessage token",
        "elo_award": 2,
        "re": [
            r"^\[\d{2}:\d{2}:\d{2}\]  (\w+): (.*)$", 
            r"^\[\d{2}:\d{2}:\d{2}\] (\S+ \S+): (.*)$"]
    },
    {
        "name": "Gifted sub",
        "elo_award": 150,
        "re": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) gifted a Tier [123] sub to \S*$",
               r"^\[\d{2}:\d{2}:\d{2}\] (\S*) gifted a Tier [123] sub to \S*! This is their first Gift Sub in the channel!$"]
    },
    {
        "name": "std sub",
        "elo_award": 75,
        "re": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed (?:with Prime|at Tier [123]). They've subscribed for \d* months(?:!|, currently on a \d* month streak!)$",
               r"^\[\d{2}:\d{2}:\d{2}\] (\S*) {1,2}subscribed with Prime.$",
               r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed at Tier [123].$", r"^\[\d{2}:\d{2}:\d{2}\] (\S*)  subscribed at Tier [123]\. They've subscribed for \d* months(?:!|, currently on a \d* month streak!)$",
               r"^\[\d{2}:\d{2}:\d{2}\] (\S*) converted from a Prime sub to a Tier [123] sub!$"]
    },
    {
        "name": "system message",
        "elo_award": None,
        "re": [
            r"^# Start logging at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \S*$",
            r"^\[\d{2}:\d{2}:\d{2}\] connected$",
            r"^\[\d{2}:\d{2}:\d{2}\] disconnected$",
            r"^\[\d{2}:\d{2}:\d{2}\] (\S*) is live!$",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* gifted a Tier [123] sub to \S*! They have given \d* Gift Subs in the channel!$",
            r"^\[\d{2}:\d{2}:\d{2}\] [MTWFS][a-z]*, \d{1,2} [JFMASOND][a-z]* \d{4}$",
            r"^\[\d{2}:\d{2}:\d{2}\] Server connection timed out, reconnecting$",
            r"^\[\d{2}:\d{2}:\d{2}\] (?:Twitch subscriber|BetterTTV channel|7TV channel) emotes reloaded\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* is continuing the Gift Sub they got from \S*!$",
            r"^\[\d{2}:\d{2}:\d{2}\] (?:\S*) is now offline\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] You were timed out for (?:\d+\w+ ?)$",
            r"^\[\d{2}:\d{2}:\d{2}\] An anonymous user gifted a Tier [123] sub to \S*$", r"^\[\d{2}:\d{2}:\d{2}\] \S* added 7TV emote \S*\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] Failed to fetch (?:BetterTTV|FrankerFaceZ|7TV) channel emotes. \(unknown error\)$",
            r"^\[\d{2}:\d{2}:\d{2}\] This room is now in slow mode. You may send messages every \d* \S*\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] Failed to load channel badges - OAuth token is missing$",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* is paying forward the Gift they got from \S* to (?:the community|\S*)!$",
            r"^\[\d{2}:\d{2}:\d{2}\] This room is no longer in slow mode.$", r"^\[\d{2}:\d{2}:\d{2}\] This channel has no \w* channel emotes\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] Login expired for user \"\S*\"! Try adding your account again\.",
            r"^\[\d{2}:\d{2}:\d{2}\] (\S*) gifted \d* months of Tier [123] to \S*\. They've gifted \d* months in the channel!$",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* is gifting \d* Tier [123] Subs to \S*'s community! They've gifted a total of \d* in the channel!$",
            r"^\[\d{2}:\d{2}:\d{2}\] Twitch Servers requested us to reconnect, reconnecting$", r"^\[\d{2}:\d{2}:\d{2}\] Message history service unavailable \(Error \d*\)$",
            r"^\[\d{2}:\d{2}:\d{2}\] This room is in slow mode and you are sending messages too quickly\. You will be able to talk again in \d* seconds\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* just earned a new \d*K Bits badge!$",
            r"^\[\d{2}:\d{2}:\d{2}\] Streamer Mode is set to Automatic, but pgrep is missing\. Install it to fix the issue or set Streamer Mode to Enabled or Disabled in the Settings\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] Message history service recovering, there may be gaps in the message history\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] An anonymous user is gifting \d* Tier [123] Subs to \S*'s community!$", r"^\[\d{2}:\d{2}:\d{2}\] \S* renamed 7TV emote \S* to \S*\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] Your message wasn't posted due to conflicts with the channel's moderation settings\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] Failed to load channel badges - An unknown error has occurred\.",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* removed 7TV emote \S*\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] Your message was not sent because it is identical to the previous one you sent, less than 30 seconds ago\.$",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* is gifting \d* Tier [123] Subs to \S*'s community!$",
            r"^\[\d{2}:\d{2}:\d{2}\] \S* is paying forward the Gift they got from an anonymous gifter to the community!$",
            r"^\[\d{2}:\d{2}:\d{2}\] You are sending messages too quickly\.$"]
    },
    {
        "name": "timeout",
        "elo_award": -50,
        "re": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) has been timed out for(?: \d*\w)*\.$"]
    },
    {
        "name": "permaban",
        "elo_award": -10000,
        "re": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) has been permanently banned\.$"]
    },
    {
        "name": "channelredeem",
        "elo_award": 100,
        "re": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) redeemed .*$"]
    },
    {
        "name": "incoming raid",
        "elo_award": 100,
        "re": [r"^\[\d{2}:\d{2}:\d{2}\] \d* raiders from (\S*) have joined!$"]
    },
    {
        "name": "some sort of error",
        "elo_award": None,
        "re": [r"^\[\d{2}:\d{2}:\d{2}\]$"]
    }
]
