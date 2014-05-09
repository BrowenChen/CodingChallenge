def balanced_brackets(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    stack = []
    for i in s:
        #print(i)
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                print("Unbalanced")
                return
            else:
                stack.pop()
            
        
    if len(stack) == 0:
        print("Balanced")
        
    elif len(stack) != 0:
        print("Unbalanced")