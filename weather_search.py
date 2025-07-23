import json

def get_weather(city: str) -> str:
    city_map = {
        "深圳": "shenzhen",
        "beijing": "beijing",
        "北京": "beijing",
        "shenzhen": "shenzhen"
    }
    city_key = city_map.get(city.lower(), city.lower())
    weather_data = {
        "beijing": {
            "location": "Beijing",
            "temperature": {
                "current": 32,
                "low": 26,
                "high": 35
            },
            "rain_probability": 10,   # 百分比
            "humidity": 40  # 百分比
        },
        "shenzhen": {
            "location": "Shenzhen",
            "temperature": {
                "current": 28,
                "low": 24,
                "high": 31
            },
            "rain_probability": 90,   # 百分比
            "humidity": 85     # 百分比
        }
    }
    if city_key in weather_data:
        return json.dumps(weather_data[city_key], ensure_ascii=False)
    return json.dumps({"error": "Weather Unavailable"}, ensure_ascii=False)