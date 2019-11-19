'''ECON 611 Midterm - Answers'''
##### Q1. #######
# 1: NO, this will create a file with the correct name, but the incorrecty named file still exists in the 
# directory and needs to be deleted.
# 2. YES, this option will rename the file. 
# 3. NO, the period (.) points at where to move the file and doesn't provide a new file name, also identical file names can not be created
# 4. NO, same as 3 

# ##### Q2. #######
# The output of pwd tells you that you start in the /Users/mario/data directory where we create a new folder called combine. 
# The comand (mv) moves the file regressions.py to the new folder (combine). 
# The next line also moves the file we just moved. The tricky part here 
# is where the file was moved to. Recall that .. means ‘go up a level’, 
# so the file should be in /Users/mario but in this case since regressions_complete.py is a file not a 
# directory the regressions.py gets lost (not best practice). Notice that .. is interpreted with respect 
# to the current working directory, not with respect to the location of the file being copied. 
# So, the only thing that will show using ls (in /Users/mario/data) is the combine folder.

# ##### Q3. #######
# 1. cd ~/Desktop/
# 2. mkdir midterm_skills
# 3. cd midterm_skills/
# 4. git init
# 5. ls -a => output: ./    ../   .git/

##### Q4. #######
# NOOOOOOO you do not need to make the another_midterm_skills sub-directory a Git repository because the midterm_skills repository 
# will track all files, sub-directories, and sub-directory files under the midterm_skills directory. 
# Recall that in the previous step (question 3) git init will create a repository that includes subdirectories and their files, thus there is 
# no need to create separate repositories nested within the midterm_skills repository, 
# whether subdirectories are present from the beginning or added later. 

##### Q5. ####### 
# Correct solution 1##
# 1) cd ../: this will take you back to ~/Desktop/midterm_skills
# 2) rm -rf another_midterm_skills/.git
# 3) cd another_midterm_skills/
# 4) ls -a: will give you this output: ./  ../
# # Correct solution 2##
# 1) if you are in the another_midterm_skills folder then you can run this:
# 2) rm -rf .git

# This option also works
# 1) rm -r another_midterm_skills/

# This option works if you are Desktop/midterm_skills/another_midterm_skills$
# 1) rm -rf ./.git
# #Brute force solution, but removes the another_midterm_skills folder, which the question is not asking you to do
# rm another_midterm_skills: wont work (rm: another_midterm_skills: is a directory)
# rm -rf another_midterm_skills: removes the entire folder (including the .git file)

##### Q6.1 ####### 
def vowel_counter_dict(input_string, vowels):
    '''List of vowels in input_string'''
    vow_list = [i for i in input_string.lower() if i in vowels.lower()]
    print("Total number of vowels in "+input_string + " %d" % len(vow_list))
    return vow_list

print (vowel_counter_dict('hEllo', 'aeiou'))
print (vowel_counter_dict('hEllo', 'aEiOU'))
print (vowel_counter_dict('hEllo World' , 'aEiOU'))
print (vowel_counter_dict('speCCiaaaAAlist', 'aEiOU'))
print (vowel_counter_dict('inSaneLy', 'aEiOU'))
print("\n")

# ##### Q6.2 ####### 
# 1) git add strings_practice.py 
# 2) git status 
# 3) git commit -m "practice midterm"

# ##### Q7. ####### 
def vowel_counter_dict(input_string, vowels):
    '''List of vowels in input_string'''
    vow_list = [i for i in input_string.lower() if i in vowels.lower()]
    print("Total number of vowels in "+input_string + " %d" % len(vow_list))
    count = {vow:sum([1 for char in input_string.lower() if char == vow]) for vow in vowels.lower()}
    return count

print (vowel_counter_dict('hEllo', 'aeiou'))
print (vowel_counter_dict('hEllo', 'aEiOU'))
print (vowel_counter_dict('hEllo World' , 'aEiOU'))
print (vowel_counter_dict('speCCiaaaAAlist', 'aEiOU'))
print (vowel_counter_dict('inSaneLy', 'aEiOU'))
print("\n")

#### Q7.2 ####### 
# The second line reveals which versions of the file Git is comparing (meaning Git is comparing the old and new versions of the file
# you have been working on), in thi case`9c17183` and `3b4ce62` are unique computer-generated labels for those versions.


#### Q.8 ####### 
def is_num_prime(n):
    if n ==1:
        return False
    k = 2
    while k < n:
        if n%k == 0:
            return False
        k += 1

    return True

for i in range(1, 101):
    if is_num_prime(i) is True:
        print("Number %d is prime" %i)
print("\n")

##### Q.9 ####### 
def manual_median(x):
    '''first check the lenght'''
    n = len(x)
    
    '''then sort the entries'''
    sorted_x = sorted(x)
    
    '''Now that the entry is sorted, find the midpoint'''
    ''' Floor Division(//) : Divides and returns the integer value of the quotient. 
        It dumps the digits after the decimal point
    '''
    midpoint = n // 2
    
    
    '''if len is odd return the middlevalue'''
    if n % 2 == 1:
        return sorted_x[midpoint]
    else:
        '''If len is even, then return average of middle values'''
        middle_1 = midpoint -1
        middle_2 = midpoint
        return(sorted_x[middle_1]+sorted_x[middle_2])/2

''''''
'''Given a list with of ages'''
ages = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(manual_median(ages))
print("\n")

##### Q 10 ####### 
def newton_squareroot(n):
    root = n/2
    for k in range(1, 21):
        root = (1/2) *(root + (n/root))
    return root

for i in range(1, 101):
    print("Newton Squareroot approximation of square root for number %d is:" %i, newton_squareroot(i))
