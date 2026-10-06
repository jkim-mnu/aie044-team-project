# elapsed_seconds 가 초 단위를 돌려주는지 검사한다.
from myapp.store import Store

s = Store()
got = s.elapsed_seconds(10, 12)
if got == 2:
    print("정상: 2초")
    raise SystemExit(0)
print("고장: 초 단위가 아님 ->", got)
raise SystemExit(1)
