import requests



def ostrichrun():
    result = {"좌우" : "", "달린횟수" : "", "회차" : ""}
    response = requests.get('https://bepick.net/live/result/jw_ostrichrun?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    req = response.json()

    result["회차"] = req['round']

    if req['fd1'] == "1":
        result["좌우"] = "좌"
    if req['fd1'] == "2":
        result["좌우"] = "우"

    if req['fd2'] == "1":
        result["달린횟수"] = "1"
    if req['fd2'] == "2":
        result["달린횟수"] = "2"
    if req['fd2'] == "3":
        result["달린횟수"] = "3"

    return result


def ostrichrun_time():
    req = requests.get('https://bepick.net/json/game/jw_ostrichrun.json?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    return req.json()['time_set']['nextTime'] + 1


