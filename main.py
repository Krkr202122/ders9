from flask import Flask
import random
app = Flask(__name__)
pass_length = 20
facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar."
              , "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."
              ,"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."
              , "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."
              ,"2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."
              ,"Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır."
              ,"Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor."
              ,"Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."
              ,"Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]

@app.route("/")
def hello_world():
    return f'<p>{"Merhaba, hosgeldiniz! Asagidaki linklerden birine basiniz."}</p>  <a href="/randomchoice">Rastgele bir gerçeği görüntüle!</a> <a href="/try">WIP site</a> <a href="/passwordmaker">Şifre oluşturucu</a>'

@app.route("/randomchoice")
def random_facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/try")
def deneme():
    return f'<p>{"WORK IN PROGRESS"}</p>'

@app.route("/passwordmaker")
def code():
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for j in range(pass_length):
        password += random.choice(elements)
    return f'<p>{password}</p>'

app.run(debug=True)


