from quizdbcon import executeQuery, executeDMLQuery

class StudySet:
    
    def __init__(self, studySetID=None, studySetUserID=None, studySetName=None):
        self.studySetID = studySetID
        self.studySetUserID = studySetUserID
        self.studySetName = studySetName

    def getStudySetByUserID(self, userID):
        query = "select * from studySet where studySetUserID = '{ui}';"\
            .format(ui=userID)
        print(query)
        rs = executeQuery(query)
        return rs