import pygame as pg, sys, random as rm, time, math, iroiro as ir, pickle, pg_custom as m
pg.init()
"""
with open("coin.pickle", mode="wb") as l:
    pickle.dump(0, l)
with open("所持自機.pickle", mode="wb") as l:
    pickle.dump(["なし"], l)
with open("種類.pickle", mode="wb") as l:
    pickle.dump("なし", l)
"""
apg = pg.image.load("アプリ自機.png")
pg.display.set_icon(apg)
screen = pg.display.set_mode((1545, 810))
myrect = pg.Rect(705, 700, 75, 75)
hoshi = pg.image.load("星.png")
hoshi = pg.transform.scale(hoshi, (30, 60))
hosi = pg.image.load("star.png")
kaifuku = pg.image.load("回復.png")
rainbow = pg.image.load("虹自機.png")
rainbow2 = pg.image.load("虹自機2.png")
bk = pg.image.load("爆発.png")
ufo = pg.image.load("UFO.png")
ufob = pg.image.load("UFOB.png")
ufoc = pg.image.load("UFOC.png")
ufod = pg.image.load("UFOD.png")
tamab = pg.image.load("弾2.png")
tamac = pg.image.load("弾3.png")
tamad = pg.image.load("弾4.png")
TMr = pg.image.load("虹弾.png")
shcart = pg.transform.scale(pg.image.load("ショッピングカート.png"), (50, 30))
shirekae = pg.transform.scale(pg.image.load("入れ替え.png"), (50, 30))
tmks = pg.image.load("弾消し.png")
sa = pg.image.load("00.png")
sb = pg.image.load("01.png")
sc = pg.image.load("02.png")
sd = pg.image.load("03.png")
se = pg.image.load("04.png")
sf = pg.image.load("05.png")
sg = pg.image.load("06.png")
sh = pg.image.load("07.png")
si = pg.image.load("08.png")
sj = pg.image.load("09.png")
sk = pg.image.load("10.png")
sl = pg.image.load("点.png")
sm = pg.image.load("てんてん.png")
sn = pg.image.load("H.png")
so = pg.image.load("P.png")
sp = pg.image.load("残.png")
sq = pg.image.load("機.png")
sr = pg.image.load("score0.png")
ss = pg.image.load("score1.png")
st100 = pg.image.load("score2.png")
su = pg.image.load("score3.png")
sv = pg.image.load("score4.png")
sw = pg.image.load("i.png")
sz = pg.image.load("g.png")
s1 = pg.image.load("x.png")
s2 = pg.image.load("y.png")
st1 = pg.image.load("story0.png")
st2 = pg.image.load("story1.png")
st1 = pg.transform.scale(st1, (200, 200))
st2 = pg.transform.scale(st2, (200, 200))
hosi = pg.transform.scale(hosi, (10, 10))
kaifuku = pg.transform.scale(kaifuku, (60, 60))
rainbow = pg.transform.scale(rainbow, (75, 75))
rainbow2 = pg.transform.scale(rainbow2, (75, 75))
bk = pg.transform.scale(bk, (60, 60))
ufo = pg.transform.scale(ufo, (60, 50))
ufob = pg.transform.scale(ufob, (60, 50))
ufoc = pg.transform.scale(ufoc, (60, 50))
ufod = pg.transform.scale(ufod, (60, 50))
TMr = pg.transform.scale(TMr, (30, 30))
TTM = pg.transform.scale(pg.image.load("なし弾.png"), (20, 20))
tamab = pg.transform.scale(tamab, (30, 30))
tamac = pg.transform.scale(tamac, (30, 30))
tamad = pg.transform.scale(tamad, (30, 30))
tmks = pg.transform.scale(tmks, (60, 47))
sa = pg.transform.scale(sa, (26, 30))
sb = pg.transform.scale(sb, (26, 30))
sc = pg.transform.scale(sc, (26, 30))
sd = pg.transform.scale(sd, (26, 30))
se = pg.transform.scale(se, (26, 30))
sf = pg.transform.scale(sf, (26, 30))
sg = pg.transform.scale(sg, (26, 30))
sh = pg.transform.scale(sh, (26, 30))
si = pg.transform.scale(si, (26, 30))
sj = pg.transform.scale(sj, (26, 30))
sk = pg.transform.scale(sk, (26, 30))
sl = pg.transform.scale(sl, (26, 30))
sm = pg.transform.scale(sm, (26, 30))
sn = pg.transform.scale(sn, (26, 30))
so = pg.transform.scale(so, (26, 30))
sp = pg.transform.scale(sp, (26, 30))
sq = pg.transform.scale(sq, (26, 30))
sr = pg.transform.scale(sr, (26, 30))
ss = pg.transform.scale(ss, (26, 30))
st100 = pg.transform.scale(st100, (26, 30))
su = pg.transform.scale(su, (26, 30))
sv = pg.transform.scale(sv, (26, 30))
sw = pg.transform.scale(sw, (26, 30))
sz = pg.transform.scale(sz, (26, 30))
s1 = pg.transform.scale(s1, (26, 30))
s2 = pg.transform.scale(s2, (26, 30))
srect = pg.Rect(0, 0, 26, 30)
pg.display.set_caption("space shooting")
ufosa = pg.transform.scale(ufo, (190, 190))
ufosb = pg.transform.scale(ufob, (190, 190))
ufosc = pg.transform.scale(ufoc, (190, 190))
ufosd = pg.transform.scale(ufod, (190, 190))
ngrbosi = pg.transform.scale(hoshi, (95, 190))
dinamite = pg.transform.scale(tmks, (190, 149))
kyuukyuu = pg.transform.scale(kaifuku, (190, 190))
coin = pg.image.load("coin.png")
coin = pg.transform.scale(coin, (50, 50))
shopp = pg.transform.scale(pg.image.load("shop.png"), (132, 54))
kaberect = pg.image.load("kabe.png")
kaberect = pg.transform.scale(kaberect, (125, 30))
f3_p = False
task = 200
def fin():
    key = pg.key.get_pressed()
    if key[pg.K_F4]:
        pg.quit()
        sys.exit()
