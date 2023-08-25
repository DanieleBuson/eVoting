questions = {
    "1": "How important is the e-voting election?",
    "2": "Are voters prepared and properly iinformed about the elections (and about e-voting)? (generally speaking)",
    "3": "How can a voter authenticate to the system?",
    "4": "What kind of information does the voter provide to authenticate to the system?",
    "5": "What is the kind of the election?"
}

answers = {
    "1": ["Extremely important (ex. national elections)", 
          "Important (ex.local elections)",
          "Relatively important (ex. student elections)"],
    "2": ["Informed about the elections and evoting", 
          "Informed about elections but not really prepared to evoting", 
          "Able to e-vote but not enough informed about the election", 
          "Not informed about the election and no clue on how e-vote"],
    "3": ["Blockchain Authentication Method",
          "Third parties Authentication with encryption",
          "Third parties Authentication without encryption",
          "Locally created website/phone application"],
    "4": ["Personal and sensitive data",
          "Just the main information (name, surname, age)",
          "Externally provided access code (anonymous)",
          "Externally provided access code (personal access code)",
          "No information needed"],
    "5": ["Controlled, only e-voting",
          "Uncontrolled, only e-voting",
          "Controlled, e-voting + papers",
          "Uncontrolled, e-voting + paper"],

}

done = False
while not done:
    print("Write the answer number in the space below, write stop to exit.\n")
    risk_count = 0
    risk_max = 0
    print(questions["1"], "\n")
    possible_answers = []
    for i in range(len(answers["1"])):
        print(i+1, " - ", answers["1"][i], "\n")
        possible_answers.append(str(i+1))
    answer = input("Insert here your answer:   ")
    print("\n")
    if answer == "stop":
        done = True
        continue
    elif answer not in possible_answers:
        print("Do not joke with me, I killed so many people...\n")
        answer = input("Insert here your answer, AGAIN:   ")
        print("\n")
        while answer not in possible_answers:
            print("Do not joke with me, I killed so many people...\n")
            answer = input("Insert here your answer, AGAIN:   ")
            print("\n")
    elif answer == "1" or answer == "2":
        if answer == "1":
            risk_count += 3
        if answer == "2":
            risk_count += 2
        risk_max += 3
        print(questions["2"], "\n")
        possible_answers = []
        for i in range(len(answers["2"])):
            print(i+1, " - ", answers["2"][i], "\n")
            possible_answers.append(str(i+1))
        answer = input("Insert here your answer:   ")
        print("\n")
        if answer == "stop":
            done = True
            continue
        elif answer not in possible_answers:
            print("Do not joke with me, I killed so many people...\n")
            answer = input("Insert here your answer, AGAIN:   ")
            print("\n")
            while answer not in possible_answers:
                print("Do not joke with me, I killed so many people...\n")
                answer = input("Insert here your answer, AGAIN:   ")
                print("\n")
        if answer in possible_answers:
            if answer == "1":
                risk_count += 1
            if answer == "2":
                risk_count += 4
            if answer == "3":
                risk_count += 3
            if answer == "4":
                risk_count += 6
            risk_max += 6
            print(questions["3"], "\n")
            possible_answers = []
            for i in range(len(answers["3"])):
                print(i+1, " - ", answers["3"][i], "\n")
                possible_answers.append(str(i+1))
            answer = input("Insert here your answer:   ")
            print("\n")
            if answer == "stop":
                done = True
                continue
            elif answer not in possible_answers:
                print("Do not joke with me, I killed so many people...\n")
                answer = input("Insert here your answer, AGAIN:   ")
                print("\n")
                while answer not in possible_answers:
                    print("Do not joke with me, I killed so many people...\n")
                    answer = input("Insert here your answer, AGAIN:   ")
                    print("\n")
            elif answer in possible_answers:
                if answer == "1":
                    risk_count += 1
                if answer == "2":
                    risk_count += 2
                if answer == "3":
                    risk_count += 5
                if answer == "4":
                    risk_count += 6
                risk_max += 6
                print(questions["4"], "\n")
                possible_answers = []
                for i in range(len(answers["4"])):
                    print(i+1, " - ", answers["4"][i], "\n")
                    possible_answers.append(str(i+1))
                answer = input("Insert here your answer:   ")
                print("\n")
                if answer == "stop":
                    done = True
                    continue
                elif answer not in possible_answers:
                    print("Do not joke with me, I killed so many people...\n")
                    answer = input("Insert here your answer, AGAIN:   ")
                    print("\n")
                    while answer not in possible_answers:
                        print("Do not joke with me, I killed so many people...\n")
                        answer = input("Insert here your answer, AGAIN:   ")
                        print("\n")
                elif answer in possible_answers:
                    if answer == "1":
                        risk_count += 5
                    if answer == "2":
                        risk_count += 2
                    if answer == "3":
                        risk_count += 1
                    if answer == "4":
                        risk_count += 3
                    if answer == "5":
                        risk_count += 1
                    risk_max += 5
                    print(questions["5"], "\n")
                    possible_answers = []
                    for i in range(len(answers["5"])):
                        print(i+1, " - ", answers["5"][i], "\n")
                        possible_answers.append(str(i+1))
                    answer = input("Insert here your answer:   ")
                    print("\n")
                    if answer == "stop":
                        done = True
                        continue
                    elif answer not in possible_answers:
                        print("Do not joke with me, I killed so many people...\n")
                        answer = input("Insert here your answer, AGAIN:   ")
                        print("\n")
                        while answer not in possible_answers:
                            print("Do not joke with me, I killed so many people...\n")
                            answer = input("Insert here your answer, AGAIN:   ")
                            print("\n")
                    elif answer in possible_answers:
                        if answer == "1":
                            risk_count += 2
                        if answer == "2":
                            risk_count += 4
                        if answer == "3":
                            risk_count += 1
                        if answer == "4":
                            risk_count += 3
                        risk_max += 4
                        print("\n\nDone! The system has calculated that your evoting ethical risk is : ", risk_count/risk_max, "\n\n")
                        done=True
    
    
    elif answer == "3":
        risk_count += 1
        risk_max += 3
        print(questions["3"], "\n")
        possible_answers = []
        for i in range(len(answers["3"])):
            print(i+1, " - ", answers["3"][i], "\n")
            possible_answers.append(str(i+1))
        answer = input("Insert here your answer:   ")
        print("\n")
        if answer == "stop":
            done = True
            continue
        elif answer not in possible_answers:
            print("Do not joke with me, I killed so many people...\n")
            answer = input("Insert here your answer, AGAIN:   ")
            print("\n")
            while answer not in possible_answers:
                print("Do not joke with me, I killed so many people...\n")
                answer = input("Insert here your answer, AGAIN:   ")
                print("\n")
        if answer in possible_answers:
            if answer == "1":
                risk_count += 1
            if answer == "2":
                risk_count += 2
            if answer == "3":
                risk_count += 5
            if answer == "4":
                risk_count += 6
            risk_max += 6
            print(questions["4"], "\n")
            possible_answers = []
            for i in range(len(answers["4"])):
                print(i+1, " - ", answers["4"][i], "\n")
                possible_answers.append(str(i+1))
            answer = input("Insert here your answer:   ")
            print("\n")
            if answer == "stop":
                done = True
                continue
            elif answer not in possible_answers:
                print("Do not joke with me, I killed so many people...\n")
                answer = input("Insert here your answer, AGAIN:   ")
                print("\n")
                while answer not in possible_answers:
                    print("Do not joke with me, I killed so many people...\n")
                    answer = input("Insert here your answer, AGAIN:   ")
                    print("\n")
            elif answer in possible_answers:
                if answer == "1":
                    risk_count += 5
                if answer == "2":
                    risk_count += 2
                if answer == "3":
                    risk_count += 1
                if answer == "4":
                    risk_count += 3
                if answer == "5":
                    risk_count += 1
                risk_max += 5
                print(questions["5"], "\n")
                possible_answers = []
                for i in range(len(answers["5"])):
                    print(i+1, " - ", answers["5"][i], "\n")
                    possible_answers.append(str(i+1))
                answer = input("Insert here your answer:   ")
                print("\n")
                if answer == "stop":
                    done = True
                    continue
                elif answer not in possible_answers:
                    print("Do not joke with me, I killed so many people...\n")
                    answer = input("Insert here your answer, AGAIN:   ")
                    print("\n")
                    while answer not in possible_answers:
                        print("Do not joke with me, I killed so many people...\n")
                        answer = input("Insert here your answer, AGAIN:   ")
                        print("\n")
                elif answer in possible_answers:
                    if answer == "1":
                        risk_count += 2
                    if answer == "2":
                        risk_count += 4
                    if answer == "3":
                        risk_count += 1
                    if answer == "4":
                        risk_count += 3
                    risk_max += 4
                    print("\n\nDone! The system has calculated that your evoting ethical risk is : ", risk_count/risk_max, "\n\n")
                    done=True
    
    