# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) > 1:
        return reverseString(aStr[1:])+aStr[0]
    else:
        return aStr

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    
    if len(x) > 1:
        pos = word.find(x[0])
        if pos >= 0:
            return x_ian(x[1:], word[pos+1:])
        else:
            return False
    elif (len(x) == 1) and (x in word):
        return True
    elif x=='':
        return True
    return False

            

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    def insertNewlinesRec (text, lineLength):
        if (len (text)>lineLength+1) :
            if text[lineLength-1] == ' ':
                #отрезаем пробел в конце
                pos = lineLength-1
            elif (text.find(' ') < 0):
                return text
            else:
                pos = text[lineLength:].find(' ')+lineLength
            return text[0:pos]+"\n"+insertNewlinesRec (text[pos+1:], lineLength)
        else:
            return text
    return insertNewlinesRec (text, lineLength)
                
        
        
