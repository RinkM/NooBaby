goals = ["track bottles", "track partial bottles", 
"create baby profile that: tracks age, name, gender, and OTHERS(weight, height??**kwargs???", 
"change and update profile", "tkinter gui interface", "track solid food", 
"include nutrional data", "represent averages over time (1 day), 1 week, 1 month, etc.",
 "track milestones: words, crawling, sitting, sounds, walking, riding a bike, etc.",
  "add calander", "LOTS MORE TO DO IF I WANT", ]
for k in goals: 
	print (k)

################################################
############  NOTES AND THOUGHTS  ############
################################################
# https://fdc.nal.usda.gov/api-guide.html
# Your API key for mrinkert@gmail.com is:
# rAZ99ea6kjnTyaSpLlAc9YX758uSMdbQHJqKnBEI

# You can start using this key to make web service requests. Simply pass your key in the URL when making a web request. Here's an example:



# https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=2&api_key=rAZ99ea6kjnTyaSpLlAc9YX758uSMdbQHJqKnBEI


#Nutrition information. How do I use it?  As kid eats more solid food?  Calories, protein, sugar, etc...Like MyFitness Pal


#so... for the 3rd time. 
# class for full bottle. Class for partial bottle.
# Information stored as :



# so... again.
# baby tracker. you say "baby fed." it adds a bottle, the time. 
# baby age tracker. how old?  need age of baby. counter for time. milestones?  1 month. 6 month. etc
#baby check list for cdc guidelines?  scrape?  baby age, which are approrpriate. tracks them. when they occur.   view a calander?  "grabbed things" "stood up" "started making sounds" "laughed at so and so"


#baby 
# 
# so...
# baby tracker.  how often do you feed?  How much?  need to record time. amount. 
# define a standard feeding - oz / ml
# graph it? track it over time?
# i actually don't know how to gather input and save it.



################################################
############  Program ####################################
################################################




# def main_menu():
# 	
# 
# 
# add a bottle, a nap, or a milestone, 
# 	Leena's information (better name)
	
# 	Settings


import datetime
# class exBaby:
# 	def __init__(self, first_name, last_name, gender, birthday):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.gender = gender
# 		self.birthday = birthday
# 		# self.age = 1
# 		#result is an object : <__main__.Baby object at 0x000001CA7F7F7FD0>



#datetime information : # https://docs.python.org/3/library/datetime.html
#timedelta can measure from two dates.  

#already - inputs can be ANYTHING. Need to fix that. 
def make_baby():
	print("Making the baby is the fun part...")
	first = input("What's your baby's first name?" )
	last = input("What's your baby's last name?" )
	gender = int(input("Their gender?\n1: Male \n2: Female "))			#How do I change pronouns later?  
	birthday = input("Their birthday: MM/DD/YY" )
	newborn = first(first, last, gender, birthday)
	print(newborn)
	# Pass this info through a class

# make_baby()
time = datetime()
print(time)


class FullBottle:
	def __init__(self, formula, time, total):
		self.formula = formula
		self.time = time
		self.remaining = 0
		self.total = total


class PartialBottle:
	def __init__(self, formula, time, remaining, total):
		self.formula = formula
		self.time = time
		self.remaining = remaining
		self.total = total


def feed(time, amount):
	pass

# #how do I track this data?  like a csv?
# [12:30, 120, "ml"], [12:30, 120, "ml"]  multple lists. 
# # dictionary : key = time value = amount   can we understand we're in mls?  or always conver to mls?  or oz?

