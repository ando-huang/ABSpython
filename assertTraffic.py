market = {'ns':'green', 'ew':'red'}

def switchLights(ixn):
    for key in ixn.keys():
        if ixn[key] == 'green':
            ixn[key] = 'yellow'
        elif ixn[key] == 'yellow':
            ixn[key] = 'red'
        else:
            ixn[key] = 'green'
            
    #crashes the program if there is an error here
    assert 'red' in ixn.values(), 'Neither light is red!' + str(ixn)

switchLights(market)
