""" Extract the following tagged forms from the Arco Corpus, along
with the two tokens preceeding and following it, and the document name.

                                Not Lenited     Lenited
    Masculine Genitive Articles:  Tdsmg*         Tdsmg
    Masculine Genitive Nouns:     Ncsmg*         Ncsmg
    Feminine Genitive Articles:   Tdsfg*         Tdsfg
    Feminine Genitive Nouns:      Ncsfg*         Ncsfg
"""
################################################################################
import re,os
path = ('/Users/pokea/Documents/Work/UofA/Current/'
        'SG_Lenition/ARCOSG/')
tags = set(["Tdsfg","Ncsfg","Tdsmg","Ncsmg"])
################################################################################

def sepTag(token,idx):
    return token[:-idx-1],token[-idx:]

def getWindow(line):
    matches = []
    sLine = line.split()
    for idx in range( len(sLine)):
        token = sLine[idx]
        for tag in tags:
            if token.endswith(tag):
                item,foundtag = sepTag(token, 5)
                lenited = True
            elif token.endswith(tag + '*'):
                item,foundtag = sepTag(token, 6)
                foundtag = foundtag[:-1]
                lenited = False
            else:
                continue
            if sLine[idx-1]:
                lwindow = sLine[idx-1]
            else:
                lwindow = None
            if idx + 1 > len(sLine)-1:
                rwindow = None
            else:
                rwindow = sLine[idx+1]
            matches.append((foundtag, item, lenited, lwindow, rwindow))
    return matches

def printVars(match,outf,f):
    for var in match:
        outf.write(str(var))
        outf.write('\t')
    outf.write(f)
    outf.write('\n')

    #[outf.write(str(var) + '\t') for var in match]
    #outf.write(f+'\n')

class Lenition:
    def __init__(self, path):
        self.path = path
        self.lDocs = {}
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.txt'):
                    ftext = re.split(r'\n+',(open(path+f,'Ur').read()))
                    self.lDocs[f[:-4]] = ftext

    def get(self):
        outf = open(self.path + 'SGitems.txt', 'w')
        for f, text in self.lDocs.items():
            for line in text:
                matches = getWindow(line)
                if len(matches) > 1:
                    [printVars(match,outf,f) for match in matches]
                    
Lenition(path).get()
