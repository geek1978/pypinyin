#coding:gbk

import sys, pypinyin

def main():
    getPy = pypinyin.GetPinyin()
    getPy.load()
    print 'text getPy: '
    results = getPy.getPy(u"wo����Ҫ�����ף������Ǹ��õط�")
    for result in results:
        print result.py
    
    print 'test getMaxPy: '
    print getPy.getMaxPy(u'wo����Ҫ�����ף������Ǹ��õط������Ȱ�����')
    print getPy.getMaxPy(u'�����й��ˣ����Ȱ��ҵ�����������ش����飬�뱨����֯')
    return 0
    

if __name__ == '__main__':
    sys.exit(main())