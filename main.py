import sys 
from urllib import request, parse, error
from multiprocessing import Process

urls = [
    'https://github.com/',
    'https://twitter.com/',
    'https://hub.docker.com/v2/users/'
]

def inspect_status_code(url):
    try:
        response = request.urlopen(url)
        return response.code
    except error.HTTPError as e:
        return e.code

def inspect(url, user_id):
    code = inspect_status_code(url+user_id)
    title = parse.urlparse(url).netloc
    prefix = '\033[32m' if code == 404 else '\033[31m'
    suffix = '\033[0m'
    result = '{}{}{}'.format(prefix, code, suffix)
    print(title.ljust(16), result)

def main():
    if len(sys.argv) < 2:
        print('usage: python3 main.py ${USER_ID}')
        exit(1)

    user_id = sys.argv[1]
    ps = [Process(target=inspect, args=(url, user_id)).start() for url in urls]

if __name__ == '__main__':
    main()
