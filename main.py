
class Node:
    def __init__(self):
        self.letter = None
        self.nodes = {}

    def __get_all__(self):
        if (self.letter is '!'):
            return ['!']
        words = []
        for key, node in self.nodes.items():
            if(node.letter is not None):
                words += node.__get_all__()
        if self.letter is not None:
            for i, word in enumerate(words):
                words[i] = self.letter + words[i]

        return words

    def __insert__(self, word):
        currentNode = self

        for letter in word :
            if letter is not '\n':
                if letter not in currentNode.nodes:
                    currentNode.nodes[letter] = Node()
                    currentNode.nodes[letter].letter = letter
                currentNode = currentNode.nodes[letter]
        if '!' not in currentNode.nodes :
            currentNode.nodes['!'] = Node()
            currentNode.nodes['!'].letter = '!'

        return True

    def __traverse__(self):
        str = ''

        for key, node in self.nodes.items():
            str += key
        str += '\n'

        for key, node in self.nodes.items():
            str += node.__traverse__()

        return str

    def __build__(self, strs, i = 0):
       j = i
       if(i not in strs):
           return j
       for ltr in strs[i]:
           self.nodes[ltr] = Node()
           self.nodes[ltr].letter = ltr
           j = self.nodes[ltr].__build__(strs, (j + 1))
       return j

class Trie:

   def __init__(self):
        self.root = Node()

   def insert(self, word):
        self.root.__insert__(word)

   def get_all(self):
        return self.root.__get_all__()
   def traverse(self):
       return self.root.__traverse__()

   def hasWord(self,word):
       currentNode = self.root
       for letter in word:
           if letter in currentNode.nodes:
               currentNode = currentNode.nodes[letter]
           else:
               return False
       if '!' in currentNode.nodes:
           return True
       return False

   def build(self, strs):
       return self.root.__build__(strs)

class DictionaryTrie:
    def __init__(self):
        self.trie = Trie();

    ''' converts regular to trie '''
    def Convert(self, filename):
        file = open(filename, 'r')

        ''' read dictionary line by line (aka word by word)'''
        for line in file :
          trie.insert(line)
          dictT.addWord(line)

        file.close()
        return True

    ''' saves as trie '''
    def Save(self, filename):
        file = open("DC_"+ filename, 'w')

        file.write(trie.traverse())
        file.close
        return True

    ''' loads from compressed structure '''
    def Load(self, filename):
        file = open(filename, 'r')

        str = file.read()
        file.close()
        '''tokenize on newline'''
        strs = {}
        i = 0
        for letter in str:
            if letter  is not '\n' and i not in strs:
                strs[i] = ""
            if letter is not '\n':
                strs[i] += letter
            else:
                i += 1

        self.trie.build(strs)
        return True

    def addWord(self, word):
        return self.trie.insert(word)

    def hasWord(self, word):
        return self.trie.hasWord(word)

    def getAll(self):
        return self.trie.get_all()

    def getAllWithPrefix(self, pref):
        currentNode = self.trie.root

        for letter in pref:
            if letter in currentNode.nodes:
                currentNode = currentNode.nodes[letter]
            else:
                return []
        return currentNode.__get_all__()

trie = Trie()
dictT = DictionaryTrie()

filename = input("File To Convert: ")
file = open(filename, 'r')

''' read dictionary line by line (aka word by word)'''
for line in file :
    trie.insert(line)

file.close()

dictT.Load('DC_testFile.txt')

print (dictT.getAll())
print (dictT.hasWord('hello'))
print (dictT.hasWord('bye'))
print (dictT.getAllWithPrefix('h'))
print (dictT.getAllWithPrefix('l'))

file = open("DC_"+ filename, 'w')

file.write(trie.traverse())
file.close


