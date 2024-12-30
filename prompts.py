# prompts.py

PROMPTS = {
    "fetaqa": {
        "direct": """
Read the following table regarding "Shagun Sharma" to answer the given question.

Year | Title | Role | Channel
2015 | Kuch Toh Hai Tere Mere Darmiyaan | Sanjana Kapoor | Star Plus
2016 | Kuch Rang Pyar Ke Aise Bhi | Khushi | Sony TV
2016 | Gangaa | Aashi Jhaa | &TV
2017 | Iss Pyaar Ko Kya Naam Doon 3 | Meghna Narayan Vashishth | Star Plus
2017–18 | Tu Aashiqui | Richa Dhanrajgir | Colors TV
2019 | Laal Ishq | Pernia | &TV
2019 | Vikram Betaal Ki Rahasya Gatha | Rukmani/Kashi | &TV
2019 | Shaadi Ke Siyape | Dua | &TV

Question: What TV shows was Shagun Sharma seen in 2019?
Answer: In 2019, Shagun Sharma played in the roles as Pernia in Laal Ishq, Vikram Betaal Ki Rahasya Gatha as Rukmani/Kashi and Shaadi Ke Siyape as Dua.
""",
        "cot": "FetaQA Direct Prompt: ...",  # Same as 'direct'
        "self-consistency": "FetaQA Self Consistency Prompt: ..."
    },
    "tabfact-simple": {
        "direct": """
Read the table below regarding "2002 u.s. open (golf)" to verify whether the provided claims are true or false.

place | player | country | score | to par
1 | tiger woods | united states | 67 + 68 + 70 = 205 | - 5
2 | sergio garcía | spain | 68 + 74 + 67 = 209 | - 1
t3 | jeff maggert | united states | 69 + 73 + 68 = 210 | e
t3 | phil mickelson | united states | 70 + 73 + 67 = 210 | e
t5 | robert allenby | australia | 74 + 70 + 67 = 211 | + 1
t5 | pádraig harrington | ireland | 70 + 68 + 73 = 211 | + 1
t5 | billy mayfair | united states | 69 + 74 + 68 = 211 | + 1
t8 | nick faldo | england | 70 + 76 + 66 = 212 | + 2
t8 | justin leonard | united states | 73 + 71 + 68 = 212 | + 2
t10 | tom byrum | united states | 72 + 72 + 70 = 214 | + 4
t10 | davis love iii | united states | 71 + 71 + 72 = 214 | + 4
t10 | scott mccarron | united states | 72 + 72 + 70 = 214 | + 4

Claim: nick faldo is the only player from england.
Explanation: the claim is true.

Claim: justin leonard score less than 212 which put him tied for the 8th place.
Explanation: the claim is false.

Claim: when player is phil mickelson, the total score is 210.
Explanation: the claim is true.
""",
        "cot": """
Read the table below regarding "2002 u.s. open (golf)" to verify whether the provided claims are true or false.

place | player | country | score | to par
1 | tiger woods | united states | 67 + 68 + 70 = 205 | - 5
2 | sergio garcía | spain | 68 + 74 + 67 = 209 | - 1
t3 | jeff maggert | united states | 69 + 73 + 68 = 210 | e
t3 | phil mickelson | united states | 70 + 73 + 67 = 210 | e
t5 | robert allenby | australia | 74 + 70 + 67 = 211 | + 1
t5 | pádraig harrington | ireland | 70 + 68 + 73 = 211 | + 1
t5 | billy mayfair | united states | 69 + 74 + 68 = 211 | + 1
t8 | nick faldo | england | 70 + 76 + 66 = 212 | + 2
t8 | justin leonard | united states | 73 + 71 + 68 = 212 | + 2
t10 | tom byrum | united states | 72 + 72 + 70 = 214 | + 4
t10 | davis love iii | united states | 71 + 71 + 72 = 214 | + 4
t10 | scott mccarron | united states | 72 + 72 + 70 = 214 | + 4

Claim: nick faldo is the only player from england.
Explanation: no other player is from england, therefore, the claim is true.

Claim: justin leonard score less than 212 which put him tied for the 8th place.
Explanation: justin leonard scored exactly 212, therefore, the claim is false.
""",  # Same as 'direct'
        "self-consistency": "TabFact-Simple Self Consistency Prompt: ..."
    },
    "tabfact-complex": {
        "direct": """
Read the table below regarding "1919 in brazilian football" to verify whether the provided claims are true or false.

date | result | score | brazil scorers | competition
may 11 , 1919 | w | 6 - 0 | friedenreich (3) , neco (2) , haroldo | south american championship
may 18 , 1919 | w | 6 - 1 | heitor , amílcar (4), millon | south american championship
may 26 , 1919 | w | 5 - 2  | neco (5) | south american championship
may 30 , 1919 | l | 1 - 2 | jesus (1) | south american championship
june 2nd , 1919 | l | 0 - 2 | - | south american championship

Claim: neco has scored a total of 7 goals in south american championship.
Explanation: the claim is true.

Claim: jesus has scored in two games in south american championship.
Explanation: the claim is false.

Claim: brazilian football has participated in five games in may, 1919.
Explanation: the claim is false.

Claim: brazilian football played games between may and july.
Explanation: the claim is true. 
""",
        "cot": """
Read the table below regarding "1919 in brazilian football" to verify whether the provided claims are true or false.

date | result | score | brazil scorers | competition
may 11 , 1919 | w | 6 - 0 | friedenreich (3) , neco (2) , haroldo | south american championship
may 18 , 1919 | w | 6 - 1 | heitor , amílcar (4), millon | south american championship
may 26 , 1919 | w | 5 - 2  | neco (5) | south american championship
may 30 , 1919 | l | 1 - 2 | jesus (1) | south american championship
june 2nd , 1919 | l | 0 - 2 | - | south american championship

Claim: neco has scored a total of 7 goals in south american championship.
Explanation: neco has scored 2 goals on may 11  and 5 goals on may 26. neco has scored a total of 7 goals, therefore, the claim is true.

Claim: jesus has scored in two games in south american championship.
Explanation: jesus only scored once on the may 30 game, but not in any other game, therefore, the claim is false.

Claim: brazilian football team has scored six goals twice in south american championship.
Explanation: brazilian football team scored six goals once on may 11 and once on may 18, twice in total, therefore, the claim is true.
"""

"""
Claim: brazilian football has participated in five games in may, 1919.
Explanation:  brazilian football only participated in four games rather than five games, therefore, the claim is false.

Claim: brazilian football played games between may and july.
Explanation: brazilian football played on june 2nd, which is between may and july, therefore, the claim is true

Claim: brazilian football team scored at least 1 goals in all the 1919 matches.
Explanation: the team scored zero goal on june 2nd, which is less than 1 goals, therefore, the claim is false.

Claim: brazilian football team has won 2 games and lost 3 games.
Explanation: the team only lost 2 games instead of 3 games, therefore, the claim is false.
"""
,
        "self-consistency": "TabFact-Complex Self Consistency Prompt: ..."
    },
    "wikitablaqa": {
        "direct": """
Read the table below regarding "2008 Clásica de San Sebastián" to answer the following questions.

Rank | Cyclist | Team | Time | UCI ProTour Points
1 | Alejandro Valverde (ESP) | Caisse d'Epargne | 5h 29' 10 | 40
2 | Alexandr Kolobnev (RUS) | Team CSC Saxo Bank | s.t. | 30
3 | Davide Rebellin (ITA) | Gerolsteiner | s.t. | 25
4 | Paolo Bettini (ITA) | Quick Step | s.t. | 20
5 | Franco Pellizotti (ITA) | Liquigas | s.t. | 15
6 | Denis Menchov (RUS) | Rabobank | s.t. | 11
7 | Samuel Sánchez (ESP) | Euskaltel-Euskadi | s.t. | 7
8 | Stéphane Goubert (FRA) | Ag2r-La Mondiale | + 2 | 5
9 | Haimar Zubeldia (ESP) | Euskaltel-Euskadi | + 2 | 3
10 | David Moncoutié (FRA) | Cofidis | + 2 | 1

read the question first, and then answer the given question. 

Question: which country had the most cyclists finish within the top 10?
The answer is Italy.

Question: how many players got less than 10 points?
The answer is 4.

Question: how many points does the player from rank 3, rank 4 and rank 5 combine to have? 
The answer is 60.

Question: who spent the most time in the 2008 Clásica de San Sebastián. 
The answer is David Moncoutié.
""",
        "cot":  """
Read the table below regarding "2008 Clásica de San Sebastián" to answer the following questions.

Rank | Cyclist | Team | Time | UCI ProTour Points
1 | Alejandro Valverde (ESP) | Caisse d'Epargne | 5h 29' 10 | 40
2 | Alexandr Kolobnev (RUS) | Team CSC Saxo Bank | s.t. | 30
3 | Davide Rebellin (ITA) | Gerolsteiner | s.t. | 25
4 | Paolo Bettini (ITA) | Quick Step | s.t. | 20
5 | Franco Pellizotti (ITA) | Liquigas | s.t. | 15
6 | Denis Menchov (RUS) | Rabobank | s.t. | 11
7 | Samuel Sánchez (ESP) | Euskaltel-Euskadi | s.t. | 7
8 | Stéphane Goubert (FRA) | Ag2r-La Mondiale | + 2 | 5
9 | Haimar Zubeldia (ESP) | Euskaltel-Euskadi | + 2 | 3
10 | David Moncoutié (FRA) | Cofidis | + 2 | 1

Question: which country had the most cyclists finish within the top 10?
Explanation: ITA occurs three times in the table, more than any others. Therefore, the answer is Italy.

Question: how many players got less than 10 points?
Explanation: Samuel Sánchez,  Stéphane Goubert, Haimar Zubeldia and David Moncoutié received less than 10 points.  Therefore, the answer is 4.

Question: how many points does the player from rank 3, rank 4 and rank 5 combine to have? 
Explanation: rank 3 has 25 points, rank 4 has 20 points, rank 5 has 15 points, they combine to have a total of 60 points. Therefore, the answer is 60.

Question: who spent the most time in the 2008 Clásica de San Sebastián?
Explanation: David Moncoutié spent the most time to finish the game and ranked the last. Therefore, the answer is David Moncoutié.
""",  # Same as 'direct'
        "self-consistency": "WikiTableQA Self Consistency Prompt: ..."
    }
}

# Dynamically set CoT prompts to reference Direct prompts where they are the same
PROMPTS["fetaqa"]["cot"] = PROMPTS["fetaqa"]["direct"]
PROMPTS["tabfact-simple"]["cot"] = PROMPTS["tabfact-simple"]["direct"]
PROMPTS["wikitablaqa"]["cot"] = PROMPTS["wikitablaqa"]["direct"]