def set(color):
    with open('種類.pickle', mode='wb') as l:
        pickle.dump(color, l)
def story(key):
    global f3_p, screen
    m.mus.start("BGM (1).wav", -1)
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
    moji = ["ここは2200年の日本。(左右キーで進む/戻る)", "「ワ―!」「逃げろー!」「UFOの襲来だー!!」", "UFOが攻めてきてパニックの中,", "1人の人間が立ち上がった。", "このロケットを操縦して，UFO達を追撃しよう!", "操作方法...移動 矢印キー", "射撃 スペースキー", "(ロケットを手に入れている場合)壁を作る Vキー", "アイテム...流れ星 一定時間無敵，弾速UP", "ダイナマイト 爆発し，その時にある敵の弾をなくす", "救急箱 残機を1増やす", "↑のUFO...弾速 ★☆☆☆☆ 速さ ★☆☆☆☆ 弾威力 ★☆☆☆☆", "↑のUFO...弾速 ★★☆☆☆ 速さ ★★★☆☆ 弾威力 ★★☆☆☆", "↑のUFO...弾速 ★★★☆☆ 速さ ★★★☆☆ 弾威力 ★★★☆☆", "↑のUFO...弾速 ★★★★☆ 速さ ★★★★☆ 弾威力 ★★☆☆☆", "では,,,スタート!"]
    if key:
        moji = ["移動 矢印キー", "射撃 スペースキー", "start!"]
    b = 0
    font = pg.font.Font("dot.ttf", 30)
    flag = True
    while True:
        screen.fill("darkblue")
        pg.draw.rect(screen, pg.Color("wH i tE"), pg.Rect(662.5, 100, 210, 210))
        pg.draw.rect(screen, pg.Color("d Ar k B l uE"), pg.Rect(672.5, 110, 190, 190))
        text = font.render(moji[b], True, pg.Color("white"))
        screen.blit(text, (500, 500))
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            if flag:
                flag = False
                b += 1
                if b >= len(moji):
                    b = len(moji)
        elif key[pg.K_LEFT]:
            if flag:
                flag = False
                b -= 1
                if b <= 0:
                    b = 0
        else:
            flag = True
        if b >= len(moji):
            m.mus.stop()
            return
        if b == 7:
            screen.blit(ngrbosi, pg.Rect(720, 110, 200, 200))
        elif b == 8:
            screen.blit(dinamite, pg.Rect(672.5, 130, 200, 200))
        elif b == 9:
            screen.blit(kyuukyuu, pg.Rect(672.5, 110, 200, 200))
        elif b == 10:
            screen.blit(ufosa, pg.Rect(672.5, 110, 200, 200))
        elif b == 11:
            screen.blit(ufosb, pg.Rect(672.5, 110, 200, 200))
        elif b == 12:
            screen.blit(ufosc, pg.Rect(672.5, 110, 200, 200))
        elif b == 13:
            screen.blit(ufosd, pg.Rect(672.5, 110, 200, 200))
        elif b >= 4:
            screen.blit(st2, pg.Rect(667.5, 105, 200, 200))
        else:
            screen.blit(st1, pg.Rect(667.5, 105, 200, 200))
        fin()
        if key[pg.K_F3]:
            if f3_p:
                screen = pg.display.set_mode((1545, 810))
                f3_p = False
            else:
                screen = pg.display.set_mode((1545, 810), pg.FULLSCREEN)
                f3_p = True
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
aiueo = 0
def hsreset():
    with open('highscore.pickle', mode='wb') as l:
        pickle.dump("1000", l)
