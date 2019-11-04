
import request
import werobot

robot = werobot.WeRoBot(token='ljh123')

def wea():
    host = 'http://aliv18.data.moji.com'
    path = '/whapi/json/alicityweather/condition'
    method = 'POST'
    appcode = '869c94dd14df4a758120b64184847206'
    querys = ''
    bodys = {}
    url = host + path

    r = requests.post(url,data={'cityId':'934','token':'50b53ff8dd7d9fa320d3d3ca32cf8ed1',},headers={'Authorization':'APPCODE '+appcode})
    name = str(r.json()['data']['city']['name'])+'\n'
    condition = u'天气： '+ str(r.json()['data']['condition']['condition'])+'\n'
    humidity = u'湿度：'+ str(r.json()['data']['condition']['humidity'])+'\n'
    pressure = u'气压：'+str(r.json()['data']['condition']['pressure'])+'\n'
    real = u'体感温度：'+str(r.json()['data']['condition']['realFeel'])+'\n'
    temp = u'温度：'+str(r.json()['data']['condition']['temp'])+'\n'
    feng = u'风：'+str(r.json()['data']['condition']['windDir'])+u'  风力：'+ str(r.json()['data']['condition']['windLevel'])+u'  风速: '+str(r.json()['data']['condition']['windSpeed'])+'\n'
    tips = u'温馨提示:'+str(r.json()['data']['condition']['tips'])+'\n'
    update = u'更新时间'+str(r.json()['data']['condition']['updatetime'])+'\n'
    w = name + condition + humidity + pressure + real+ temp + feng + tips + update

    return w
    
@robot.filter(u"天气")
def a():
    w = wea()
    return w

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
