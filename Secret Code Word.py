def repeatLength(string,length):
    return (string * (int(length / len(string))+1))[:length]


def main():
    x = input("enter code word: ") # user enters code
    x= x.upper() # code converted to all upercase

    shift = int(x.split(";")[0]) # isolates the shift

    while shift >=0: # use a whileloop to make sure code only runs when positive
        word = x.split(';')[1] # isolates secret word
        message = x.split(';')[2] # isolate the secret message
        message = message.replace (" ", "") # takes out any spaces the user inputed in the message

        expandword = repeatLength(word, len(message))#expands the word to cover the length of the message

        aList =[] # creates empty list where ord/shifted values of word will go
        for i in range(len(expandword)):
            y= ord(expandword[i]) # asciiswitched values now for the word
            y-=64 # subtract out 64 so asc values start from 1 for the word
            z = (y + int(shift)) #take the asc values and shift them  for the word
            aList.append(z) #add all these new shifted asc values for the word into alist
        #print(aList)

        bList = [] # create empty list out of for loop to store the message shifted asc values
        for i in range(len(message)):
            j= ord(message[i]) #find asc values for each letter of the message
            j-=64 # lower the asc values to start from 1 by subtracting out 64
            k = (j+int(shift)) # shift over the asc values for the message
            if k > 26:
                k = k-26
                bList.append(k) #failsafe option but just add the k values into the bList essentially
            else:
                bList.append(k) # same as above
        #print(bList)

        cList = [sum(i) for i in zip(aList, bList)] # add up the cipher values of a and b
        dList = []
        for i in range(len(cList)):
            if cList[i] > (26 + shift):
                cList[i] = (cList[i] + 64 - 26 - shift)
            else:
                cList[i] = (cList[i] + 64 - shift)

            #if cList[i] > (26 +shift): # if each letter is past 26 + shift
       # cList[i] = (cList[i] + 64 - 26-shift) # subtract out the 26 and shift so it can wrap around alphabet
                    # add 64 so it is converted back to normal asc values
            #else:
         # add back the 64 to convert to normal asc values
                 # shift is subtracted so original message can be determined from the asc values without the shift as the user entered
        #print(cList)
        for i in range(len(cList)):
                m = chr(cList[i])  # for each letter convert back from asc number into the letter form
                dList.append(m)  # put all these letters in a dList
        eList = "".join(dList)  # keep it all in one line
        #print(dList)
        print(eList)  # view the secret letter code



        x = input("")  # add this outside of loop so user can enter again
        x=x.upper()
        shift=int(x.split(";")[0])  # user can enter again and follow whileloop


main()