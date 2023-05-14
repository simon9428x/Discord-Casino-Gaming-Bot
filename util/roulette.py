import requests



def roulette():
    result = {"빨노" : "", "언오" : "", "홀짝" : "", "회차" : ""}
    response = requests.get('https://bepick.net/live/result/y_roulette?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    req = response.json()

    result["회차"] = req['round']

    if req['fd1'] == "1":
        result["빨노"] = "빨"
    if req['fd1'] == "2":
        result["빨노"] = "노"

    if req['fd2'] == "1":
        result["언오"] = "언"
    if req['fd2'] == "2":
        result["언오"] = "오"

    if req['fd3'] == "1":
        result["홀짝"] = "홀"
    if req['fd3'] == "2":
        result["홀짝"] = "짝"

    return result


def roulette_time():
    req = requests.get('https://bepick.net/json/game/y_roulette.json?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    return req.json()['time_set']['nextTime'] + 1


