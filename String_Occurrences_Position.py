#!/usr/bin/env python
# coding: utf-8

# jupyter notebook
# 
# Python 3
# #qns 2 is:
# 
# 
#  Accept a String input
#  Accept a search String to search in the above input
#  Verify if the search String is present in the input string and the position and number of occurrences
# Eg. If the String input is - I like reading about threading
# and the search String is read
# then the output should be as below
# Occurrences - 2
# Position - 8,24 

# In[1]:


text = input("Enter strings : ")


# In[13]:


pat = input("Enter string to check matching: ")


# In[35]:


def find_index(String_input, searching_string):
    List = []
    index = 0 #index starting from 0
    length = len(String_input)
    while index < length:
        i = String_input.find(searching_string, index)
        if i == -1:
            print("Occurrences -", len(List))
            return List
        List.append(i)
        index = i + 1  
    return List


# In[36]:


#main function
if __name__ == '__main__':     
    print("Position-",find_index(text,pat))
    

