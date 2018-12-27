#! /bin/python2.7
# -*- coding: utf-8 -*-
#
# mmp - several tools.
#
# @Xiong X. 2017/10/20

import sys, os, re

def usage(args):
    print("""\
usage: mmp [version] [help] [<command> [<args>]]\n
There are common MMP commands used in various situations:\n
    rename      rename file(s) or directory(s) in FORMAT
    comment     remove comment from file(s) or directory(s)
    cr          remove cr ('\\r') from file(s) or directory(s)
    keyword     search keyword from file(s) or directory(s)
    version     print current mmp version
    help        print manual text""")


def version(args):
    print("MMP version 0.0.1")


def mmp_rename(args):
    optlen = len(args)
    mmpdir = ""
    mmpfmt = ""
    recur = False
    force = False
    sub_usage = """\
usage: mmp rename [help] [<directory> <format> [-r] [--force]]"""

    if optlen == 0:
        return sub_usage
    elif optlen == 1 and args[0] == "help"[:optlen]:
        return sub_usage
    elif optlen == 2:
        mmpdir = args[0]
        mmpfmt = args[1]
    elif optlen == 3:
        mmpdir = args[0]
        mmpfmt = args[1]
        if args[2] == "-r":
            recur = True
        elif args[2] == "--force":
            force = True
        else:
            return sub_usage
    elif optlen == 4:
        mmpdir = args[0]
        mmpfmt = args[1]
        if args[2] == "-r":
            recur = True
        elif args[2] == "--force":
            force = True
        else:
            return sub_usage
        if args[3] == "-r":
            recur = True
        elif args[3] == "--force":
            force = True
        else:
            return sub_usage
    else:
        return sub_usage

    if "%s" not in mmpfmt and not os.path.isdir(mmpdir):
        return sub_usage

    mmpfiles = os.listdir(mmpdir)
    cnt = 1
    for i in mmpfiles:
        src = os.path.join(mmpdir, i)
        dst = os.path.join(mmpdir, mmpfmt % str(cnt))
        os.rename(src, dst)
        cnt += 1
    return 0


def mmp_comment(args):
    regex = "\/\*[\s\S]*\*\/|\/\/.*"
    reobj = re.compile(regex)
    txt = []
    with open(args[0], 'rt') as f:
        for i in f:
            rst, cnt = reobj.subn("", i)
            txt.append(rst)
    with open(args[0], 'wt') as f:
        for i in txt:
            f.write(i)


def mmp_cr(args):
    cnt = 0
    cnt_n = 0
    cnt_r = 0
    cnt_rn = 0
    text = []
    with open(args[0], "rt") as f:
        for i in f:
            if len(i) > 1 and i[-2:] == '\r\n':
                cnt_rn += 1
                i = i[:-2]
            elif len(i) > 0 and i[-1] == '\r':
                cnt_r += 1
                i = i[:-1]
            elif len(i) > 0 and i[-1] == '\n':
                cnt_n += 1
                i = i[:-1]
            else:
                cnt += 1
            text.append(i)
    print "[REMOVE] CRLF= %d, CR= %d, LF= %d, NOT DEL=%d" % (cnt_rn, cnt_r, cnt_n, cnt)

    with open(args[0], 'wt') as f:
        for i in text:
            f.write(i+"\n")
    print "COMPLETED!"


def __mmp_keyword(f, kw):
    text = list()
    with open(f, "rt") as fp:
        for i in fp:
            if kw in i:
                print i


def mmp_keyword(args):
    pathes = os.listdir(args[0])
    for i in pathes:
        i = os.path.join(args[0], i)
        if os.path.isfile(i):
            __mmp_keyword(i, args[1])
        elif os.path.isdir(i):
            mmp_keyword([i, args[1]])


def parse_command(cmd):
    cmdlen = len(cmd)
    if cmdlen == 0:
        return None
    elif cmd == "help"[:cmdlen]:
        return usage
    elif cmdlen > 1 and cmd == "comment"[:cmdlen]:
        return mmp_comment
    elif cmd == "cr":
        return mmp_cr
    elif cmd == "rename"[:cmdlen]:
        return mmp_rename
    elif cmd == "keyword"[:cmdlen]:
        return mmp_keyword
    elif cmd == "version"[:cmdlen]:
        return version
    else:
        return None


if __name__ == "__main__":
    args = sys.argv
    if (len(args) == 1):
        usage(None)
        exit()
    cmd_fn = parse_command(args[1])
    ## Can not parse command
    if cmd_fn == None:
        usage(None)
        exit()
    ## return 0 if run command successful
    ## return sub-command usage info. else
    ret = cmd_fn(args[2:])
    if ret == 0:
        exit()
    print(ret)
    exit()