import discord, asyncio, requests, sqlite3
from discord.ext import commands
from util import bubble_power, bubble_ladder, duyenha, dice, angelsdemons, ostrichrun, eosball1m, eosball3m, eosball5m, roulette


def start_db():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    return con, cur


command_prefix = "."
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=command_prefix, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"[!] 초대링크 : https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot\n")
    print(f"[!] 봇 이름 : {bot.user.name}\n[!] 봇 아이디 : {bot.user.id}\n[!] 참가 중인 서버 : {len(bot.guilds)}개")
    await bot.change_presence(activity=discord.Game(name="최고의 무료 카지노"), status=discord.Status.online)




"""설정"""
token = ""
admin_id = 
배팅채널 = 
가입채널 = 
꽁머니채널 = 
보글볼배팅리스트 = ["파홀", "파짝", "파언", "파옵", "일홀", "일짝", "일언", "일옵", "대", "중", "소"]
보글사다리배팅리스트 = ['좌', "우", "3줄", "4줄", "홀", "짝"]
바카라배팅리스트 = ["뱅커", "플레이어", "타이"]
주사위배팅리스트 = ["홀", "짝", "블루", "레드", "하이", "로우" , "타이" , "무"]
천사와악마배팅리스트 = ['천사', "악마"]
타조게임배팅리스트 = ['좌', '우', '1', '2', '3']
이오스배팅리스트 = ["파홀", "파짝", "파언", "파옵", "일홀", "일짝", "일언", "일옵", "대", "중", "소"]
룰렛배팅리스트 = ["홀", "짝", "빨", "노", "언", "오"]
"""설정"""


@bot.command()
async def 명령어(ctx):

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()


    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        
    return await ctx.reply(f"""
>>> **```{command_prefix}일반명령어 : 일반명령어를 확인합니다!
``````{command_prefix}배팅명령어 : 일반명령어를 확인합니다!
```**""")


@bot.command()
async def 일반명령어(ctx):

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()


    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        
    return await ctx.reply(f"""
>>> **```{command_prefix}내정보 : 내 정보를 출력합니다!
``````{command_prefix}정보 [ 유저 멘션 ] : 멘션한 유저의 정보를 출력합니다!
``````{command_prefix}가입 : 무료 카지노에 가입합니다!
```**""")

@bot.command()
async def 배팅명령어(ctx):

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()


    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        
    return await ctx.reply(f"""
>>> **```{command_prefix}보글볼 [ 결과 ] [ 금액 ]
``````{command_prefix}보글사다리 [ 결과 ] [ 금액 ]
``````{command_prefix}바카라 [ 결과 ] [ 금액 ]
``````{command_prefix}주사위 [ 결과 ] [ 금액 ]
``````{command_prefix}천악 [ 결과 ] [ 금액 ]
``````{command_prefix}타조 [ 결과 ] [ 금액 ]
``````{command_prefix}룰렛 [ 결과 ] [ 금액 ]
``````{command_prefix}이오스1분 [ 결과 ] [ 금액 ]
``````{command_prefix}이오스3분 [ 결과 ] [ 금액 ]
``````{command_prefix}이오스5분 [ 결과 ] [ 금액 ]
```**""")


@bot.command()
async def 정보(ctx, 유저 : discord.User):

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (유저.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (유저.id, 0))
        con.commit()
        con.close()
        
        return await ctx.reply(f"> **{유저.name}님의 잔액은 0원 입니다!**")
    else:
        return await ctx.reply(f"> **{유저.name}님의 잔액은 {format(userinfo[1], ',')}원 입니다!**")  


@bot.command()
async def 가입(ctx):
    if ctx.channel.id != 가입채널:
        return None
    

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()


    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **가입하신걸 환영합니다 {ctx.author.name}님**")
    else:
        return await ctx.reply(f"> **이미 가입한 유저 입니다!**")


@bot.command()
async def 내정보(ctx):

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        
        return await ctx.reply(f"> **{ctx.author.name}님의 잔액은 0원 입니다!**")
    else:
        return await ctx.reply(f"> **{ctx.author.name}님의 잔액은 {format(userinfo[1], ',')}원 입니다!**")  



