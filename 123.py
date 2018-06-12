key_data = {
    "first":"{'rid':'R_SO_4_326904','offset':'0','total':'true','limit':'20','csrf_token':''}",
    "second":"010001",
    "third":"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7",
    "forth":"0CoJUm6Qyw8W8jud"
}

import base64
# from crypto.Clpher import AES
import codecs
def aesEncrypt(text,key):
    iv = '0102030405060708'
    pad = 16-len(text)%16
    text = text + pad*chr(pad)
    encryptor = AES.new(key,2,iv)
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext
"""
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b),
    d = CryptoJS.enc.Utf8.parse("0102030405060708"),
    e = CryptoJS.enc.Utf8.parse(a),
    f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}"""
def get_params(text):
    first_param = {'rid':'R_SO_4_326904','offset':'0','total':'true','limit':'20','csrf_token':''}
    params = aesEncrypt(first_param,"0CoJUm6Qyw8W8jud").decode("utf-8")
    params = aesEncrypt(params,text)
    return params
def rsaEncrypt(pubKey,text,modulus):
    text = text[::-1]
    rs = int(codecs.encode(text.encode("utf-8"),'hex_codec'),18) ** int(pubKey,16)%int(modulus,16)
    return format(rs,'x').zfill(256)
def get_encSEcKey(text):
    pubKey = "010001"
    modulus = key_data["third"]
    encSecKey = rsaEncrypt(pubKey,text,modulus)
    return encSecKey
text = "A"*16
params = get_params(text)
encSecKey = get_encSEcKey(text)
formdata = {"params":params,"encSecKey":encSecKey}

"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        c = "";
        for (d = 0; a > d; d += 1) e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
        return c
    }
    
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b),
    d = CryptoJS.enc.Utf8.parse("0102030405060708"),
    e = CryptoJS.enc.Utf8.parse(a),
    f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}
    
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b, "", c),
    e = encryptedString(d, a)
}
    
function d(d, e, f, g) {
    var h = {},
    i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}
    
function e(a, b, d, e) {
    var f = {};
    return f.encText = c(a + e, b, d),
    f
}
window.asrsea = d,


"""

















