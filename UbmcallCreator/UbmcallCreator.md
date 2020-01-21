UBC*.kt 소스코드 자동 생성하기
===================================

# 문제 설명

- 해나라는 동일한 규칙의 코틀린 소스코드 파일을 일일히 만드는 대신, 파이썬으로 자동 생성을 해보고자 합니다.

- 아래와 같이 주어진 함수 목록이 있습니다. 

```
setAttribute
getAttribute
removeAttribute
...
```

- 이 함수 명들을 가지고 아래와 같은 코틀린 파일을 생성하고자 합니다.

```
UBCsetAttribute.kt
UBCgetAttribute.kt
UBCremoveAttribute.kt
...
```
 
# 요구 사항

- 생성할 UBC*.kt 코틀린 파일 명명규칙은 아래와 같다. 
```
UBC + 함수명 + .kt
```

- 생성된 코틀린 파일의 내부에 입력될 소스코드는 아래와 같다.
```
package com.harex.feature.ubmcall

import com.harex.core.Ubm
import org.json.JSONObject

class UBC*(command: String, rawData: JSONObject) : Ubmcall(command, rawData) {
    override fun execute(): UbmcallCallback {
        Ubm.log.v("$command ubmcall has executed.")
        return UbmcallCallback(true, successKey(), "")
    }
}
```

# 예제 입력
```
setAttribute
getAttribute
```

# 예제 출력


- 파일명 :  UBCsetAttribute.Kt
- 소스코드 : 
```
package com.harex.feature.ubmcall

import com.harex.core.Ubm
import org.json.JSONObject

class UBCsetAttribute(command: String, rawData: JSONObject) : Ubmcall(command, rawData) {
    override fun execute(): UbmcallCallback {
        Ubm.log.v("$command ubmcall has executed.")
        return UbmcallCallback(true, successKey(), "")
    }
}
```

- 파일명 :  UBCsetAttribute.Kt
- 소스코드 : 

```
package com.harex.feature.ubmcall

import com.harex.core.Ubm
import org.json.JSONObject

class UBCsetAttribute(command: String, rawData: JSONObject) : Ubmcall(command, rawData) {
    override fun execute(): UbmcallCallback {
        Ubm.log.v("$command ubmcall has executed.")
        return UbmcallCallback(true, successKey(), "")
    }
}
```

# 풀이

- 소스 코드 : [UbmcallCreator.py](UbmcallCreator.py)


