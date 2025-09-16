# 1. 모듈에 함수까지 전부 불러와서 사용하는 방법
from com.py.oop.other_module import other_function
other_function()

# 2. 모듈을 불러와서 별칭 부여 후 사용하는 방법
from com.py.oop import other_module as mo
mo.other_function()

# 3. 전체 패키지 불러와서 별칭 부여 후 사용
import com.py.oop.other_module as mo
mo.other_function()

# 1과 2와 3의 차이는 같은 의미를 갖지만 입력 방식의 차이
# 1은 파일에서 특정한 기능만 불러오는 것으로 추후 파일 데이터가 엄청 클 때 필요한 것만 빼올 수 있음
# 2: from 파일위치 import 파일명 as 별칭
# 3: import 파일위치+파일명 as 별칭