import itertools
def getBitRepresentation(C: str) -> str:
    # represent string C in bits of 1 and 0s
    string = ""
    print(C)
    for i in C:
        print(i)
        if i == "A":
            string+= "0"
        elif i == "B":
            string+= "1"
        else:
            # invalid choice: how best to handle this ?
            return ""

    return string

def getStringRepresentation(C: str) -> str:
    string = ""
    for i in C:
        if i == "1":
            string+="B"
        elif i == "0":
            string+="A"
        else:
            return ""

    return string



def getWrongAnswers(N: int, C: str) -> str:
    # Write your code here
    if N != len(C):
        # answers missing
        return ""
    mainstring = "".join(list(itertools.repeat("1", N)))
    string = getBitRepresentation(C)


    wrong_values = getStringRepresentation(str(int(mainstring) - int(string)))

    return wrong_values

ans = getWrongAnswers(5, "BBBBB")
print(ans)