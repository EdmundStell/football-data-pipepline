import random
import json
import itertools


teams = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspurs", "West Ham United", "Wolverhampton Wanderers"]

arsenal_o = ["Oleksandr Zinchenko", "William Saliba", "Gabriel", "Ben White", "Declan Rice", "Thomas Partey", "Martin Odegaard", "Bukayo Saka", "Eddie Nketiah", "Gabriel Martinelli", "Gabriel Jesus"]
aston_villa_o = ["Tyrone Mings", "Matty Cash", "Ezri Konsa", "Carlos", "Douglas Luiz", "John McGinn", "Emiliano Buendia", "Ollie Watkins", "Leon Bailey", "Jacob Ramsey", "Moussa Diaby"]
bournemouth_o = ["Chris Mepham", "Adam Smith", "Lloyd Kelly", "Marcos Senesi", "Lewis Cook", "David Brooks", "Tyler Adams", "Dominic Solanke", "Justin Kluivert", "Antoine Semenyo", "Kieffer Moore"]
brentford_o = ["Rico Henry", "Aaron Hickey", "Ethan Pinnock", "Ben Mee", "Christian Norgaard", "Mathias Jensen", "Frank Onyeka", "Ivan Toney", "Neal Maupay", "Bryan Mbeumo", "Yoane Wissa"]
brighton_o = ["Tariq Lamptey", "Lewis Dunk", "Igor", "Pervis Estupinan", "Pascal Gross", "Adam Lallana", "Billy Gilmour", "Karou Mitoma", "Evan Ferguson", "Danny Welbeck", "James Milner"]
burnley_o = ["Charlie Taylor", "Vitinho", "Dara O'Shea", "Connor Roberts", "Josh Brownhill", "Aaron Ramsey", "Sander Berge", "Jay Rodriguez", "Wout Weghorst", "Nathan Redmond", "Jack Cork"]
chelsea_o = ["Reece James", "Ben Chilwell", "Levi Colwill", "Thiago Silva", "Moises Caicedo", "Cole Palmer", "Romeo Lavia", "Raheem Sterling", "Christopher Nkunku", "Nicolas Jackson", "Malo Gusto"]
crystal_palace_o = ["Joel Ward", "Tyrick Mitchell", "Rob Holding", "Marc Guehi", "Will Hughes", "Micheal Olise", "Jefferson Lerma", "Eberechi Eze", "Jordan Ayew", "Odsonne Edouard", "Jeffrey Schlupp"]
everton_o = ["Ashley Young", "James Tarkowski", "Michael Keane", "Vitali Mykolenko", "Amadou Onana", "Abdoulaye Doucoure", "James Garner", "Dwight McNeil", "Beto", "Dominic Calvert-Lewin", "Youssef Chermiti"]
fulham_o = ["Timothy Castagne", "Kenny Tete", "Calvin Bassey", "Issa Diop", "Harrison Reed", "Tom Cairney", "Joao Palinha", "Raul Jimenez", "Harry Wilson", "Willian", "Adama Traore"] 
liverpool_o = ["Trent Alexander-Arnold", "Virgil Van Dijk", "Joel Matip", "Andrew Robertson", "Dominik Szoboszlai", "Thiago", "Alexis Mac Allister", "Mo Salah", "Darwin Nunez", "Luis Diaz", "Diogo Jota"]
luton_o = ["Tom Lockyer", "Dan Potts", "Teden Mengi", "Mads Andersen", "Ross Barkley", "Marvelous Nakamba", "Tahith Chong", "Calton Morris", "Jacob Brown", "Elijah Adebayo", "Cauley Woodrow"]
manchester_city_o = ["Kyle Walker", "Nathan Ake", "Ruben Dias", "John Stones", "Bernardo Silva", "Kevin De Bruyne", "Rodri", "Erling Haaland", "Julian Alvarez", "Jeremy Doku", "Mateo Kovacic"]
manchester_united_o = ["Luke Shaw", "Lisandro Martinez", "Raphael Varane", "Aaron Wan-Bissaka", "Bruno Fernandes", "Casemiro", "Christian Eriksen", "Rasmus Hojlund", "Antony", "Marcus Rashford", "Alejandro Garnacho"]
newcastle_o = ["Kieran Trippier", "Sven Botman", "Dan Burn", "Lewis Hall", "Bruno Guimares", "Joelinton", "Sandro Tonali", "Miguel Almiron", "Callum Wilson", "Alexander Isak", "Anthony Gordon"]
nottingham_o = ["Joe Worrall", "Neco Williams", "Willy Boly", "Serge Aurier", "Orel Mangala", "Ibrahim Sangare", "Cheikou Kouyate", "Morgan Gibbs-White", "Taiwo Awoniyi", "Callum Hudson-Odoi", "Anthony Elanga"]
sheffield_o = ["George Baldock", "Max Lowe", "Chris Basham", "Yasser Larouci", "John Fleck", "Gustavo Hamer", "Oliver Norwood", "Rhian Brewster", "Oliver McBurnie", "Cameron Archer", "Ismaila Coulibaly"]
spurs_o = ["Christian Romero", "Pedro Porro", "Ben Davies", "Micky van de Ven", "Yves Bissouma", "James Maddison", "Rodrigo Bentancur", "Heung-Min Son", "Dejan Kulusevski", "Richarlison", "Brennan Johnson"]
west_ham_o = ["Aaron Cresswell", "Kurt Zouma", "Vladmir Coufal", "Nayef Aguerd", "James Ward-Prowse", "Mohammed Kudus", "Lucas Paqueta", "Michail Antonio", "Danny Ings", "Jarrod Bowen", "Said Benrahama"]
wolves_o = ["Matt Doherty", "Rayan Ait-Nouri", "Max Dawson", "Max Kilman", "Mario Lemina", "Joao Gomes", "Boubacar Traore", "Pedro Neto", "Hee Chan Hwang", "Matheus Cunha", "Fabio Silva"]

