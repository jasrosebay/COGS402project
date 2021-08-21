from flask import Flask, render_template, request, Response, make_response, jsonify, json
from flask import redirect, url_for 
import requests
import os
import re
import html
import sqlite3
import csv
import sys
import json
from datetime import datetime, date
import time
import codecs
import array as arr 
import pprint
from dateutil.parser import parse

app = Flask(__name__)

#auto creates current time particular to the timezone that they're in
CURRENT_TIME = time.strftime('%H:%M:%S')


@app.route("/")
def index():
	return render_template('index.html')
@app.route("/summary")
def summary():
	return render_template('summary.html')

# csv file name
filename = "2021data.csv"
	
# initializing the titles and rows list
fields = []
rows = []
	
# reading csv file
with open(filename, 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)
		
	# extracting field names through first row
	fields = next(csvreader)
	
	# extracting each data row one by one
	for row in csvreader:
		rows.append(row)
	
	# get total number of rows
	# print("Total no. of rows: %d"%(csvreader.line_num))
	
# printing the field names
# print('Field names are:' + ', '.join(field for field in fields))
print(fields[0])
print(len(fields))

# _______________ start of VARIABLE list _______________

rowCount = 0
colCount = 0

serviceItems = []
companyList = []
usernameList = []
companyServicePairs = []
companyServiceAndHrsKeyPair = {}
companyServiceHRSKeyPairs = {}
ultimateFilteredRows = []

# _______________ end of VARIABLE list _______________



# _______________ start of initializing _______________

def getUsernames():
	colCount = 0
	rowCount = 0

	for row in rows:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")

		for col in row:
			# print("[" + fields[colCount] + "]: " + col)
			if colCount == 0:
				if str(col) in usernameList:
					print("already in list")
				else:
					usernameList.append(col)
			colCount += 1
		rowCount += 1
		colCount = 0
		print("\n")

getUsernames()

# getCompanyList -- gets a list of companies

def getCompanyList(): 
	colCount = 0
	rowCount = 0

	for row in rows:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")

		for col in row:
			# print("[" + fields[colCount] + "]: " + col)
			if colCount == 12:
				if str(col) in companyList:
					print("already in list")
				else:
					companyList.append(col)
			colCount += 1
		rowCount += 1
		colCount = 0
		print("\n")

getCompanyList()

# getServiceItems -- gets a list of services

def getServiceItems():
	colCount = 0
	rowCount = 0

	for row in rows:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")

		for col in row:
			# print("[" + fields[colCount] + "]: " + col)
			if colCount == 16:
				if str(col) in serviceItems:
					print("already in list")
				else:
					serviceItems.append(col)
			colCount += 1
		rowCount += 1
		colCount = 0
		print("\n")

getServiceItems()

def createCompanyServicePairs():
	for company in companyList:
		for service in serviceItems:
			companyServicePairs.append([company,service])


createCompanyServicePairs()

def createCompanyServiceHRSKeyPairs():
	for pair in companyServicePairs:
		companyServiceHRSKeyPairs.update({str(pair): 0})
		# print(pair)

createCompanyServiceHRSKeyPairs()


print("Usernames (" + str((len(usernameList))) + " count ):")
print(usernameList)

print("\n")

print("Companies (" + str((len(companyList))) + " count ):")
print(companyList)

print("\n")

print("Companies-Service (" + str((len(companyServicePairs))) + " count ):")
for pair in companyServicePairs:
	print(pair)

print("\n")

print("Companies-Service: Hrs (" + str((len(companyServiceHRSKeyPairs))) + " count ):")
for key, value in companyServiceHRSKeyPairs.items():
	print(key, value)

print("\n")

print("Service Item (" + str((len(serviceItems))) + " count ):")
print(serviceItems)

print("\n<-------INITIALIZATION COMPLETED...\n")


# _______________ end of initializing _______________



# _______________ start of FUNCTION list _______________

def printRow(row):
	print(row)

