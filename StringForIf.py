# Ik heb hieronder al enkele tests opgesomd. Gewoon even de #, "hash sign", "spoorwegteken", "hashtag", ... weghalen 
# voor String1 en String2 van de test die je wil uitvoeren
String1 ="--++--"
String2 = "++--++"
# resultaat -> "000000"
#String1 ="-++-"
#String2 = "-+-+"
# resultaat -> "-+00"
#String1 ="-+-+-+"
#String2 = "-+-+-+"
# resultaat -> "-+-+-+"

resultaat = ""
for i in range(len(String1)):
    if String1[i] == String2[i]:
        resultaat += String1[i]
    else:
        resultaat += "0"
print(resultaat)
