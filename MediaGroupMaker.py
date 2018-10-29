import csv

with open('Event_Feedback.csv', mode='r') as csv_file:
    #consult your file for which group dictionary is which
    groups = [{},{},{},{},{},{}]
    final = [ [],
              [],
              [],
              [],
              [],
              [] ] #list of final MAP groups
    free = []
    groupSize = 4 #this can be changed
    
    data = [row for row in csv.reader(csv_file)] #reads csv into matrix form
    #Sets up groups
    for i, row in enumerate(data):
        for col in range(2, len(row)): #starts at 2 to ignore timestamp and name columns
            if i != 0:  #ignore first row
                groups[col-2][data[i][1]] = data[i][col]
            else: #inserts name of group into list to avoid confusion
                final[col-2].append(data[i][col])

    #list of people not placed into groups
    for name in groups[0]:
        free.append(name)
        
    #update for top choices
    target = 0
    while (target != 7): #loop through choice rankings
        for i in range(len(groups)): #loop through topics
            for k,v in groups[i].items():
                #if student has chosen this group and is not already in a group
                if int(v) == target and len(final[i]) <= groupSize and k in free:
                    final[i].append(k)
                    free.remove(k) #student is placed in a group
        target+=1
        
    for f in final:
        print(f)
