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

# with open('data/pilot79.txt', 'r') as f:
#     pilot79s = f.readlines()

# with open('data/winmax.txt', 'r') as f:
#     winmaxs = f.readlines()

# with open('data/vip88.txt', 'r') as f:
#     vip88s = f.readlines()

# with open('data/may68.txt', 'r') as f:
#     may68s = f.readlines()

text = """### AUTOFILL PROFILES ###,,,,,,
Profile ID,Name,Site,Hotkey,,,
### AUTOFILL RULES ###,,,,,,
Rule ID,Type,Name,Value,Site,Mode,Profile
r24,0,"^userNumber$","{lottery}","92lottery.club/",1,
r11,1,"\[data-v-c16e655a\] > div > input\[data-v-b0ac9d23\]","GiaMinh123","92lottery.club/",1,
r12,1,"\[data-v-93816af6\] > div > input\[data-v-b0ac9d23\]","GiaMinh123","92lottery.club/",1,
r13,0,"^userNumber$","{vn168}","vn168-1.com/",1,
r14,1,"\[data-v-ba1985c0\] > div > input\[data-v-2c10910c\]","GiaMinh123","vn168-1.com/",1,
r15,1,"\[data-v-b5d6270a\] > div > input\[data-v-2c10910c\]","GiaMinh123","vn168-1.com/",1,
r25,0,"^userNumber$","{vesovn}","vesovn.cc/",1,
r16,1,"\[data-v-a761d0b2\] > div > input\[data-v-934f92c4\]","GiaMinh123","vesovn.cc/",1,
r17,1,"\[data-v-584ff9a2\] > div > input\[data-v-934f92c4\]","GiaMinh123","vesovn.cc/",1,
r19,0,"^userNumber$","{vn82}","82vn.com/",1,
r18,1,"\[data-v-b677e826\] > div > input\[data-v-34ec8998\]","GiaMinh123","82vn.com/",1,
r20,1,"\[data-v-c0d4b9dc\] > div > input\[data-v-34ec8998\]","GiaMinh123","82vn.com/",1,
r22,0,"^userNumber$","{club66}","66club.com/",1,
r21,1,"\[data-v-ce756f6e\] > div > input\[data-v-3059f33c\]","GiaMinh123","66club.com/",1,
r23,1,"\[data-v-ebe6b156\] > div > input\[data-v-3059f33c\]","GiaMinh123","66club.com/",1,
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
sound,0,,,,,
vars,1,,,,,
voice,0,1,,,,"""

workbook = openpyxl.load_workbook('data/autofill.xlsx')
sheet = workbook.active

for i in range(1, 301):
    cell = 'B' + str(i+1)
    formatted_text = text.format(
        lottery=lotterys[i-1].strip(),
        vn168=vn168s[i-1].strip(),
        vn82=vn82s[i-1].strip(),
        vesovn=vesovns[i-1].strip(),
        club66=club66s[i-1].strip(),
        # pilot79=pilot79s[i-1].strip(),
        # winmax=winmaxs[i-1].strip(),
        # vip88=vip88s[i-1].strip(),
        # may68=may68s[i-1].strip()
    )
    sheet[cell] = formatted_text

workbook.save('data/autofill.xlsx')