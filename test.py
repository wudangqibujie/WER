import requests
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_36308924?csrf_token="
post_data = {
'params': 'DHYrfyGjVVYmbmm/57pwDn0KezTSojS8RBoZNPUQ685J9YH6q7vOK3rTKwKoLqVuZXqk+Sk4fjTN+Dib37lrZRMJkbB0sepcVLPpJMd43R8uNCgvqiZEZBHCrajXbYP6PcpYJIO+RQ1FEcB4f2N0Brbzr64sraAjXwHCRQ3A0oqaSI/7XDPLxzDvU7ofz1wg',
'encSecKey': '396ccc4a53204c4bff2e1aee1fe834779cf6f55693698de23775262d02d85ae1e7185f3e61912ac4194d6f85c23719dbab96e61a90eeba5031f9e43914aaddb0b97c3b457b1ffbbe14f1754500fcdee0d83d3e3b29accb43f7e351daf6c7dfd5afc5ad628026fa8407e407dd1cdda1d88b6c63db0e4b13f7f7d7370e10a0f081'
}
headers=  {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"}
r = requests.post(url,data=post_data,headers=headers)
print(r.text)