def parse_script(script):
    KW = ["users\n", "MORAL\n"]
    SEPLINE = "\n"
    users = []
    parsed_script = []
    currUser = ""
    moral = ""
    nmoral = False
    userC = False
    # loop through lines
    for i, line in enumerate(script):
        if line == SEPLINE:
            userC = False
            nmoral = False
            currUser = ""
            continue

        if userC:
            users.append(line.strip() + "\n")
            continue
        
        if nmoral:
            moral = line.strip()
            continue

        if line in KW:
            if line == "users\n":
                currUser = ""
                userC = True
                continue
            if line == "MORAL\n":
                currUser = ""
                nmoral = True
                continue

        if line in users:
            currUser = line.strip()
            continue
        
        parsed_script.append({
            "lineNum": str(i+1),
            "userSpeaking": currUser,
            "content": line     
        })

    return parsed_script, moral, users


