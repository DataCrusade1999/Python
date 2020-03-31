import learn as learn

print('helloworld')
print('iamking')
print('kill me')
print('fishisbad')
print(5+7)
print(5+5)
print("i am on top of the world")
print("x=5")
print("y=5")
print("x+y")
#print i can
print('i can')
print("Hello\nWorld")
int(1.1)
float("2")
str("hty")
int(True)
print(25//5)
print(int(25//6))
#gotta do it other way
print("totalSec")
user_input=5
y=8
Guess_count= user_input + y
print(Guess_count)
#find out the reason why form line 22 to 25 worked
total_time=25+25
#btw line 13 has a new line function\n don't forget about it
print(total_time)
total_sec=total_time//25
print(total_sec)
float(total_sec)
#now look at line 27 to 32 and understan why it worked
import sys
print(sys.version)
#always remember that python is an interpreted language not a compiled one where the coding language knows in advanced that at the output you will get an error because at the time of compiling it encounter"s the error but doesn't tell us about it it only tell's us about the error at the time of output python can"t do this because it doesn't analyze the code like compiled language hence we know about it at the time of output
import sys
print(sys.float_info)
user_input= 30 * 8 + 58
print(user_input)
print(len("ashutosh"))# use len function to obtain the length of the string
print("do%"*120)
Guess_count=89
print(Guess_count)
print("45"*8)
demon=5
angel=5
print(demon+angel)
not_get=True
print(not_get)
#python is a case sensitive language i.e it can differentiate between upper and lower case letter
#name ='John Smith'
age=20
is_new=True
#print(name)
print(age)
print(is_new)
#name=input("why" )#analyze the use of the input function
#print('Hi' + name)
# target is mosh likes blue
#name=input("what is your name?")
#colour=input("what is your favourite colour?")
#print(name + 'likes' + colour)
#the above use of input function
#FROM LINE 61 TO 63 WE'VE USED INPUT FUNCTION WHICH TAKES USER INPUT AFTER WE'VE RAN THE CODE
#Name=input("what is your name?")
#Colour=input("what is your favourite colour?")
#print(Name + 'likes' + Colour)
#Weight=input('What is you weight in pounds?')
#print(type(Weight))
#Converted_Weight=int(Weight)*0.45359237
#print(Converted_Weight)
name='ashutosh'
print(name[0:-1])
#Name=input('What is your name?')
#print(Name[:] + 'Good Luck')
first_name="Ashutosh"
last_name="Pandey"
overall_name=f'{first_name}  {last_name}  is a niche person'
print(overall_name)
#d_wave=input(f"What could be your name sire? ")
#print(d_wave   +   "your highness")
#IN LINE 79 WE'VE USED FORMATTED STRING WHICH IS NICE SUBSTITUTE AS COMPARED TO RUDIMENTARY CONCATANATION
course="language for me"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('me'))
print("language" in course)
print(course.replace("language" , "25"))
#FROM LINE 84 TO 90 WE'VE USED SEVRAL FUNCTION/METHODS TRY TO ANALYZE THEM ONE BY ONE
#import math
#print(round(2.3))
#print(abs(-2))
#print(math.ceil(2.9))#TO USE ADDITIONAL MATH FUNCTION WE GOTTA IMPORT MATH IN PYTHON AS WE'VE DONE ABOVE FROM LINE 92 TO 94
if_yes=True
if_no=True
if_not=True
if if_yes:
    print("ip man")
if if_no:
    print("go to hell")
if if_not:
    print('bathe first')
#FROM LINE 96 TO 104 WE'VE USED IF ELIF CONDITIONS UNDERSTAND THEM.
import math
print(int(math.copysign(1 , -1)))
user_input=2
user_input+=44#we've used assignment operator
print(user_input)
good_credit_score=False
can_payback=False
cannot_Payback=True
if good_credit_score:
    print('Your loan has been approved')
    print("we're very happy that you are here" )
    if can_payback:
        print('good job')
elif cannot_Payback:
    print('sorry')
print('okay')
has_high_income=True
good_credit_score=True
if has_high_income:
    print("Approved")
    if good_credit_score:
        print('Approved')
#FROM LINE111 TO 127 WE'VE USED ELSE IF OPERATIONS ANALYZE THEM CAREFULLY
first=True
second=True
if first and second:
    print('logical operator and')
third=True
fourth=False
if third and not fourth:
    print('logical operator and not')
fifth=True
sixth=False
if fifth or sixth:
    print('logical operator or')
#from line 129 to 140 we've used logical operator understand the concept
name='j'
print(len(name))
if len(name)<3:
    print('name must be at least three chracter')
elif len(name)>=50:
    print('high')
#Weight=input('What is your weight?')
#x=int(Weight)*8
#print(x)
#name=input('what is your name?')
#x=len(name)
#if x>8:
    print('your name looks good')
#if x<8:
    print('your name must be at least 8 character long')
#elif x==8:
    print('on point')
#Weight=input('What is your weight?')
#unit=input('pound or kilogram')
#if unit.lower()=='kilogram':
 #   x=int(Weight)/0.453592
  #  print(f'you weigh {x} kilos')
#if unit.lower()=='pound':
   # y=int(Weight)*0.453592
    #print(f'you weigh {y} pound')
#FROM LINE 159 TO 166 WE'VE WRITTEN A PROGRAM THAT CONVERTS GIVEN WEIGHT INTO DIFFERENT UNTS IT'S A GOOD PROGRAM UNDERSTAN IT CAREFULLY AND TRY TO MODIFY IT i.e TRY TO WORK WITH 3 DIFFRENT WEIGHT UNT.
t=1
while t<=5:
    print('*'*t)
    t=t+1
#WHILE LOOPS HAVE AMAZING PROPERTIES CHECK OUT THE ABOVE CODE
secret_number=9
Guess_count=1
Guess_limit=3
# while Guess_count<=Guess_limit:
#    x=int(input('Guess: '))
#     Guess_count= Guess_count + 1
#     if x == secret_number:
#        print('You Won!')
#        break
# else:
#     print('Sorry You Failed :-(')
x='ashu'
print(x.find('u'))
print(x.replace('ashu' , '32'))
z=0
while z<=1:
    print(z)
    z=z+2
find_out_even_or_odd=19
x=find_out_even_or_odd%2
if x==1:
    print('the number is not odd')
else:
    print('try some other time')
e= 'king was here'
print(e[0])
my_string="ashutosh pandey"
print(my_string[2:-1])
print('ashutosh\tpandey')#we've used a new command "\t" which automatically gives us four spaces.
print(my_string[0])
#slicing[start:stop:step] is the form of slicing remember that whitespace count as a character.
print(my_string[0:5:2])
print(my_string[::-1])#so in slicing the step value not only tells pyhton about the step size that it should take but also about the orientation i.e from which side python should view the sentence.
print(my_string.replace('ashutosh','Ashutosh'))
first_letter=my_string[1:]
print('A'+ first_letter)#from line 207 to 208 we've used string concatnation to replace a word from the given function not that the above operation can also be performed by the "replace" operator.
print(my_string.split())
print(my_string.split('a'))#we've used split fuction analyze it carefully.
print('Ashutosh {}'.format('Pandey'))#this is '.format'method for string concatnation which is much easier than formatted string method as we've done above.because here we don't have to define a variable like we've done in fomatted string.
print('The {} {} {} {}'.format('brown','fox','was','quick'))
result=29/89
print(f'this was my number{result:1.2f}')#we've used prescion method 'variable:width.prescionf'this is the format that we use to determine the prescion.i've done this in formatted string but it can be done in'.format'too.
print('this is my {b}'.format(b='briefcase'))
print('this is my {0} {1} {2}'.format('briefcase',"don't",'leave it here'))
#from line 215to216 i've done work on some amazing properties of '.format' method of string concatnation make sure to look at them.
#OLD METHOD FOR STRING CONCATNATION
print("I think i'am %s here and you are %s too." %('done','done'))
my_list=[1,5,3,7]
print(my_list.sort())
print(my_list)
my_list[0]=2
print(my_list)
another_list=['a']
print(another_list.append('b'))
print(another_list)
print(my_list.reverse())
print(my_list)
my_list[0]=2
print(my_list)
still_another_list=[1,0,9,8,7,3]
print(another_list.pop())
print(another_list)
print(still_another_list.pop())
print(still_another_list)
print(still_another_list.pop(0))
print(still_another_list)
my_list_world=[1,1,3,5,3]
print(my_list_world.sort())
print(my_list_world)
#FROM LINE 220 TO 241 WE USED SEVERAL METHODS WHICH HAVE DIFFERENT USAGE IN PYTHON UNDERSTAND THEM CAREFULLY.BY THE WAY THE LIST IS GETTING UPDATED EVERY TIME UNLIKE JUPYTER NOTEBOOK.CHECK OUT THE UDEMY VIDEO WHICH IS CONCERNCED WITH THIS TOPIC FOR MORE INFORMATIN.\
my_dict={'key1':'a','key2':24}
print(my_dict['key1'].upper())
my_dicti={'key3':[0,1,2,4,3],'key4':['a','b','c','d']}
print(my_dicti['key3'].sort())
print(my_dicti['key3'])
print(my_dicti['key4'][0].upper())
my_dicti['key5']=['@','#','$','%']
print(my_dicti)
my_dicti['key6']={'another_dic':100}
print(my_dicti)
print(my_dicti['key6']['another_dic']*2)
print(my_dicti.keys())
print(my_dicti.values())
print(my_dicti.items())
#FROM LINE 243 TO 256 WE'VE USED DICTATIONARY TO HOLD OUR OBJECTS UNDERSTAND THEM CAREFULLY.
t=(1,2,3)
z=(1,4,5)
print(type(t))
print(t.count(1))
print(t.index(1))
#we cannot change the value of tuples like we can do with lists
print(t.__add__(z))
print(t.__contains__(1))
print(t.__getitem__(1))
print(t.__hash__())
#from line 258 to 266 we've used some amazing meyhods of tuples which can also be applied on other function.
my_set=set()
print(my_set)
print(my_set.add(1))
print(my_set)
g_list=[2,5,8,8,9,0]
print(set(g_list))
print(set(my_dicti['key3']))
print(1>2)#just using the bool.
print('hello'=='bye')#just using the bool.
#print(open('this is a text file .txt'))
#print(open('this is a text file.txt').read())
#print(open('this is a text file.txt').read().upper())
#print(open('this is a text file.txt').writable())
#print(open('this is a text file.txt').readable())
#print(open('this is a text file.txt').mode)
#print(open('this is a text file.txt').close())
print('hello'=='Hello')#just using the bool CAPTILIZATION DOES MATTER.
print('2'==2)#just using the bool.
print(2.0==2)
#from line 268 to 275 we've used 'set' method which has some unique properties that can be compared with 'sort' method.by the way it (set) also sorts out a list with some changes in them by the virtue of the properties that the 'set' funtion posses'mainly not repeating the same element twice.
#from line 278 to 284 we've used several methods to open a '.txt' file in python there is an image too availble in 'important stuff' folder where we've seen how to open a '.txt' file which is located in computer anywhere.
#we've also seen some operations that perform several tasks hence understand them carefully.
p={'k1':[{'nest key':['this is deep',['hello']]}]}
print(p['k1'][0]['nest key'][1][0])
print(p['k1'])
print(p['k1'][0])
d1={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d1['k1'][2]['k2'][1]['tough'][2][0])
list4=[1,2,[3,4,'hello']]
list4[2][2]='goodbye'
print(list4)
list5=[3,4,6,7,90,3]
print(sorted(list5))
print(set(list5))#set method to sort out a list is not recommended because it compromises data integrity.by the one of the interesting property of set is that it returns the value in dictionary format.
#WE'VE SOLVED SOME QUESTION ABOVE UNDERSTAND THEM CAREFULLY.
print(not (1==1))
h8=[1,9,0,7,8,9]
for num in h8:
    if num%2!=0:
        print(num)
    else:
        print('even numbers={}'.format(num))
my_dicti={'k1':7,'k2':8}
for (item,values) in my_dicti.items():
    print(item)
    print(values)
my_string='hello world'
for letters in my_string.split():
    print(letters)
print(len(my_string.split()))
tuples=(1,2,3),(4,5,6),(7,8,9)
print(len(tuples))
for (elements,fire,air) in tuples:
    print(elements)
    print(fire)
    print(air)
my_list=[88,34,54,76]
print(len(my_list))
for elements in sorted(my_list):
    print(elements)
#from 305 to 328 we've done work on several example of for loops understan them carefully it's really good.
my_string='playboy'
for letters in my_string.upper():
    if letters=='Y':
        continue
    print(letters)
my_list1=[1,1,2,3,4,5,55]
for elements in my_list1:
    if elements==1:
        print('you lost')
    else:
        print('your number is {}'.format(elements))
my_string='david'
for letter in my_string:
    if letter=='d':
        print("don't print")
x=0
while x<5:
    if x==2:
        pass
    print(x)
    x+=1
for num in range(10):
    print(num)#range is genrator type funtion.
index_count=0
for letters in 'ashutosh':
    print('At index {} the letter is {}'.format(index_count,letters))
    index_count+=1
words='ashutosh'
for letters in enumerate(words):#we can also use tuple unpacking here.
    print(letters)
#from line 359 to 361 we've used enumerate funtion understand it carefully.
my_list1=[1,2,3,4]
my_list2=['a','s','d']
for items in zip(my_list1,my_list2):
    print(items)#notice here the output is given in tuple hence tuple unpacking can be used here just as in enumerate and several other function.
#from line 363 to 366 we've used zip function understand it carefully.
print('a'in 'ashutosh pandey')# by the way this in function can also find whitespaces.
d={'key2':675}
print(675 in d.values())
#from line 368 to 370 we've used in method to find basically anything that the variable encapsulates.
t=(1,2)
print(min(t))
print(max(t))
#from line 372 to 374 we've used min and max function which perform the job as stated by their name. by the way do not use it for string for obivious reasons.
from random import shuffle
my_list=[2,3,4,5,6,7,8,9,0]
print(shuffle(my_list))# we  had to use print statement in line 379 because print shuuffle kinda stores the value and we have to ask for that value only then we can see the shuffled value.ther are some other functions that behave like this.
print(my_list)
from random import randint
print(randint(0,10))
st='print only the words that start with s in this sentence'
for elements in st.split():
    if elements[0]=='s':
        print(elements)
st='print only the words that start with s in this sentence'
for words in st.split():
    if len(words) %2 ==0:
        print(words  + ' the word is even!')
for num in range(1,101):
    if num%3==0:
        print('fizz')
    if num%5==0:
        print('buzz')
    else:
        print('fizzbuzz')
d={'key1': 645}
print(645 in d.values())
my_dicti={'k1':7,'k2':8}
for (item,values) in my_dicti.items():
    print(item)
    print(values)
print(my_dicti.__sizeof__())
print(my_dicti.pop('k1'))
print(my_dicti.items())
for (words,quash) in enumerate(my_list):
    print(words)
    print(quash)
def Add(a,b):
    c=a+b
    print(c)
Add(3,900)
def name_function(name='gypsy'):
    print('hello '+ name)
name_function('ashutosh pandey')
def my_function(parameter='that'):
    return 'something '+parameter
result=my_function('nothing')
print(result)
def add(n1,n2):
    return n1+n2
result=add(1,2)
print(result)
def pig_latin(words):
    first_word=words[0]
    if first_word in 'aeiou':
        pig_word=words+'ay'
    else:
        pig_word=words[1:]+first_word+'ay'
    return pig_word
result=pig_latin('apple')
print(result)
def my_func(*arg):
    return sum(arg)
result=my_func(12,34)
print(result)
def my_function(**kwarg):
    print(kwarg)
    if 'fruit' in kwarg:
        print("i don't eat {}".format(kwarg['fruit']))
my_function(fruit='apple')
def my_function_1(*args,**kwargs):
    print("i don't like {} eggs with {}".format(args[2],kwargs['food']))
my_function_1(10,90,88,food='milk')
#from line 409 to line 440 we've used def,arg,kwargs methods understand them
print(sum(range(1,99)))
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        result=min(a,b)
    elif a%2!=0  or b%2!=0:
        result=max(a,b)
    return result
result = lesser_of_two_evens ( 4 , 8 )
print(result)
def converter(name):
    return name
name=converter('ashutosh')
print(name[0:].upper())
def animal_cracker(name="nothing"):
    if name[0]==name[-5]:
        print('true')
    else:
        print('false')
    return name
name=animal_cracker('levelheaded llama').upper()
print(name)
def captilization(something='not'):
    return something
ashu=captilization('ashutosh'.capitalize())
print(ashu)
def sqrt(num):
    return num*num
my_num=[1,2,3,4]
for items in map(sqrt,my_num):
    print(items)
print(list(map(sqrt,my_num)))
def splicer(string):
    if len(string)%2==0:
        return "even"
    else:
        return string[0]
names=['andy','eve','sally']
print(list(map(splicer,names)))
for items in map(splicer,names):
    print(items)
def check_even(num):
    if num%2==0:  #can put return
        return 'even'
my_num=[1,2,3,4,5,6,7,8,9]
print(list(filter(check_even,my_num)))
print(list(map(lambda num:num*num,my_num)))
print(list(filter(lambda num:num%2==0,my_num)))
print(list(map(lambda x:x[0],names)))
x=23
def number():
    x=50
    return x
print(number())   #this is a example of LEGB(local global enclosing builtin) rule
x=50
def conte(x):
    print(f'X is {x}')
    x=200
    print(f'X is changed to {x}')
print(conte(x))
#CLASS BEGINS HERE OR OOP IN PYTHON (OBJECT ORIENTED PROGRAMMMING)
class Dog():
    def __init__(self,mybreed,leg,name,spot):
        self.breed=mybreed
        self.leg=leg
        self.name=name
        self.spot=spot
my_dog=Dog('german shephard', 4,False ,'dexter' )
print(my_dog.leg)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spot)
class Super():

    #CLASS OBJECT ATTRIBUTE
    conditions='favourble'
    def __init__(self,chemical,temprature,extraction):
        self.chemical=chemical
        self.temprature=temprature
        self.extraction=extraction
burkina_faso=Super(chemical='graphite',temprature='hot',extraction='solvent extraction method')
print(burkina_faso.chemical)
print(burkina_faso.conditions)
class Dog():
    species='mammal'#class object attribute
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self,color):
        print('WOOF My name is {} and my color is {} '.format(self.name,color))

