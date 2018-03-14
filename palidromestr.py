def reverse(s):
    return s[::-1]
def isPalindrome(s):
   rev = reverse(s)
   if (s == rev):
        return True
   else:
        return False
s =input("Enter the string:")
ans = isPalindrome(s)
if ans == 1:
    print("Yes")
else:
    print("No")
