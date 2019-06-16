import csv


def ShowPlayer(TotalPlayers):
  for player in TotalPlayers:
    print("{}, {}, {}".format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))
    
def ReadPlayersFile(file):
   with open(file, newline = '') as csvfile:
      filereader = csv.DictReader(csvfile)
      return list(filereader)
    
def divideEXandNoEX(totalplayer):
  PlayerWEx = []
  PlayerWOEx = []
  # get two list, player with experience and player without experience
  for Player in TotalPlayers:
    if Player['Soccer Experience'] == 'YES':
      PlayerWEx.append(Player)
    else:
      PlayerWOEx.append(Player)

  return PlayerWEx, PlayerWOEx

def AssignPlayers(Players,league):
  while Players != []:
    for team, players in league.items():
      players.append(Players.pop())
      
  return league

def ExportLeague(league):
  with open("teams.txt", 'w') as file:
    for team, players in league.items():
      file.write("{}\n".format(team))
      for player in players:
        file.write("{}, {}, {}\n".format(player['Name'], player['Soccer Experience'], player['Guardian Name(s)']))

        
def WelcomeLetter(team,player):
  name = []
  name = player['Name'].split()
  with open("{}_{}.txt".format(name[0].lower(),name[1].lower()), 'w') as file:
    file.write("Dear {}\n\n".format(player['Guardian Name(s)']))
    file.write(" we are happy to invite {} to join team \"{}\".\n The first practice time is 2019/06/15 06:00 AM.\n Looking forward to see you.\n\n".format(player['Name'],team))
    file.write("Sincerely\nSoccer League")    

    
if __name__ == "__main__":

  #get file data
  TotalPlayers = ReadPlayersFile("soccer_players.csv")
  #divide experienced player and non-experienced players
  ExpPlayers , NoExpPlayers = divideEXandNoEX(TotalPlayers)
      
  #ShowPlayer(ExpPlayers)
  #ShowPlayer(NoExpPlayers)
  # create league
  league = {'Dragons': [], 'Sharks':[], 'Raptors':[]}
  
  # assign players to league
  league = AssignPlayers(ExpPlayers,league)
  league = AssignPlayers(NoExpPlayers,league)

  print('Dragons')
  ShowPlayer(league['Dragons'])
  print('Sharks')
  ShowPlayer(league['Sharks'])
  print('Raptors')
  ShowPlayer(league['Raptors'])
  
  ExportLeague(league)
  
  
  # Extra Credit create welcome letter
  for team, players in league.items():
    for player in players:
      WelcomeLetter(team,player)
  
