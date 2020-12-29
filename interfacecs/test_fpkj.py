import requests


class Testfpkj:
    # 以下完全是将postman请求的数据搬过来组装起来的，但是postman请求后返回正常，而以下代码运行后返回报错，为什么？
    def test_fpkj(self):
        url = "https://www.fapiao.com:53085/fpt-rhqz/prepose"
        headers = {
            "Cookie":"ukdjz2-ali-ukey-sk-51608-to-8443=node-10.10.16.41-pod-10.128.81.12",
            "Postman-Token":"<calculated when request is sent>",
            "Content-Type": "application/json",
            "Content-Length":"<calculated when request is sent>",
            "Host":"<calculated when request is sent>",
            "User-Agent":"PostmanRuntime/7.26.4",
            "Accept":"*/*",
            "Accept-Encoding":"gzip, deflate, br",
            "Connection":"keep-alive"
                   }
        data = {
            "json":
                {
                    "interface": {
                        "globalInfo": {
                            "appId": "0931144454bea341db1922720727f5f372d0e7edc2917bec83e77793954da322",
                            "interfaceId": "",
                            "interfaceCode": "GP_FPKJ",
                            "requestCode": "DZFPQZ",
                            "requestTime": "2020-09-30 09:58:53",
                            "responseCode": "DS",
                            "dataExchangeId": "DZFPQZDFXJ10012020072198A6123D0"
                        },
                        "returnStateInfo": {
                            "returnCode": "",
                            "returnMessage": ""
                        },
                        "data": {
                            "dataDescription": {
                                "zipCode": "0"
                            },
                            "content": "ewoJIlJFUVVFU1RfQ09NTU9OX0ZQS0oiOiB7CgkJIk5TUlNCSCI6ICIxMTAxMTAyMDIwNTIxMTUiLAoJCSJTQkxYIjogIjMiLAoJCSJTQkJIIjogIjIzNzAwMDEyMTEwNyIsCgkJIkZQUVFMU0giOiAiR1hEUDIwMjAwOTMwMTQ1NDAwNCIsCgkJIktQWkRETSI6ICIiLAoJCSJGUExYRE0iOiAiMDI2IiwKCQkiS1BMWCI6ICIwIiwKCQkiQk1CX0JCSCI6ICIiLAoJCSJaU0ZTIjogIjAiLAoJCSJYU0ZfTlNSU0JIIjogIjExMDExMDIwMjA1MjExNSIsCgkJIlhTRl9NQyI6ICLmtYvor5V1a2V5NTIxMTUiLAoJCSJYU0ZfRFpESCI6ICLmt7HlnLPljZflsbEwNzU1LTg1NDE0NzgiLAoJCSJYU0ZfWUhaSCI6ICLkuK3lm73pk7booYw2NTQ0NDQ0NzQ0Nzc0IiwKCQkiR01GX05TUlNCSCI6ICIxMTAxMDk1MDAzMjE2NTQiLAoJCSJHTUZfTUMiOiAi5rWL6K+VMSIsCgkJIkdNRl9EWkRIIjogIua3seWcszA3NTUtODU0MTQ1OCIsCgkJIkdNRl9ZSFpIIjogIjg1NDQ1NzQxMjU2OTk4NzQ0IiwKCQkiR01GX1NKSCI6ICIxODgyMDk0NzI4OSIsCgkJIkdNRl9EWllYIjogImNoZW5yb25nQGZhcGlhby5jb20iLAoJCSJGUFRfWkgiOiAiIiwKCQkiV1hfT1BFTklEIjogIiIsCgkJIktQUiI6ICLpmYjlrrkiLAoJCSJTS1IiOiAiIiwKCQkiRkhSIjogIiIsCgkJIllGUF9ETSI6ICIiLAoJCSJZRlBfSE0iOiAiIiwKCQkiSlNISiI6ICIxMDAiLAoJCSJISkpFIjogIjk0LjM0IiwKCQkiSEpTRSI6ICI1LjY2IiwKCQkiS0NFIjogIiIsCgkJIkJaIjogIiIsCgkJIkJZMSI6ICIiLAoJCSJCWTIiOiAiIiwKCQkiQlkzIjogIiIsCgkJIkJZNCI6ICIiLAoJCSJCWTUiOiAiIiwKCQkiQlk2IjogIiIsCgkJIkJZNyI6ICIiLAoJCSJCWTgiOiAiIiwKCQkiQlk5IjogIiIsCgkJIkJZMTAiOiAiIiwKCQkiV1hfT1JERVJfSUQiOiAiIiwKCQkiV1hfQVBQX0lEIjogIiIsCgkJIlpGQl9VSUQiOiAiIiwKCQkiVFNQWiI6ICIwMCIsCgkJIlFKX09SREVSX0lEIjogIiIsCgkJIlFEQloiOiAiMCIsCgkJIlRaREJIIjogIiIsCgkJIkNPTU1PTl9GUEtKX1hNWFgiOiBbewoJCQkiRlBIWFoiOiAiMCIsCgkJCSJTUEJNIjogIjMwNjA0OTkwMDAwMDAwMDAwMDAiLAoJCQkiWlhCTSI6ICIiLAoJCQkiWUhaQ0JTIjogIjAiLAoJCQkiTFNMQlMiOiAiIiwKCQkJIlpaU1RTR0wiOiAiIiwKCQkJIlhNTUMiOiAi6YeR6J6NIiwKCQkJIkdHWEgiOiAiIiwKCQkJIkRXIjogIiIsCgkJCSJYTVNMIjogIjEiLAoJCQkiWE1ESiI6ICI5NC4zMzk2MjI2NDE1MSIsCgkJCSJYTUpFIjogIjk0LjM0IiwKCQkJIlNMIjogIjAuMDYiLAoJCQkiU0UiOiAiNS42NiIsCgkJCSJIU0JaIjogIjAiLAoJCQkiQlkxIjogIiIsCgkJCSJCWTIiOiAiIiwKCQkJIkJZMyI6ICIiLAoJCQkiQlk0IjogIiIsCgkJCSJCWTUiOiAiIgoJCX1dLAoJCSJDQUxMQkFDS19VUkwiOiAiIiwKCQkiTFNIIjogIiIKCX0KfQ==",
                            "contentKey": "DgFhVmzUHEif2RgxodqbwPUtktxqr2Fpsblt5v57XQTJFpgwCtNWtRC+iZzexImXPBvHcdY7coVCWxpTIqidQlr4rZwGCQHo6jxkwMNsgTg="
                        }
                    }
                }

        }
        r = requests.post(url, json=data, headers=headers).json()
        print(r)
