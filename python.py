answers_tuple = ("yes", "no", "Full mark", "Within 24 hours ?", "Yes or No: ", 
                 "Is there a valid reason for Late Submission ? ", "MC\nAccepted? ",
                 "-10 marks from overall mark but not below 40", "Submitted within 5 days ?",
                 "Is there a valid reason ?", "MC (late submission option)\n Accepted ?", "Mark = 0",
                 "MC(non-deferral) before specified deadline\nAccepted\nDeferral reassessment",
                 "Did you submitted Cw Submission on Time ?")

print(answers_tuple[13])
answer = input(answers_tuple[4])
if answer.lower() == answers_tuple[0]:
    print(answers_tuple[2])
    exit(0)

else:
    print(answers_tuple[3])
    answer = input(answers_tuple[4])
    if answer.lower() == answers_tuple[0]:
        print(answers_tuple[5])

        answer = input(answers_tuple[4])
        if answer.lower() == answers_tuple[0]:
            print(answers_tuple[6])
            answer = input(answers_tuple[4])
            if answer.lower() == answers_tuple[0]:
                print(answers_tuple[2])
            else:
                print(answers_tuple[7])
        else:
            print(answers_tuple[7])
    else:
        print(answers_tuple[8])
        answer = input(answers_tuple[4])

        if answer.lower() == answers_tuple[0]:
            print(answers_tuple[9])
            answer = input(answers_tuple[4])
            if answer.lower() == answers_tuple[0]:
                print(answers_tuple[10])
                answer = input(answers_tuple[4])
                if answer.lower() == answers_tuple[0]:
                    print(answers_tuple[2])
                else:
                    print(answers_tuple[11])
            else:
                print(answers_tuple[11])
        else:
            print(answers_tuple[9])
            answer = input(answers_tuple[4])
            if answer.lower() == answers_tuple[0]:
                print(answers_tuple[12])
            else:
                print(answers_tuple[11])

