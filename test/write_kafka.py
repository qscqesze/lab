import sys

def test_write():
    file = open("kafka/submission.txt", 'a')
    submission = {
        'id':-1,
        'user':'qscqesze',
        'problem':1001,
        'code':'#include<bits/stdc++.h>using namespace std;int main(){std::cout<<"fuck"<<std::endl;}',
        'status':'',
    }
    file.write(str(submission)+'\n')
    file.close()

def test_read():
    with open('kafka/submission.txt','r') as f:
        lines = f.readlines()
        print len(lines)
        print lines[-1]


if __name__ == '__main__':
    test_write()
    test_read()
