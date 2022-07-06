'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    
    Cond1 = False
    Cond2 = False
    relationship1 = 'friends'
    relationship2 = 'followed by'
    relationship3 = 'follower'
    relationship4 = 'no relationship'
    
    from_following = social_graph[from_member]['following']

    to_following = social_graph[to_member]['following']
    
    for i in to_following: # if from_member is followed by to_member
        if i == from_member:
            Cond1 = True
    
    for j in from_following: # if to_member is followed by from_member
        if j == to_member:
            Cond2 = True
    
    if Cond1 == True and Cond2 == True:
        return relationship1
    else:
        if Cond1 == True or Cond2 == True:
               if Cond1 == True:
                    return relationship2
               else:
                    return relationship3
        
        else:
            return relationship4

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    repetitions = len(board)
    
    diagonal1 = []
    diagonal2 = []
    
    winner = 'NO WINNER'
    
    horizontals = [set(x) for x in board]
    
    verticals = [set(x) for x in zip(*board)]
 
    for i in range(repetitions): # to check horizontals
        check1 = len(horizontals[i])
        if check1 == 1:
            winner = ''.join(horizontals[i])
    
    for i in range(repetitions): # to check verticals
        check2 = len(verticals[i])
        if check2 == 1:
            winner = ''.join(verticals[i])
    
    for i in range(repetitions): # first diagonal
        diagonal1.append(board[i][i])
    
    CheckDiagonal1 = set(diagonal1)
    if len(CheckDiagonal1) == 1:
            winner = ''.join(CheckDiagonal1)
    
    for j in range(repetitions): # second diagonal
        diagonal2.append(board[repetitions-1-j][j])
        
    CheckDiagonal2 = set(diagonal2)
    if len(CheckDiagonal2) == 1:
            winner = ''.join(CheckDiagonal2)
            
    return winner

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass