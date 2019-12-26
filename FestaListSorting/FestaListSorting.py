###########################################################
#
# 예제 입력 : 
# >2019년 12월 21일 오후 1:00
# >Android Dev Summit 2019 extended Seoul
# >GDG Korea Android
# >2018년 04월 22일 오전 9:00
# >DroidKnights
# >DroidKnights Community
# >2018년 06월 10일 오전 11:00
# >Google I/O Extended 2018 Seoul
# >GDG Korea
# >
#
# # 예제 출력
# ###  Android Dev Summit 2019 extended Seoul 
# 
# - ** 일시** :  2019년 12월 21일 오후 1:00
# - ** 주최** :  GDG Korea Android
# 
# 
# ###  Google I/O Extended 2018 Seoul
# 
# - ** 일시** :  2018년 06월 10일 오전 11:00
# - ** 주최** :  GDG Korea
# 
# 
# ###  DroidKnights
# 
# - ** 일시** :  2018년 04월 22일 오전 9:00
# - ** 주최** :  DroidKnights Community
#
###########################################################


import operator
import datetime

# 페스타 이벤트 정보를 담는 클래스
class FeastaEvent:
    def __init__(self, name, date, host):
        self.name = name
        self.date = date
        self.host = host

    def printEvent(self):
        print('### ', self.name, '\n')
        print("- ** 일시** : ", self.date)
        print("- ** 주최** : ", self.host)

# 2019년 12월 21일 오후 1:00 ---> 2018. 04. 22 (토) 형태로 변경
def date_format_kor(origin_str):
    dateStr = origin_str.replace('오전', 'AM').replace('오후', 'PM')
    day_kor = ['(일)', '(월)', '(화)', '(수)', '(목)', '(금)', '(토)']
    date = datetime.datetime.strptime(dateStr, '%Y년 %m월 %d일 %p %I:%M').strftime('%Y. %m. %d')
    day = day_kor[int(datetime.datetime.strptime(dateStr, '%Y년 %m월 %d일 %p %I:%M').strftime('%w'))]
    return date + " " + day

# 여러줄의 페스타 이벤트 목록을 입력받을 함수
def read_feasta_list():
    string = []
    events = []
    
    while True:
        input_str = input(">")
        if input_str == "":
            break
        else:
            string.append(input_str)

    date = ""
    name = ""
    host = ""        
    for i in range(len(string)):
        # 첫번째 줄은 날짜
        if (i % 3 ==0):
            date = date_format_kor(string[i])
        # 두번째 줄은 행사 이름
        elif (i % 3 ==1):
            name = string[i]
        # 세번째 줄은 행사 주최자
        elif (i % 3 ==2):
            host = string[i]
            # 다 입력받은것을 class에 담는다.
            events.append(FeastaEvent(name, date, host))
    
    return events

events = read_feasta_list()

# 입력받은 페스타 이벤트 정보를 최신 순으로 정렬
events.sort(key=operator.attrgetter('date'), reverse=True)

for event in events:
    event.printEvent()
    print("\n")
