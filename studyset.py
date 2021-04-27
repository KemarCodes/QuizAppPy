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
    
    def getTermsByStudySetID(self, studySetID):
        query = "select studySetName, tadTerm, tadDescription, tadID, tadStudySetID \
            from termAndDescription, studySet \
            where studySetID = tadStudySetID \
                and tadStudySetID = '{si}';"\
            .format(si=studySetID)
        print(query)
        rs = executeQuery(query)
        return rs
    
    def addTerm(self, studySetID, term, description):
        query = "insert into termAndDescription (tadStudySetID,\
            tadTerm, tadDescription)\
                 values ('{si}','{tm}','{dn}');"\
                .format(si=studySetID, tm=term, dn=description)
        print(query)
        rs = executeDMLQuery(query)
        return rs