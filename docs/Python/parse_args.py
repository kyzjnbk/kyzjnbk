
def get_opts():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=int,default=1,help='example')
    parser.add_argument('files',type=str,nargs='+')
    opts=parser.parse_args()
    return opts

if __name__ =='__main__':
    opts=get_opts()
    print(vars(opts))