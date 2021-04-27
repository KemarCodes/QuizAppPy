from user import User
from studyset import StudySet

user1 = User()
studySet1 = StudySet()
# print(user1.getUserByName('kstudy'))
# print(user1.getUserByEmailAddress('iliketostudy@example.com'))
# print(user1.checkIfUserExists('kstudy', 'iliketostudy@example.com'))
# print(user1.checkIfUserExists('kstudy', 'idontlikestudying@example2.com'))
# print(user1.addNewUser('sami', 'sami22@gmail.com', 'samispassword'))
# print(user1.createSession(7))
print(studySet1.getTermsByStudySetID(1))