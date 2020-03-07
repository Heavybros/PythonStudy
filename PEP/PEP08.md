# PEP 8 -- Style Guide for Python Code

## Introduction

PEP 8(Python Enhancement Proposal 8)는 파이썬 표준 라이브러리 배포를 위한 coding convention 이다.

## 주의 사항

본 가이드라인의 주 목적은 코드의 가독성(readability) 증진과 여러 파이썬 코드 간의 일관성(consistency)의 유지이다.
따라서 본 가이드라인의 적용으로 인해 기존 프로젝트 코드의 일관성이 무너지거나 기존에 구성된 coding convention이 있는 경우에는 개발자의 판단에 따라 적용여부를 결정해야 한다.
특히 과거 호환성(backward compatibility)가 깨지지 않도록 하는게 중요하다.

## Code Lay-out

### Indetation

- 각 indentation level 당 공백 4칸으로 사용해야함
- Hanging indent의 경우 예외적 허용됨 (Optional 참조)

Yes:

```:python
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

No:

```:python
# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

Optional:

```:python
# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```

- if-statement에서 긴 조건으로 인한 indent에는 명시적인 제한을 두지 않으며 다음과 같은 옵션을 허용함

```:python
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

- closing brace/bracket/parenthesis(')','}', ']' 의 경우)이 multiline을 구성하는 경우 다음과 같이 허용됨

```:python
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )

my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

### Tabs or Spaces?

- indent 구성 시 space가 선호됨
- tab으로 indent를 이미 구성한 경우 일관성 유지로 tab 사용이 허용
- Python 3.x 은 tab과 space를 혼용한 indent가 허용되지 않음
- Python 2.x 은 tab과 space 혼용 시, 명시적으로 tab이 space로 변환됨
  - python 2.x를 command 에서 실행시 -t 옵션으로 실행하면 혼용 사용에 대해 경고, -tt 옵션은 혼용 사용에 대해 에러를 생성
  - python 2.x 에서는 -tt 옵션을 권장

### Maximum Line Length

- 모든 line에서는 최대 79자로 제한됨
- docstring이나 comment와 같은 구조적 제한이 없는 text의 경우에는 한 line 당 72자로 제한
- 위와 같이 제한할 경우 code review tool이나 여러 코드를 동시에 확인할 때 유리
- 팀에 따라서 긴 line을 선호하는 경우 docstring, comment를 72자로 제한하는 한에서 최대 99자까지 늘려서 사용 가능
- 긴 줄을 감싸는 방법(wrapping)으로 괄호가 선호되며, 감싸진 괄호 내의 line을 multiline으로 나눌 경우 백슬래쉬(\\)가 허용됨
  - with, assert 구문에서 백슬래쉬로 긴 문장을 나누어 표기 가능

```:python
#백슬래쉬 허용 예제
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

### Should a Line Break Before or After a Binary Operator?

- 수십년동안 이항 연산자(binary operator) 이후에 줄바꿈을 수행하나, 가독성이 떨어지는 문제를 가짐
  - 이항 연산자의 위치가 일정치 않음
  - 이전 피연산자 뒤에 이항 연산자가 뒤 따라오기에 추적하기 어려움

```:python
# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

- 가독성 문제를 해결하기 위해 이항 연산자 이전에 줄바꿈을 수행하여야 함
  - (참조) Donald Knuth explains the traditional rule in his Computers and Typesetting series: "Although formulas within a paragraph always break after binary operations and relations, displayed formulas always break before binary operations"

```:python
# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### Blank lines

- 최상위 레벨의 함수와 클래스 정의에는 2개의 빈줄로 감싸야 함
- 클래스 내부에 정의된 메소드 정의는 1개의 빈줄로 감싸야 함
- 연관된 함수 그룹끼리 분류하기 위해 추가적인 빈줄 사용이 허가됨
- 논리적 구역(logical section) 구분 하기 위해서 함수 내에서 빈줄 사용이 가능
- ctrl-L과 같은 form feed 가 허용되나 form feed 지원하지 않는 툴의 사용자가 있음을 인지하고 있어야 함

### Source File Encoding

- core Python distribution 에서는 항상 UTF-8로 설정 (Python 2.x 에서는 ASCII)
- ASCII(python 2.x의 경우)와 UTF-8(python 3.x의 경우)에서는 인코딩 선언을 권장하지 않음 
- 표준 라이브러리에서는 테스트 목적이나 comment, docstring에 non-ASCII 문자가 포함된 작성자 이름을 명시해야 하는 경우 한시적으로 허용 가능하며 그 이외에는 \\x, \\u, \\U, \\N 등의 esacpe 문자만 허용
- Python 3.x 및 그 이후의 경우는 PEP3131 참조
  - 모든 식별자들의 이름은 ASCII 문자로만 구성할 것
  - 식별자의 이름은 영어 단어로 알아볼 수 있는 형태여야 함
- 다국적으로 참여하는 open source project에서도 위와 유사한 정책 수행을 권장

### Import

- import는 각 줄에 따로 정의할 것을 권장

```:python
Yes: import os
     import sys

No:  import sys, os
```

- 다음과 같은 경우에는 허용

```:python
from subprocess import Popen, PIPE
```

- Import는 다음과 같은 순서로 그룹화 해야하며, 각 그룹마다 공백줄을 추가함으로 분류하는 것을 권장
  1. 표준 라이브러리 imports
  2. 연관된 third party imports
  3. 특정 local application/library import

- 절대 경로 import (Absolute import)가 권장
  - 가독성과 configure에 영향을 받지 않고 import 수행됨

```:python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

