# -*- coding: utf-8 -*-
# Without changing the provided array's and dicts, create a script that cycles
# through all the parents and prints to the terminal the proper activities for
# their child's age group. When there are no more activities for that parent,
# print “curriculum complete!” and move on to the next parent.
#
# (Make sure your script accounts for any edge cases in the provided variables!)

parents = [
    {'parent': 'Henry', 'child': {'name': 'Calvin', 'age': 2}},
    {'parent': 'Ada', 'child': {'name': 'Lily', 'age': 3}},
    {'parent': 'Emilia', 'child': {'name': 'Petra', 'age': 1}},
    {'parent': 'Biff', 'child': {'name': 'Biff Jr', 'age': 4}},
    {'parent': 'Milo', 'child': {}}
]

curriculum = [
    {
        'age': 1,
        'activity': [
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Go outside and feel surfaces.',
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

def apology():
    print("Sorry, we couldn't find any activities for you right now.")

def checknumber(n):
    while not n.isdigit():
        n = raw_input("Sorry, I don't understand your input. \n Please ",
            "type a numerical answer (e.g. 3): ")
    return n

def sectionend():
    print("------")

yeses = ['yes', 'y', 'yeah', 'ya']

def main():
    # ask user if they want to add new tasks
    change = raw_input('Would you like to add '
        'new activities to the curriculum? \n Type yes or no: ')

    if change.lower() in yeses:
        nc = raw_input('How many activities do you want to add? ')
        checknumber(nc)
        for i in range(int(nc)):
            print("New activity " + str(i + 1) + ":")
            a1 = raw_input("What age is this new activity for? (e.g. 3) ")
            checknumber(a1)
            a1 = int(a1)
            new = raw_input("Please describe the activity: ")
            agefound = False
            for elem in curriculum:
                if elem['age'] == a1:
                    elem['activity'].append(new)
                    agefound = True
                    break
            if not agefound:
                curriculum.append({'age': a1, 'activity': [new]})
            raw_input('Activity added! Press enter to continue ')
            sectionend()

    # ask user if they want to add new parents
    new_parent = raw_input('Would you like to add a new parent to the database?'
        ' Type yes or no: ')
    if new_parent.lower() in yeses:
        np = raw_input('How many parents do you want to add? ')
        checknumber(np)
        for j in range(int(np)):
            print("New parent " + str(j + 1) + ":")
            n = raw_input("What is the name of the new parent? ")
            c = raw_input("What is the name of this person's child? ")
            age = raw_input("How old is this child? ")
            checknumber(age)
            parents.append({'parent':n,'child':{'name':c,'age':int(age)}})
            raw_input('Parent added! Press enter to continue ')

    # print out tasks
    sectionend()
    for p in parents:
        p_name = p['parent']
        print('Hey ' + p_name + '!')
        if p['child']:
            c_name = p['child']['name']
            a = p['child']['age']
            age_included = False
            for x in curriculum:
                if x['age']==a:
                    age_included = True
                    print("Here are some tasks for " + c_name + ":")
                    numtasks = len(x['activity'])
                    for i in range(numtasks):
                        print(str(i+1) + ".) " + x['activity'][i])
                    print("Curriculum complete!")
                    break
            if not age_included:
                apology()
        else:
            apology()
        sectionend()

if __name__=="__main__":
    main()

# Want to really shine and show us your chops?  Work in some of these stretch
# goals using any tools or libraries you see fit.
# - Personalize the message output to make it more friendly.
# - Print one activity at a time per parent and continue cycling through until
#   all parents have recieved all their activities.
# - Allow users to input new activities & parents before executing the script.
#
# Get creative and have fun!
# - Create a way to extend this challenge based on skills you're good at!
# - Utilize git workflow and unit tests to build your script.
# - Create a web page for users to enter their details and recieve activities.