@bot.command()
async def 보글볼(ctx, 결과:str, 돈:int):

    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 보글볼배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님  파홀, 파짝, 파언, 파옵, 일홀, 일짝, 일언, 일옵, 대, 중, 소 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if bubble_power.bubble_power_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  
    
    cur.execute("SELECT * FROM bubble_power WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  

    회차 = int(bubble_power.bubble_power()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO bubble_power Values(?, ?);", (ctx.author.id, f"보글볼:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  

@bot.command()
async def 보글사다리(ctx, 결과:str, 돈:int):
    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 보글사다리배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님 좌, 우, 3줄, 4줄, 홀, 짝 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if bubble_ladder.bubble_ladder_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  

    
    cur.execute("SELECT * FROM bubble_ladder WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  


    회차 = int(bubble_ladder.bubble_ladder()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO bubble_ladder Values(?, ?);", (ctx.author.id, f"보글사다리:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  


@bot.command()
async def 바카라(ctx, 결과:str, 돈:int):
    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 바카라배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님 뱅커, 플레이어, 타이 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if duyenha.duyenha_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  

    
    cur.execute("SELECT * FROM duyenha WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  


    회차 = int(duyenha.duyenha()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO duyenha Values(?, ?);", (ctx.author.id, f"두옌하바카라:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  



@bot.command()
async def 주사위(ctx, 결과:str, 돈:int):
    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 주사위배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님 홀, 짝, 블루, 레드, 하이, 로우 , 타이 , 무 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if dice.dice_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  

    
    cur.execute("SELECT * FROM dice WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  


    회차 = int(dice.dice()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO dice Values(?, ?);", (ctx.author.id, f"주사위:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  





@bot.command()
async def 천악(ctx, 결과:str, 돈:int):
    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 천사와악마배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님 천사, 악마 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if angelsdemons.angelsdemons_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  

    
    cur.execute("SELECT * FROM angelsdemons WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  


    회차 = int(dice.dice()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO angelsdemons Values(?, ?);", (ctx.author.id, f"천사와악마:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  




@bot.command()
async def 타조(ctx, 결과:str, 돈:int):
    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 타조게임배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님 좌, 우, 1, 2, 3 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if ostrichrun.ostrichrun_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  

    
    cur.execute("SELECT * FROM ostrichrun WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  


    회차 = int(dice.dice()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO ostrichrun Values(?, ?);", (ctx.author.id, f"타조게임:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  







@bot.command()
async def 이오스1분(ctx, 결과:str, 돈:int):

    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 이오스배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님  파홀, 파짝, 파언, 파옵, 일홀, 일짝, 일언, 일옵, 대, 중, 소 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if eosball1m.eosball1m_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  
    
    cur.execute("SELECT * FROM eosball1m WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  

    회차 = int(eosball1m.eosball1m()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO eosball1m Values(?, ?);", (ctx.author.id, f"이오스1분:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  





@bot.command()
async def 이오스3분(ctx, 결과:str, 돈:int):

    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 이오스배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님  파홀, 파짝, 파언, 파옵, 일홀, 일짝, 일언, 일옵, 대, 중, 소 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if eosball3m.eosball3m_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  
    
    cur.execute("SELECT * FROM eosball1m WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  

    회차 = int(eosball3m.eosball3m()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO eosball3m Values(?, ?);", (ctx.author.id, f"이오스3분:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  




@bot.command()
async def 이오스5분(ctx, 결과:str, 돈:int):

    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 이오스배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님  파홀, 파짝, 파언, 파옵, 일홀, 일짝, 일언, 일옵, 대, 중, 소 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if eosball5m.eosball5m_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  
    
    cur.execute("SELECT * FROM eosball5m WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  

    회차 = int(eosball5m.eosball5m()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO eosball5m Values(?, ?);", (ctx.author.id, f"이오스5분:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  


@bot.command()
async def 룰렛(ctx, 결과:str, 돈:int):

    if ctx.channel.id != 배팅채널:
        return None

    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()
        con.close()
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if not 결과 in 룰렛배팅리스트:
        return await ctx.reply(f"> **{ctx.author.name}님  빨, 노, 언, 오, 홀, 짝 중 하나를 골라 배팅해주세요!**")  

    if 돈 <= 0:
        return await ctx.reply(f"> **{ctx.author.name}님 0원 이하의 배팅은 불가능합니다!**")  
    
    if 돈 > userinfo[1]:
        return await ctx.reply(f"> **{ctx.author.name}님 잔액이 부족합니다!**")  

    if roulette.roulette_time() <= 10:
        return await ctx.reply(f"> **{ctx.author.name}님 10초전에는 배팅이 불가능합니다!**")  
    
    cur.execute("SELECT * FROM roulette WHERE id == ?;", (ctx.author.id, ))
    betinfo = cur.fetchone()
    if betinfo != None:
        return await ctx.reply(f"> **{ctx.author.name}님 이미 배팅을 하셨습니다!**")  

    회차 = int(roulette.roulette()['회차']) + 1
    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] - 돈, ctx.author.id))
    cur.execute("INSERT INTO roulette Values(?, ?);", (ctx.author.id, f"와이룰렛:{돈}:{결과}:{회차}"))
    con.commit()
    con.close()

    return await ctx.reply(f"> **{ctx.author.name}님 {결과}에 {format(돈, ',')}원이 배팅되었습니다!**")  









@bot.command()
async def 수동충전(ctx, 유저 : discord.User, 돈:int):

    if ctx.author.id != admin_id:
        return None
    
    con, cur = start_db()
    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (유저.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (유저.id, 0))
        con.commit()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (유저.id, ))
    userinfo = cur.fetchone()

    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] + 돈, 유저.id))
    con.commit()
    con.close()
    return await ctx.reply(f"> **<@{유저.id}>님의 현재 잔액은 {format(userinfo[1] + 돈, ',')}원 입니다!**")  




@bot.command()
async def 꽁머니(ctx):

    if ctx.channel.id != 꽁머니채널:
        return None
    
    con, cur = start_db()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    if userinfo == None:
        cur.execute("INSERT INTO userinfo Values(?, ?);", (ctx.author.id, 0))
        con.commit()

    cur.execute("SELECT * FROM userinfo WHERE id == ?;", (ctx.author.id, ))
    userinfo = cur.fetchone()

    cur.execute("UPDATE userinfo SET money = ? WHERE id == ?;", (userinfo[1] + 10000, ctx.author.id))
    con.commit()
    con.close()

    return await ctx.reply(f"> **<@{ctx.author.id}>님 꽁머니 10,000원이 지급되었습니다!**")  




try:
    bot.run(token)
except:
    pass