def printFieldValuePerRow(row):
	print("---From printFieldValuePerRow(row) ---")
	currColCount = 0
	# for field in fields:
	# 	# for cellValue in row:
	while currColCount < len(fields):
		print("[" + fields[currColCount] + "]: " + row[currColCount])
		currColCount += 1

def printFieldsValues():
	rowCount = 0
	colCount = 0
	for row in rows[:5]:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")

		for col in row:
			print("[" + fields[colCount] + "]: " + col)
			colCount += 1
		colCount = 0
		rowCount += 1
		print("\n")

def chooseEmployee(username):
	colCount = 0
	rowCount = 0
	chooseEmployeeCount = 0
	for row in rows[:50]:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")
		for col in row:
			if colCount == 12:
				if col == username:
					print("____chooseEmployee: " + str(chooseEmployeeCount))
					printRow(row)
					chooseEmployeeCount += 1
					# printRow(row)
					# print("\n")
			colCount += 1
		rowCount += 1
		colCount = 0
		
	print("# matches found = " + str(chooseEmployeeCount))
	print("Out of total rows from file: " + str(rowCount))

def chooseDateRange(month, year):
	colCount = 0
	rowCount = 0
	currMonth = 0
	currYr = 0
	chooseDateRangeCount = 0
	for row in rows[:100]:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")
		for col in row:
			if colCount == 6:
				# print(col)
				dt = datetime.strptime(col, '%Y-%m-%d')
				if month == dt.month:
					if year == dt.year:
						print("____chooseDateRange: " + str(chooseDateRangeCount))
						printRow(row)
						chooseDateRangeCount += 1
						# print(col)
				# 		printRow(row)
				# 		print("\n")
			# if col == username:
			# 	print(row)
			# 	print("\n")
			colCount += 1
		rowCount += 1
		colCount = 0
		
	print("# matches found = " + str(chooseDateRangeCount))
	print("Out of total rows from file: " + str(rowCount))

def chooseService(service):
	colCount = 0
	rowCount = 0
	chooseServiceRowCount = 0
	for row in rows[:100]:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")

		# print("ROW COUNT: " + str(rowCount))
		for col in row:
			if colCount == 16:
				if col == service:
					print("____chooseServiceRowCount: " + str(chooseServiceRowCount))
					printRow(row)
					chooseServiceRowCount += 1
					# print(row)
				# print("\n")
			colCount += 1
		rowCount += 1
		colCount = 0
	
	print("# matches found = " + str(chooseServiceRowCount))
	print("Out of total rows from file: " + str(rowCount))

def chooseCompany(company):
	colCount = 0
	rowCount = 0
	chooseCompanyCount = 0
	for row in rows[:100]:
		print("______________________________________")
		print("Row Count from File: " + str(rowCount))
		print("--------------------------------------")

		for col in row:
			if colCount == 12:
				if col == company:
					print("____chooseServiceRowCount: " + str(chooseCompanyCount))
					printRow(row)
					chooseCompanyCount += 1
					# print(row)
				# print("\n")
			colCount += 1
		rowCount += 1
		colCount = 0
	
	print("# matches found = " + str(chooseCompanyCount))
	print("Out of total rows from file: " + str(rowCount))

def usernameInRow(username, row):
	if not username:
		isAMatch = True
	else:
		isAMatch = row[0] == username
	# print("usernameInRow isAMatch: " + str(isAMatch))
	return isAMatch

def firstNameInRow(fname, row):
	if not fname:
		isAMatch = True
	else:
		isAMatch = row[2] == fname
	# print("firstNameInRow isAMatch: " + str(isAMatch))
	return isAMatch

def lastNameInRow(lname, row):
	if not lname:
		isAMatch = True
	else:
		isAMatch = row[3] == lname
	# print("lastNameInRow isAMatch: " + str(isAMatch))
	return isAMatch

