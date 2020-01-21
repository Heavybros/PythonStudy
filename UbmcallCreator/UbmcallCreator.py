import os

def create_ubm_files(command_list):
    for command in command_list:
        # open 을 해서 없는 파일이면 새로 생성한다.
        # a는 내용 추가, r은 읽기전용, w은 쓰기이다.
        f = open("UBC" + command + ".kt", mode='w', encoding='utf8')
        content = "package com.harex.feature.ubmcall\n"
        content += "import com.harex.core.Ubm\n"
        content += "import org.json.JSONObject\n"
        content += "\n"
        content += "class UBC"+ command + "(command: String, rawData: JSONObject) : Ubmcall(command, rawData) {\n"
        content += "    override fun execute(): UbmcallCallback {\n"
        content += "        Ubm.log.v(\"$command ubmcall has executed.\")\n"
        content += "        return UbmcallCallback(true, successKey(), \"\")\n"
        content += "    }\n"
        content += "}\n"
        f.write(content)
        f.close

def read_list():
    command = []
    
    while True:
        input_str = input(">")
        if input_str == "":
            break
        else:
            command.append(input_str)
    
    return command

command_list = read_list()
create_ubm_files(command_list)

