import os, sys

marble_sell = "curl 'https://www.drakemoon.com/api/drake-clash/sell' -H 'origin: https://www.drakemoon.com' -H 'accept-encoding: gzip, deflate, br' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: en-US,en;q=0.8' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: */*' -H 'referer: https://www.drakemoon.com/moon-wars' -H 'authority: www.drakemoon.com' -H 'cookie: __cfduid=ded42f3d1adab1c09edae6fa3e52940df1504557800; maxtu=0dc31ff994f25e8f15b011bc03ebb6ab; mt_bounce=1; AWSELB=794F55FD06150522EC710DEB13393C6BF68A80101A1A13321BFE326E6F54999D98B62C729D9E230B9AE04330FB706A9AFFDDFF2F0AF1BCC1D6775DCDA51C0A1C8AE7B95540; maxtv=1504573964; maxtf=6; _ga=GA1.2.1840635686.1504557803; _gid=GA1.2.1832637218.1504557803; __ar_v4=6CAFYIG6XRE6HOOLME5X5X%3A20170904%3A76%7CA673YPDJVJBJ7FAWVUECHF%3A20170904%3A36%7CIUEQYX36XZDNXOMI47C2V4%3A20170904%3A112%7CN6ZMMBDUWNGURNVAJYSAV2%3A20170904%3A112; __zlcmid=iLgirDdhH7lmRr; XSRF-TOKEN=eyJpdiI6IlFZY3lvYTl5ZXZPQlgxbk5JMWxVMWc9PSIsInZhbHVlIjoiUVNvaVY2XC8zd2xLT2JiS0ppYlFQSWhGeTl6aDlnOVFaWTFadTdhVEhzYUFnYmxTQ1l4NEFpUDZ3aTkzK0l2cVF4MjFvbEZ6b25yYktCVVU2OUhPQ3BRPT0iLCJtYWMiOiI1MWQzZDA1ZmM2YzA0ZWZlNjdiM2Y4NmY1NWY5Y2MyNDdmY2UxYjNhNTkzNDAwZTQwMzYyNmQzNGViYmJiZmVmIn0%3D; laravel_session=eyJpdiI6ImxLK1wvT0x4eWdlbjc0R0NPaG5hTHJ3PT0iLCJ2YWx1ZSI6IndWY2tsa1BoUmVMVVpKRG5kZG9TYzVtUWk1c3pMeWxJVEtrNHRwUVB2eTdsek1PajN4MCs3dDFCUkhiZEdTU1RvSnJlMkhZVjB3bWlLV2IzaTJrTkpBPT0iLCJtYWMiOiI1ZDdiODAwMGUyOTdjZjE0ZWNkOTNiNjFhZmJlY2UzNTNmMTdmOTYwNzJkMTZiNDVhOWRjNTY4NDdkY2JmYTAzIn0%3D; maxtp=79:54' --data 'winning%5B%5D=143069531&_token=3XfM9L6f1TzhTt7ADn66warHmSiuquuR5PIPYWTz' --compressed"
nyd_sell = "curl 'https://www.drakemoon.com/api/drake-clash/sell' -H 'origin: https://www.drakemoon.com' -H 'accept-encoding: gzip, deflate, br' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: en-US,en;q=0.8' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: */*' -H 'referer: https://www.drakemoon.com/moon-wars' -H 'authority: www.drakemoon.com' -H 'cookie: __cfduid=ded42f3d1adab1c09edae6fa3e52940df1504557800; maxtu=0dc31ff994f25e8f15b011bc03ebb6ab; mt_bounce=1; AWSELB=794F55FD06150522EC710DEB13393C6BF68A80101A1A13321BFE326E6F54999D98B62C729D9E230B9AE04330FB706A9AFFDDFF2F0AB5C8C44DCE6F65874BB5244E05095113; maxtv=1504576091; _gat=1; maxtf=7; _ga=GA1.2.1840635686.1504557803; _gid=GA1.2.1832637218.1504557803; __zlcmid=iLgirDdhH7lmRr; __ar_v4=6CAFYIG6XRE6HOOLME5X5X%3A20170904%3A84%7CA673YPDJVJBJ7FAWVUECHF%3A20170904%3A36%7CIUEQYX36XZDNXOMI47C2V4%3A20170904%3A120%7CN6ZMMBDUWNGURNVAJYSAV2%3A20170904%3A120; XSRF-TOKEN=eyJpdiI6IldBQVJ0SWFMMG9TUVVEaGZQSWhEYmc9PSIsInZhbHVlIjoiS0FQbUdzcHBcL2s1Q29CN3ZGdHFtQzdXRzBQaDA4Z0k1MlEzdXF2alIzNFExQlNkK3pnbWhTbFIxbEVrc3VLcmFqQVV0WmNyTjBLUUtwMlwvM24yUE9yZz09IiwibWFjIjoiZWRjMmIwNWY3YTczYThhZWRlYzQ4YzE2NGIwMTFkNzc0ZWMwMjc4MDVjM2I3YjgyOWJjZjYwM2NiMmU2OWEwMiJ9; laravel_session=eyJpdiI6ImExSHhnZTBicW1KOFQ1bUtZODdpcnc9PSIsInZhbHVlIjoiKzBJRHZuWnpiN0NIVEY3eEdrN3JjeUd0Q1pleEtqT3pYZ1psUzlnSnhLdjRHUzNiVHp6bjBXODQ4UmlCQTV0clgzM0d4aFpxNThtMlNUMFhLUnNyUlE9PSIsIm1hYyI6ImM5Mjg5YTU5ZmM2YjI4MmU2YjllYmE5Zjg0ODk5NDVlMzNjODM5N2E5NDM1Mzg1MGIzMTlkYTJlY2Y0MGRiMzQifQ%3D%3D; maxtp=89:28' --data 'winning%5B%5D=143073041&_token=3XfM9L6f1TzhTt7ADn66warHmSiuquuR5PIPYWTz' --compressed"

