import os
def check_deleted(opt,author_dic):
    for i in author_dic.keys():
        if not os.path.isdir(os.path.join(opt.outf,str(author_dic[i]))):
            author_dic[i] = -1