root=Dog(name='Frankie',breed='german shephard')
print(root.name)
root.bark(color='black&white')
class Circle():
    #pi=3.14 we can have default argument just like function in class
    def __init__(self,pi,radius=10):
        self.radius=radius
        self.area=radius*radius*pi
        self.pi=pi
    def get_circumference(self):
        return self.radius*self.pi*2
my_circle=Circle(pi=3.14)
print(my_circle.get_circumference())
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
class Circle():
    pi=3.14# there are various ways to call a class object attribute as seen below
    def __init__(self,radius=10):
        self.radius=radius
        self.area=radius*radius*Circle.pi
    def get_circumference(self):
        return self.radius*Circle.pi*2
my_circle=Circle(radius=10)
print(my_circle.get_circumference())
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
class Supernode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)

root = Supernode(96403)
root.PrintTree()
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
#above is binary tree gotta understand it later
class Animal():
    def __init__(self):
        print('animal created')
    def who_am_i(self):
        print('i am a mammal')
    def eat(self):
        print('i am eating')
my_animal=Animal()
my_animal.eat()
class Whale(Animal):
    def __init__(self):
        Animal.__init__(self)
    def who_am_i(self):
        print('i am a fish')
my_fish=Whale()
my_fish.eat()
my_fish.who_am_i()
my_fish.__init__()

class Book():

    def __init__(self,author,title,pages):
        self.author=author
        self.title=title
        self.pages=pages

    def __str__(self):

     return f"{self.title} by {self.author} has {self.pages} pages"

    def __len__(self):

        return self.pages

   # def __del__(self):

        #print('a book has been deleted')  #try to understand why it is printing a book has been deleted even when we are not using del commmand
break_a=Book('Ashutosh Pandey','Python for Everybody',167)
print(break_a)
print(len(break_a))
try:
    rwanda=10+10
except:
    print("you are not adding correctly")
else:
    print('look like everything went well')
print(rwanda)
try:
    f=open('test_file','r')
    f.write('write a test line')
except TypeError:
    print('there was a type error')
except OSError:
    print('there was an os error')
finally:
    print('i always run')
def ask_for_int():
    while True:
        try:
            result=int(input('please give me a number: '))
            break
        except TypeError:
            print('that is not a number')
        except:
            print('check for other errors')

        else:
            print('end of the conundrum')
ask_for_int()


















































