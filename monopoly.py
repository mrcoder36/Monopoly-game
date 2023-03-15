from colorama import Fore
import sys,time
import random
import os

def sprint (str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

players=[]#players get added to this list
while True:#GETTING ALL THE PLAYERS
  try:
    numOfPlayers=int(input(Fore.WHITE+"How many people do you want to play?: "))
    if numOfPlayers>=2 and numOfPlayers<=8:
      if numOfPlayers >=2:
        p1=input(Fore.WHITE+"Player 1: "+Fore.LIGHTYELLOW_EX)
        players.append(Fore.LIGHTYELLOW_EX+p1)
        p2=input(Fore.WHITE+"Player 2: "+Fore.CYAN)
        players.append(Fore.CYAN+p2)
      if numOfPlayers >=3:
        p3=input(Fore.WHITE+"Player 3: "+Fore.RED)
        players.append(Fore.RED+p3)
      if numOfPlayers >=4:
        p4=input(Fore.WHITE+"Player 4: "+Fore.GREEN)
        players.append(Fore.GREEN+p4)
      if numOfPlayers >=5:
        p5=input(Fore.WHITE+"Player 5: "+Fore.MAGENTA)
        players.append(Fore.MAGENTA+p5)
      if numOfPlayers >=6:
        p6=input(Fore.WHITE+"Player 6: "+Fore.WHITE)
        players.append(Fore.WHITE+p6)
      if numOfPlayers >=7:
        p7=input(Fore.WHITE+"Player 7: "+Fore.BLACK)
        players.append(Fore.BLACK+p7)
      if numOfPlayers ==8:
        p8=input(Fore.WHITE+"Player 8: "+Fore.YELLOW)
        players.append(Fore.YELLOW+p8)
      break
    else:
      print(Fore.RED+"ERROR! MUST HAVE FROM 2 TO 8 PLAYERS!")
  except:
    print(Fore.RED+"ERROR! Try again!")
#the whole board
board=[["GO","no"],["Old Kent Road",60],["Community Chest","no"],["Whitechapel Road",60],["Income Tax","no"],["Kings Cross Station",200],["The Angel Islington",100],["CHANCE","no"],["Euston Road",100],["Pentonville Road",120],["Just Visiting","no"],["Pall Mall",140],["Electric Company",150],["Whitehall",140],["Northumberl'd Avenue",160],["Marylebone Station",200],["Bow Street",180],["COMMUNITY CHEST","no"],["Marleborough Street",180],["Vine Street",200],["Free Parking","no"],["Strand",220],["CHANCE","no"],["Fleet Street",220],["Trafalgar Square",240],["Frenchurch Street Station",200],["Leicester Square",260],["Coventry Street",260],["Water Works",150],["Piccadilly",280],["Go To Jail","no"],["Regent Street",300],["Oxford Street",300],["Community Chest","no"],["Bond Street",320],["Liverpool Street Station",200],["CHANCE","no"],["Park Lane",350],["Super Tax","no"],["Mayfair",400]]
#checks if someone owns this [property][who owns]
available=[["GO",""],["Old Kent Road",""],["Community Chest",""],["Whitechapel Road",""],["Income Tax",""],["Kings Cross Station",""],["The Angel Islington",""],["CHANCE",""],["Euston Road",""],["Pentonville Road",""],["Just Visiting",""],["Pall Mall",""],["Electric Company",""],["Whitehall",""],["Northumberl'd Avenue",""],["Marylebone Station",""],["Bow Street",""],["COMMUNITY CHEST",""],["Marleborough Street",""],["Vine Street",""],["Free Parking",""],["Strand",""],["CHANCE",""],["Fleet Street",""],["Trafalgar Square",""],["Frenchurch Street Station",""],["Leicester Square",""],["Coventry Street",""],["Water Works",""],["Piccadilly",""],["Go To Jail",""],["Regent Street",""],["Oxford Street",""],["Community Chest",""],["Bond Street",""],["Liverpool Street Station",""],["CHANCE",""],["Park Lane",""],["Super Tax",""],["Mayfair",""]]
#prices starting from rent price going onward...
prices=[["no"],[2,10,30,90,160,250],["no"],[4,20,60,180,320,450],["no"],[25,50,100,200],[6,30,90,270,400,550],["no"],[6,30,90,270,400,550],[8,40,100,300,450,600],["no"],[10,50,150,450,625,750],[4,10],[10,50,150,450,625,750],[12,60,180,500,700,900],[25,50,100,200],[14,70,200,550,750,950],["no"],[14,70,200,550,750,950],[16,80,220,600,800,1000],["no"],[18,90,250,700,875,1050],["no"],[18,90,250,700,875,1050],[20,100,300,750,925,1100],[25,50,100,200],[22,110,330,800,975,1150],[22,110,330,800,975,1150],[4,10],[24,120,360,850,1025],["no"],[26,130,390,900,1100,1275],[26,130,390,900,1100,1275],["no"],[28,150,450,1000,1200,1400],[25,50,100,200],["no"],[35,175,500,1100,1300,1500],["no"],[50,200,600,1400,1700,2000]]
#starting board positions
bPos=[0,0,0,0,0,0,0,0]
#who owns what
own=[[],[],[],[],[],[],[],[]]
money=[1500,1500,1500,1500,1500,1500,1500,1500]#money of every player

while True:
  for x in range(numOfPlayers):
    os.system("clear")
    input(Fore.WHITE+"Click <ENTER> to begin your go... ")
    while True:
      print(players[x])
      input("<enter> to roll ")
      die1=random.randint(1,6)
      die2=random.randint(1,6)
      if die1==die2:
        print("You rolled a double! Roll again...")
        bPos[x]=die1+die2+bPos[x]
      else:
        bPos[x]=die1+die2+bPos[x]
        break
        
    if bPos[x] >= 40:
      bPos[x]=bPos[x]-40
    #giving people money at the start of your turn
    if available[bPos[x]][0]=="":
      if players[available[bPos[x]][1]]==players[x]:
        pass
      else:
        print("You landed on the property of",players[available[bPos[x]][1]])
        money[available[bPos[x]][1]]=money[available[bPos[x]][1]]+prices[bPos[x]][0]
 # type: ignore       #currently no houses or hotels etc...
        money[x]=money[x]-prices[bPos[x]][0]
    while True:#Turn fully begins here
      os.system("clear")
      print(players[x])
      print("$",money[x])
      print("Landed on",board[bPos[x]][0])
      if board[bPos[x]][1]=="no":
        print("\nwhat would you like to do?\n(1)Buying is unavailable here!\n(2)Morgage(CURRENTLY UNAVAILABLE)\n(3)Check properties\n(4)End turn\n(5)Bankrupt")
      else:
        print("\nwhat would you like to do?\n(1)Buy for",board[bPos[x]][1],"\n(2)Morgage(CURRENTLY UNAVAILABLE)\n(3)Check properties\n(4)End turn\n(5)Bankrupt")
      while True:
        try:
          wyd=int(input(">> "))
          break
        except:
          print("ERROR! TRY AGAIN")
          
      if wyd==1:
        if board[bPos[x]][1]=="no":
          print("This cannot be bought!")
        elif board[bPos[x]][0] != available[bPos[x]][0]:
          print("This property is already owned by",players[available[bPos[x]][1]],"!")
        else:
          if money[x] >= board[bPos[x]][1]:
            money[x]=money[x]-board[bPos[x]][1]
            own[x].append(available[bPos[x]][0])
            available[bPos[x]][0]=""
            print("You successfully bought",board[bPos[x]][0])
            available[bPos[x]][1]=x
          else:
            print("You cannot afford this!")

      elif wyd==2:
        pass

      elif wyd==3:
        print("You currently own the following: ",own[x])

      elif wyd==4:
        if money[x]>=0:
          break
        else:
          print("You cannot end your go with negative cash!")
      elif wyd==5:
        if money[x]<0:
          print("You Lose!")
          players.pop(x)
          money.pop(x)
          if len(players)==1:
            print(players[0],"is the Winner!")
            sys.exit()
        else:
          print("You can only bankrupt with a negative balance!")
      else:
        print("Unavailable!")
      input("<ENTER> to continue...")
