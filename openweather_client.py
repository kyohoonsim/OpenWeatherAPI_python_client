import requests


stadium_loc = {
    "KIA": {"lat": 35.1682592, "lon": 126.8884114},  # 광주-기아 챔피언스 필드
    "LG": {"lat": 37.5122579, "lon": 127.0719011},  # 잠실 야구장
    "DOOSAN": {"lat": 37.5122579, "lon": 127.0719011},  # 잠실 야구장
    "KIWOOM": {"lat": 37.49979715, "lon": 126.86548015},  # 고척스카이돔
    "SAMSUNG": {"lat": 35.8410136, "lon": 128.6819955},  # 대구삼성라이온즈파크
    "HANHWA": {"lat": 36.3172026, "lon": 127.4285703},  # 한화생명이글스파크
    "NC": {"lat": 35.2225335, "lon": 128.5823895},  # 창원 NC파크
    "LOTTE": {"lat": 35.1940316, "lon": 129.0615183},  # 사직야구장
    "SSG": {"lat": 37.4370423, "lon": 126.6932617},  # 인천 SSG 랜더스필드
    "KT": {"lat": 37.2997553, "lon": 127.0096685},  # 수원KT위즈파크
}


class OpenWeatherClient:
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_all(self, lat: float, lon: float):
        params = {"lat": lat, "lon": lon, "appid": self.api_key, "units": "metric"}
        res = requests.get(OpenWeatherClient.API_URL, params=params)
        res_json = res.json()
        return res_json

    def get_temp(self, lat: float, lon: float):
        res_json = self.get_all(lat, lon)
        temp = res_json["main"]["temp"]
        return temp

    def get_rain(self, lat: float, lon: float):
        res_json = self.get_all(lat, lon)
        weather = res_json["weather"][0]["main"]

        if weather != "Rain":
            rain = 0
        else:
            rain = res_json["rain"]["1h"]  # mm/h

        return rain

    def get_baseball_stadium_temp(self, team_name: str):
        if team_name not in stadium_loc.keys():
            raise Exception("존재하지 않는 KBO 야구 팀명입니다.")

        params = {
            "lat": stadium_loc[team_name]["lat"],
            "lon": stadium_loc[team_name]["lon"],
            "appid": self.api_key,
            "units": "metric",
        }
        res = requests.get(OpenWeatherClient.API_URL, params=params)
        res_json = res.json()

        temp = res_json["main"]["temp"]
        return temp

    def get_baseball_stadium_rain(self, team_name: str):
        if team_name not in stadium_loc.keys():
            raise Exception("존재하지 않는 KBO 야구 팀명입니다.")

        params = {
            "lat": stadium_loc[team_name]["lat"],
            "lon": stadium_loc[team_name]["lon"],
            "appid": self.api_key,
            "units": "metric",
        }
        res = requests.get(OpenWeatherClient.API_URL, params=params)
        res_json = res.json()

        weather = res_json["weather"][0]["main"]

        if team_name == "KIWOOM":
            rain = 0

        if weather != "Rain":
            rain = 0
        else:
            rain = res_json["rain"]["1h"]  # mm/h

        return rain
