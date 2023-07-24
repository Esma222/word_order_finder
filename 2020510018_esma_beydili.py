# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 13:49:47 2021

@author: Hp
"""

#birinci fonksiyonun çalışması yaklaşık olarak 8 dk sürüyor
#ikinci fonksiyonun çalışması yaklaşık  18 dk sürüyor.
def Word_Order_Frequency_One_Book (Book, Word_Order, File_Output="missing.txt"):
    
 try:
  # 3 parametreden az girerse  error verdirmek için
  if File_Output=="missing.txt":
     print("ERROR! Please enter the parameters correctly")  
     
  elif Word_Order==1:
  
    outfile=open(File_Output,"w")   
    outfile.write("|  WORD       |   WORD        |"+"\n")
    outfile.write("|  ORDER      |   ORDER       |"+"\n")
    outfile.write("|  FREQUENCY  |   SEQUENCE    |"+"\n")
    outfile.write("-------------------------------"+"\n")
    k=0
    #sort dictionarynin içindeki elemanları value ya göre sıralar.
    # reverse ise sıralmayı ters çevirerek en büyük olanı en başa alır
    for key ,value in reversed(sorted(bir_kitap_bir_kelime(Book).items(),key=lambda t:t[1])):
        outfile.writelines(f"{str(value):^14}"+"| "+str(key)+"\n")
        k+=1
        if k==100:
            break
    outfile.close()
    
  elif Word_Order==2:
      
    outfile=open(File_Output,"w")   
    outfile.write("|  WORD       |   WORD        |"+"\n")
    outfile.write("|  ORDER      |   ORDER       |"+"\n")
    outfile.write("|  FREQUENCY  |   SEQUENCE    |"+"\n")
    outfile.write("-------------------------------"+"\n")
    k=0
    #sort dictionarynin içindeki elemanları value ya göre sıralar.
    # reverse ise sıralmayı ters çevirerek en büyük olanı en başa alır
    for key ,value in reversed(sorted(bir_kitap_iki_kelime(Book).items(),key=lambda t:t[1])):
        outfile.writelines(f"{str(value):^14}"+"| "+str(key)+"\n")
        k+=1
        if k==100:
            break
    outfile.close()
    
  else:
      print("ERROR! The word order must be 1 or 2. ")
 except :
        print("ERROR!")  
    
 
    
def Word_Order_Frequency_Two_Books (Book_1, Book_2, Word_Order, File_Output="missing.txt"):
 try:
  # 3 parametreden az girerse  error verdirmek için
  if File_Output=="missing.txt":
     print("ERROR! Please enter the parameters correctly")  
     
  elif Word_Order==1:

      dictbook1=bir_kitap_bir_kelime(Book_1)
      dictbook2=bir_kitap_bir_kelime(Book_2)
      dicttotal=bir_kitap_bir_kelime(Book_2)
      #iki dictionary birleştirildi
      dicttotal.update(bir_kitap_bir_kelime(Book_1))
      # key hem 1. hem 2. kitapta varsa  valuelarını toplayıp total value ya eşitlemek için
      for key in dictbook2:
        if key in dictbook1:
            dicttotal[key]=dictbook2[key]+dictbook1[key]
            

      
      outfile=open(File_Output,"w")   
      outfile.write("| TOTAL     |  BOOK1      |  BOOK2      |  WORD        |"+"\n")
      outfile.write("| ORDER     |  ORDER      |  ORDER      |  ORDER       |"+"\n")
      outfile.write("| FREQUENCY |  FREQUENCE  |  FREQUENCY  |  SEQUENCY    |"+"\n")
      outfile.write("--------------------------------------------------------"+"\n")
      
      k=0
      #sort dictionarynin içindeki elemanları value ya göre sıralar.
      # reverse ise sıralmayı ters çevirerek en büyük olanı en başa alır
      for key ,value in reversed(sorted(dicttotal.items(),key=lambda t:t[1])):
        outfile.writelines(f"{str(value):^12}" +"|"+f"{str(dictbook1.get(key,0)):^13}"+"|"+f"{str(dictbook2.get(key,0)):^13}"+"| "+f"{str(key):<14}"+"\n")
        k+=1
        if k==100:
            break
      outfile.close()
     
  elif Word_Order==2:
      
      dictbook1=bir_kitap_iki_kelime(Book_1)
      dictbook2=bir_kitap_iki_kelime(Book_2)
      dicttotal=bir_kitap_iki_kelime(Book_2)
      #iki dictionary birleştirildi
      dicttotal.update(bir_kitap_iki_kelime(Book_1))
      # key hem 1. hem 2. kitapta varsa  valuelarını toplayıp total value ya eşitlemek için
      for key in dictbook2:
        if key in dictbook1:
            dicttotal[key]=dictbook2[key]+dictbook1[key]
            

      
      outfile=open(File_Output,"w")   
      outfile.write("| TOTAL     |  BOOK1      |  BOOK2      |  WORD        |"+"\n")
      outfile.write("| ORDER     |  ORDER      |  ORDER      |  ORDER       |"+"\n")
      outfile.write("| FREQUENCY |  FREQUENCE  |  FREQUENCY  |  SEQUENCY    |"+"\n")
      outfile.write("--------------------------------------------------------"+"\n")
      
      k=0
      #sort dictionarynin içindeki elemanları value ya göre sıralar.
      # reverse ise sıralmayı ters çevirerek en büyük olanı en başa alır
      for key ,value in reversed(sorted(dicttotal.items(),key=lambda t:t[1])):
        outfile.writelines(f"{str(value):^12}" +"|"+f"{str(dictbook1.get(key,0)):^13}"+"|"+f"{str(dictbook2.get(key,0)):^13}"+"| "+f"{str(key):<14}"+"\n")
        k+=1
        if k==100:
            break
      outfile.close()
    
  else:
      print("ERROR! The word order must be 1 or 2. ")
 except :
        print("ERROR!")    
    
def bir_kitap_bir_kelime(book):
    #Bu fonksiyon word order 1 iken kelimeleri ve tekrar sayısını içeren dictionary geri döndürür.
    #bir kitap için  tekli kelimeyse
    infile = open(book,encoding="utf8")
    allwords=infile.read()
    infile.close()
    #harf ve boşluk olmayan her şeyi silmek için
    ascii=["÷", "×", "–", "—", "˜", "™", "›", "¡", "¢", "£", "¤", "¥", "¦", "§", "¨", "©", "ª", "«", "¬", "­", "®", "¯", "°", "±", "²", "³", "´", "µ", "¶", "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿","~", "}", "|", "}", "`", "_", "^", "]", '\\', "[", "@", "?", ">", "=", "<", ";", ":", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "/", ".", "-", ",", "+", "*", ")", "(", "'", "&", "%", "$","#", '"', "!", "€", "‚", "„",	"…", "†", "‡",	"ˆ", "‰", "‹",  "‘", "’", "“",	"”", "•"] 
    for i in ascii:
            if allwords.find(i)!=-1:
                 allwords = allwords.replace( i , "")
    #üst satırdaki son kelime ile alt satırdaki ilk kelimenin birleşmesini önlemek için 
    allwords=allwords.replace("\n", " ")       
    allwords=allwords.lower()# küçük harfe çevrildi


    #stop wordsleri sildirmek için
    stop_words=['able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', 'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant', 'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs', 'currently', 'dare', 'darent', 'definitely', 'described', 'despite', 'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt', 'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half', 'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im', 'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its', 'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me', 'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only', 'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought', 'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes', 'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', 'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', 'therell', 'therere', 'theres', 'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll', 'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', 'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what', 'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl', 'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt', 'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours', 'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens', 'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www', 'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give', 'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse', 'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah', 'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent', 'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol', 'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately', 'importance', 'important', 'index', 'information', 'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg', 'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted', 'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran', 'readily', 'ref', 'refs', 'related', 'research', 'resulted', 'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state', 'states', 'stop', 'strongly', 'substantially', 'successfully', 'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto', 'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til', 'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols', 'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words', 'world', 'youd', 'youre']

    for j in stop_words:
            if allwords.find(j)!=-1:
                j=" "+j+" "
                allwords = allwords.replace( j , " ")
                       
    clearwordslist =allwords.split(' ')#içinde stop words bulundurmayan kelime listesi
    
    #ikili kelimeleri ve kaç kez tekrar ettiklerini içinde bulunduracak
    printfrequencesequence={}

    for i in clearwordslist:
         counter=0
         if i!='' and i.isalpha():#elemanlar boşluksa yazdırmamak için
          for j in clearwordslist:
             if i==j :
               counter+=1
          printfrequencesequence[i]=counter#'word': counter şu anda dictionary de bu durumda
                    
    return printfrequencesequence


def bir_kitap_iki_kelime(book):
    #Bu fonksiyon word order 2 iken kelimeleri ve tekrar sayısını içeren dictionary geri döndürür.
    #bir kitap için  ikili kelimeyse
    infile = open(book,encoding="utf8")
    allwords=infile.read()
    infile.close()

    ascii=["÷", "×", "–", "—", "˜", "™", "›", "¡", "¢", "£", "¤", "¥", "¦", "§", "¨", "©", "ª", "«", "¬", "­", "®", "¯", "°", "±", "²", "³", "´", "µ", "¶", "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿","~", "}", "|", "}", "`", "_", "^", "]", '\\', "[", "@", "?", ">", "=", "<", ";", ":", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "/", ".", "-", ",", "+", "*", ")", "(", "'", "&", "%", "$","#", '"', "!", "€", "‚", "„",	"…", "†", "‡",	"ˆ", "‰", "‹",  "‘", "’", "“",	"”", "•"] 
    for i in ascii:
            if allwords.find(i)!=-1:
                 allwords = allwords.replace( i , "")
    #üst satırdaki son kelime ile alt satırdaki ilk kelimenin birleşmesini önlemek için 
    allwords=allwords.replace("\n", " ")       
    allwords=allwords.lower()#küçük harflere çevrildi


    #stop wordsleri sildirmek için
    stop_words=['able', 'about', 'above', 'abroad', 'according', 'accordingly', 'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against', 'ago', 'ahead', "ain't", 'all', 'allow', 'allows', 'almost', 'alone', 'along', 'alongside', 'already', 'also', 'although', 'always', 'am', 'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are', "aren't", 'around', 'as', "a's", 'aside', 'ask', 'asking', 'associated', 'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both', 'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', "can't", 'caption', 'cause', 'causes', 'certain', 'certainly', 'changes', 'clearly', "c'mon", 'co', 'co.', 'com', 'come', 'comes', 'concerning', 'consequently', 'consider', 'considering', 'contain', 'containing', 'contains', 'corresponding', 'could', "couldn't", 'course', "c's", 'currently', 'dare', "daren't", 'definitely', 'described', 'despite', 'did', "didn't", 'different', 'directly', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'during', 'each', 'edu', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even', 'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far', 'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed', 'following', 'follows', 'for', 'forever', 'former', 'formerly', 'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore', 'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going', 'gone', 'got', 'gotten', 'greetings', 'had', "hadn't", 'half', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", 'hello', 'help', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', "here's", 'hereupon', 'hers', 'herself', "he's", 'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit', 'however', 'hundred', "i'd", 'ie', 'if', 'ignored', "i'll", "i'm", 'immediate', 'in', 'inasmuch', 'inc', 'inc.', 'indeed', 'indicate', 'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead', 'into', 'inward', 'is', "isn't", 'it', "it'd", "it'll", 'its', "it's", 'itself', "i've", 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known', 'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', "let's", 'like', 'liked', 'likely', 'likewise', 'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', "mayn't", 'me', 'mean', 'meantime', 'meanwhile', 'merely', 'might', "mightn't", 'mine', 'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', "mustn't", 'my', 'myself', 'name', 'namely', 'nd', 'near', 'nearly', 'necessary', 'need', "needn't", 'needs', 'neither', 'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'no-one', 'nor', 'normally', 'not', 'nothing', 'notwithstanding', 'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', "one's", 'only', 'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought', "oughtn't", 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'own', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably', 'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather', 'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding', 'regardless', 'regards', 'relatively', 'respectively', 'right', 'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second', 'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously', 'seven', 'several', 'shall', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'six', 'so', 'some', 'somebody', 'someday', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying', 'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that's", "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', "there'd", 'therefore', 'therein', "there'll", "there're", 'theres', "there's", 'thereupon', "there've", 'these', 'they', "they'd", "they'll", "they're", "they've", 'thing', 'things', 'think', 'third', 'thirty', 'this', 'thorough', 'thoroughly', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', "t's", 'twice', 'two', 'un', 'under', 'underneath', 'undoing', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using', 'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz', 'vs', 'want', 'wants', 'was', "wasn't", 'way', 'we', "we'd", 'welcome', 'well', "we'll", 'went', 'were', "we're", "weren't", "we've", 'what', 'whatever', "what'll", "what's", "what've", 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', "where's", 'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while', 'whilst', 'whither', 'who', "who'd", 'whoever', 'whole', "who'll", 'whom', 'whomever', "who's", 'whose', 'why', 'will', 'willing', 'wish', 'with', 'within', 'without', 'wonder', "won't", 'would', "wouldn't", 'yes', 'yet', 'you', "you'd", "you'll", 'your', "you're", 'yours', 'yourself', 'yourselves', "you've", 'zero', 'a', "how's", 'i', "when's", "why's", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'I', 'www', 'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt', 'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give', 'hasnt', 'herse', 'himse', 'interest', 'itse”', 'mill', 'move', 'myse”', 'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten', 'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance', 'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah', 'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent', 'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol', 'briefly', 'ca', 'date', 'ed', 'effect', 'et-al', 'ff', 'fix', 'gave', 'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately', 'importance', 'important', 'index', 'information', 'invention', 'itd', 'keys', 'kg', 'km', 'largely', 'lets', 'line', "'ll", 'means', 'mg', 'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted', 'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages', 'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran', 'readily', 'ref', 'refs', 'related', 'research', 'resulted', 'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'slightly', 'somethan', 'specifically', 'state', 'states', 'stop', 'strongly', 'substantially', 'successfully', 'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto', 'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til', 'tip', 'ts', 'ups', 'usefully', 'usefulness', "'ve", 'vol', 'vols', 'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words', 'world', 'youd', 'youre']
    for j in stop_words:
            if allwords.find(j)!=-1 :
                j=" "+j+" "
                allwords = allwords.replace( j , " ")
              
    clearwordslist =allwords.split(' ')#içinde stop words bulundurmayan kelime listesi

    wordlist2=[]#ikili kelimeleri içine bulundurmak için
    for i in range(0,len(clearwordslist)-1):
        # elemanlar boşluk ise iptal etmek için
        if  clearwordslist[i]!=''and clearwordslist[i].isalpha() and clearwordslist[i+1]!=''and clearwordslist[i+1].isalpha() :
          wordlist2.append(clearwordslist[i]+" "+clearwordslist[i+1])
    
    #ikili kelimeleri ve kaç kez tekrar ettiklerini içinde bulunduracak
    printfrequencesequence={}

    for i in wordlist2:
          counter=0
          for j in wordlist2:
             if i==j :
               counter+=1
          printfrequencesequence[i]=counter#'word': counter şu anda dictionary de bu durumda
                        
    return printfrequencesequence

 
