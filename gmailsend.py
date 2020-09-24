# -*- coding: utf-8 -*-

import smtplib, ssl
from email.mime.text import MIMEText

# 以下にGmailの設定を書き込む
gmail_account = "xxxxxxxx@gmail.com"
gmail_password = ""

# メールの送信先
mail_to = input("""送信先アドレスを入力してください
>>> """)
#本文の内容を個別に変更
sannkasha = str(input("""参加者の苗字を入力してください
>>> """))
tsuki = int(input("""実験を実施する月を入力してください
>>> """))
hiniti = int(input("""実験を実施する日にちを入力してください
>>> """))
youbi = str(input("""実験を実施する曜日を入力してください
>>> """))
jikann = int(input("""実験を実施する時間を入力してください
>>> """))
hunn = int(input("""実験を実施する分を入力してください
>>> """))

# メールデータ(MIME)の作成
subject = "xxゼミの実験参加のお願い"
body ="""はじめまして、xxゼミx年のxxxxです。
今回は実験参加の確認のためにメールをさせていただきました。
{}さんの実験が以下の日程に決まりましたので確認をお願いします。

[日程] {}月{}日({}曜日)
[時間] {}時{}分
[場所] xxxxx教室

実験にかかる時間は45から60分を想定しております。
ご都合が合わないようなら、無理に参加していただかなくても大丈夫です。
実験に参加できる、できないに関わらず返信をしていただけると幸いです。
また、実験に参加していただいた方には、QUOカード300円分を差し上げます。
ただし、この実験への参加は、xxxxxの平常点には影響しませんのでご了承ください。

お忙しいところ恐れ入りますが、実験へのご協力をお願いいたします。

------------------------------------------------
xx大学 xxxxx部 xx学科
xxxx (xxxx)
Mail:xxxxxxxx@xxxxx.ac.jp
------------------------------------------------""".format(sannkasha,tsuki,hiniti,youbi,jikann,hunn)

msg = MIMEText(body,"plain")#maltipart/alternative
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account

# Gmailに接続
server = smtplib.SMTP_SSL("smtp.gmail.com",465,
                         context=ssl.create_default_context())
server.login(gmail_account,gmail_password)
server.send_message(msg) #メールの送信
print("success")
