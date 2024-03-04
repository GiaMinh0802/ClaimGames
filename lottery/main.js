const TU = require('./modules.js');

function yt() {
    return "xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx".replace(/[xy]/g, function(e) {
        var A = Math.random() * 16 | 0;
        var n = e === "x" ? A : A & 3 | 8;
        return n.toString(16);
    });
}

function St(e) {
    return TU.exports.MD5(e).toString().toUpperCase().slice(0, 32);
}

function Redpage(giftCode) {
    var data = {
        language: "",
        random: ""
    };
    
    data.language = 2;
    data.random = yt();
    data.giftCode = giftCode;
    
    var i = JSON.parse(JSON.stringify(data));
    var c = Object.keys(i);
    c.sort();
    var m = {};
    var p = ["signature", "track", "xosoBettingData"];
    for (var j = 0; j < c.length; j++) {
        var h = c[j];
        if (i[h] !== null && i[h] !== "" && p.indexOf(h) === -1) {
            m[h] = i[h] === 0 ? 0 : i[h];
        }
    }
    data.signature = St(JSON.stringify(m));
    data.timestamp = Math.floor(Date.now() / 1e3);
    return data;
}

function listRedpage(giftCode) {
    var result = "";
    for (var index = 1; index <=500; index++) {
        var content = JSON.stringify(Redpage(giftCode)) + "\n";
        result = result + content;
    }
    return result;
}

const giftCode = process.argv[2];
console.log(listRedpage(giftCode));