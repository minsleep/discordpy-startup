# python pkmn.py で起動

import discord
import csv
import pprint
import math

TOKEN = 'NzczODU5NDUzODE1NjE5NjE0.X6PWxw.jeYD_17Pe631hkR9EXNSOakUWEM'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('login success')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    filepath = str(message.author.id) + '.csv'

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == '!view':
        await message.channel.send(str(message.author) + ' の厳選回数表')
        with open(filepath, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                await message.channel.send(row)

    if message.content == '!quit':
        if 'GM' in [users_role.name for users_role in message.author.roles]:
            # await message.channel.send('quit')
            await client.logout()
        else:
            await message.channel.send('GM COMMAND')

    pkmn = ''

    if message.content == '/aku':
        pkmn = 'アクジキング'
    if message.content == '/agu':
        pkmn = 'アグノム'
    if message.content == '/ibe':
        pkmn = 'イベルタル'
    if message.content == '/utu':
        pkmn = 'ウツロイド'
    if message.content == '/emr':
        pkmn = 'エムリット'
    if message.content == '/ent':
        pkmn = 'エンテイ'
    if message.content == '/kai':
        pkmn = 'カイオーガ'
    if message.content == '/kkk':
        pkmn = 'カプ・コケコ'
    if message.content == '/ttf':
        pkmn = 'カプ・テテフ'
    if message.content == '/brr':
        pkmn = 'カプ・ブルル'
    if message.content == '/rhr':
        pkmn = 'カプ・レヒレ'
    if message.content == '/kam':
        pkmn = 'カミツルギ'
    if message.content == '/kyu':
        pkmn = 'キュレム'
    if message.content == '/gir':
        pkmn = 'ギラティナ'
    if message.content == '/gra':
        pkmn = 'グラードン'
    if message.content == '/kre':
        pkmn = 'クレセリア'
    if message.content == '/san':
        pkmn = 'サンダー'
    if message.content == '/jig':
        pkmn = 'ジガルデ'
    if message.content == '/zgd':
        pkmn = 'ズガドーン'
    if message.content == '/sui':
        pkmn = 'スイクン'
    if message.content == '/zek':
        pkmn = 'ゼクロム'
    if message.content == '/zer':
        pkmn = 'ゼルネアス'
    if message.content == '/sol':
        pkmn = 'ソルガレオ'
    if message.content == '/tnd':
        pkmn = 'ツンデツンデ'
    if message.content == '/dia':
        pkmn = 'ディアルガ'
    if message.content == '/tek':
        pkmn = 'テッカグヤ'
    if message.content == '/den':
        pkmn = 'デンジュモク'
    if message.content == '/trn':
        pkmn = 'トルネロス'
    if message.content == '/nec':
        pkmn = 'ネクロズマ'
    if message.content == '/par':
        pkmn = 'パルキア'
    if message.content == '/hid':
        pkmn = 'ヒードラン'
    if message.content == '/fai':
        pkmn = 'ファイヤー'
    if message.content == '/fer':
        pkmn = 'フェローチェ'
    if message.content == '/frz':
        pkmn = 'フリーザー'
    if message.content == '/hou':
        pkmn = 'ホウオウ'
    if message.content == '/vlt':
        pkmn = 'ボルトロス'
    if message.content == '/mas':
        pkmn = 'マッシブーン'
    if message.content == '/myu':
        pkmn = 'ミュウツー'
    if message.content == '/yuk':
        pkmn = 'ユクシー'
    if message.content == '/rai':
        pkmn = 'ライコウ'
    if message.content == '/tia':
        pkmn = 'ラティアス'
    if message.content == '/tio':
        pkmn = 'ラティオス'
    if message.content == '/rnd':
        pkmn = 'ランドロス'
    if message.content == '/rug':
        pkmn = 'ルギア'
    if message.content == '/lun':
        pkmn = 'ルナアーラ'
    if message.content == '/res':
        pkmn = 'レシラム'
    if message.content == '/rek':
        pkmn = 'レックウザ'

    if message.content.startswith('/') and pkmn != '':
        flag = 0
        with open(filepath, 'r', newline='') as f:
            reader = csv.reader(f)
            l = [row for row in reader]
            for a in range(len(l)):
                if l[a][0] == pkmn:
                    l[a][1] = int(l[a][1]) + 1
                    e = (1.0 - (0.99 ** float(l[a][1]))) * 100.0
                    e = round(e,1)
                    await message.channel.send(str(message.author) + ' の ' + pkmn + ' の厳選回数が1増加。現在の厳選回数：' + str(l[a][1]) + '  色確率 ' + str(e) + ' %')
                    flag = 1
        if flag == 1:
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(l)
        if flag == 0:
            with open(filepath, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([pkmn,'1'])
                await message.channel.send(str(message.author) + ' の ' + pkmn + ' の厳選回数が1増加。現在の厳選回数：1  色確率 1.0 %')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)