def game(gamecrear_c__gameover_o):
    global gamecrear, gameover, re, rect, rect2, screen, mx, my, gz, push, f3_p, task
    m.mus.stop()
    re = pg.image.load("return!.png")
    re = pg.transform.scale(re, (100, 80))
    rect = pg.Rect(367.5, 0, 0, 0)
    rect2 = pg.Rect(700, 500, 100, 80)
    push = pg.mouse.get_pressed()
    gz = 0
    mx = 0
    my = 0
    gameover = pg.image.load("gameover.png")
    gameover = pg.transform.scale(gameover, (810, 810))
    gamecrear = pg.image.load("クリア.png")
    gamecrear = pg.transform.scale(gamecrear, (810, 810))
    if gamecrear_c__gameover_o == "c":
        pg.mixer.Sound("GAMECREAR.wav").play()
    else:
        pg.mixer.Sound("GAMEOVER.wav").play()
    m.mus.start("待機.wav", -1)
    while True:
        if gamecrear_c__gameover_o == "c":
            screen.fill("ORANGE")
            screen.blit(gamecrear, rect)
            suuji(1250, 30, (str(int(hour))+":"+str(int(minute))+":"+str(int(second))))
        else:
            screen.fill("#000250")
            screen.blit(gameover, rect)
            suuji(30, 30, (str(task)+"/"+str(taositakazu)))
            suuji(1250, 30, (str(int(hour))+":"+str(int(minute))+":"+str(int(second))))
            with open("highscore.pickle", mode="rb") as l:
                f = pickle.load(l)
                suuji(30, 80, ("HIGH SCORE:"+ str(f[0])+":"+str(f[1])+str(f[2])+":"+str(f[3])))
        push = pg.mouse.get_pressed()
        gz = screen.blit(re, rect2)
        (mx, my) = pg.mouse.get_pos()
        if rect2.collidepoint(mx, my):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            if push[0]:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                m.mus.stop()
                m.mus.start("shootingBGM.wav", -1)
                return
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        key = pg.key.get_pressed()
        fin()
        if key[pg.K_F3]:
            if f3_p:
                screen = pg.display.set_mode((1545, 810))
                f3_p = False
            else:
                screen = pg.display.set_mode((1545, 810), pg.FULLSCREEN)
                f3_p = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
def suuji(x, y, suuji):
    global screen, srect
    srect.x = x
    srect.y = y
    for i in suuji:
        if i == "0":
            screen.blit(sa, srect)
        elif i == "1":
            screen.blit(sb, srect)
        elif i == "2":
            screen.blit(sc, srect)
        elif i == "3":
            screen.blit(sd, srect)
        elif i == "4":
            screen.blit(se, srect)
        elif i == "5":
            screen.blit(sf, srect)
        elif i == "6":
            screen.blit(sg, srect)
        elif i == "7":
            screen.blit(sh, srect)
        elif i == "8":
            screen.blit(si, srect)
        elif i == "9":
            screen.blit(sj, srect)
        elif i == "/":
            screen.blit(sk, srect)
        elif i == ".":
            screen.blit(sl, srect)
        elif i == ":":
            screen.blit(sm, srect)
        elif i == "H":
            screen.blit(sn, srect)
        elif i == "P":
            screen.blit(so, srect)
        elif i == "残":
            screen.blit(sp, srect)
        elif i == "機":
            screen.blit(sq, srect)
        elif i == "S":
            screen.blit(sr, srect)
        elif i == "C":
            screen.blit(ss, srect)
        elif i == "O":
            screen.blit(st100, srect)
        elif i == "R":
            screen.blit(su, srect)
        elif i == "E":
            screen.blit(sv, srect)
        elif i == "I":
            screen.blit(sw, srect)
        elif i == "G":
            screen.blit(sz, srect)
        elif i == "x":
            screen.blit(s1, srect)
        elif i == "y":
            screen.blit(s2, srect)
        srect.x += 26
