import requests
import base64
from Crypto.Cipher import AES
import requests
import codecs
key_data = {
    "first":"{'rid':'R_SO_4_523042176','offset':'20','total':'true','limit':'20','csrf_token':''}",
    "second":"010001",
    "third":"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7",
    "forth":"0CoJUm6Qyw8W8jud"
}
def aesEncrypt(text,key):
    iv = '0102030405060708'
    pad = 16-len(text)%16
    text = text + pad*chr(pad)
    encryptor = AES.new(key,2,iv)
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext
def get_params(text):
    first_param = "{'rid':'R_SO_4_523042176','offset':'20','total':'true','limit':'20','csrf_token':''}"
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
text = "sdwrf54654132sdf"
params = get_params(text)
encSecKey = get_encSEcKey(text)
formdata = {"params":params.decode("utf-8"),"encSecKey":encSecKey}
print(formdata)
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_523042176?csrf_token="
test_data = {
"params":"vqlD+YTom3ecQt3uNB3MwOQ71SHpQv1eWFkyj5wKLiXCzOaATAt/fS3vPIp63LJafVqUqBaM23qxgsu0OAmwWhkPFeV4mrsEJ8Ieg2vSGXhtJi6tZfZaq3ZgosCACMK7a8w9SVCcQ2CGl17gagBz2K7i03rGN1571ci4M1r4IKpZSCbmqUxzUuY7JCZvEGcT",
"encSecKey":"cf94855d41c421178a1064c56ca3f41661dd22a551c0b920f881ba17c051639f78b310b47175969ff270e393c6b2ddd424d586c7b60a336269a085d39e3dd3db85dd7d2b2ca45af4692e0e97ca9d7146b7b78c5c942beb62e3b31a4617ccaff425e3b6fbcbf6511c6aabc7fbd14073479922e29e387a96663b480115f460f6e8"
}
headers=  {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"}
r = requests.post(url,data=formdata,headers=headers)
print(r.url)
print(r.text)
