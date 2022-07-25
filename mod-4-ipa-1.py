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
    follower = 'follower'
    followedBy = 'followed by'
    friends = 'friends'
    noRelationship = 'no relationship'
    isFollowing = 0 
    isFollowed = 0
    
    for x in social_graph[to_member]['following']: # if from_member is followed by to_member
        if x == from_member:
            isFollowing = 1
    
    for y in social_graph[from_member]['following']: # if to_member is followed by from_member
        if y == to_member:
            isFollowed = 1
    
    if isFollowing == 0 and isFollowed == 0:
        return noRelationship
    elif isFollowing == 1 and isFollowed == 1:
        return friends
    elif isFollowing == 0 and isFollowed == 1:
        return follower
    elif isFollowing == 1 and isFollowed == 0:
        return followedBy



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
        
    lengthOfBoard = len(board)
    counterX = 0
    counter0 = 0
    pointX = 0
    point0 = 0
    winner = ''
    
    #for horizontals
    for row in range(lengthOfBoard):
        for col in range(lengthOfBoard):
            if board[row][col] == 'X':
                counterX = counterX + 1
            elif board[row][col] == 'O':
                counter0 = counter0 + 1
        if counterX == lengthOfBoard:
            pointX = pointX + 1
        elif counter0 == lengthOfBoard:
            point0 = point0 + 1
        counterX = 0
        counter0 = 0
        
    #for verticals
    for col in range(lengthOfBoard):
        for row in range(lengthOfBoard):
            if board[row][col] == 'X':
                counterX = counterX + 1
            elif board[row][col] == 'O':
                counter0 = counter0 + 1
        if counterX == lengthOfBoard:
            pointX = pointX + 1
        elif counter0 == lengthOfBoard:
            point0 = point0 + 1
        counterX = 0
        counter0 = 0
        
    #for \ bsta slant yan
    for LtoR in range(lengthOfBoard):
        if board[LtoR][LtoR] == 'X':
            counterX = counterX + 1
        elif board[LtoR][LtoR] == 'O':
            counter0 = counter0 + 1
    if counterX == lengthOfBoard:
        pointX = pointX + 1
    elif counter0 == lengthOfBoard:
        point0 = point0 + 1
    counterX = 0
    counter0 = 0    
    
    #for / bsta slant yan
    for RtoL in range(lengthOfBoard):
        if board[lengthOfBoard-1-RtoL][RtoL] == 'X':
            counterX = counterX + 1
        elif board[lengthOfBoard-1-RtoL][RtoL] == 'O':
            counter0 = counter0 + 1
    if counterX == lengthOfBoard:
        pointX = pointX + 1
    elif counter0 == lengthOfBoard:
        point0 = point0 + 1
    counterX = 0
    counter0 = 0   
    
    #yung points
    if pointX == 1:
        winner = 'X'
    elif point0 == 1:
        winner = 'O'
    else:
        winner = 'NO WINNER'

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

    Block = list(route_map.keys())
    StationOne = 0
    StationTwo = 0
    TimeSpent = 0
    
    for x in range(len(route_map)):
        if first_stop == Block[x][0]:
            StationOne = x
    
    for x in range(len(route_map)):
        if second_stop == Block[x][1]:
            StationTwo = x
    
    if StationOne > StationTwo:
        for z in range(len(route_map)):
            if z >= StationOne or z <= StationTwo:
                UpdatedDict = route_map[Block[z]]
                TimeSpent =  TimeSpent + UpdatedDict['travel_time_mins']
    
    elif StationOne <= StationTwo:
        for y in range(len(route_map)):
            if y <= StationTwo and y >= StationOne:
                if (StationOne == StationTwo or StationOne < StationTwo):
                    UpdatedDict = route_map[Block[y]]
                    TimeSpent = TimeSpent + UpdatedDict['travel_time_mins']
    
    return(TimeSpent)
