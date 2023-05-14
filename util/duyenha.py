import requests



카드 =  {'S' : "스페이드", 'H' : "하트", 'C' : "클로버", 'D' : "다이아"}


def duyenha():
    result = {"바카라결과" : "", "플레이어카드리스트" : "", "뱅커카드리스트" : "",  "회차" : ""}
    response = requests.get('https://bepick.net/live/result/duyenha?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    req = response.json()

    result["회차"] = req['round']

    if req['fd1'] == "1":
        result["바카라결과"] = "플"
    if req['fd1'] == "2":
        result["바카라결과"] = "뱅"
    if req['fd1'] == "3":
        result["바카라결과"] = "타이"

    플레이어1카드 = str(req['p1'][:1]) + " " + 카드[req['p1'][-1:]]
    플레이어2카드 = str(req['p2'][:1]) + " " + 카드[req['p2'][-1:]]

    if not str(req['p3']) == "0":
        플레이어3카드 = str(req['p3'][:1]) + " " + 카드[req['p3'][-1:]]

        result['플레이어카드리스트'] = [플레이어1카드, 플레이어2카드, 플레이어3카드]
    else:
        result['플레이어카드리스트'] = [플레이어1카드, 플레이어2카드]

    

    뱅커1카드 = str(req['b1'][:1]) + " " + 카드[req['b1'][-1:]]
    뱅커2카드 = str(req['b2'][:1]) + " " + 카드[req['b2'][-1:]]
    if not str(req['b3']) == "0":
        뱅커3카드 = str(req['b3'][:1]) + " " + 카드[req['b3'][-1:]]

        result['뱅커카드리스트'] = [뱅커1카드, 뱅커2카드, 뱅커3카드]
    else:
        result['뱅커카드리스트'] = [뱅커1카드, 뱅커2카드]


    return result


def duyenha_time():
    req = requests.get('https://bepick.net/json/game/duyenha.json?', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    return req.json()['time_set']['nextTime'] + 1


