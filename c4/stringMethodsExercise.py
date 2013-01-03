def countCharsIn(c, someString):
    """precondtion: c is a one-character string, someString is 
a string.
postcondition:  returns the number of times c appears in 
someString"""
def hasExtension(fileName, ext):
   """precondition:  filename is a string that is a file name 
and ext is a file extension.
postcondition:  return True if fileName ends with a period (.), 
then the extension.  Returns false if fileName contains any 
spaces in it regardless of its suffix."""
def chompEnds(c, someString:
   """precondition:  c is a one-character string that appears 
at least twice in someString.  
postcondition:  returns the substring of someString beginning 
after the first instance of c and ending before the last 
instance of c in someString.  """

print "countChars(\"a\", \"alabaster\") = ", 
countChars("a", "alabaster"), "expected:  3"
print "hasExtension(\"cat.cpp\", \"cpp\") = ", 
countChars("cat.cpp", "cpp"), "expected:  True"
print "hasExtension(\"siamese cat.cpp\", \"cpp\") = ", 
countChars("siamese cat.cpp", "cpp"), "expected:  False"