x0 = {"Arsenal": {"goalkeeper":"Aaron Ramsdale", "outfielders": arsenal_o}, "Aston Villa": {"goalkeeper": "Emi Martinez", "outfielders": aston_villa_o}, 
      "Bournemouth": {"goalkeeper": "Neto", "outfielders": bournemouth_o}, "Brentford": {"goalkeeper": "Mark Flekken", "outfielders": brentford_o},
      "Brighton": {"goalkeeper": "Jason Steele", "outfielders": brighton_o}, "Burnley":{"goalkeeper": "James Trafford", "outfielders": burnley_o}, 
      "Chelsea": {"goalkeeper": "Robert Sanchez", "outfielders": chelsea_o}, "Crystal Palace": {"goalkeeper": "Sam Johnstone", "outfielders": crystal_palace_o}, 
      "Everton": {"goalkeeper": "Jordan Pickford", "outfielders": everton_o}, "Fulham": {"goalkeeper": "Bernd Leno", "outfielders": fulham_o}, 
      "Liverpool":{"goalkeeper":"Allison", "outfielders": liverpool_o}, "Luton": {"goalkeeper": "Tim Krul", "outfielders": luton_o}, 
      "Manchester City":{"goalkeeper":"Ederson", "outfielders": manchester_city_o}, "Manchester United": {"goalkeeper": "Andre Onana", "outfielders": manchester_united_o}, 
      "Newcastle United": {"goalkeeper": "Nick Pope", "outfielders": newcastle_o}, "Nottingham Forest": {"goalkeeper": "Matt Turner", "outfielders": nottingham_o}, 
      "Sheffield United": {"goalkeeper": "Adam Davies", "outfielders": sheffield_o}, "Tottenham Hotspurs": {"goalkeeper": "Guglielmo Vicario", "outfielders": spurs_o},
      "West Ham United": {"goalkeeper": "Alphonse Areola", "outfielders": west_ham_o}, "Wolverhampton Wanderers":{"goalkeeper": "Jose Sa", "outfielders": wolves_o}}

num_teams = 20
num_gameweeks = 38
schedule = {}
teams_played = []

# Generate the round-robin schedule
for gameweek in range(1, num_gameweeks + 1):
    # Create a list to store the matches for this gameweek
    matches = []
    
    for i in range(num_teams // 2):
        home_team = teams[i]
        away_team = teams[num_teams - 1 - i]
        
        match = (home_team, away_team)
        matches.append(match)
        
        # Mark the teams as played in this gameweek
        teams_played.append(home_team)
        teams_played.append(away_team)
    
    # Add the matches for this gameweek to the schedule dictionary
    schedule[f"Gameweek {gameweek}"] = matches

    # Rotate the teams for the next gameweek
    teams = [teams[-1]] + teams[:-1]
    
    # Shuffle the teams to ensure different pairings in the next gameweek
    teams = teams[:1] + teams[1:][::-1]

print(schedule)

class match_engine:
    def __init__(self, home, away):
        self.home = home
        self.away = away
    
    def generate_result(self):
        self.h = random.randint(0,4)
        self.a = random.randint(0,3)
        return [self.h,self.a]
    
    def lineups(self):
        home_gk = x0[self.home]["goalkeeper"]
        home_outfielders = x0[self.home]["outfielders"]
        home_bench = home_outfielders.pop(random.randint(0,10))
        self.home_lineup = [home_gk] + home_outfielders
        away_gk = x0[self.away]["goalkeeper"]
        away_outfielders = x0[self.away]["outfielders"]
        away_bench = away_outfielders.pop(random.randint(0,10))
        self.away_lineup = [away_gk] + away_outfielders
        return self.home_lineup, self.away_lineup
    
    def goalscorers(self):
        home_scorers = []
        h = self.h
        a = self.a
        away_scorers = []
        while h > 0:
            home_scorers.append(self.home_lineup[random.randint(1,10)])
            h -= 1
        while a > 0:
            away_scorers.append(self.away_lineup[random.randint(1,10)])
            a -= 1
        return home_scorers, away_scorers
    
    def generate_match_data(self):
        result = self.generate_result()
        lineups = self.lineups()
        goal_scorers = self.goalscorers()
        match_data = {
            "Fixture" : [self.home, self.away],
            "Result": result,
            "Lineups": {
                "Home": lineups[0],
                "Away": lineups[1]
            },
            "GoalScorers": {
                self.home: goal_scorers[0],
                self.away: goal_scorers[1]
            }
        }
        return match_data
    
def generate_match_data_for_gameweek(gameweek, schedule):
    gameweek_data = {}
    matches = schedule[f"Gameweek {gameweek}"]
    
    for match_number, (home, away) in enumerate(matches, 1):
        me = match_engine(home, away)
        match_data = me.generate_match_data()
        gameweek_data[f"Match {match_number}"] = match_data
    
    return gameweek_data

week_1 = generate_match_data_for_gameweek(1, schedule)
print(" ")
print(week_1)




# me = match_engine("Liverpool", "Manchester City")
# match_data = me.generate_match_data()



# me2 = match_engine(schedule["Gameweek 1"][0][0], schedule["Gameweek 1"][0][1])
# match_data = me2.generate_match_data()


if __name__ == '__main__':
    with open("match_data02.json", "w") as json_file:
        json.dump(week_1, json_file, indent=4)

# print(match_data)