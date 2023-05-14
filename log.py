from util import bubble_power, bubble_ladder, duyenha, dice, angelsdemons, ostrichrun, eosball1m, eosball3m, eosball5m, roulette
import requests
import time
import sqlite3
from threading import Thread

def start_db():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    return con, cur

def bubble_powerwebhook_send(): # 보글 파워볼 웹훅
    req = bubble_power.bubble_power()

    시간 = bubble_power.bubble_power_time()
    url = "" 

    data = {
        "username" : str(req['회차'])
    }

    data["embeds"] = [
        {
            "title" : "보글 파워볼 결과",
            "description" : f""">>> **회차 : {req['회차']}\n파워볼 결과 : {req['파워볼홀짝']}/{req['파워볼언옵']}\n일반볼 결과 : {req['일반홀짝']}/{req['일반언옵']}/{req['대중소']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)

def bubble_ladderwebhook_send(): # 보글사다리 웹훅
    req = bubble_ladder.bubble_ladder()

    시간 = bubble_ladder.bubble_ladder_time()
    url = "" 

    data = {
        "username" : str(req['회차'])
    }

    data["embeds"] = [
        {
            "title" : "보글 사다리 결과",
            "description" : f""">>> **회차 : {req['회차']}\n보글사다리 결과 : {req['좌우']}/{req['3줄4줄']}/{req['홀짝']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)

def duyenhawebhook_send(): # 바카라 웹훅
    req = duyenha.duyenha()

    시간 = duyenha.duyenha_time()
    url = ""

    data = {
        "username" : str(req['회차'])
    }
    if req['바카라결과'] == "플":
        바카라결과 = "🔵 플레이어"
    elif req['바카라결과'] == "뱅":
        바카라결과 = "🔴 뱅커"
    elif req['바카라결과'] == "타이":
        바카라결과 = "🟢 타이"

    data["embeds"] = [
        {
            "title" : "바카라 결과",
            "description" : f""">>> **회차 : {req['회차']}\n플레이어카드 : {', '.join(req['플레이어카드리스트'])}\n뱅커카드 : {', '.join(req['뱅커카드리스트'])}\n바카라 결과 : {바카라결과}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)

def dicewebhook_send(): # 주사위 웹훅
    req = dice.dice()

    시간 = dice.dice_time()
    url = ""

    data = {
        "username" : str(req['회차'])
    }


    data["embeds"] = [
        {
            "title" : "주사위 결과",
            "description" : f""">>> **회차 : {req['회차']}\n주사위 결과 : {req['홀짝']}/{req['블루레드무']}/{req['하이로우타이']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)





def angelsdemonswebhook_send(): # 천사와 악마 웹훅
    req = angelsdemons.angelsdemons()

    시간 = angelsdemons.angelsdemons_time()
    url = ""

    data = {
        "username" : str(req['회차'])
    }

    if req['천사와악마'] == "천사":
        결과 = "👼 천사"
    elif req['천사와악마'] == "악마":
        결과 = "👿 악마"

    data["embeds"] = [
        {
            "title" : "천사와악마 결과",
            "description" : f""">>> **회차 : {req['회차']}\n천사와악마 결과 : {결과}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)


def ostrichrunwebhook_send(): # 타조게임 웹훅
    req = ostrichrun.ostrichrun()

    시간 = ostrichrun.ostrichrun_time()
    url = ""

    data = {
        "username" : str(req['회차'])
    }


    data["embeds"] = [
        {
            "title" : "타조게임 결과",
            "description" : f""">>> **회차 : {req['회차']}\n타조게임 결과 : {req['좌우']}/{req['달린횟수']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)



def eosball1mwebhook_send(): # 이오스 1분 웹훅
    req = eosball1m.eosball1m()

    시간 = eosball1m.eosball1m_time()

    url = ""

    data = {
        "username" : str(req['회차'])
    }


    data["embeds"] = [
        {
            "title" : "이오스 1분 결과",
            "description" : f""">>> **회차 : {req['회차']}\n파워볼 결과 : {req['파워볼홀짝']}/{req['파워볼언옵']}\n일반볼 결과 : {req['일반홀짝']}/{req['일반언옵']}/{req['대중소']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)


def eosball3mwebhook_send(): # 이오스 3분 웹훅
    req = eosball3m.eosball3m()

    시간 = eosball3m.eosball3m_time()

    url = ""

    data = {
        "username" : str(req['회차'])
    }


    data["embeds"] = [
        {
            "title" : "이오스 3분 결과",
            "description" : f""">>> **회차 : {req['회차']}\n파워볼 결과 : {req['파워볼홀짝']}/{req['파워볼언옵']}\n일반볼 결과 : {req['일반홀짝']}/{req['일반언옵']}/{req['대중소']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)


def eosball5mwebhook_send(): # 이오스 5분 웹훅
    req = eosball5m.eosball5m()

    시간 = eosball5m.eosball5m_time()

    url = ""

    data = {
        "username" : str(req['회차'])
    }


    data["embeds"] = [
        {
            "title" : "이오스 5분 결과",
            "description" : f""">>> **회차 : {req['회차']}\n파워볼 결과 : {req['파워볼홀짝']}/{req['파워볼언옵']}\n일반볼 결과 : {req['일반홀짝']}/{req['일반언옵']}/{req['대중소']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)


def roulettewebhook_send(): # 와이룰렛 웹훅
    req = roulette.roulette()

    시간 = roulette.roulette_time()

    url = "" 

    data = {
        "username" : str(req['회차'])
    }


    data["embeds"] = [
        {
            "title" : "와이룰렛 결과",
            "description" : f""">>> **회차 : {req['회차']}\n와이룰렛 결과 : {req['빨노']}/{req['언오']}/{req['홀짝']}\n다음 회차까지 {시간}초 남았습니다.**"""
        }
    ]

    requests.post(url, json = data)




def bubble_power_send():
    try:
        print("보글 파워볼 로그 시작")
        bubble_powerwebhook_send()

        while True:
            print(str(bubble_power.bubble_power_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(bubble_power.bubble_power_time() + 1)
            print("로그 전송 시작")
            bubble_powerwebhook_send()
            req = bubble_power.bubble_power()

            현재회차 = req['회차']

            결과리스트 = [req['파워볼홀짝'], req['파워볼언옵'], req['일반홀짝'], req['일반언옵'], req['대중소']]
            con, cur = start_db()

            cur.execute("SELECT * FROM bubble_power")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM bubble_power WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue
                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()
                    if 결과 in ("대", "중", "소"):
                        돈 = 배팅한금액 * 2.98
                    else:
                        돈 = 배팅한금액 * 1.98
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM bubble_power WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM bubble_power WHERE id = ?", (userid,))
                    con.commit()
    except:
        bubble_power_send()


def bubble_ladder_send():
    try:
        print("보글 사다리 로그 시작")
        bubble_ladderwebhook_send()

        while True:
            print(str(bubble_ladder.bubble_ladder_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(bubble_ladder.bubble_ladder_time() + 1)
            print("로그 전송 시작")

            bubble_ladderwebhook_send()

            req = bubble_ladder.bubble_ladder()

            현재회차 = req['회차']

            결과리스트 = [req['좌우'], req['3줄4줄'], req['홀짝']]

            con, cur = start_db()

            cur.execute("SELECT * FROM bubble_ladder")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM bubble_ladder WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue
                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()
                    돈 = 배팅한금액 * 1.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM bubble_ladder WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM bubble_ladder WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        bubble_ladder_send()




def duyenha_send():
    try:
        print("바카라 로그 시작")
        duyenhawebhook_send()

        while True:
            print(str(duyenha.duyenha_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(duyenha.duyenha_time() + 1)
            print("로그 전송 시작")

            duyenhawebhook_send()

            req = duyenha.duyenha()

            현재회차 = req['회차']

            결과리스트 = [req['바카라결과']]

            con, cur = start_db()

            cur.execute("SELECT * FROM duyenha")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM duyenha WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue
                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()
                    if 결과 == "플레이어":
                        돈 = 배팅한금액 * 2
                    elif 결과 == "뱅커":
                        돈 = 배팅한금액 * 1.98
                    elif 결과 == "타이": 
                        돈 = 배팅한금액 * 9
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM duyenha WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM duyenha WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        duyenha_send()



def dice_send():
    try:
        print("주사위 로그 시작")
        dicewebhook_send()

        while True:
            print(str(dice.dice_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(dice.dice_time() + 1)
            print("로그 전송 시작")

            dicewebhook_send()

            req = dice.dice()

            현재회차 = req['회차']

            결과리스트 = [req['홀짝'], req['블루레드무'], req['하이로우타이']]

            con, cur = start_db()

            cur.execute("SELECT * FROM dice")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM dice WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue
                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()

                    if 결과 == "타이" or 결과 == "무": 
                        돈 = 배팅한금액 * 9
                    else:
                        돈 = 배팅한금액 * 1.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM dice WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM dice WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        dice_send()



def angelsdemons_send():
    try:
        print("천악 로그 시작")
        angelsdemonswebhook_send()

        while True:
            print(str(angelsdemons.angelsdemons_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(angelsdemons.angelsdemons_time() + 1)
            print("로그 전송 시작")

            angelsdemonswebhook_send()

            req = angelsdemons.angelsdemons()

            현재회차 = req['회차']

            결과리스트 = [req['천사와악마']]

            con, cur = start_db()

            cur.execute("SELECT * FROM angelsdemons")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM angelsdemons WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue

                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()

                    돈 = 배팅한금액 * 1.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM angelsdemons WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM angelsdemons WHERE id = ?", (userid,))
                    con.commit()
    except: 
        time.sleep(10)
        angelsdemons_send()

def ostrichrun_send():
    try:
        print("타조게임 로그 시작")
        ostrichrunwebhook_send()

        while True:
            print(str(ostrichrun.ostrichrun_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(ostrichrun.ostrichrun_time() + 1)
            print("로그 전송 시작")

            ostrichrunwebhook_send()

            req = ostrichrun.ostrichrun()

            현재회차 = req['회차']

            결과리스트 = [req['좌우'], req["달린횟수"]]

            con, cur = start_db()

            cur.execute("SELECT * FROM ostrichrun")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM ostrichrun WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue
                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()

                    if 결과 == "좌" or 결과 == "우": 
                        돈 = 배팅한금액 * 1.98
                    else:
                        돈 = 배팅한금액 * 2.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM ostrichrun WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM ostrichrun WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        ostrichrun_send()



def eosball1m_send():
    try:
        print("이오스 1분 로그 시작")
        eosball1mwebhook_send()

        while True:
            print(str(eosball1m.eosball1m_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(eosball1m.eosball1m_time() + 1)
            print("로그 전송 시작")

            eosball1mwebhook_send()

            req = eosball1m.eosball1m()

            현재회차 = req['회차']

            결과리스트 = [req['파워볼홀짝'], req['파워볼언옵'], req['일반홀짝'], req['일반언옵'], req['대중소']]

            con, cur = start_db()

            cur.execute("SELECT * FROM eosball1m")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM eosball1m WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue

                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()

                    if 결과 in ("대", "중", "소"):
                        돈 = 배팅한금액 * 2.98
                    else:
                        돈 = 배팅한금액 * 1.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM eosball1m WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM eosball1m WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        eosball1m_send()


def eosball3m_send():
    try:
        print("이오스 3분 로그 시작")
        eosball3mwebhook_send()

        while True:
            print(str(eosball3m.eosball3m_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(eosball3m.eosball3m_time() + 1)
            print("로그 전송 시작")

            eosball3mwebhook_send()

            req = eosball3m.eosball3m()

            현재회차 = req['회차']

            결과리스트 = [req['파워볼홀짝'], req['파워볼언옵'], req['일반홀짝'], req['일반언옵'], req['대중소']]

            con, cur = start_db()

            cur.execute("SELECT * FROM eosball3m")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM eosball3m WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue

                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()

                    if 결과 in ("대", "중", "소"):
                        돈 = 배팅한금액 * 2.98
                    else:
                        돈 = 배팅한금액 * 1.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM eosball3m WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM eosball3m WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        eosball3m_send()


def eosball5m_send():
    try:
        print("이오스 5분 로그 시작")
        eosball5mwebhook_send()

        while True:
            print(str(eosball5m.eosball5m_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(eosball5m.eosball5m_time() + 1)
            print("로그 전송 시작")

            eosball5mwebhook_send()

            req = eosball5m.eosball5m()

            현재회차 = req['회차']

            결과리스트 = [req['파워볼홀짝'], req['파워볼언옵'], req['일반홀짝'], req['일반언옵'], req['대중소']]

            con, cur = start_db()

            cur.execute("SELECT * FROM eosball5m")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM eosball5m WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue

                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()

                    if 결과 in ("대", "중", "소"):
                        돈 = 배팅한금액 * 2.98
                    else:
                        돈 = 배팅한금액 * 1.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM eosball5m WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM eosball5m WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        eosball5m_send()








def roulette_send():
    try:
        print("와이룰렛 로그 시작")
        roulettewebhook_send()

        while True:
            print(str(roulette.roulette_time()) + "초 뒤 로그가 전송됩니다.")
            time.sleep(roulette.roulette_time() + 1)
            print("로그 전송 시작")

            roulettewebhook_send()

            req = roulette.roulette()

            현재회차 = req['회차']

            결과리스트 = [req['빨노'], req['언오'], req['홀짝']]

            con, cur = start_db()

            cur.execute("SELECT * FROM roulette")
            betdata_list = cur.fetchall()

            for betdata in betdata_list:
                종류, 배팅한금액, 결과, 회차 = betdata[1].split(":")
                userid = betdata[0]
                배팅한금액 = int(배팅한금액)

                if 결과 in 결과리스트:
                    if 회차 != 현재회차:
                        cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(배팅한금액), userid))
                        cur.execute("DELETE FROM roulette WHERE id = ?", (userid,))
                        con.commit()
                        con.close()
                        continue

                    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (userid, ))
                    userinfo = cur.fetchone()


                    돈 = 배팅한금액 * 1.98
                    
                    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (int(userinfo[1]) + int(돈), userid))
                    cur.execute("DELETE FROM roulette WHERE id = ?", (userid,))
                    con.commit()
                else:
                    cur.execute("DELETE FROM roulette WHERE id = ?", (userid,))
                    con.commit()
    except:
        time.sleep(10)
        roulette_send()





Thread(target=roulette_send).start()
Thread(target=eosball1m_send).start()
Thread(target=eosball3m_send).start()
Thread(target=eosball5m_send).start()
Thread(target=angelsdemons_send).start()
Thread(target=bubble_power_send).start()
Thread(target=bubble_ladder_send).start()
Thread(target=duyenha_send).start()
Thread(target=dice_send).start()
Thread(target=ostrichrun_send).start()