'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
     '''
    // make a list of the letters
    // get the index of the letter given
    // now get the new index after the shift
    // return the new letter
    '''
    try:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = alphabet.index(letter)
        NewIndex = index+shift
        if NewIndex > 25:
            return(alphabet[NewIndex-26])
        else:
            return(alphabet[NewIndex])
    
    except ValueError:
        return(" ")
        
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
     '''
    // get the text
    // get the index of each individual letters in the text
        // get the length of the text ?
        // get the index of the letter in the message
    // get the new index of each individual letters in the text
    // print the new message
    '''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    repetitions = len(message)
    ThisText = ""
    
    for i in range(repetitions):
        letter = message[i]
        if letter == " ":
            ThisText += " "
        else:
            index = alphabet.index(letter)
            NewIndex = index+shift
            if NewIndex > 25:
                ThisText += (alphabet[NewIndex-26])
            else:
                ThisText += (alphabet[NewIndex])
    
    return ThisText

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        LetterIndex = alphabet.index(letter)
        ShiftIndex = alphabet.index(letter_shift)
        NewIndex = LetterIndex + ShiftIndex
        if NewIndex > 25:
            return(alphabet[NewIndex-26])
        else:
            return(alphabet[NewIndex])

    except ValueError:
        return(" ")

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    15 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    '''
    /// get the individual letters in the message
    // get the index of each individual letters in the text
        // get the length of the text for the loop
        // get the index of each letter in the message
    
     // get the length of the key
         // make sure the length of the key is the same as the length of the message
     // get the individual letters in the key
    // get the index of each individual letters in the key
        // get the length of the text for the loop
        // get the index of each letter in the key
        
    // get the new index of each individual letters in the text by getting the sum
    // print the new message
    // ignore spaces, put what happens if Z + 1
    '''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    repetitions = len(message)
    
    ThisText = ''
    
    for i in range(repetitions):
        MsgLetter = message[i]
        KeyLetter = key[i]
        
        KeyLength = len(key)
        MsgLength = len(message)
        
        if MsgLength > KeyLength:
            LenDifference = MsgLength - KeyLength
            for i in range(LenDifference):
                key += key[i]
        
        if MsgLetter == " " or KeyLetter == " ":
            ThisText += " "
        else:
            MsgIndex = alphabet.index(MsgLetter)
            if MsgIndex == " ":
                ThisText += " "
            else:
                KeyIndex = alphabet.index(KeyLetter)
                NewIndex = MsgIndex + KeyIndex
                if NewIndex > 25:
                    ThisText += (alphabet[NewIndex-26])
                else:
                    ThisText += (alphabet[NewIndex])
    return ThisText

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    count = len(message) #count characters
    AddUnderscores = shift-(count % shift) #to know the number of underscores to add
    Underscore = ""
    ThisText = ""

    if count % shift > 0:
        for i in range(AddUnderscores): #to add the underscores
            Underscore += "_"
        
        Text = message + Underscore
        NewCount = len(Text)
        
        for i in range(NewCount): #to cypher the message
            index = (i//shift) + (NewCount//shift) * (i % shift) #get the new index
            letter= Text[index] #get the equivalent letter of the new index      
            ThisText += letter

    else:
        for i in range(count):
            index = (i//shift) + (count//shift) * (i % shift)
            letter= message[index]
            ThisText += letter
    
    return ThisText

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass
