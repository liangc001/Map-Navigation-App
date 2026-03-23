import sys
from unittest import result

H = 100
INF = 100011

f = [[0 for i in range(105)] for i in range(105)]
path = [[0 for i in range(105)] for i in range(105)]
d = [[0 for i in range(105)] for i in range(105)]
num={}
loc={}
#loc即为道路节点信息


def read_node(data):
    cnt=0
#cnt为结点数目
    for i in range(len(data)):
        for j in range(0,2):
            if data[i][j] in num.keys():
                continue
            num[data[i][j]]=cnt
            loc[cnt]=data[i][j]
            cnt+=1
    return (loc,cnt)
          

#floyed算法计算最短路
def Floyd (data):
    n=read_node(data)[1]
    #print(n)
    for i in range(len(data)):
        f[num[data[i][0]]][num[data[i][1]]]=data[i][3]
        d[num[data[i][0]]][num[data[i][1]]]=data[i][2]
    for i in range(0,n):
        for j in range(0,n):
            if f[i][j]==0:
                f[i][j]=INF
            if i==j:
                f[i][j]=0
            path[i][j]=j
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if f[i][j]>f[i][k]+f[k][j]:
                    f[i][j]=f[i][k]+f[k][j]
                    path[i][j]=path[i][k]
  

#查询函数
def query_path(data,start,end):
    #floyed预处理
    Floyd(data)
    #可反复查询两点间的最短路
    dis_=read_node(data)
    dis_2=dis_[0]
    s=list(dis_2.keys())[list(dis_2.values()).index(start)]
    e=list(dis_2.keys())[list(dis_2.values()).index(end)]
    u=0
    v=0
    u=s
    v=e
    cnt_path=0
    result_=[]
    while u!=v:
        cnt_path+=1
        if cnt_path==1:
            str1=f'由{str(loc[u])}'+f'向{d[u][path[u][v]]}行走{f[u][path[u][v]]}米到达{str(loc[path[u][v]])}'
            result_.append(str1)
        else:
            str2=f'再向{d[u][path[u][v]]}行走{f[u][path[u][v]]}米到达{str(loc[path[u][v]])}'
            result_.append(str2)
        ##print(v)
        #print(loc[u])
        #print(loc[v])
        u=path[u][v]
    str3=f'共需要走{f[s][e]}米'
    result_.append(str3)
    #print(v)
    #print(path[u][v])
    print(result_)
    return result_


        # 判断是否终止
        # print("退出请输入Q 继续查询请输入G: ",end="")
        # mode=''
        # mode=input()
        # if mode=='Q':
        #     break

# 测试代码
if __name__ == "__main__":
    data=[('清真食堂', '基础学院大门', '西', 300), ('基础学院大门', '清真食堂', '东', 300), ('清真食堂', '清真食堂南侧路口', '南', 50), ('清真食堂南侧路口', '清真食堂', '北', 50), ('清真食堂', '操场', '北', 200), ('操场', '清真食堂', '南', 200), ('申一教', '基础学院大门', '西', 100), ('基础学院大门', '申一教', '东', 100)]
    t=query_path(data,'清真食堂','基础学院大门')