def reset():
    global kabe, val, tmk, kf, hour, minute, second, jikan, jikan2, bkhrect, zanki, mtk, starb, star, myrect, cooltime, tekitama, tama, tamax, tamay, teki, tekix, tekiy, tekiugoku, b, tmx, tmy, random, hindo, tx, tekiflag, bkx, bky, bkh, taositakazu, tekitamash, tekish, f5, f5flag
    f5flag = True
    val = 100
    kabe = []
    f5 = False
    hour = 0
    minute = 0
    second = 0
    cooltime = 0
    tekitamash = []
    tekish = []
    mtk = 0
    tama = []
    tamay = []
    tamax = []
    teki = []
    tekix = []
    tekiy = []
    tekiugoku = []
    b = 0
    tmx = 0
    tmy = 0
    random = 0
    hindo = 150
    pg.mixer.Sound("エイリアン.wav").play()
    tx = 0
    tekiflag = []
    bkx = []
    bky = []
    bkh = []
    taositakazu = 0
    tekitama = []
    myrect.x = 1545/2-75/2
    star = []
    starb = []
    zanki = 3
    bkhrect = ""
    jikan = time.time()
    jikan = round(jikan)
    jikan2 = 0
    kf = pg.Rect(rm.randint(0, 1545), rm.randint(-10000, -500), 60, 60)
    tmk = pg.Rect(rm.randint(0, 1545), rm.randint(-10000, -500), 60, 47)
