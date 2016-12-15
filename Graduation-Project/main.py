# coding= utf-8
import jieba
from jieba import analyse

def sortedDictValues2(adict):
    items = adict.items()
    items = sorted(items, key=lambda item: item[1], reverse=True)
    return items

if __name__ == '__main__':
    dic = dict()
    ans = open('test.txt', 'r').read()

    tags = jieba.analyse.extract_tags(ans, 10)
    for tag in tags:
        print tag.encode('utf-8')
    # seg_list = jieba.cut(ans, cut_all=False) # generator
    # for seg in seg_list:
    #     if dic.has_key(seg):
    #         dic[seg] += 1
    #     else:
    #         dic[seg] = 1
    #
    # print '=========================================='
    #
    # lister = sortedDictValues2(dic)
    # for li in lister:
    #     print li



# http://gaopenghigh.iteye.com/blog/1483864
# http://www.cnblogs.com/linyawen/archive/2012/03/15/2398292.html





