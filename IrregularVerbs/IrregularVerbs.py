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
import random

class IrregularVerb:
    def __init__(self, infinitive, simplePast, pastParticiple, meaningInKOR):
        self.infinitive = infinitive
        self.simplePast = simplePast
        self.pastParticiple = pastParticiple
        self.meaningInKOR = meaningInKOR

class IrregularVerbList:
    def __init__(self):
        self.__list = []

    def appendList(self, irregularVerb):
        self.__list.append(irregularVerb)

    def appendListByElement(self, infinitive, simplePast, pastParticiple, meaningInKOR):
        irregularVerb = IrregularVerb(infinitive, simplePast, pastParticiple, meaningInKOR)
        self.appendList(irregularVerb)

    def SaveIrregularVerbsByFile(self, fileName):
        f = open(fileName, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        words = []
        for line in lines:
            words = line.split('|')
            if (len(words) >= 4) and (not self.IsOverlap(words[0], words[1], words[2])):
                self.appendListByElement(words[0], words[1], words[2], words[3])

    def IsOverlap(self, infinitive, simplePast, pastParticiple):
        for i in range(len(self.__list)):
            if (self.__list[i].infinitive == infinitive) and (self.__list[i].simplePast == simplePast) and (self.__list[i].pastParticiple == pastParticiple):
                return True
        return False

    def QuizStart(self):
        if not self.__list:
            print('입력된 불규칙동사가 없습니다.')
            return
        random.shuffle(self.__list)
        quizMsg = ''
        inputWord = ''
        CorrectAnswer = ''
        CorrectCount = 0
        BlankIdx = 0
        i = 0
        while i <= len(self.__list):
            infinitive = self.__list[i].infinitive
            simplePast = self.__list[i].simplePast
            pastParticiple = self.__list[i].pastParticiple
            BlankIdx = random.randrange(0, 3)
            if BlankIdx == 0:
                quizMsg = '(' + ' ' * len(infinitive) + ') - ' + simplePast + ' - ' + pastParticiple + ' : '
                CorrectAnswer = infinitive
            elif BlankIdx == 1:
                quizMsg = infinitive + ' - (' + ' ' * len(simplePast) + ') - ' + pastParticiple + ' : '
                CorrectAnswer = simplePast
            elif BlankIdx == 2:
                quizMsg = infinitive + ' - ' + simplePast + ' - (' + ' ' * len(pastParticiple) + ') : '
                CorrectAnswer = pastParticiple
            inputWord = input(quizMsg)
            if inputWord.upper() == 'Q':
                break
            if CorrectAnswer.find(inputWord) >= 0:  # 정답 판별 로직 보완 필요 알파벳 하나만 치면 다 정답이래
                print('정답!!!')
                CorrectCount += 1
            else:
                print('오답... (정답 : %s)' %CorrectAnswer)
            i += 1
        print(f'총 {len(self.__list)}문항 중 {i}문항 출제 학습률 {i / len(self.__list) * 100}%')
        print(f'출제 문항 {i}문항 정답 개수 {CorrectCount}개 정답률 {CorrectCount / i * 100}%')

    def testPrintList(self):
        for IrregularVerb in self.__list:
            print(IrregularVerb.infinitive, IrregularVerb.simplePast, IrregularVerb.pastParticiple, IrregularVerb.meaningInKOR)
        print('총 %d개' %len(self.__list))

irregularVerbList = IrregularVerbList()
irregularVerbList.SaveIrregularVerbsByFile('./IrregularVerbs/IrregularVerbs.txt')
# irregularVerbList.testPrintList()
irregularVerbList.QuizStart()