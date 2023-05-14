import requests



def dice():
    result = {"홀짝" : "", "블루레드무" : "", "하이로우타이" : "", "회차" : ""}
    response = requests.get('https://bepick.net/live/result/s8_dice?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    req = response.json()

    result["회차"] = req['round']


    if req['fd1'] == "1":
        result["홀짝"] = "홀"
    if req['fd1'] == "2":
        result["홀짝"] = "짝"

    if req['fd2'] == "1":
        result["블루레드무"] = "블루"
    if req['fd2'] == "2":
        result["블루레드무"] = "레드"
    if req['fd2'] == "0":
        result["블루레드무"] = "무"

    if req['fd3'] == "1":
        result["하이로우타이"] = "로우"
    if req['fd3'] == "2":
        result["하이로우타이"] = "하이"
    if req['fd3'] == "0":
        result["하이로우타이"] = "타이"


    return result


def dice_time():
    req = requests.get('https://bepick.net/json/game/s8_dice.json?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    return req.json()['time_set']['nextTime'] + 1