- 상대 경로 import(relative import)은 절대 경로가 반영된 복잡한 구조의 패키지 내에서 가독성을 위해 절대 경로 import 대신 사용 가능
  - 단, python 3 에서는 상대 경로 import 삭제

```:python
from . import sibling
from .sibling import example
```

- 클래스를 포함하는 모듈에서 클래스 import 시, 다음과 사용 가능

```:python
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

- import 한 클래스와 현재 local 내에 정의된 이름과 충돌나는 경우 다음과 같이 정의하여 사용

```:python
import myclass
import foo.bar.yourclass
```

- import 시에 wildcard import(from \<module\> import *)는 피하는 것이 좋음
  - wildcard import는 자동화 툴에서 각 변수 및 함수, 클래스간의 구조를 불분명하게 하여 분석이 용이하지 않음
  - 단, Public API의 internal interface를 재정의하기 위해서 wildcard import가 사용될 여지는 있음

### Module Level Dunder Name

- Module Level dunder (__version__, __all__ 와 같이 2개의 underscore로 감싸져 있는 변수)는 docstring과 __future__ import 다음에 정의되어야 함

```:python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

## String Quotes

- 큰따옴표와 작은 따옴표에 대한 제한은 크게 없으나 작성 시에 정해진 정책에 따라서 작성할 것을 권장
- docstring을 구성하는 block에서는 큰따옴표를 권장

## Wihtespace in Expressions and Statements

### Pet Peeves

- 다음과 같은 추가적인 공백은 권장되지 않음
  - 괄호 다음에 바로 추가되는 공백

```:python
Yes: spam(ham[1], {eggs: 2})
No:  spam( ham[ 1 ], { eggs: 2 } )
```

  - 쉼표와 닫는 괄호 사이에 공백 추가

```:python
Yes: foo = (0,)
No:  bar = (0, )
```

  - 콤마, 세미콜론, 콜론 앞에 공백 추가

```:python
Yes: if x == 4: print x, y; x, y = y, x
No:  if x == 4 : print x , y ; x , y = y , x
```
  - 콜론이 slice 로 사용되는 경우, 우선순위가 제일 낮은 이항 연산자로 취급됨
  - slice로 사용된 콜론의 경우 양 쪽에 동일한 크기의 공백이 할당이 되어야 함
  - 예외적으로 슬라이스 사이의 파라미터가 없는 경우, 해당 공백 파라미터에 공백은 할당되지 않음

```:python
Yes:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

No:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

  - 함수 호출 시 괄호 이전에 공백 추가

```:python
Yes: spam(1)
No:  spam (1)
```

  - 인덱싱, 슬라이싱에 사용되는 여는 괄호 이전에 공백 추가

```:python
Yes: dct['key'] = lst[index]
No:  dct ['key'] = lst [index]
```

  - 다른 줄의 줄맞춤을 위한 추가적인 공백 시
```:python
Yes:
x = 1
y = 2
long_variable = 3

No:
x             = 1
y             = 2
long_variable = 3
```

### Other Recommendation

- 어디서든 trailing whitespace(line 마지막에 추가되는 공백들)는 없어야 하며, 이러한 공백은 보이지 않기 때문에 확인하기 어려움
- 항상 아래의 모든 이항 연산자들은 단일 공백으로 둘러쌓여야 함
  - assignment (=)
  - augmented assignment (+=, -= etc.)
  - comparison  (==, <, >, !=, <>, <=, >=, in, not in, is, is not)
  - Boolean (and, or, not)
- 다양한 우선순위의 연산자를 사용하는 경우에는 가장 낮은 우선순위의 연산자에 공백을 추가하는 것이 고려될 수 있음
- 단, 하나 이상의 다중 공백의 사용은 불허하며, 이항 연산자의 경우 양쪽에 동일한 크기의 공백이 할당되어야 함
```:python
Yes:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

No:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

- Function annotation의 콜론은 기본 법칙을 따르며, 화살표 (->)은 양 옆으로 공백이 있어야 함
```:python
Yes:
def munge(input: AnyStr): ...
def munge() -> PosInt: ...

No:
def munge(input:AnyStr): ...
def munge()->PosInt: ...
```

- keyword argument와 unannotated function parameter의 default value를 할당하기 위해 사용되는 할당 연산자(=)에는 공백이 추가될 수 없음
```:python
Yes:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

No:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

- argument annotation과 default value가 같이 정의된 경우에는 할당 연산자에 공백을 추가함
```:python
Yes:
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

No:
def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```

 - Compound statement(한 줄에 여러 문장이 들어가는 경우)는 일반적으로 권장되지 않음
 ```:python
Yes:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

Rather not:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```

- for, while, if의 구성이 작다면 한줄로 처리해도 괜찮을 수 있으나, 큰 구문을 하나의 줄로 처리하는 경우는 허용하지 않음
 ```:python
Rather not:
if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()

Definitely not:
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()
```

### When to Use Trailing Commas

- 일반적으로 trailing comma는 선택 사항이나, 1개의 element만 가지는 tuple의 생성하는 경우는 필수적으로 사용해야 함
- trailing comma 사용 시 혼동을 주리익 위해서 괄호로 감싸는 것을 권장

 ```:python
Yes:
FILES = ('setup.cfg',)

OK, but confusing:
FILES = 'setup.cfg',
```
