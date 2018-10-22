import csv

with open('Event_Feedback.csv', mode='r') as csv_file:
    #consult your file for which group dictionary is which
    groups = [{},{},{},{},{},{}]
    final = [ ["Hacking"],
              ["Artificial Intelligence"],
              ["Encryption"],
              ["Piracy and Open Source"],
              ["Social Media"],
              ["Robotics"] ]
    free = []
    
    data = [row for row in csv.reader(csv_file)] #csv in matrix form
    #Sets up groups
    for i, row in enumerate(data):
        for col in range(2, len(row)):
            if i != 0:  #ignore first row
                groups[col-2][data[i][1]] = data[i][col]

    #list of people not placed into groups
    for name in groups[0]:
        free.append(name)
        
    #update for top choices
    target = 0
    while (target != 7): #loop through choice rankings
        for i in range(len(groups)): #loop through topics
            for k,v in groups[i].items():
                #if student has chosen this group and is not already in a group
                if int(v) == target and len(final[i]) <= 4 and k in free:
                    final[i].append(k)
                    free.remove(k) #student is placed in a group
        target+=1
        
    for f in final:
        print(f)
