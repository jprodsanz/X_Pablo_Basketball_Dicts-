class Player:
    def __init__(self, info):
        self.name = info['name']
        self.age = info['age']
        self.position = info ['position']
        self.team = info ['team']
    
    def __repr__(self) -> str:
        show = f"Player: {self.name}, {self.age}, {self.position}, {self.team}"
        return show

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
},
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
},

kyrie ={
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
},
damian = {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
},

joel={
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
}

p_jayson = Player(jason)
p_kevin = Player(kevin)
p_kyrie = Player(kyrie)
p_damian = Player(damian)
p_joel = Player(joel)
print(p_jayson)
print(p_kevin)
print(p_kyrie)
print(p_damian)
print(p_joel)

