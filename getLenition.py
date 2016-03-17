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
################################################################################

class Lenition:
    def __init__(self, path):
        self.lDocs = {}
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.endswith('.txt'):
                    self.lDocs[f[:-4]] = re.split(r'\n+',(open(path+f,'Ur').read()))

         
    def get(self):
        [print(key) for key,value in self.lDocs.items()]
        pass
                    
Lenition(path).get()
