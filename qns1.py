#!/usr/bin/env python
# coding: utf-8

# jupyter notebook
# 
# Python 3
# 
# qns 1 is:
# 
# Suppose you have a sequence consisting of L’s and M’s where L denotes a descending and M denotes an ascending sequence. Take a sequence as an input and decode it to construct a number without repeated digits.
# (For example:
# MMLLMLML -> 125437698
# MMMM -> 12345
# LLLL-> 54321
# )

# In[1]:


Pattern1 = input("Enter the Pattern : ")


# In[2]:


Pattern2 = input("Enter the Pattern : ")


# In[3]:


Pattern3 = input("Enter the Pattern : ")


# In[14]:


def printPattern(patternvalue): 
    curr_max = 0 #Avoid repeated char
    last_entry = 0  # find last printed char
    i = 0
    while i < len(patternvalue): 
        NextM_count = 0 #find next M 
        if patternvalue[i] == "M": 
            # calculate  next  M's  count
            j = i + 1
            while j < len(patternvalue) and patternvalue[j] == "L": 
                NextM_count += 1
                j += 1
            if i == 0: 
                curr_max = NextM_count + 2
                last_entry += 1
  
                print("", last_entry, end = "") 
                print("", curr_max, end = "") 
                last_entry = curr_max  #last entry is maximum
            else: 
                curr_max += NextM_count + 1
                last_entry = curr_max 
                print("", last_entry, end = "") 
            for k in range(NextM_count): 
                last_entry -= 1
                print("", last_entry, end = "") 
                i += 1 
        elif patternvalue[i] == "L": 
            if i == 0: 
                j = i + 1
                while j < len(patternvalue) and patternvalue[j] == "L": 
                    NextM_count += 1
                    j += 1
                curr_max = NextM_count + 2
                print("", curr_max, curr_max - 1, end = "") 
                last_entry = curr_max - 1
            else: 
                print("", last_entry - 1, end = "") 
                last_entry -= 1
        i += 1
    print()    


# In[12]:


if __name__ == "__main__": 
    print(Pattern1 + "->")
    printPattern(Pattern1)
    print(Pattern2 + "->")
    printPattern(Pattern2)
    print(Pattern3 + "->")
    printPattern(Pattern3) 

