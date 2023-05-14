import requests



def bubble_ladder():
    result = {"좌우" : "", "3줄4줄" : "", "홀짝" : "", "회차" : ""}
    response = requests.get('https://bepick.net/live/result/bubble_ladder3?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    req = response.json()

    result["회차"] = req['round']

    if req['fd1'] == "1":
        result["좌우"] = "좌"
    if req['fd1'] == "2":
        result["좌우"] = "우"

    if req['fd2'] == "1":
        result["3줄4줄"] = "3줄"
    if req['fd2'] == "2":
        result["3줄4줄"] = "4줄"

    if req['fd3'] == "1":
        result["홀짝"] = "홀"
    if req['fd3'] == "2":
        result["홀짝"] = "짝"

    return result


def bubble_ladder_time():
    req = requests.get('https://bepick.net/json/game/bubble_ladder3.json?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    return req.json()['time_set']['nextTime'] + 1
