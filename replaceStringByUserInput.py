# 1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
#    a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
#    b. Logic -> Replace <<UserName>> with the proper name
#    c. O/P -> Print the String with User Name

# Username is valid if it has the minimum length 3
def is_valid(name):
    if len(name) >= 3:
        return True
    else:
        return False


# Replace the existing username with the new one.
def replace_by(uname_, new_uname_):
    # Convert string to list
    ls = list(uname_.split(' '))
    ls[1] = new_uname_+','
    # Convert list to string
    st = ' '
    return st.join(ls)


if __name__ == '__main__':
    try:
        uname = 'Hello <<UserName>>, How are you?'
        new_uname = input('Enter a valid Username : ')
        # Check weather username is valid or not.
        if is_valid(new_uname):
            s = replace_by(uname, new_uname)    # if valid then replaced by new one.
            print(s)
        else:
            print('UserName must has minimum 3 character')
    except Exception as e:
        print(e)
