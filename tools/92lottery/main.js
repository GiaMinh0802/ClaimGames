const TU = require('./modules.js');

function yt() {
    return "xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx".replace(/[xy]/g, function (e) {
        var A = Math.random() * 16 | 0
            , n = e === "x" ? A : A & 3 | 8;
        return n.toString(16)
    })
}

function St(e) {
    return TU.exports.MD5(e).toString().toUpperCase().slice(0, 32);
}

function Redpage(giftCode) {
    let data = {
        language: "",
        random: ""
    }

    data.language = 2
    data.random = yt()
    data.giftCode = giftCode

    const i = JSON.parse(JSON.stringify(data))
        , c = Object.keys(i);
    c.sort()
    const m = {}
        , p = ["signature", "track", "xosoBettingData"];
    c.forEach(h => {
        i[h] !== null && i[h] !== "" && !p.includes(h) && (m[h] = i[h] === 0 ? 0 : i[h])
    })
    data.signature = St(JSON.stringify(m))
    data.timestamp = Math.floor(Date.now() / 1e3)
    return data
}

function getSignature(payload) {
    payload.random = yt()
    const i = JSON.parse(JSON.stringify(payload))
        , c = Object.keys(i);
    c.sort()
    const m = {}
        , p = ["signature", "track", "xosoBettingData"];
    c.forEach(h => {
        i[h] !== null && i[h] !== "" && !p.includes(h) && (m[h] = i[h] === 0 ? 0 : i[h])
    })
    payload.signature = St(JSON.stringify(m))
    return [payload.signature, payload.random]
}

function Token(phone) {
    let data = {
        language: "",
        random: ""
    }
    data.language = 0
    data.logintype = "mobile"
    data.phonetype = 0
    data.pwd = "GiaMinh123"
    data.random = yt()
    data.username = "84" + phone

    const i = JSON.parse(JSON.stringify(data))
        , c = Object.keys(i);
    c.sort()
    const m = {}
        , p = ["signature", "track", "xosoBettingData"];
    c.forEach(h=>{
        i[h] !== null && i[h] !== "" && !p.includes(h) && (m[h] = i[h] === 0 ? 0 : i[h])
    })
    data.signature = St(JSON.stringify(m))
    data.timestamp = Math.floor(Date.now() / 1e3)

    return data
}

function listToken() {
    const fs = require('fs');

    fs.readFile('data/tk.txt', 'utf8', (err, data) => {
    const lines = data.split('\n');
    for (const line of lines) {
        const content = JSON.stringify(Token(line.replace("\r", "")));
        console.log(content)
    }
    });
}