# OpenWeather API Python Client

OpenWeather API를 활용하여 실시간 날씨 정보를 조회하는 파이썬 클라이언트 소스코드입니다. (This is a source code for OpenWeather API Python Client to get real-time weather information over world.)

위도, 경도 좌표값을 전달하면 해당 위치의 기온, 강수량 등의 정보를 얻을 수 있습니다. (If you pass latitude, longitude on a site, you can get weather information like temperature, the amount of rainfall.)

프로야구 직관을 좋아하시는 분들을 위해서 10개 구단 야구장의 실시간 날씨를 팀명만 입력하면 쉽게 조회할 수 있게 해놓았습니다. (For those who like KBO, we have made it easy to search the real-time weather of 10 club baseball fields by simply entering the team name.)

## 사용 준비 (Ready for Utilization)

1. 우선 아래 웹사이트에서 OpenWeather의 API KEY를 얻습니다. (Get API KEY of OpenWeather in the following URL link.)

   - <https://home.openweathermap.org/>

2. 필요 파이썬 패키지를 설치합니다. (Install required python packages.)

   - `pip install requests`

## 사용 예시 (Utilization Example)

```
from openweather_client import OpenWeatherClient


OW_client = OpenWeatherClient("API_KEY")

yeouido_temp = OW_client.get_temp(37.5295803, 126.9326803)
print(f"여의도의 현재 기온은 섭씨 {yeouido_temp}도입니다.")
yeouido_rain = OW_client.get_rain(37.5295803, 126.9326803)
print(f"여의도의 현재 강수량은 {yeouido_rain}mm/h입니다.")

lotte_temp = OW_client.get_baseball_stadium_temp("LOTTE")
print(f"LOTTE 구장의 현재 기온은 섭씨 {lotte_temp}도입니다.")
lotte_rain = OW_client.get_baseball_stadium_rain("LOTTE")
print(f"LOTTE 구장의 현재 강수량은 {lotte_rain}mm/h입니다.")

```

API_KEY 부분에는 여러분의 API_KEY를 기입해주셔야 합니다. (It is required to enter your API KEY in the above code.)

예제 코드 실행 결과 화면은 다음과 같습니다. (The execution result screen of the example source code is as follows.)

![예제실행화면](./Screenshot.png)
