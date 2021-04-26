CREATE TABLE "user" (
	"userID"	        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"userName"	        TEXT NOT NULL UNIQUE,
	"userEmailAddress"	TEXT NOT NULL UNIQUE,
	"userPassword"	    TEXT NOT NULL
);

CREATE TABLE "studySet" (
	"studySetID"	    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"studySetUserID"	INTEGER NOT NULL,
	"studySetName"	    TEXT NOT NULL,
    FOREIGN KEY (studySetUserID) REFERENCES user (userID)
);

CREATE TABLE "termAndDescription" (
    "tadID"             INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "tadStudySetID"     INTEGER NOT NULL UNIQUE,
    "tadTerm"           TEXT NOT NULL,
    "tadDescription"    TEXT NOT NULL,
    FOREIGN KEY (tadStudySetID) REFERENCES studySet (studySetID)
);


CREATE TABLE "session" (
	"sessionID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"sesUserID"	INTEGER NOT NULL,
	"sesStartTime"	TEXT NOT NULL,
	FOREIGN KEY (sesUserID) REFERENCES user (userID)
);

