# KON BANEGA CROREPATI
# A terminal-based quiz game using basic Python concepts

# Prize money for each question

prize = [1000000, 2000000, 4000000, 8000000, 10000000]

# QUES1
ques1 = ["Which planet is known as the Red Planet?"]
option1 = ["a = Earth", "b = Mars", "c = Jupiter", "d = Venus"]
print("QUES1.", ques1[0])
print("Options:", *option1, sep="\n")
ans1 = input("enter ans: ").lower()
print()

if ans1 == "b":
    print("sahi 10 lakh")
    win1 = prize[0]
else:
    print("glt utar")
    win1 = 0
print()

# QUES2
ques2 = ["What is the capital of Australia?"]
option2 = ["a = Sydney", "b = Canberra", "c = Melbourne", "d = Perth"]
print("QUES2.", ques2[0])
print("Options:", *option2, sep="\n")
ans2 = input("enter ans: ").lower()
print()

if ans2 == "b":
    print("sahi 20 lakh")
    win2 = prize[1]
else:
    print("glt utar")
    win2 = 0
print()

# QUES3
ques3 = ["Which language is used to style web pages?"]
option3 = ["a = HTML", "b = Python", "c = CSS", "d = SQL"]
print("QUES3.", ques3[0])
print("Options:", *option3, sep="\n")
ans3 = input("enter ans: ").lower()
print()

if ans3 == "c":
    print("sahi 40 lakh")
    win3 = prize[2]
else:
    print("glt utar")
    win3 = 0
print()

# QUES4
ques4 = ["Who painted the Mona Lisa?"]
option4 = ["a = Picasso", "b = Da Vinci", "c = Van Gogh", "d = Rembrandt"]
print("QUES4.", ques4[0])
print("Options:", *option4, sep="\n")
ans4 = input("enter ans: ").lower()
print()

if ans4 == "b":
    print("sahi 80 lakh")
    win4 = prize[3]
else:
    print("glt utar")
    win4 = 0
print()

# QUES5
ques5 = ["Which Indian startup became a unicorn in record time?"]
option5 = ["a = CRED", "b = BYJU’S", "c = Zomato", "d = Paytm"]
print("QUES5.", ques5[0])
print("Options:", *option5, sep="\n")
ans5 = input("enter ans: ").lower()
print()

if ans5 == "a":
    print("1 crore")
    win5 = prize[4]
else:
    print("glt utar")
    win5 = 0
print()

# Final Result
print("AP JEETATE HAI")
totalWin = [win1, win2, win3, win4, win5]
print("Total Winning Amount:", sum(totalWin))

