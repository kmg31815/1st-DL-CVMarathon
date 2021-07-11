import requests
url = 'https://www.zhihu.com/explore'

headers = {
    'authority': 'www.zhihu.com',
    'method': 'GET',
    'path': '/explore',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_zap=60909310-369e-46ca-9884-407def344c01; d_c0="ANCWtJGmEhKPTh_yTxRMx743-G5pAidZUn4=|1603269269"; __snaker__id=XxqVRyZblLv4Wx2b; gdxidpyhxdE=UBB4zkYzMWdSse5CGf9PXyU4V6IS4KgLfxVycN%2B%2FzjeyDRa%2Fqhn2Ms%2FCECzMBaxHxNjN0df%5CJwtZuVZMAO1JCMptGxnMVp6Y16UX57rWQ6mLUV09b0TOdkonojQb5NnmWyY9lPeyIie36xy35T7ZNG35f7ZIj8Vq11k1HAGo0Yf%2BaOpS%3A1625744665575; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=njqPlhRfxV9zNPL%2Fo%2FjeE8Bm3wn49QH%2FK0C4ILQvAc3GAnFqQp1rbNKDQKiQMucZkBtDQGwsEKkD1cU7mX%2FJlNitmSgVOgpJQyEtcGyrYWpFpw%2BMbqocYMbA4dWeKzyDRXU%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb2d55487879da6e53b90ac8bb2d84e838b8fbaf53a8b8aa293d843a1f58e96c22af0fea7c3b92aaeb6bfb1ef6492bab8b7bc728e9084d0ee25aabb8bd9c167f1a9a2d5bc5b8cf185d1c2408b949f97c469f1998f8fc57b93b0ff93e146899c9facec5b8fabadbbea4ab89c9fa8f6798795a5a5b46997e9a3b9ae42b092a795f059a58a8188f34293a78b95e24dbbae97b8f34eb4a9e5aee17badbd97aee14bf8bc9986ca72bb9c9eb9d837e2a3; YD00517437729195%3AWM_TID=woON43%2BlZ6xBAFUUERY6yNQivQJZ7QvW; captcha_session_v2="2|1:0|10:1625743770|18:captcha_session_v2|88:bmhIN2hBMEd3WU9zMTF4R1QzNk1MRFZKS0VwWkVHcTdIbDBMQ1Q4R1NpREVVeFlpM0hSYUVZZHBaVEtTNWlCcg==|42dfeb6be555046bdfccd700e4641ebe62b061c89072a2e6ff03452f3f80f3b4"; _xsrf=5b656880-32c2-4b69-a6c5-03452c777555; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1625743673,1625743705,1625743770,1625906109; SESSIONID=JJ1Yt21cqB9RRBJ4nyvBHrIElnLo2Xwujnwumpptwwl; JOID=U1AWBUi6_1ppvZqmR720ii0ShzFU-b5uNcuhnCHJtGg-6trleLk8sA62mKhHzEaS42jD3UU78MYFODA5oHyrLNQ=; osd=VlkRBEy_9l1ouZ-vQLywjyQVhjVR8LlvMc6omyDNsWE5697gcb49tAu_n6lDyU-V4mzG1EI69MMMPzE9pXWsLdA=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1626000647; KLBRSID=fe78dd346df712f9c4f126150949b853|1626000647|1626000640',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = requests.get(url, headers = headers)
r.encoding = 'utf-8'
print(r.text[0:600])