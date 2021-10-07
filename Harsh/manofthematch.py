def score(p):
    
    #Initialize all variables..
    points=0
    name=p['name']
    run=p['runs']
    six=p['6']
    four=p['4']
   

    #Calculation according to the description
    
    points=run/2
    points=points+four
    points=points+(2*six)
    
    # making a dictionary with player_name & points
    print(name , ",Points Scored is = ",points)

def demo(name):
    print("\nSee It Works!" + name)
    
