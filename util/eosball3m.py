import requests



def eosball3m():
    result = {"파워볼홀짝" : "", "파워볼언옵" : "", "일반홀짝" : "", "일반언옵" : "", "대중소" : "", "회차" : ""}
    response = requests.get('https://bepick.net/live/result/eosball3m?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    req = response.json()

    result["회차"] = req['round']

    if req['fd1'] == "1":
        result["파워볼홀짝"] = "파홀"
    if req['fd1'] == "2":
        result["파워볼홀짝"] = "파짝"

    if req['fd2'] == "1":
        result["파워볼언옵"] = "파언"
    if req['fd2'] == "2":
        result["파워볼언옵"] = "파옵"

    if req['fd3'] == "1":
        result["일반홀짝"] = "일홀"
    if req['fd3'] == "2":
        result["일반홀짝"] = "일짝"

    if req['fd4'] == "1":
        result["일반언옵"] = "일언"
    if req['fd4'] == "2":
        result["일반언옵"] = "일옵"

    if req['fd5'] == "1":
        result["대중소"] = "소"
    if req['fd5'] == "2":
        result["대중소"] = "중"
    if req['fd5'] == "3":
        result["대중소"] = "대"

    return result


def eosball3m_time():
    req = requests.get('https://bepick.net/json/game/eosball3m.json?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    return req.json()['time_set']['nextTime'] + 1
