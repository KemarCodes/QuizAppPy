from quizdbcon import executeQuery

class User:
    
    def __init__(self, userName, userEmailAddress, userPassword):
        self.userName = userName
        self.userEmailAddress = userEmailAddress
        self.userPassword = userPassword
        self.retrievedUserName = None
        self.retrievedUserEmailAddress = None
        self.retrievedPassword = None

    def __init__(self):
        self.userName = None
        self.userEmailAddress = None
        self.userPassword = None

    def getUserByName(self, userName):
        query = "select * from user where userName = '{un}';".format(un=userName)
        print(query)
        rs = executeQuery(query)
        return rs

    def getUserByEmailAddress(self, userEmailAddress):
        query = "select * from user where userEmailAddress = '{em}';".format(em=userEmailAddress)
        print(query)
        rs = executeQuery(query)
        return rs
    
    def checkPassword(self, pwProvided, pwRetrieved):     
        if(pwProvided == pwRetrieved):
            return 1
        else:
            return 0
