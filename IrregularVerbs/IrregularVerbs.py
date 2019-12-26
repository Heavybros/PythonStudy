# ###################################################
# 예제 파일 형식
# IrregularVerbs.txt

# be|was/were|been|~이다.
# bear|bore|born|(새끼를)낳다.
# ...반복
# 
# 출력 형식
# be - (    ) - been - ~이다 : 정답입력
# (    ) - bore - born - (새끼를)낳다. : 정답입력
# ...반복
# ###################################################

class IrregularVerb:
    def __init__(self, infinitive, simplePast, pastParticiple, meaningInKOR):
        self.infinitive = infinitive
        self.simplePast = simplePast
        self.pastParticiple = pastParticiple
        self.meaningInKOR = meaningInKOR

class IrregularVerbList:
    def __init__(self):
        self.list = []

    def appendList(self, IrregularVerb):
        self.list.append(IrregularVerb)
    
    def printList(self):
        for IrregularVerb in self.list:
            print(IrregularVerb.infinitive, IrregularVerb.simplePast, IrregularVerb.pastParticiple, IrregularVerb.meaningInKOR)
        print('총 %d개' %len(self.list))
