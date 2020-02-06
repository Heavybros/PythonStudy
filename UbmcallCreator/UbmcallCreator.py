import os

def create_ubm_files(command_list):
    for command in command_list:
        # open 을 해서 없는 파일이면 새로 생성한다.
        # a는 내용 추가, r은 읽기전용, w은 쓰기이다.
        f = open("Ubmcall_" + command + ".kt", mode='w', encoding='utf8')
        content = ""
        content += "package com.harex.feature.ubmcall\n" 
        content += " \n"
        content += "import com.harex.core.Ubm\n" 
        content += "import org.json.JSONObject\n" 
        content += " \n"
        content += "class Ubmcall_" + command +"(command: String, rawData: JSONObject) : Ubmcall(command, rawData) {\n" 
        content += "    override fun execute(onFinished: (result: UbmcallCallback) -> Unit) {\n" 
        content += "        Ubm.log.v(\"$command ubmcall has executed.\")\n" 
        content += "        onFinished(UbmcallCallback(true, success, \"\"))\n" 
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

