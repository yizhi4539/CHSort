#coding:gbk
from core import SearchEscape,SearchWord,unquote

CHSIGN='【','】','《','》','‘','’','“','”','；','，','。','？','、','：','·','￥','…','（','）','—'
ALP=set('abcdefghijklmnopqrstuvwxyz')
NUM=set('0123456789')

CAP_LOW=0
CAP_CAP=1
CAP_UPP=2
def SignTest():
    for i in CHSIGN:
        try:
            print i,SearchWord(i,code='gb18030')
        except Exception,e:
            print e
    return None

def Translate(string,code=None,cap=0):
    if code:
        string=string.decode(code)
    SU=string.encode('unicode_escape')
    Len=len(SU)
    C=0
    S2=''
    while C<Len:
        if SU[C]=='\\' and C<=Len-6 and SU[C+1]=='u':
            s=SU[C:C+6]
            p=SearchEscape(s)
            if len(p)>0:
                if cap==0:
                    p[0]=p[0].lower()
                elif cap==1:
                    p[0]=p[0][0].upper()+p[0][1:].lower()
                S2+=p[0]
            C+=6
            continue
        S2+=SU[C]
        C+=1
    return S2
    
def Sorti(Names,code=None,cap=0):
    def Filter(string):
        if string[0] in ALP or string[0] in NUM:
            return string
        else:
            pass
    NamesU={Translate(i,code,cap):i for i in Names}
    Keys=NamesU.keys()
    Keys.sort()
    return [(NamesU[i],i) for i in Keys]

def Sortp(names,code=None,cap=0):
    enc=[]
    chc=[]
    for i in names:
        if i[0] in ALP or i[0] in NUM:
            enc.append(i)
        else:
            chc.append(i)
    return Sorti(enc,code,cap)+Sorti(chc,code,cap)

def Sort(names,reverse=False,code=None,cap=0):
    names=Sortp(names,code,cap)
    if reverse:
        names.reverse()
    return names

if __name__=="__main__":
    a=u'智障吗',u'我们hello 您们 world好嘛',u'我觉得不太行','hello c','what are you','can','no','alp',u'啊'
    for i in Sort(a,True,cap=CAP_CAP):
        print i[0],i[1]
