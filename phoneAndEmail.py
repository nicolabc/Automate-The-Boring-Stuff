#! python3

# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip,re,sys

if __name__ == '__main__':
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', re.VERBOSE)

    # TODO: Create email regex.
    emailRegex = re.compile(r'''(
           [a-zA-Z0-9._%+-]+      # username
           @                      # @ symbol
           [a-zA-Z0-9.-]+         # domain name
           (\.[a-zA-Z]{2,4})      # dot-something
           )''', re.VERBOSE)

    # TODO: Find matches in clipboard text.
    text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    # TODO: Copy results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')

    # BUG: TESTING THIS BUG IMMEDIATELY
    # FIXME: FIX THIS NOW


    # a = "42 1,234 6,368,745 but not the following: 12,34,567 (which has only two digits between the commas) 1234 (wh"
    # b = re.compile(r'(\d){3}*^,')
    # print(b.group(a))
    c = re.compile(r'^\d{1,3}(,\d{3})*$')
    mo1 = c.search('42 1,234 6,368,745 but not the following: 12,34,567 (which has only two digits between the commas) 1234 (wh')
    if mo1:
        print(mo1.groups() == True)

    sys.exit()
