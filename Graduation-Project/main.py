# coding= utf-8
import jieba


def sortedDictValues2(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

if __name__ == '__main':
    dict_1 = dict()
    file = open('test.txt', 'r')
    lines = file.readlines()
    ans = []
    for line in lines:
        ans.append(line.decode('utf-8'))
        # ans.append(line)

    # for line in ans:
    #     print line
    for line in ans:
        seg_list = jieba.cut(line, cut_all=False)
        for seg in seg_list:
            # print type(seg)
            # print seg.encode('utf-8')
            try:
                dict_1[seg] += 1
            except:
                dict_1[seg] = 1

    dict_1 = sortedDictValues2(dict_1)
    for k,v in dict_1.items():
        print k.encode('utf-8') + ' : ' + str(v)
