
import requests
import time

s = requests.session()


start_time=time.time()
for i in range(50):
    r = s.get('https://www.baidu.com')
print('耗时{}秒'.format(time.time() - start_time))