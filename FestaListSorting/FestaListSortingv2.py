import operator
import datetime
import os
import re

# 페스타 이벤트 정보를 담는 클래스
class FeastaEvent:
    def __init__(self, name, date, host):
        self.name = name
        self.date = date
        self.host = host

    # 생성할 파일 이름
    # 요구사항대로 특수문자를 빼고 띄어쓰기를 _ 로 대치한다.
    # 정규식을 이용하여 대치했다.
    def getFileName(self):
        regExp = '[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]'
        file_name = re.sub(regExp, '', event.name).strip().replace("  ", " ").replace(" ", "_")
        return file_name

    # 생성할 파일 경로 (YYYY/mmdd/파일이름.md) 를 반환
    def getFileNameWithPath(self):
        file_path = self.date[:4]
        month_date = self.date[6:12].replace(".", "").replace(" ", "").strip() 
        file_name_path = self.date[:4] + "/" + month_date + "/" + month_date + "_" + self.getFileName() + ".md"
        return file_name_path
        
    # 어째서인지 이모지를 콘솔에 찍으면 깨지는 버그가 있어서
    # 그냥 아예 temp.txt에 생성하도록 변경하였다.
    def printEvent(self):
        # open 을 해서 없는 파일이면 새로 생성한다.
        # a는 내용 추가, r은 읽기전용, w은 쓰기이다.
        # w대신 a를 쓴 이유는 내용을 계속 추가해야하는데 w로 쓰면 덮어씌워져서 이전 반복문에서 추가한 내용이 사라지기 때문.
        f= open("temp.txt", "a")
        content = "### " + self.name + "\n\n"
        content += "- **⏰ 일시** : " + self.date + "\n"
        content += "- **💁 주최** : " + self.host + "\n"
        content += "- **📝 총평** : 추가 예정\n"
        content += "- **👀 리뷰** : [상세 리뷰 보러 가기](" + self.getFileNameWithPath() + ")\n\n\n"
        f.write(content)
        f.close()
    
    ## 파일 경로가 없다면 생성
    def createDirectory(self, year):
        if not os.path.exists(year):
            os.mkdir(year)

    # 상세리뷰 md 파일안에 들어갈 기본 포맷 문자열
    def file_contents_text(self):
        content = "# " + self.name + "\n\n"
        content += "![" + self.name + "](image.jpg)\n\n"
        content += "- ⏰ 일시 : " + self.date + "\n"
        content += "- 💁 주최 : " + self.host + "\n"
        content += "- ⛳ 장소 : \n"
        content += "- 🔗 링크 : \n\n"
        content += "## 👏 총평 \n\n- ㅁ\n\n"
        content += "## 인증샷\n\n![인증샷](self.png)\n"
        return content

    # 실제 상세리뷰 md 파일을 만드는 함수
    def createFile(self):
        year = self.date[:4]
        day = self.date[6:12].replace(".", "").replace(" ", "").strip()
        self.createDirectory(year)
        self.createDirectory(year + "/" + day)
        # 파일이 없으면 생성
        if not os.path.exists(self.getFileNameWithPath()):
            f= open(self.getFileNameWithPath(),"w+")
            f.write(self.file_contents_text())
            f.close()

# 내가 원하던 YYYY. mm. dd (요일) 포맷으로 변경하는 함수
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
    event.createFile()
    print("\n")
