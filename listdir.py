import datetime
import argparse
from pathlib import Path
import stat

def listdir(path:str='.', all = False, detail = False, human = False):
    #900 2000 = 2k 2000000 =2000k = 2m
    def _get_human(size:int):
        units = ['', 'K', 'M', 'G', 'T', 'P']
        # units = " KMGTP" #字符串性能更好，不会每次迭代都生成新的变量
        depth = 0
        while size >= 1000:
            size = size // 1000
            depth += 1
        return "{}{}".format(size, units[depth])

    def _showdir(path:str='.', all = False, detail = False, human = False):
        p = Path(path)
        for file in p.iterdir():
            if all and str(file.name).startswith('.'): #.开头 不打印 -all
                continue
            # 处理 -l
            if detail:
                st = file.stat()
                h = str(st.st_size)
                if human:
                    h = _get_human(st.st_size)

                yield str(stat.filemode(st.st_mode), st.st_nlink, st.st_uid, st.st_gid, h,
                       datetime.datetime.fromtimestamp(st.st_atime).strftime('%Y-%m-%d %H:%M:%S'), file.name)
            else: #没有 -l
                yield str(file.name,)

    yield from sorted(_showdir(args.path, args.all, args.l, args.h), key = lambda x: x[-1])


parser = argparse.ArgumentParser(prog="ls", add_help=False, description='list all files')
parser.add_argument('path', nargs='?', default= '.', help = 'path help') #位置参数
parser.add_argument('-l', action='store_true')
parser.add_argument('-h', action='store_true')
parser.add_argument('-a','--all', action='store_true')

# ls [path] [-l] [-h] [-a]

if __name__ == '__main__':
    # showdir('d:/')
    args = parser.parse_args()
    parser.print_help()

    print('args = ',args)
    # print(args.path, args.l, args.h, args.all)

    # sorted(showdir(args.path,args.all,args.l,args.h), lambda x:x[-1])

    for st in listdir(args.path,args.all,args.l,args.h):
        print(st)
    # print(*listdir(args.path,args.all,args.l,args.h))