def dateInRow(month, year, row):
	dt = datetime.strptime(row[6], '%Y-%m-%d')
	
	monthIsAMatch = False
	yrIsAMatch = False
	isAMatch = False

	# if not month and year is not None:
	# if not month and not year:
	if not month and year is not None:
		monthIsAMatch = True
		yrIsAMatch = dt.year == year
	# elif not year and not month:
	elif not year and month is not None:
		monthIsAMatch = dt.month == month
		yrIsAMatch = True
	elif year is None and month is None:
		monthIsAMatch = True
		yrIsAMatch = True
	else:
		monthIsAMatch = dt.month == month
		yrIsAMatch = dt.year == year

	# yrIsAMatch = dt.year == year
	
	isAMatch = monthIsAMatch & yrIsAMatch

	# print("dateInRow isAMatch: " + str(isAMatch))
	return isAMatch

def serviceInRow(service, row):
	if not service:
		isAMatch = True
	else:
		isAMatch = row[16] == service
	# print("serviceInRow isAMatch: " + str(isAMatch))
	return isAMatch

def companyInRow(company, row):
	if not company:
		isAMatch = True
	else:
		isAMatch = row[12] == company
	# print("companyInRow isAMatch: " + str(isAMatch))
	return isAMatch

def filterByDateEmployeeCompanyService(month, year, username, company, service, row):

	found = dateInRow(month, year, row) & userNameInRow(username, row) & companyInRow(company, row) & serviceInRow(service, row)
	# print("found? " + str(found))
	return found

def returnHoursOfCompanyServiceKeyPair(company, service):
	
	companyServiceKey = "['" + company + "', '" + service + "']"
	companyServiceHrs = 0

	for key, value in companyServiceHRSKeyPairs.items():
		if key == companyServiceKey:
			companyServiceHrs = value

	return companyServiceHrs


# _______________ end of FUNCTION list _______________



# _______________ start of FILTERS _______________

def ultimateFilter(month, year, username, company, service):
	colCount = 0
	rowCount = 0
	matches = 0
	monthMatched = False
	yearMatched = False
	dateMatched = False
	usernameMatched = False
	companyMatched = False
	serviceMatched = False
	# filteredRows = []

	for row in rows:
		# print("______________________________________")
		# print("Row Count from File: " + str(rowCount))
		# print("--------------------------------------")
		# print(row)
		for col in rows:
			# print("[" + fields[colCount] + "]: " + col)
			if colCount == 0:
				# if not username:
				# 	usernameMatched = True
				# 	# print("No username filter")
				# else:
					usernameMatched = usernameInRow(username, row)
			if colCount == 6:
				dateMatched = dateInRow(month, year, row)
				# if not month and year is not None:
				# 	monthMatched = True
				# 	yearMatched = dateInRow(month, year, row)
				# # print(dateInRow(month, year, row))
			if colCount == 12:
				# if not company:
				# 	companyMatched = True
				# 	# print("No company filter")
				# else:
					companyMatched = companyInRow(company, row)
			if colCount == 16:
				# if not service:
				# 	serviceMatched = True
				# 	# print("No service filter")
				# else:
					serviceMatched = serviceInRow(service, row)
			# print("Match Results:")
			# print("usernameMatched: " + str(usernameMatched))
			# print("companyMatched: " + str(companyMatched))
			# print("serviceMatched: " + str(serviceMatched))

			colCount += 1
		rowCount += 1
		colCount = 0
		# print("\n")
		if usernameMatched & dateMatched & companyMatched & serviceMatched:
			# print(row)
			ultimateFilteredRows.append(row)
			# filteredRows.append(row)

	# return filteredRows
		# else:
	# print("# matches found = " + str(chooseDateRangeCount))
	# print("Out of total rows from file: " + str(rowCount))

	# print("Match Results:")
	# # print(row)
	# print("usernameMatched: " + str(usernameMatched))
	# print("companyMatched: " + str(companyMatched))
	# print("serviceMatched: " + str(serviceMatched))
	# print("usernameMatched: " + str(usernameMatched))


