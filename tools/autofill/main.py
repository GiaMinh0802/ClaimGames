import openpyxl

with open('data/lottery.txt', 'r') as f:
    lotterys = f.readlines()

with open('data/vn168.txt', 'r') as f:
    vn168s = f.readlines()

with open('data/vn82.txt', 'r') as f:
    vn82s = f.readlines()

with open('data/vesovn.txt', 'r') as f:
    vesovns = f.readlines()

with open('data/club66.txt', 'r') as f:
    club66s = f.readlines()

with open('data/pilot79.txt', 'r') as f:
    pilot79s = f.readlines()

with open('data/winmax.txt', 'r') as f:
    winmaxs = f.readlines()

with open('data/vip88.txt', 'r') as f:
    vip88s = f.readlines()

with open('data/may68.txt', 'r') as f:
    may68s = f.readlines()

text = """### AUTOFILL PROFILES ###,,,,,,
Profile ID,Name,Site,Hotkey,,,
### AUTOFILL RULES ###,,,,,,
Rule ID,Type,Name,Value,Site,Mode,Profile
r1,0,"^Điện thoại$","{lottery}","92lottery.com/",1,
r2,0,"^Mật khẩu$","GiaMinh123","92lottery.com/",1,
r7,0,"^userNumber$","{vn168}","vn168-1.com/",1,
r25,1,"\[data-v-ba1985c0\] > div > input\[data-v-34ec8998\]","GiaMinh123","vn168-1.com/",1,
r26,1,"\[data-v-b5d6270a\] > div > input\[data-v-34ec8998\]","GiaMinh123","vn168-1.com/",1,
r10,0,"^Tên đăng nhập hoặc SĐT$","{vn82}","82vn.com/",1,
r11,1,"^Mật khẩu$","GiaMinh123","82vn.com/",1,
r12,0,"^userNumber$","{vesovn}","vesovn.cc/",1,
r27,1,"\[data-v-b677e826\] > div > input\[data-v-34ec8998\]","GiaMinh123","vesovn.cc/",1,
r28,1,"\[data-v-c0d4b9dc\] > div > input\[data-v-34ec8998\]","GiaMinh123","vesovn.cc/",1,
r15,0,"^Tên đăng nhập hoặc SĐT$","{club66}","66club.com/",1,
r16,1,"^Mật khẩu$","GiaMinh123","66club.com/",1,
r17,0,"^username$","{pilot79}","pilot79.com/login",1,
r18,1,"^password$","GiaMinh123","pilot79.com/login",1,
r19,0,"^Điện thoại$","{winmax}","winmax68.club/login",1,
r20,1,"^Mật khẩu$","GiaMinh123","winmax68.club/login",1,
r21,0,"^Điện thoại$","{vip88}","88vip.live/login",1,
r22,1,"^Mật khẩu$","GiaMinh123","88vip.live/login",1,
r23,0,"^Tên đăng nhập hoặc SĐT$","{may68}","may68.club/login",1,
r24,1,"^Mật khẩu$","GiaMinh123","may68.club/login",1,
### AUTOFILL OPTIONS ###,,,,,,
advanced,"[]",,,,,
exceptions,"[]",,,,,
textclips,"[]",,,,,
variables,"[]",,,,,
activecat,1,,,,,
attributesoff,0,,,,,
autoimport,0,,,,,
backup,0,30,,,,
badge,1,,,,,
closeinfobar,1,1,,,,
debug,0,,,,,
delay,0,0.5,,,,
filtercats,0,,,,,
fluid,1,,,,,
hidebackup,0,,,,,
manual,0,,,,,
mask,1,,,,,
menu,1,,,,,
overwrite,1,,,,,
sitefilters,1,,,,,
skiphidden,0,,,,,
sound,1,,,,,
vars,1,,,,,
voice,0,1,,,,"""

workbook = openpyxl.load_workbook('data/autofill.xlsx')
sheet = workbook.active

for i in range(1, 201):
    cell = 'B' + str(i+1)
    formatted_text = text.format(
        lottery=lotterys[i-1].strip(),
        vn168=vn168s[i-1].strip(),
        vn82=vn82s[i-1].strip(),
        vesovn=vesovns[i-1].strip(),
        club66=club66s[i-1].strip(),
        pilot79=pilot79s[i-1].strip(),
        winmax=winmaxs[i-1].strip(),
        vip88=vip88s[i-1].strip(),
        may68=may68s[i-1].strip()
    )
    sheet[cell] = formatted_text

workbook.save('data/autofill.xlsx')