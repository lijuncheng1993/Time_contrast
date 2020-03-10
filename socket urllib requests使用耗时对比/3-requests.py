import requests
import time

# session所有的api和requests都是一样的
s = requests.session()
start_time = time.time()
for i in range(50):
    r = requests.get('https://www/baidu.com')
print('耗时{}秒'.format(time.time() - start_time))
