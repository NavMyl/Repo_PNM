import sys
import pyodbc
import datetime



conn = pyodbc.connect("DRIVER={SQL Server};SERVER=USVDCVMSQLDEV03\INST02;UID=ETLUSER.GDIM;PWD=eTLu$@3r;DATABASE=EDWApac")

cur=conn.cursor()

querystring =   "SELECT top 10 [JobId] ,[Countryname],[JobStartTime],[JobEndTime],[JobStatus],[JobFrequency],[JobType],[ETLCreatedon],[ETLCreatedBy],[ETLUpdatedon],[ETLUpdatedBy],[EDWStagingDate]FROM [EDWApac].[Auditdata].[JobControl]"

cur.execute(querystring)

for row in cur.fetchall():
    print(row)
print datetime.datetime.now()