def shop():
    global jikan, f3_p, screen
    m.mus.start("BGM (1).wav", -1)
    aiueo = jikan2-jikan
    wa = (100, 100)
    wb = (20, 20)
    shopaa = pg.transform.scale(pg.image.load("赤自機.png"), wa)
    shopab = pg.transform.scale(pg.image.load("赤弾.png"), wb)
    shopba = pg.transform.scale(pg.image.load("青自機.png"), wa)
    shopbb = pg.transform.scale(pg.image.load("青弾.png"), wb)
    shopca = pg.transform.scale(pg.image.load("緑自機.png"), wa)
    shopcb = pg.transform.scale(pg.image.load("緑弾.png"), wb)
    shopda = pg.transform.scale(pg.image.load("桃自機.png"), wa)
    shopdb = pg.transform.scale(pg.image.load("桃弾.png"), wb)
    shopea = pg.transform.scale(pg.image.load("橙自機.png"), wa)
    shopeb = pg.transform.scale(pg.image.load("橙弾.png"), wb)
    shopfa = pg.transform.scale(pg.image.load("なし自機.png"), wa)
    shopfb = pg.transform.scale(pg.image.load("なし弾.png"), wb)
    jikirect = pg.Rect(772.5-wa[0]/2, 405-wa[0]/2, 50, 50)
    tamarect = pg.Rect(772.5-wb[0]/2, 405-wa[0]/2-10-wb[0], 50, 50)
    buttrect = pg.Rect(772.5-25, 700, 50, 30)
    re = pg.transform.scale(pg.image.load("return!.png"), (100, 80))
    rect = pg.Rect(1425, 700, 100, 80)
    colist = ["なし", "赤", "青", "緑", "桃", "橙"]
    nedan = [0, 1000, 2000, 4000, 10000, 50000]
    blist = [shopfa, shopaa, shopba, shopca, shopda, shopea]
    blist2 = [shopfb, shopab, shopbb, shopcb, shopdb, shopeb]
    page = 0
    flag = False
    while True:
        screen.fill("c Y An")
        screen.blit(coin, pg.Rect(50, 50, 50, 50))
        with open("coin.pickle", mode="rb") as l:
            coi = pickle.load(l)
        suuji(90, 60, ":"+str(coi))
        screen.blit(re, rect)
        (mx, my) = pg.mouse.get_pos()
        if rect.collidepoint(mx, my):
            press = pg.mouse.get_pressed()
            if press[0]:
                global myv, TM, jiki
                with open("種類.pickle", mode="rb") as l:
                    f = pickle.load(l)
                    myv = pg.image.load(f+"自機.png")
                    TM = pg.image.load(f+"弾.png")
                    jiki = colist.index(f)
                myv = pg.transform.scale(myv, (75, 75))
                TM = pg.transform.scale(TM, (30, 30))
                jikan = round(time.time()-aiueo)
                m.mus.stop()
                return
            cursor = False
        else:
            cursor = True
        pg.draw.rect(screen, pg.Color("grey30"), pg.Rect(300, 200, 945, 410))
        pg.draw.rect(screen, pg.Color("grey80"), pg.Rect(310, 210, 925, 390))
        screen.blit(blist[page], jikirect)
        screen.blit(blist2[page], tamarect)
        (mx, my) = pg.mouse.get_pos()
        with open("所持自機.pickle", mode="rb") as l:
            x = pickle.load(l)
        fa = True
        for i in x:
            with open("所持自機.pickle", mode="rb") as l:
                if pickle.load(l).count(colist[page]) != 0:
                    fa = False
            if i == colist[page]:
                if colist[page] == i:
                    with open("種類.pickle", mode="rb") as l:
                        f = pickle.load(l)
                    if f != colist[page]:
                        screen.blit(shirekae, buttrect)
                        if buttrect.collidepoint(mx, my):
                            cursor = False
                            if pg.mouse.get_pressed()[0]:
                                with open("種類.pickle", mode="wb") as l:
                                    pickle.dump(colist[page], l)
            else:
                screen.blit(coin, pg.Rect(250+945/2, 620, 50, 50))
                suuji(300+945/2, 620, "x"+str(nedan[page]))
                if fa:
                    screen.blit(shcart, buttrect)
                    if buttrect.collidepoint(mx, my):
                        cursor = False
                        if pg.mouse.get_pressed()[0] and coi >= nedan[page]:
                            with open("所持自機.pickle", mode="rb") as l:
                                f = pickle.load(l)
                            if f.count(colist[page]) == 0:
                                with open("所持自機.pickle", mode="wb") as l:
                                    f += colist[page]
                                    pickle.dump(f, l)
                                with open("coin.pickle", mode="wb") as l:
                                    pickle.dump(coi-nedan[page], l)
        if cursor:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            if flag:
                page += 1
                if page >= 6:
                    page -= 1
                flag = False
        elif key[pg.K_LEFT]:
            if flag:
                page -= 1
                if page <= -1:
                    page += 1
                flag = False
        else:
            flag = True
        fin()
        if key[pg.K_F3]:
            if f3_p:
                screen = pg.display.set_mode((1545, 810))
                f3_p = False
            else:
                screen = pg.display.set_mode((1545, 810), pg.FULLSCREEN)
                f3_p = True
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
story(False)
reset()
shop()
reset()
mx = 0
my = 0
gameover = pg.image.load("gameover.png")
gameover = pg.transform.scale(gameover, (810, 810))
gamecrear = pg.image.load("クリア.png")
gamecrear = pg.transform.scale(gamecrear, (810, 810))
re = pg.image.load("return!.png")
re = pg.transform.scale(re, (100, 80))
rect = pg.Rect(367.5, 0, 0, 0)
rect2 = pg.Rect(700, 500, 0, 0)
gz = ""
push = 0
tkrect = 0
hosidata = []
hosiugoku = []
for i in range(30):
    ir.listapp(hosidata, pg.Rect(rm.randint(0, 1545), rm.randint(0, 810), 10, 10), 1)
    ir.listapp(hosiugoku, rm.randint(100, 500) / 100, 1)
def TDD(bangou):#TekiDataDelete
    global teki, tekix, tekiy, tekiflag, tekiugoku, tekish
    del teki[bangou]
    del tekix[bangou]
    del tekiy[bangou]
    del tekiflag[bangou]
    del tekiugoku[bangou]
    del tekish[bangou]
