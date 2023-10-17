CREATE TABLE Teams 
(
    Team_id INT,
    Team NVARCHAR(50) NOT NULL,
    Played INT,
    Wins INT,
    Draws INT,
    Losses INT,
    GF INT,
    GA INT,
    GD INT
);

INSERT INTO Teams (team_id, team)
VALUES (1, 'Arsenal');

INSERT INTO Teams (team_id, team)
VALUES (2, 'Aston Villa');

INSERT INTO Teams (team_id, team)
VALUES (3, 'Bournemouth');

INSERT INTO Teams (team_id, team)
VALUES (4, 'Brentford');

INSERT INTO Teams (team_id, team)
VALUES (5, 'Brighton');

INSERT INTO Teams (team_id, team)
VALUES (6, 'Burnley');

INSERT INTO Teams (team_id, team)
VALUES (7, 'Chelsea');

INSERT INTO Teams (team_id, team)
VALUES (8, 'Crystal Palace');

INSERT INTO Teams (team_id, team)
VALUES (9, 'Everton');

INSERT INTO Teams (team_id, team)
VALUES (10, 'Fulham');

INSERT INTO Teams (team_id, team)
VALUES (11, 'Liverpool');

INSERT INTO Teams (team_id, team)
VALUES (12, 'Luton');

INSERT INTO Teams (team_id, team)
VALUES (13, 'Manchester City');

INSERT INTO Teams (team_id, team)
VALUES (14, 'Manchester United');

INSERT INTO Teams (team_id, team)
VALUES (15, 'Newcastle United');

INSERT INTO Teams (team_id, team)
VALUES (16, 'Nottingham Forest');

INSERT INTO Teams (team_id, team)
VALUES (17, 'Sheffield United');

INSERT INTO Teams (team_id, team)
VALUES (18, 'Tottenham Hotspur');

INSERT INTO Teams (team_id, team)
VALUES (19, 'West Ham United');

INSERT INTO Teams (team_id, team)
VALUES (20, 'Wolverhampton Wanderers');
