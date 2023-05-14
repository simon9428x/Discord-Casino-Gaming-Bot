import requests



def angelsdemons():
    result = {"천사와악마" : "", "회차" : ""}
    response = requests.get('https://bepick.net/live/result/jw_angelsdemons?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    req = response.json()
    result["회차"] = req['round']

    if req['fd1'] == "1":
        result["천사와악마"] = "천사"
    if req['fd1'] == "2":
        result["천사와악마"] = "악마"

    return result


def angelsdemons_time():
    req = requests.get('https://bepick.net/json/game/jw_angelsdemons.json?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    return req.json()['time_set']['nextTime'] + 1

