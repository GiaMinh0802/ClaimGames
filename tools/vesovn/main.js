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
    const i = JSON.parse(JSON.stringify(payload))
        , c = Object.keys(i);
    c.sort()
    const m = {}
        , p = ["signature", "track", "xosoBettingData"];
    c.forEach(h => {
        i[h] !== null && i[h] !== "" && !p.includes(h) && (m[h] = i[h] === 0 ? 0 : i[h])
    })
    payload.signature = St(JSON.stringify(m))
    payload.timestamp = Math.floor(Date.now() / 1e3)
    return payload
}

module.exports = { Redpage, getSignature }