aiueo = jikan
fafafa = 0
#メインループ
def main():
    m.mus.start("shootingBGM.wav", -1)
    f3_p = True
    fps = 30
    global task, jiki, screen, fafafa, kabe, val, tmk, kf, hour, minute, second, jikan, jikan2, bkhrect, zanki, mtk, starb, star, myrect, cooltime, tekitama, tama, tamax, tamay, teki, tekix, tekiy, tekiugoku, b, tmx, tmy, random, hindo, tx, tekiflag, bkx, bky, bkh, taositakazu, tekitamash, tekish, f5, f5flag
    while True:
        screen.fill("DARKBLUE")
        with open("種類.pickle", mode="rb") as l:
            f = pickle.load(l)
            jiki = ["なし", "赤", "青", "緑", "桃", "橙"].index(f)
        rl = 25/1.4
        if jiki == 2 or jiki == 4 or jiki == 5:
            rl = 14
        if jiki == 1:
            rl = 23
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        if 0 == rm.randint(0, 1500):
            star.append(pg.Rect(rm.randint(0, 1545), 0, 30, 60))
            starb.append(rm.randint(7, 10))
        if myrect.collidelist(star) != -1 and mtk <= 0:
            mtk = 1000
            pg.mixer.Sound("get.wav").play()
            pg.mixer.Sound("Dance Energetic.wav").play()
            del star[myrect.collidelist(star)]
        if not mtk <= 0:
            mtk -= 2
        if taositakazu >= task:
            with open('highscore.pickle', mode='rb') as l:
                f = pickle.load(l)
                if int(f[0]) * 3600 + (int(f[1])+int(f[2])) * 60 + int(f[3]) >= hour * 3600 + minute * 60 + second:
                    with open('highscore.pickle', mode='wb') as l:
                        if len(str(minute)) == 1:
                            pickle.dump((str(hour), "0", str(minute), str(second)), l)
                        else:
                            pickle.dump((str(hour), str(minute), str(second)), l)
            game("c")
            reset()
        (mx, my) = pg.mouse.get_pos()
        hindo -= 0.015
        hindo = int(hindo*1000)/1000
        if hindo <= 60:
            hindo = 60
        b = 0
        for i in hosidata:
            screen.blit(hosi, i)
            if mtk <= 0:
                i.y += hosiugoku[b]
            else:
                i.y += hosiugoku[b] * 2
            if i.y >= 900:
                i.y = rm.randint(-200, -10)
                i.x = rm.randint(0, 1545)
                hosiugoku[b] = rm.randint(100, 500) / 100
            b += 1
        b = 0
        for i in star:
            screen.blit(hoshi, i)
            i.y += starb[b]
            b += 1
        random = rm.randint(0, round(hindo))
        if random == 0:
            tekish.append(1)
            tx = rm.randint(0, 1)#745
            teki.append((tx * 1545, 0, 60, 50))
            tekix.append(tx * 1545)
            tekiy.append(0)
            tekiflag.append(tx + 1)
            tekiugoku.append(rm.randint(6, 10))
        else:
            random = rm.randint(0, round(hindo * 2))
            if random == 0:
                tekish.append(2)
                tx = rm.randint(0, 1)
                teki.append((tx * 1545, 0, 60, 50))
                tekix.append(tx * 1545)
                tekiy.append(0)
                tekiflag.append(tx + 1)
                tekiugoku.append(rm.randint(10, 13))
            else:
                random = rm.randint(0, round(hindo + 50 * 1.5))
                if random == 0:
                    tekish.append(3)
                    tx = rm.randint(0, 1)
                    teki.append((tx * 1545, 0, 60, 50))
                    tekix.append(tx * 1545)
                    tekiy.append(0)
                    tekiflag.append(tx + 1)
                    tekiugoku.append(rm.randint(8, 12))
                else:
                    random = rm.randint(0, round(hindo + 50 * 1.5))
                    if random == 0:
                        tekish.append(4)
                        tx = rm.randint(0, 1)
                        teki.append((tx * 1545, 0, 60, 50))
                        tekix.append(tx * 1545)
                        tekiy.append(0)
                        tekiflag.append(tx + 1)
                        tekiugoku.append(rm.randint(12, 15))
        key = pg.key.get_pressed()
        if f5flag:
            if key[pg.K_F5]:
                if f5:
                    f5 = False
                else:
                    f5 = True
        if f5:
            suuji(30, 200, "x:"+str(myrect.x))
        if ir.k.right() or ir.k.d():
            if jiki == 2 or jiki == 5:
                myrect.x += 3
            myrect.x += 7
        if ir.k.left() or ir.k.a():
            if jiki == 2 or jiki == 5:
                myrect.x -= 3
            myrect.x -= 7
        if key[pg.K_SPACE]:
            if cooltime == 0:
                cooltime = rl
                tama.append((myrect.x + 25, myrect.y - 20, 30, 30))
                tamay.append(myrect.y - 20)
                tamax.append(myrect.x + 25)
                pg.mixer.Sound("発射.wav").play()
        if mtk <= 0:
            cooltime -= 1
        else:
            cooltime -= 2
        if cooltime <= -1:
            cooltime = 0
        b = 0
        for i in teki:
            if tekish[b] == 1:
                tkrect = screen.blit(ufo, i)
            elif tekish[b] == 2:
                tkrect = screen.blit(ufob, i)
            elif tekish[b] == 3:
                tkrect = screen.blit(ufoc, i)
            elif tekish[b] == 4:
                tkrect = screen.blit(ufod, i)
            if tekiflag[b] == 1:
                if tekish[b] == 2:
                    tekiy[b] += math.sin(math.radians(tekix[b])) * 4
                tekix[b] += tekiugoku[b]
                if tekix[b] >= 1485:
                    tekiflag[b] = 2
                    tekiy[b] += 50
            else:
                if tekish[b] == 2:
                    tekiy[b] += math.sin(math.radians(tekix[b])) * 4
                tekix[b] -= tekiugoku[b]
                if tekix[b] <= 5:
                    tekiflag[b] = 1
                    tekiy[b] += 50
            teki[b] = (tekix[b], tekiy[b], 60, 50)
            if mtk <= 0:
                if myrect.colliderect(tkrect):
                    game("o")
                    reset()
            if 0 == rm.randint(0, round(hindo/2)):
                if tekish[b] == 4:
                    tekitama.append(pg.Rect(tekix[b] + 25, tekiy[b] + 20, 35, 35))
                    tekitamash.append(tekish[b])
            if 0 == rm.randint(0, round(hindo)):
                tekitamash.append(tekish[b])
                if tekish[b] == 1:
                    tekitama.append(pg.Rect(tekix[b] + 25, tekiy[b] + 20, 20, 20))
                elif tekish[b] == 2:
                    tekitama.append(pg.Rect(tekix[b] + 25, tekiy[b] + 20, 28, 28))
                elif tekish[b] == 3:
                    tekitama.append(pg.Rect(tekix[b] + 25, tekiy[b] + 20, 30, 30))
                elif tekish[b] == 4:
                    tekitama.append(pg.Rect(tekix[b] + 25, tekiy[b] + 20, 35, 35))
            b += 1
        b = 0
        for i in tekitama:
            if i.collidelist(kabe) != -1:
                del tekitamash[b], tekitama[b]
                kabe.clear()
                continue
            if not i.y >= 910:
                if tekitamash[b] == 1:
                    screen.blit(TTM, i)
                    i.y += 5
                elif tekitamash[b] == 2:
                    screen.blit(tamab, i)
                    i.y += 7
                elif tekitamash[b] == 3:
                    screen.blit(tamac, i)
                    i.y += 6
                elif tekitamash[b] == 4:
                    screen.blit(tamad, i)
                    i.y += 10
                if mtk <= 0:
                    if myrect.colliderect(i):
                        zanki -= 1
                        if tekitamash[b] == 3:
                            zanki -= 1
                        del tekitama[b]
                        del tekitamash[b]
                        pg.mixer.Sound("爆発.wav").play()
                        bkx.append(i.x)
                        bky.append(i.y)
                        bkh.append(0)
                        if zanki <= 0:
                            game("o")
                            reset()
                            break
            b += 1
        frb = 0
        b = 0
        for i in tama:
            tmx = tamax[b]
            tmy = tamay[b]
            if mtk <= 0:
                tmrect = screen.blit(TM, (tmx, tmy, 30, 30))
            else:
                tmrect = screen.blit(TMr, (tmx, tmy, 30, 30))
            tama[b] = (tamax[b], tamay[b], 30, 30)
            if mtk <= 0:
                tamay[b] -= 10
            else:
                tamay[b] -= 15
            if tamay[b] <= -20:
                del tamay[b]
                del tamax[b]
                del tama[b]
                continue
            frb = tmrect.collidelist(teki)
            if frb != -1:
                pg.mixer.Sound("爆発.wav").play()
                taositakazu += 1
                with open("coin.pickle", mode="rb") as l:
                    f = pickle.load(l)
                if jiki == 3 or jiki == 5:
                    f += tekish[frb]*2
                with open('coin.pickle', mode='wb') as l:
                    pickle.dump(f+tekish[frb], l)
                bkx.append(tmx)
                bky.append(tmy)
                bkh.append(0)
                TDD(frb)
                del tamay[b]
                del tamax[b]
                del tama[b]
                continue
            e = pg.Rect(tama[b]).collidelist(tekitama)
            if e != -1:
                if (mtk <= 0 or tekitamash[e] == 1) and jiki != 1 or jiki != 5:
                    del tamay[b]
                    del tamax[b]
                    del tama[b]
                del tekitama[e]
                del tekitamash[e]
                pg.mixer.Sound("爆発.wav").play()
                bkx.append(tmx)
                bky.append(tmy)
                bkh.append(0)
                continue
            b += 1
        if myrect.x <= 100:
            myrect.x = 100
        if myrect.x >= 1365:
            myrect.x = 1365
        if mtk <= 0:
            screen.blit(myv, myrect)
        else:
            if int(str(mtk)[0]) == 1 or int(str(mtk)[0]) == 3 or int(str(mtk)[0]) == 5:
                screen.blit(rainbow2, myrect)
            else:
                screen.blit(rainbow, myrect)
        if fafafa > 0:
            fafafa += 1
            screen.blit(kaberect, (myrect.x-31, myrect.y-40))
            kabe.clear()
            kabe.append(pg.Rect(myrect.x-31, myrect.y - 40, 125, 30))
            if fafafa > 500:
                fafafa = 0
        b = 0
        for i in bkh:
            bkhrect = screen.blit(bk, (bkx[b] - 15, bky[b] - 15, 60, 60))
            bkh[b] += 1
            if i >= 20:
                del bkh[b]
                del bkx[b]
                del bky[b]
                continue
            if bkhrect.collidelist(tekitama) != -1:
                if tekitamash[bkhrect.collidelist(tekitama)] == 1:
                    del tekitama[bkhrect.collidelist(tekitama)]
                    del tekitamash[bkhrect.collidelist(tekitama)]
            b += 1
        kf.y += 5
        screen.blit(kaifuku, kf)
        if kf.y >= 810:
            kf.x = rm.randint(0, 1545)
            kf.y = rm.randint(-10000, -500)
        if kf.colliderect(myrect):
            zanki += 1
            pg.mixer.Sound("回復!.wav").play()
            kf.x = rm.randint(0, 1545)
            kf.y = rm.randint(-10000, -500)
        tmk.y += 5
        screen.blit(tmks, tmk)
        if tmk.y >= 810:
            tmkx = rm.randint(0, 1545)
            tmk.y = rm.randint(-10000, -500)
        if tmk.colliderect(myrect):
            tekitama = []
            tekitamash = []
            for i in range(20):
                bkh.append(-20)
                bkx.append(rm.randint(0, 1545))
                bky.append(rm.randint(0, 810))
            pg.mixer.Sound("爆発.wav").play()
            tmk.x = rm.randint(0, 1545)
            tmk.y = rm.randint(-10000, -500)
        suuji(30, 30, (str(task)+"/"+str(taositakazu)))
        suuji(50, 730, ("残機:"+str(zanki)))
        with open("highscore.pickle", mode="rb") as l:
            f = pickle.load(l)
            suuji(30, 80, ("HIGH SCORE:"+ str(f[0])+":"+str(f[1])+str(f[2])+":"+str(f[3])))
        with open("coin.pickle", mode="rb") as l:
            f = pickle.load(l)
            screen.blit(coin, pg.Rect(30, 150, 50, 50))
            suuji(70, 160, ":"+str(f))
        jikan2 = time.time()
        jikan2 = round(jikan2)
        hour = ((jikan2 - jikan) / 3600) // 1
        minute = ((jikan2 - jikan) / 60) // 1
        second = ((jikan2 - jikan) - hour * 3600 - minute * 60) // 1
        suuji(1250, 30, (str(int(hour))+":"+str(int(minute))+":"+str(int(second))))
        (mx, my) = pg.mouse.get_pos()
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        couu = pg.Rect(50, 810-110-27, 132, 54)
        screen.blit(shopp, couu)
        if val >= 1000:
            if key[pg.K_v]:
                val = 0
                fafafa = 1
        fin()
        if key[pg.K_F3]:
            if f3_p:
                screen = pg.display.set_mode((1545, 810))
                f3_p = False
            else:
                screen = pg.display.set_mode((1545, 810), pg.FULLSCREEN)
                f3_p = True
        if couu.collidepoint(mx, my):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            if pg.mouse.get_pressed()[0]:
                shop()
        with open("種類.pickle", mode="rb") as l:
            f = pickle.load(l)
            jiki = ["なし", "赤", "青", "緑", "桃", "橙"].index(f)
        if jiki == 4 or jiki == 5:
            val += 1
            pg.draw.rect(screen, "white", pg.Rect(0, 780, 1545, 30))
            pg.draw.rect(screen, "red", pg.Rect(0, 780, val * 1.545, 30))
            if val > 1000:
                val = 1000
        pg.time.Clock().tick(100)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
main()
