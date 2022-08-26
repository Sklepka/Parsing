import requests
from bs4 import BeautifulSoup

def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    return requests.post(url, headers = headers, data = body)
    
# Сайт - Ф12 - выбрали нужные параметры в отображении и нажали "показать предложения" - во вкладке "Fetch/XHR" - "listing" - правой кнопкой - copy - "Copy as Node.js fetch"
response = fetch("https://auto.ru/-/ajax/desktop/listing/", {
    "headers": {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6",
        "content-type": "application/json",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "same-origin",
        "sec-fetch-site": "same-origin",
        "x-client-app-version": "132.0.9918963",
        "x-client-date": "1661509048305",
        "x-csrf-token": "1c74c471bad1e40b2e8160818e7646ed16a66653bd85f99c",
        "x-page-request-id": "9ff31f8e9d95150276d373858bada627",
        "x-requested-with": "XMLHttpRequest",
        "x-retpath-y": "https://auto.ru/cars/lamborghini/used/?year_to=2010",
        "x-yafp": "{\"a1\":\"YtIs26HgPmaOFw==;0\",\"a2\":\"9xbmEsxorsQmzzJh2s+bsViFbMiPiQ==;1\",\"a3\":\"XAZUXdmg6wtN8FNgCmIIXQ==;2\",\"a4\":\"h6/l9xTFusG2Vs5i+L9kY+pQScH1PMXIKTKSccVybvRcs+LctV/Ri4mAL9aW5A==;3\",\"a5\":\"ORYIXSzLvciFFg==;4\",\"a6\":\"RWE=;5\",\"a7\":\"f/SzMjSF18ZOyA==;6\",\"a8\":\"Gh1010RJtfo=;7\",\"a9\":\"saEIlLtw8+e6YA==;8\",\"b1\":\"8D55UFKmIXI=;9\",\"b2\":\"6UTJTguvQsqYnA==;10\",\"b3\":\"7vXeroGqng5A1g==;11\",\"b4\":\"mKWX/izAWp0=;12\",\"b5\":\"G7iRIkviLo2ouA==;13\",\"b6\":\"k2Mm0xP0gr06QA==;14\",\"b7\":\"JCoD/6ole/CxtQ==;15\",\"b8\":\"ko9pTnBQw7jiqQ==;16\",\"b9\":\"3Gzhnr0pt76pQw==;17\",\"c1\":\"r/ZV3w==;18\",\"c2\":\"VaTimv0OtTCd/IZKylacKebq;19\",\"c3\":\"vT64fs2jfBhF67RL6pxuBSRV;20\",\"c4\":\"ARcjKjK15SY=;21\",\"c5\":\"dm+180bOENw=;22\",\"c6\":\"rSr3ag==;23\",\"c7\":\"yY1WfWggY2Y=;24\",\"c8\":\"Cfs=;25\",\"c9\":\"OXcUKEfwMuM=;26\",\"d1\":\"nl4vf6/CN3w=;27\",\"d2\":\"wC4=;28\",\"d3\":\"3UZ1KJYG7iJbtg==;29\",\"d4\":\"DBxWNMiIY2k=;30\",\"d5\":\"mkaIlaKGqlU=;31\",\"d7\":\"W8k01PHi18c=;32\",\"d8\":\"BQXacXUMTlYGRNS495fNa+GZXfVvPyHfYiY=;33\",\"d9\":\"Bw3FG0CthnI=;34\",\"e1\":\"HMJjLvaiNGxbpg==;35\",\"e2\":\"2Yvf0Fm4Ak4=;36\",\"e3\":\"5iRVRwxYXDY=;37\",\"e4\":\"DNTwiIobmDU=;38\",\"e5\":\"lQlo58ZFCV06cw==;39\",\"e6\":\"2SImXnZysus=;40\",\"e7\":\"TuPrnBZWz0FyPQ==;41\",\"e8\":\"0DdXx1k9GN0=;42\",\"e9\":\"XmYJSmqGzUU=;43\",\"f1\":\"HoCXCpZSXTK1lg==;44\",\"f2\":\"TBCgdLM8RJ4=;45\",\"f3\":\"/eruSt+pymOU3A==;46\",\"f4\":\"wP4lPFFgr4s=;47\",\"f5\":\"k2NiuLXj8kbyaQ==;48\",\"f6\":\"2ORfMNnCIgFO7g==;49\",\"f7\":\"ACDNszqynPtF/w==;50\",\"f8\":\"UeuuBCUhtDBqrA==;51\",\"f9\":\"5X7r+3p83EM=;52\",\"g1\":\"VVWUIjnaVkcDRw==;53\",\"g2\":\"o9avbI0yDiMZUw==;54\",\"g3\":\"iPB9yQR0Dcc=;55\",\"g4\":\"guBc+5yVwSh0Sw==;56\",\"g5\":\"1fC3iIAvB+8=;57\",\"g6\":\"+p/KeTYOXzc=;58\",\"g7\":\"fo/LE6+9QqQ=;59\",\"g8\":\"wFyy+ZqdXhQ=;60\",\"g9\":\"3KCIc5u/YXA=;61\",\"h1\":\"TbCe42W7ipnLhg==;62\",\"h2\":\"LRlsbdSbAntPog==;63\",\"h3\":\"zFF+YmqTIvRegA==;64\",\"h4\":\"M0OwV0mYlbR1Og==;65\",\"h5\":\"m1VKjNf3JB4=;66\",\"h6\":\"vU+6l/DqngoQiw==;67\",\"h7\":\"5ufLo06VOr92rRE4sZZfV/bgVmAmh7kDcYjVGjLQf/P+j/z/;68\",\"h8\":\"unwI979BX4xR5g==;69\",\"h9\":\"fP3MT7ptXQ25FA==;70\",\"i1\":\"2B76SteyevY=;71\",\"i2\":\"UM3z3iyhO4jf/w==;72\",\"i3\":\"W7DOxHyTR5Iztw==;73\",\"i4\":\"Wk2VVM/+na4BoA==;74\",\"i5\":\"rsHg/guPoG6f9g==;75\",\"z1\":\"kBVaUIGpsP+0umT+9/s82JaXR/ZFc9HuLgnh+sMDwpHIHdtWl9VzOpdJQN6BTyuVCn7eK6rtpBXD2d7UqW50Uw==;76\",\"z2\":\"jjhekGiy3o8G3NkIxKkfyGnkf0CG0KjBjHdecYQK4YrvSwQO9rTNn+y1X94xf0AVUvqHNhAK4XFktKntDGWndA==;77\",\"y2\":\"ZZ95PbHbmas16Q==;78\",\"y3\":\"b6wjL6R9urfWLQ==;79\",\"y6\":\"8ph/Wze0o44OEw==;80\",\"y8\":\"K0DAUkZ5LJtmCw==;81\",\"x4\":\"tBACNyx3vPnnIg==;82\",\"z5\":\"gDFUzCa8puc=;83\",\"z4\":\"lY2KhITKsm33gw==;84\",\"z6\":\"mMMLkkprgHltNS1O;85\",\"z7\":\"KLiBOqlvpv84wrNI;86\",\"z8\":\"lZ+uhIDva/5EupvPHrA=;87\",\"z9\":\"JgoEmIEvYyQkgXld;88\",\"y1\":\"+NmAZ8+/w2AqIQFb;89\",\"y4\":\"bT+4kuRG2b+aJKRO;90\",\"y5\":\"Nx03BU5JkRB0j6OjPdU=;91\",\"y7\":\"hoj29CpK20TSSFei;92\",\"y9\":\"UdEjrT97SzmdOlMIjqw=;93\",\"y10\":\"5m/BGt0+Jnq1b2zGYSY=;94\",\"x1\":\"fsfE0nMXFwUwOWCn;95\",\"x2\":\"FqqJ6cb+Gs6bO1X/lyE=;96\",\"x3\":\"VCcjEAlBuY3iOjBH;97\",\"x5\":\"wZEBahwQn8oL3Hly;98\",\"z3\":\"D2GC3ADoqQTo2KYQaIUr2Th7y0TSqw9xUFoAiS/TIbU=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"fRKHOZf0iaY8IuvXkWehx+v6sl0=;100\",\"pgrd\":\"i41b/3pML9YQqkBXtsWo7EjPGKYoqFYASDA7QqrQ/9I9agiP93iT+6nHd5OVgYgeUnbQJ0+5XFiEqKo7THvOf6i4enWdgLM1MsNXmEYldOIKJKo7M2DJterw5tj/aY1ImxLdsf/fv0q8KRn3yalQthK/nkvpKYJxAt3lQkhSbS/TcqcmV6A17LcSoGjS9bw+aV+pakE3225YJUfVdBngFZ/9QEQ=\"}",
        "cookie": "suid=e2b761bb6bd52d8f927c37cb0d108f89.84934fcccfdc10a71714bc212a2a2adc; _ym_uid=1614936480318533222; yandex_login=iSklepka; gdpr=0; _ym_isad=1; _ym_visorc=b; spravka=dD0xNjYxNTA4NjI0O2k9MTg4LjY4LjE4NS43MjtEPUNCMEE0MTQxNkExMzFBRDkzODBDOERGOTc5Q0JBRjg0RjZENDkwNDVBODE4NTZCQ0QwODA1REUxQ0Y0MTM0MDRGMTE0QkRCQTt1PTE2NjE1MDg2MjQzMzE2NDE2MjA7aD1lYThmMzc5YmU3ZDkwOWQ1Mjc5ZjRkYzUzY2I5ZjQzYQ==; _csrf_token=1c74c471bad1e40b2e8160818e7646ed16a66653bd85f99c; autoru_sid=a%3Ag63089c10289u3q7ur0p0vnqa4m0gluh.dfa2ee281e9a243ff56efc593222dd62%7C1661508624402.604800.QabO7knOj2IXbX288Bz5lA.rHNoaaMQKxXLQLQuFQsgc3Ucqjgx9RHCd6tR9Ryhfe8; autoruuid=g63089c10289u3q7ur0p0vnqa4m0gluh.dfa2ee281e9a243ff56efc593222dd62; from=direct; yuidlt=1; yandexuid=6525066891610979608; my=YwA%3D; counter_ga_all7=2; crookie=ca16vrXV04ZfkUzbf0gFqe6ROkLR252ma5mtrnBujqFiLiiJ2MB/WM+31YXgUoKEMs1rhk7Ci6VXvDiWU0Z8qv3ZUys=; cmtchd=MTY2MTUwODYyNDU2OA==; Session_id=3:1661508626.5.1.1654939685510:uNxDUA:f.1.2:1|1409382841.-1.0.1:287535713|1192400256.98592.2.2:98592|61:10006930.964508.PuxHu7nPS3ptjvDUUlIZF50AB-w; ys=udn.cDppU2tsZXBrYQ%3D%3D#c_chck.732783048; i=3514AdNqxxTC1uq1inRxc5T5+AZ+lu95h48Wd/4GJux7BJnWBNN3ij8DvCJmQDq8LQtLM6Nedjr8hAWvtPZ9AWa2j28=; mda2_beacon=1661508626254; sso_status=sso.passport.yandex.ru:synchronized; _yasc=+vK6ssXZLfL21x2ZA1jIKp8NAOYdGGwUw/TJndMvKvna76RB; gids=; gradius=200; los=1; bltsr=1; layout-config={\"win_width\":1924,\"win_height\":937}; from_lifetime=1661509041854; _ym_d=1661509044",
        "Referer": "https://auto.ru/cars/lamborghini/used/?year_to=2010",
        "Referrer-Policy": "no-referrer-when-downgrade"
    },
    "body": "{\"year_to\":2010,\"catalog_filter\":[{\"mark\":\"LAMBORGHINI\"}],\"section\":\"used\",\"category\":\"cars\",\"output_type\":\"list\"}",
    "method": "POST"
})


lambo_data = response.json()
for car in lambo_data["offers"]:
    mark = car['vehicle_info']['mark_info']
    model = car['vehicle_info']['model_info']
    tech = car['vehicle_info']['tech_param']
    print(f'{mark["name"]} {model["name"]} за {car["price_info"]["RUR"]} руб. / {tech["human_name"]}')
