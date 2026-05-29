########### Regular Expressions ########### 
# Regular expressions are a powerful tool for matching patterns in text.
# They are used for searching, replacing, and manipulating strings based on specific patterns.  
# The 're' module in Python provides functions for working with regular expressions.
import re
# Example: Finding all occurrences of a pattern in a string
text = "The rain in Spain stays mainly in the plain."
pattern = r'\b\w+ain\b'  # Matches words that end with 'ain'
matches = re.findall(pattern, text)
print(matches)  # Output: ['rain', 'Spain', 'plain']
# Example: Replacing a pattern in a string
new_text = re.sub(r'\bain\b', 'XXX', text)
print(new_text)  # Output: "The rXXX in SpXXX stays mainly in the plXXX."   

########## About the regular expression pattern ##########
# \b: Word boundary, ensures that we match whole words.
# \w+: Matches one or more word characters (letters, digits, or underscores).
# 'ain': The specific sequence of characters we want to match.      


######### understanding the regular expression pattern ##########
# The regular expression pattern r'\b\w+ain\b' can be broken down as follows:
# \b: This asserts a word boundary, meaning that the match must start at the beginning of a word.
# \w+: This matches one or more word characters (letters, digits, or underscores). It ensures that we are matching a whole word that contains the sequence 'ain'.           

######### Regular expression quick guide ##########
# . : Matches any character except a newline.
# ^ : Matches the start of a string.
# $ : Matches the end of a string.
# * : Matches 0 or more repetitions of the preceding pattern.
# + : Matches 1 or more repetitions of the preceding pattern.
# ? : Matches 0 or 1 repetition of the preceding pattern.
# {n} : Matches exactly n repetitions of the preceding pattern.
# {n,} : Matches n or more repetitions of the preceding pattern.
# {n,m} : Matches between n and m repetitions of the preceding pattern.
# [] : Matches any one of the characters inside the brackets.
# | : Acts as a logical OR between patterns.
# () : Groups patterns together and captures the matched text.  

############## Re module functions ##############
# re.findall(pattern, string): Returns a list of all non-overlapping matches of the pattern in the string.
# re.search(pattern, string): Searches for the first occurrence of the pattern in the string and returns a match object if found, otherwise returns None.
# re.sub(pattern, replacement, string): Replaces all occurrences of the pattern in the string with the specified replacement.
# re.match(pattern, string): Checks for a match only at the beginning of the string and returns a match object if found, otherwise returns None.
# re.split(pattern, string): Splits the string by the occurrences of the pattern and returns a list of substrings.      


print ("****************************** Below output from regular expression *************************************")
import re
import os
os.chdir("/Users/ayushkumar/Learning/GitHub/Ayush_Personal/Coding/Python/Practice/Coursera_Python")
file1=open("mbox-short.txt")
for line in file1:
    line=line.rstrip()
 #    print(re.search('From:',line))
    if re.search('^From:',line):  ####### The ^ symbol is used to indicate that the pattern should match only at the beginning of the line.
        print(line)


################# ^X-C.* : This regular expression pattern can be broken down as follows:
# ^: Asserts the start of a line.
# X-C: Matches the literal characters "X-C".
# .*: Matches any characters (zero or more) that follow "X-C" on the same line. The dot (.) matches any character except a newline, and the asterisk (*) allows for zero or more occurrences of that character. This means that it will match any line that starts with "X-C" followed by any characters until the end of the line.

#################### ^X-\S+ : This regular expression pattern can be broken down as follows:
# ^: Asserts the start of a line.
# X-: Matches the literal characters "X-".
# \S+: Matches one or more non-whitespace characters that follow "X-" on the same line. The \S matches any character that is not a whitespace character (such as space, tab, or newline), and the plus sign (+) allows for one or more occurrences of that non-whitespace character. This means that it will match any line that starts with "X-" followed by one or more non-whitespace characters until the end of the line.  

########## Matching and extracting data with regular expressions ##########
# Regular expressions can be used to not only match patterns but also to extract specific data from strings. For example, if we want to extract email addresses from a text, we can use the following regular expression pattern:
# [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} : This pattern can be broken down as follows:
# [a-zA-Z0-9._%+-]+: Matches one or more characters that can be part of an email username (letters, digits, dots, underscores, percent signs, plus signs, or hyphens).
# @: Matches the literal "@" character that separates the username from the domain.
# [a-zA-Z0-9.-]+: Matches one or more characters that can be part of a domain name (letters, digits, dots, or hyphens).
# \.: Matches the literal dot character that separates the domain from the top-level domain.
# [a-zA-Z]{2,}: Matches two or more letters that represent the top-level domain (such as "com", "org", "net", etc.). This pattern will allow us to extract valid email addresses from a given text.         



