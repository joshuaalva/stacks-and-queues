from que import Queue

print("Welcome to Thibodeaux's Tech Triage")
def menu():
    print("Type the number for the action you wish to perform and hit Enter")
    print("1. Open a new ticket")
    print("2. List all open tickets")
    print("3. Close ticket")
    print("4. Review all closed tickets")
    print("5. Review previously closed tickets")
    print("6. Quit")

menu()
myQueue = Queue()
response = input("What do you want to do?")


while(response != "6"):
    if(response == "1"):
        # open a new ticket 
        # 001 pc won't turn on 
        # ticket opened! 
        print("Open a new ticket!")
        userOpenTicket = input("Please enter a 4 digit code: \n")
        userProblem = input("Please describe the problem you are having")
        data = {"Ticket Num" : userOpenTicket, "User Problem" : userProblem }
        myQueue.enqueue(data)
        print(f'Ticket Opened! Ticket Number: {userOpenTicket}, Description: {userProblem}')
    if(response == "2"):
        print(myQueue)
    if(response == "6"):
        print("You have Quit")
        break
