import regex

file_name = "./hw2.xml"
out_file_name = "lexical_analysis_out.txt"
ansDict = {}
ansText = "Number of Distinct Words in the Texts\n"

with open(file_name, 'r', encoding='UTF-8') as open_book:
    with open(out_file_name, 'w') as open_out_book:
        text = open_book.read()
        text = regex.sub(r'<(.*?)>', r' ', text)
        text = regex.sub(r'\n',r' ',text)
        text = text.lower()
        text = regex.sub(r'\'{2,}',r' ',text)
        text = regex.sub(r'\d ',r' ',text)
        text = regex.sub(r'[^\w\'\s]|_+', r' ', text)
        countWord = text.split()
        for word in countWord:
            if word in ansDict:
                ansDict[word] += 1
            else:
                ansDict[word] = 1
        for key, value in ansDict.items():
            ansText += key + ": " + str(value) + "\n"
        open_out_book.write(ansText)