# _______________ end of FILTERS _______________

def filterIt(row, user):

	# companyName = ""

	# summarize

	summaryOfAllCompanyServiceHrs = []


	filteredCompanyList =[]

	def getFilteredCompanyList(): 
		colCount = 0
		rowCount = 0

		for row in ultimateFilteredRows:
			print("______________________________________")
			print("Row Count from File: " + str(rowCount))
			print("--------------------------------------")

			for col in row:
				# print("[" + fields[colCount] + "]: " + col)
				if colCount == 12:
					if str(col) in filteredCompanyList:
						print("already in list")
					else:
						filteredCompanyList.append(col)
				colCount += 1
			rowCount += 1
			colCount = 0
			print("\n")

	getFilteredCompanyList()


	filteredServiceItems =[]

	def getFilteredServiceItems():
		colCount = 0
		rowCount = 0

		for row in ultimateFilteredRows:
			print("______________________________________")
			print("Row Count from File: " + str(rowCount))
			print("--------------------------------------")

			for col in row:
				# print("[" + fields[colCount] + "]: " + col)
				if colCount == 16:
					if str(col) in filteredServiceItems:
						print("already in list")
					else:
						filteredServiceItems.append(col)
				colCount += 1
			rowCount += 1
			colCount = 0
			print("\n")

	getFilteredServiceItems()

	filteredCompanyServicePairs = []

	def createCompanyServicePairsForFilteredRows():
		for company in filteredCompanyList:
			for service in filteredServiceItems:
				filteredCompanyServicePairs.append([company,service])


	createCompanyServicePairsForFilteredRows()

	filteredCompanyServiceHRSKeyPairs = {}

	def createCompanyServiceHRSKeyPairsForFilteredRows():
		for pair in filteredCompanyServicePairs:
			filteredCompanyServiceHRSKeyPairs.update({str(pair): 0})
			# print(pair)

	createCompanyServiceHRSKeyPairsForFilteredRows()

	# def addHours():

	def totalHoursPerCompanyServicePair(company, service):
		companyMatched = False
		serviceMatched = False
		totalHours = float(0.0)
		colCount = 0
		rowCount = 0

		for row in ultimateFilteredRows:
			# print("______________________________________")
			# print("Row Count from File: " + str(rowCount))
			# print("--------------------------------------")
			# print(row)

			for col in row:
				# if colCount == 12:
				companyMatched = companyInRow(company, row)
				# if colCount == 16:
				serviceMatched = serviceInRow(service, row)

				if colCount == 11:
					# print(col)
					if companyMatched & serviceMatched:
				# 		# print(col)
						totalHours = totalHours + float(col)

				colCount += 1
			rowCount += 1
			colCount = 0	

		return totalHours

	print("\n")

	print("Companies (" + str((len(filteredCompanyList))) + " count ):")
	print(filteredCompanyList)

	print("\n")

	print("Companies-Service (" + str((len(filteredCompanyServicePairs))) + " count ):")
	for pair in filteredCompanyServicePairs:
		print(pair)

	print("\n")

	print("Companies-Service: Hrs (" + str((len(filteredCompanyServiceHRSKeyPairs))) + " count ):")
	for key, value in filteredCompanyServiceHRSKeyPairs.items():
		print(key, value)

	print("\n")

	print("Service Item (" + str((len(filteredServiceItems))) + " count ):")
	print(filteredServiceItems)
	
	# print("\nTotal: " + str(totalHoursPerCompany("Hoppier", "T4/T5's")))
	print(totalHoursPerCompanyServicePair("Hoppier", "T4/T5's"))

	for pair in filteredCompanyServicePairs:
		summaryOfEachCompanyServiceHrs = []
		print("[" + pair[0] + ", " + pair[1] + "] hours : " + str(totalHoursPerCompanyServicePair(pair[0], pair[1])))
		# print("\n")
		summaryOfEachCompanyServiceHrs.append(user)
		summaryOfEachCompanyServiceHrs.append(pair[0])
		summaryOfEachCompanyServiceHrs.append(pair[1])
		summaryOfEachCompanyServiceHrs.append(totalHoursPerCompanyServicePair(pair[0], pair[1]))

		summaryOfAllCompanyServiceHrs.append(summaryOfEachCompanyServiceHrs)

	return summaryOfAllCompanyServiceHrs