################### findall method ##############
# The re.findall() function is used to find all occurrences of a pattern in a string and return them as a list. For example, if we want to find all the words that start with "a" in a given text, we can use the following code:
text = "The cat sat on the mat and ate an apple."
pattern = r'\ba\w*'  # Matches words that start with 'a'
matches = re.findall(pattern, text) 
print(matches)  # Output: ['ate', 'an', 'apple']
# In this example, the regular expression pattern r'\ba\w*' is used to
# \b: Asserts a word boundary, ensuring that we match the start of a word.
# a: Matches the literal character 'a', indicating that we want to find words that start with 'a'.
# \w*: Matches zero or more word characters (letters, digits, or underscores) that follow the initial 'a'. This allows us to match the entire word that starts with 'a'. The re.findall() function will return a list of all the words in the text that start with the letter 'a'.  
####### what is r' in regular expression ##########
# The r in r'...' stands for "raw string". In Python, raw strings are used to treat backslashes (\) as literal characters rather than escape characters. This is particularly useful in regular expressions, where backslashes are commonly used to denote special characters or to escape certain characters. By using a raw string, you can avoid having to double backslashes in your regular expression patterns. For example, instead of writing '\\b' to represent a word boundary, you can simply write r'\b' in a raw string, making the regular expression easier to read and write.   



####################### re.findall([AEIOU], text) : This regular expression pattern can be broken down as follows:
# [AEIOU]: This character class matches any single uppercase vowel (A, E, I, O, U) in the text. The square brackets [] indicate a character class, and the characters inside the brackets specify the set of characters to match. In this case, it will match any occurrence of the uppercase vowels in the given text. The re.findall() function will return a list of all the uppercase vowels found in the text. For example, if the text is "Hello World", the output will be ['E', 'O', 'O'].      

################## re.findall([AEIOUS]+, text) : This regular expression pattern can be broken down as follows:
# [AEIOUS]+: This character class matches one or more occurrences of uppercase vowels (A, E, I, O, U, S) in the text. The plus sign (+) indicates that we want to match one or more occurrences of the characters specified in the character class. In this case, it will match sequences of uppercase vowels that may include the letter 'S' as well. For example, if the text is "HELLO WORLD", the output will be ['E', 'O', 'O']. If the text is "AEIOUS", the output will be ['AEIOUS']. The re.findall() function will return a list of all the sequences of uppercase vowels found in the text.          


############## re.findall('^F.+:', text) : This regular expression pattern can be broken down as follows:
# ^: Asserts the start of a line.
# F: Matches the literal character 'F', indicating that we want to find lines that start with 'F'.
# .+: Matches one or more of any character (except a newline) that follows the initial 'F'. The dot (.) matches any character, and the plus sign (+) allows for one or more occurrences of that character. This means that it will match the entire line that starts with 'F' and continues until the first colon (:) is encountered.
# :: Matches the literal colon character that follows the sequence of characters after 'F'. This ensures that we are matching lines that start with 'F' and contain a colon somewhere in the line. The re.findall() function will return a list of all the lines in the text that start with 'F' and contain a colon. For example, if the text is "From:        John Doe", the output will be ['From: John Doe']. If the text is "F: Hello World", the output will be ['F: Hello World']. If the text is "Hello World", there will be no matches, and the output will be an empty list. 

############ but i want largest word that start with F and end with : then i can use the below regular expression pattern ############
# re.findall('^F.*:', text) : This regular expression pattern can be broken down as follows:
# ^: Asserts the start of a line.
# F: Matches the literal character 'F', indicating that we want to find lines that start with 'F'.
# .*: Matches zero or more of any character (except a newline) that follows the initial 'F'. The dot (.) matches any character, and the asterisk (*) allows for zero or more occurrences of that character. This means that it will match the entire line that starts with 'F' and continues until the last colon (:) is encountered in the line.
# :: Matches the literal colon character that follows the sequence of characters after 'F'. This ensures that we are matching lines that start with 'F' and contain a colon somewhere in the line. The re.findall() function will return a list of all the lines in the text that start with 'F' and contain a colon. For example, if the text is "From:        John Doe", the output




########## There is more difference in search () and findall() method in regualr expression is that search() method search and return true or false but findall() find the characters and return the result in list format.


########### how we can stop to make non-greedy match in regular expression ##########
# By default, regular expressions are greedy, meaning they will match as much of the text as possible while still satisfying the pattern. To make a non-greedy match, you can use the question mark (?) after the quantifier. For example, if you want to match the smallest possible string that starts with 'F' and ends with ':', you can use the following regular expression pattern:
# re.findall('^F.*?:', text) : This regular expression pattern can be broken down as follows:
# ^: Asserts the start of a line.       


############### Paranthesses in regular expression ##############
# In regular expressions, parentheses () are used for grouping and capturing. They allow you to group parts of the pattern together and extract specific portions of the matched text. For example, if you want to extract the username and domain from an email address, you can use the following regular expression pattern: 
# re.findall(r'(\w+)@(\w+\.\w+)', text) : This regular expression pattern can be broken down as follows:
# (\w+): This captures a sequence of one or more word characters (letters, digits, or underscores) and stores it as the first group. This will typically match the username part of an email address.
# @: Matches the literal "@" character that separates the username from the domain.
# (\w+\.\w+): This captures a sequence of one or more word characters followed by a dot and then one or more word characters. This will typically match the domain part of an email address. The re.findall() function will return a list of tuples, where each tuple contains the captured groups. For example, if the text is "Please contact us at           

