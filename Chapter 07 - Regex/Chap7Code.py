#! python3
import sys, re

#-----------CHAPTER 7-----------#

if __name__ == '__main__':
    ## Matching Regex Objects ##
    # phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # mo = phoneNumRegex.search('My number is 415-555-4242.')
    # print('Phone number found: ' + mo.group())

    ## Grouping with Parentheses ##
    # phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    # mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
    # print(mo.groups())

    ## Matching Multiple Groups with the Pipe ##
    # heroRegex = re.compile(r'Batman|Tina Fey')
    # mo1 = heroRegex.search('Batman and Tina Fey.')
    # print(mo1.group())

    # batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    # mo = batRegex.search('Batmobile lost a wheel')
    # print('This ' + mo.group(0) + ', ' + mo.group(1)+ ' and ' + mo.group())

    ## Optional Matching with the Question Mark ##
    # batRegex = re.compile(r'Bat(wo)?man')
    # mo1 = batRegex.search('The Adventures of Batwoman')
    # print(mo1.group())
    #
    # phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    # mo1 = phoneRegex.search('My number is 415-555-4242')
    # print(mo1.group())

    ## Matching Zero or More with the Star *##
    # batRegex = re.compile(r'Bat(wo)*man')
    # mo1 = batRegex.search('The Adventures of Batman')
    # print(mo1.group())
    #
    # mo2 = batRegex.search('The Adventures of Batwoman')
    # print(mo2.group())
    #
    # mo3 = batRegex.search('The Adventures of Batwowowowoman')
    # print(mo3.group())

    ## Matching One or More with the Plus +##
    # batRegex = re.compile(r'Bat(wo)+man')
    # mo1 = batRegex.search('The Adventures of Batwoman')
    # print(mo1.group())

    # mo2 = batRegex.search('The Adventures of Batwowowowoman')
    # print(mo2.group())

    # mo3 = batRegex.search('The Adventures of Batman')
    # print(mo3 == None)  #(wo) does not appear, therefore None == True

    ## Matching Specific Repetitions with Curly Brackets ##
    # haRegex = re.compile(r'(Ha){3,5}') #Can use {,5} or {,} as well
    # mo1 = haRegex.search('HaHaHaHaHaHa')
    # print(mo1.group())

    # The ? may mean to use non-greedy approach or flagging an optional group

    ## The findall() Method ##
    # phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
    # print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

    ## Character Classes ##
    # xmasRegex = re.compile(r'\d+\s\w+')
    # print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

    ## Making Your Own Character Classes ##
    # Use square brackets'[]' to create your own character classes
    # vowelRegex = re.compile(r'[aeiouAEIOU]')
    # print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
    #
    # consonantRegex = re.compile(r'[^aeiouAEIOU]')   #Match every character not in brackets
    # print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

    ## The Wildcard Character .##
    # atRegex = re.compile(r'.at')
    # print(atRegex.findall('The cat in the hat sat on the flat mat.'))

    ## Matching Everything with Dot-Star ##
    # nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    # mo = nameRegex.search('First Name: Al Last Name: Sweigart')
    # print(mo.groups())
    #
    # nongreedyRegex = re.compile(r'<.*?>')
    # mo = nongreedyRegex.search('<To serve man> for dinner.>')
    # print(mo.group())
    #
    # greedyRegex = re.compile(r'<.*>')
    # mo = greedyRegex.search('<To serve man> for dinner.>')
    # print(mo.group())

    ## Matching Newlines with the Dot Character

    # noNewlineRegex = re.compile('.*')
    # print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
    #
    # print()
    #
    # NewlineRegex = re.compile('.*', re.DOTALL)
    # print(NewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

    ## Substituting Strings with the sub() Method ##
    # namesRegex = re.compile(r'Agent \w+')
    # print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
    #
    # print()
    #
    # agentNamesRegex = re.compile(r'Agent (\w)\w*')
    # print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

    ## Managing Complex Regexes re.compile(r'''\d\d\d\d\d ''', re.VERBOSE)##

    ##------------Project: Phone Number and Email Address Extractor-----------

    sys.exit()


