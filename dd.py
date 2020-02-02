curl 'https://oapi.dingtalk.com/robot/send?access_token=350ef93014a35fd97f33c4849e7747153cf314ff52736165d66ab7a1759c3fff' \
   -H 'Content-Type: application/json' \
   -d '{"msgtype": "text", 
        "text": {
             "content": "DDtest"
        }
      }'