def getHoursFilteredByDateEmployeeCompanyService(month, year, username):
	
	#filter by date and employee
	ultimateFilter(month, year, username, "", "")
	filteredIt = filterIt(ultimateFilteredRows, username)
	# ultimateFilteredRows = []

	return filteredIt

summarizedHoursList = []

# htmlFilter =

month = 07
yr = 2021
user = ""

def defaultFilter(month, yr, user):
	summarizedHoursList = []
	# filteredData = getHoursFilteredByDateEmployeeCompanyService(04, 2021, "scott@experienceyourblueprint.com")
	filteredData = getHoursFilteredByDateEmployeeCompanyService(month, yr, user)
	print("Test Data: ")
	print(filteredData)
	summarizedHoursList = filteredData

	return summarizedHoursList

# summarizedHoursList = defaultFilter(month, yr, user)


summarizedHoursListPerEmployee = []

for employee in usernameList:
	summarizedHoursList = defaultFilter(month, yr, employee)
	summarizedHoursListPerEmployee.append(summarizedHoursList)
	# print(summarizedHoursList)

summarizedHoursPerCompanyServicePerEmployee = [] 

for pair in companyServicePairs:
	# print(pair)
	for summary in summarizedHoursListPerEmployee:
		for s in summary:
			# print(s)
		# print("user: " + str(s[0]))
			if pair[0] == s[1] and pair[1] == s[2]:
				tempArr = []
				print("==========Finding matches for " + str(pair) + ": ")
				print("pair[0] : " + str(pair[0]) + " mathces w/ s[1]: " + str(s[1]))
				print("pair[1] : " + str(pair[1]) + " matches w/ s[2]: " + str(s[2]))
				print("This is for employee: " + str(s[0]))
				if s[3] > 0:
					tempArr.append(pair)
					tempArr.append(s[0])
					tempArr.append(round(s[3],2))				
					summarizedHoursPerCompanyServicePerEmployee.append(tempArr)

				# print("It's a match ")
			# print("pair[0] : " + str(pair[0]) + " checking match with s[1]: " + str(s[1]))
			# print("pair[1] : " + str(pair[1]) + " checking match with s[2]: " + str(s[2]))

print("------summarizedHoursPerCompanyServicePerEmployee------")

summarizedHoursPerCompanyServicePerEmployee.sort()

ultimateFilteredRows.sort()

for entry in summarizedHoursPerCompanyServicePerEmployee:
	print(entry)

# print(summarizedHoursList)

@app.route("/getdata", methods=['GET','POST'])
def fetchData():
	username = request.form.get('username') #month from the log in screen
	year = request.form.get('year') #month from the log in screen
	month = request.form.get('month') #username from the log in screen
	print(month)
	print(year)
	print(username)

	return jsonify(ultimateFilteredRows)

@app.route("/getFields", methods=['GET'])
def getFields():
	return jsonify(fields)

usernameList.sort()

@app.route("/getEmployees", methods=['GET'])
def getEmployees():
	return jsonify(usernameList)

companyList.sort()

@app.route("/getClients", methods=['GET'])
def getClients():
	return jsonify(companyList)

serviceItems.sort()

@app.route("/getServiceItems", methods=['GET'])
def getServiceItems():
	return jsonify(serviceItems)

@app.route("/summarizehours", methods=['GET','POST'])
def summarizehours():
	return jsonify(summarizedHoursPerCompanyServicePerEmployee)


if __name__ == '__main__':
	 app.run()



