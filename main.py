import random
import json

arsenal_0 = ["Oleksandr Zinchenko", "William Saliba", "Gabriel", "Ben White", "Declan Rice", "Thomas Partey", "Martin Odegaard", "Bukayo Saka", "Eddie Nketiah", "Gabriel Martinelli", "Gabriel Jesus"]
liverpool_o = ["Trent Alexander-Arnold", "Virgil Van Dijk", "Joel Matip", "Andrew Robertson", "Dominik Szoboszlai", "Thiago", "Alexis Mac Allister", "Mo Salah", "Darwin Nunez", "Luis Diaz", "Diogo Jota"]
manchester_city_o = ["Kyle Walker", "Nathan Ake", "Ruben Dias", "John Stones", "Bernardo Silva", "Kevin De Bruyne", "Rodri", "Erling Haaland", "Julian Alvarez", "Jeremy Doku", "Mateo Kovacic"]
manchester_united_o = ["Luke Shaw", "Lisandro Martinez", "Raphael Varane", "Aaron Wan-Bissaka", "Bruno Fernandes", "Casemiro", "Christian Eriksen", "Rasmus Hojlund", "Antony", "Marcus Rashford", "Alejandro Garnacho"]
teams = {"Liverpool":{"goalkeeper":"Allison", "outfielders": liverpool_o}, "Manchester City":{"goalkeeper":"Ederson", "outfielders": manchester_city_o}}

class match_engine:
    def __init__(self, home, away):
        self.home = home
        self.away = away
    
    def generate_result(self):
        self.h = random.randint(0,4)
        self.a = random.randint(0,3)
        return f"{self.h}-{self.a}"
    
    def lineups(self):
        home_gk = teams[self.home]["goalkeeper"]
        home_outfielders = teams[self.home]["outfielders"]
        home_bench = home_outfielders.pop(random.randint(0,10))
        self.home_lineup = [home_gk] + home_outfielders
        away_gk = teams[self.away]["goalkeeper"]
        away_outfielders = teams[self.away]["outfielders"]
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
            "Result": result,
            "Lineups": {
                self.home: lineups[0],
                self.away: lineups[1]
            },
            "GoalScorers": {
                self.home: goal_scorers[0],
                self.away: goal_scorers[1]
            }
        }
        return match_data




me = match_engine("Liverpool", "Manchester City")
match_data = me.generate_match_data()

# if __name__ == '__main__':
#     with open("match_data.json", "w") as json_file:
#         json.dump(match_data, json_file, indent=4)

print(match_data)