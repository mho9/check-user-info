import requests
import json
import time


def check(xa):
    
        url = 'https://www.instagram.com/'+ xa +'/?__a=1'
        res = requests.get(url)
        if res.status_code ==404:
            print('username not found !!')
        elif res.status_code == 200:
            json_data = json.loads(res.text)  
            user = json_data['graphql'].get("user").get("username")
            baio = json_data['graphql'].get("user").get("biography")
            followed =json_data['graphql'].get("user").get("edge_followed_by").get('count')
            follow = json_data['graphql'].get("user").get("edge_follow").get('count')
            posted = json_data['graphql'].get("user").get("edge_owner_to_timeline_media").get('count')
            
            print('='*60)
            print(user)
            print('\n')
    
            if len(baio)==0:
                print('bio : no bio')
            else:
                 print('bio : '+ baio)
            print('followed : '+ str(followed))
            print('follow : '+ str(follow))
            print('-=-'*20)
            print('post : '+ str(posted))

while True:          
    tin = input("Start (y/n)?: ")
    if tin.lower() =='y':
        f = input('Enter username : ')
        check(f)
    elif tin.lower() =='n':
        exit()
    else:
        print(':@')
