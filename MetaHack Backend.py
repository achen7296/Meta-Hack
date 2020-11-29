import random
import time

#Add member to team
def addMember(team, npc):
  team.append(npc)
  percentage = 0.00
  for i in team:
    percentage += i[5]
    if percentage > 1:
        team.remove(npc)
        print("\n" + str(npc[0]) + " cannot be added because the cut would be over 100%") 


#calculates and distributes the total amount of collaboration points team has
def applyBoost(team):
	for i in team:
		if i[2] != 0:
			for j in team:
				if j != i:
					j[1] += i[4]
					j[2] += i[4]

#Remove member from team and removes collab buff if member had collab points
def removeMember(team, idx):
  if team[idx][4] > 0:
    for i in team:
      if i != team[idx]:
        i[1] -= team[idx][4]
        i[2] -= team[idx][4]
  team.remove(team[idx])

#Create tasks for each hackathon 
def createTasks(hackathon):
  tasks = []
  if hackathon[3] == "Frontend":
    if (hackathon[1] == 1):
        for i in range(4): #Each task is separated into two scores that needs to be completed [“Front end”, “Back end”]
          tasks.append([random.randint(0,20),random.randint(0,10)])
    if (hackathon[1] == 2):
        for i in range(5):
          tasks.append([random.randint(0,25),random.randint(0,15)])
    if (hackathon[1] == 3):
        for i in range(6):
          tasks.append([random.randint(0,30),random.randint(0,20)])
  if hackathon[3] == "Backend":
    if (hackathon[1] == 1):
        for i in range(4): #Each task is separated into two scores that needs to be completed [“Front end”, “Back end”]
          tasks.append([random.randint(0,10),random.randint(0,20)])
    if (hackathon[1] == 2):
        for i in range(5):
          tasks.append([random.randint(0,15),random.randint(0,25)])
    if (hackathon[1] == 3):
        for i in range(6):
          tasks.append([random.randint(0,20),random.randint(0,30)])
  return tasks

#Allows user to assign task to each npc
def assignTask(npc, i, tasks):
  count = 0
  if npc[6] == False and npc[3] != 0: #Only 1 task can be assigned to each npc and Once stamina is 0 npc must rest
    npc[6] = True
    while (tasks[i][0] > 0 or tasks[i][1] > 0):
      count += 1
      time.sleep(1)
      print("\n" + str(count)+ " seconds has passed.")
      tasks[i][0] = tasks[i][0] - npc[1]
      tasks[i][1] = tasks[i][1] - npc[2]
    npc[3] -= 1 #Decrements stamina per task done 
    tasks.remove(tasks[i]) #Remove task from task list once completed
    npc[6] = False
    print("\n" + str(npc[0])+ " has completed task " + str(i+1) + " from the " + "hackathon." + "\n They have " + str(npc[3]) + " stamina left.")
  else:
	  print("This member is currently busy or out of stamina")

#Add money to total balance
def moneyAdd(money, team):
    percentage = 0.00
    for i in team:
      percentage += i[5] #Adds up the percentage cut of each member of team
    money += hackathon[2] * (1-percentage) #Calculates amount user will be recieving
    return int(money)

#Submit hackathon project and claim prize 
def submit(hackathon, tasks):
  if len(tasks) == 0: #Checks if all tasks are completed
    print("\nCongratulations you have won " + str(money) + " dollars!")
  else:
    print("\nThere are still tasks to do")

money = 0
team = []
hackathon = None
tasks = []
hackathons=[
	["Who wants to be a hackionare?",1,100, "Frontend"],
	["Hackadoons 2020", 1, 100, "Backend"],
	["Health Hacking", 1, 100, "Backend"],
	["Blockchain Hacks",2,500, "Frontend"],
	["Robot DeFi Hack", 2, 500, "Frontend"],
	["Neural Hackz 1.0",2,500, "Backend"],
	["Hack to the past", 2, 500, "Backend"],
  ["XYZ University Hacks",3,1000,"Frontend"],
	["WiseHack 5.0",3,1000, "Backend"],
	["Sigmund Hacks",3,1000, "Frontend"],
]

npcs= [
 	["Arifur Full Stack Rahman",1, 2, 4, 2, 0.10,False],
	["Andrew Chen",3, 4, 2, 0, 0.10, False],
	["George Haltz", 4, 5, 6, 0, 0.15, False],
	["Jamool from Mumbai",2, 4, 4, 2, 0.15, False],
	["Rima Lawson",3, 3, 2, 2, 0.15, False],
	["Judah Alvarado",2, 2, 1, 2, 0.20, False],
	["Hamza Chong", 4, 1, 5, 0, 0.15, False],
	["Owen Lezon",4, 4, 4, 2, 0.60, False],
	["Salim Shady",1, 2, 2, 0, 0.10, False],
	["Kanye East",3, 2, 3, 1, 0.20, False],
	["Xuyang deadweight Jiang", 0, 0, 0, 0, 1.0, False],
]

while True:
  for i in npcs:
    print("\n"+str(i))
  while len(team) != 5:
    x = input("\nEnter the members' index you want to add: ")
    if int(x) >= len(npcs):
      print('This member is out of range')
    else:
      addMember(team, npcs[int(x)])
      print(str(npcs[int(x)][0]) + " has been added to your team!")
    if len(team) == 5:
      break

  while hackathon == None:
    hackathonNum = input("\nEnter a hackathon index to attempt: ")
    if int(hackathonNum) > len(hackathons):
      print("This hackathon index is out of range")
    else:
      hackathon = hackathons[int(hackathonNum)]
      print("\nYou are currently attempting the " + str(hackathon[0]) + " hackathon!")
    if hackathon != None:
      break

  tasks = createTasks(hackathon)
  print("\nYour current tasks are " + str(tasks))
  while len(tasks) != 0:
    select = input("Please enter the task you want to complete: ")
    member = input("Please enter the member that you want to assign the task to: ")
    assignTask(team[int(member)], int(select), tasks)
    print("\nYour current tasks are " + str(tasks))
  
  moneyAdd(money, team)
  submit(hackathon,tasks)
  break


  




