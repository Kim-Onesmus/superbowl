superbowl_ls = [{'St. Louis Rams', 'Tennessee Titans'}, {'Baltimore Ravens', 'New York Giants'}, 
                {'St.Louis Rams', 'New England Patriots'}, 
                {'Tampa Bay Buccaneers', 'Oakland Raiders'}, {'New England Patriots', 'Carolina Panthers'}, 
                {'Philadelphia Eagles', 'New England Patriots'}, 
                {'Seattle Seahawks', 'Pittsburgh Steelers'}, 
                {'Indianapolis Colts', 'Chicago Bears'}, {'New York Giants', 'New England Patriots'}, 
                {'Arizona Cardinals', 'Pittsburgh Steelers'}, {'New Orleans Saints', 'Indianapolis Colts'}, 
                {'Green Bay Packers', 'Pittsburgh Steelers'}, {'New York Giants', 'New England Patriots'}, 
                {'San Francisco 49ers', 'Baltimore Ravens'}, {'Denver Broncos', 'Seattle Seahawks'}, 
                {'Seattle Seahawks', 'New England Patriots'}, {'Denver Broncos', 'Carolina Panthers'}, 
                {'Atlanta Falcons', 'New England Patriots'}, {'Philadelphia Eagles', 'New England Patriots'}, 
                {'New England Patriots', 'Los Angeles Rams'}, {'San Francisco 49ers', 'Kansas City Chiefs'}, 
                {'Tampa Bay Buccaneers', 'Kansas City Chiefs'}, {'Cincinnati Bengals', 'Los Angeles Rams'}]

total = ''
years = int(input("How many years do you want to enter data for? "))
for i in range(years):
    year = int(input("What year do you want from 2000 to 2022? "))
    
    if year == 2000:
        superbowl = superbowl_ls[0]
    if year == 2001:
        superbowl = superbowl_ls[1]
    if year == 2002:
        superbowl = superbowl_ls[2]
    if year == 2003:
        superbowl = superbowl_ls[3]
    if year == 2004:
        superbowl = superbowl_ls[4]
    if year == 2005:
        superbowl = superbowl_ls[5]
    if year == 2006:
        superbowl = superbowl_ls[6]
    if year == 2007:
        superbowl = superbowl_ls[7]
    if year == 2008:
        superbowl = superbowl_ls[8]
    if year == 2009:
        superbowl = superbowl_ls[9]
    if year == 2010:
        superbowl = superbowl_ls[10]
    if year == 2011:
        superbowl = superbowl_ls[11]
    if year == 2012:
        superbowl = superbowl_ls[12]
    if year == 2013:
        superbowl = superbowl_ls[13]
    if year == 2014:
        superbowl = superbowl_ls[14]
    if year == 2015:
        superbowl = superbowl_ls[15]
    if year == 2016:
        superbowl = superbowl_ls[16]
    if year == 2017:
        superbowl = superbowl_ls[17]
    if year == 2018:
        superbowl = superbowl_ls[18]
    if year == 2019:
        superbowl = superbowl_ls[19]
    if year == 2020:
        superbowl = superbowl_ls[20]
    if year == 2021:
        superbowl = superbowl_ls[21]
    if year == 2022:
        superbowl = superbowl_ls[22]
        
    
    total += str(superbowl)
    print("The list of the years entered by NFL teams in the Super Bowl are: ", total)
