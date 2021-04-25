from quizdbcon import executeQuery, executeDMLQuery

class User:
    
    def __init__(self, userName = None, userEmailAddress = None, userPassword = None):
        self.userName = userName
        self.userEmailAddress = userEmailAddress
        self.userPassword = userPassword
        self.retrievedUserName = None
        self.retrievedUserEmailAddress = None
        self.retrievedPassword = None

    def getUserByName(self, userName):
        query = "select * from user where userName = '{un}';".format(un=userName)
        print(query)
        rs = executeQuery(query)
        return rs

    def getUserByEmailAddress(self, userEmailAddress):
        query = "select * from user where userEmailAddress =\
         '{em}';".format(em=userEmailAddress)
        print(query)
        rs = executeQuery(query)
        return rs

    def addNewUser(self, userName, userEmailAddress, userPassword):
        query = "insert into user (userName, userEmailAddress, userPassword)\
            values ('{un}', '{em}', '{pw}');"\
                .format(un=userName, em=userEmailAddress, pw=userPassword)
        print(query)
        rs = executeDMLQuery(query)
        return rs

    def checkIfUserExists(self, userName, userEmailAddress):
        userNameResult = self.getUserByName(userName)
        userEmailResult = self.getUserByEmailAddress(userEmailAddress)
        if((len(userNameResult) or len(userEmailResult)) > 0):
            return True
        else:
            return False

    def checkPassword(self, pwProvided, pwRetrieved):     
        if(pwProvided == pwRetrieved):
            return 1
        else:
            return 0