open = "curl 'https://www.drakemoon.com/api/drake-clash/open?case_id=1&_token=3XfM9L6f1TzhTt7ADn66warHmSiuquuR5PIPYWTz'" +
    " -H 'accept-encoding: gzip, deflate, br' -H 'x-requested-with: XMLHttpRequest' -H 'accept-language: en-US,en;q=0.8' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' -H 'accept: */*' -H 'referer: https://www.drakemoon.com/moon-wars' -H 'authority: www.drakemoon.com' -H 'cookie: __cfduid=ded42f3d1adab1c09edae6fa3e52940df1504557800; maxtu=0dc31ff994f25e8f15b011bc03ebb6ab; mt_bounce=1; AWSELB=794F55FD06150522EC710DEB13393C6BF68A80101A1A13321BFE326E6F54999D98B62C729D9E230B9AE04330FB706A9AFFDDFF2F0AF1BCC1D6775DCDA51C0A1C8AE7B95540; maxtv=1504573964; maxtf=6; _ga=GA1.2.1840635686.1504557803; _gid=GA1.2.1832637218.1504557803; _gat=1; __zlcmid=iLgirDdhH7lmRr; " + 
    "__ar_v4=N6ZMMBDUWNGURNVAJYSAV2%3A20170904%3A99%7CIUEQYX36XZDNXOMI47C2V4%3A20170904%3A99%7CA673YPDJVJBJ7FAWVUECHF%3A20170904%3A36%7C6CAFYIG6XRE6HOOLME5X5X%3A20170904%3A63; " + 
    "XSRF-TOKEN=eyJpdiI6IjgwZHp5MXA2c1BUa1pxMnR0cGNvbHc9PSIsInZhbHVlIjoieTQxV2JiZUpsWmxPajZvMXg0MlNaazRaSmpTbDlsRzc5UFc2eHZuVzh3VWdtZWw2Q2NcL3FPcitMNFloMlFvV3g3Z3dtVUhUdVVMNlNCY1VrK2ludktnPT0iLCJtYWMiOiI0NTZlZjc5YmZiMDVmOGMyOWQ2MTE2NmU3NGU5MWY3ZDkzOTQyY2ZiOThiZmU1Mzk5MDNkN2QyNTk3Nzc4OTk4In0%3D; laravel_session=eyJpdiI6InFTXC9WOUlJZWlRcDRZdWxKZGNFRnpBPT0iLCJ2YWx1ZSI6IkxHYUZhRHRvYXowOXd1MDVXSzNoWXA3cm05d091aTczeG1vUjdrVEhzb2dhTEFjMVI4YmlibVRTOGlpYlwvUkNMSlYyQkZqMmw2cDJNWXVpOWVKOUQxZz09IiwibWFjIjoiMDY0ZWE5ZmJkYjE3ZGVlZDllYmQzZDNlM2I2ODQ4YjA5ZmM4OGU4OWYzNDc2NGYwZGY0NGY1NWMxN2VhMWJmYSJ9; maxtp=58:69' --compressed"
    
    def sell_marble:
    def sell_nyd:
    
    def open:
        s = ""
        while 1:
            line = p.readline()
            if not line: break
            s += line
            print line
        winid = s.split("{")[13]
        chest_name = s.split("{")[15]
        if "Marble" in chest_name:
            print "Marble Case\n"
            print winid
        else if "Not your " in chest_name:
            print "Not Your Day\n"
            print winid
