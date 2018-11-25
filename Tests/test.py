from SeleniumTest.src import utility as ut
import csv

# print(ut.deCode(ut.enCode('abcd')))
path = 'D:\Workspace_Pycharm/Selenium/loginData.csv'
with open(path, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['key', 'username', 'password'])
while True:
    ut.newUserData(path)
print(ut.getUserData(path,'king'))