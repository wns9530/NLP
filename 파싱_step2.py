import os,csv,pymysql.cursors, itertools

conn=pymysql.connect(host='localhost', user='root', password='1234',
                     db='jw', charset='utf8')

c=0
print("%03d"%c)
s="%03d"%c
print(s)

path1="C:/Users/JW/Desktop/차세정자료/python/next_gen_output_conllu_etri"
path2="C:/Users/JW/Desktop/차세정자료/python/next_gen_output_conllu_ulsan"

file_list1 = os.listdir(path1)
file_list2 = os.listdir(path2)
#print(file_list1[0])

for i in range(0,len(file_list1)):
    s="%03d"%c
    full_name1 = os.path.join(path1,file_list1[i])
    full_name2 = os.path.join(path2,file_list2[i])
    #print(full_name1)
    #print(full_name2)
    with open(full_name1,'r',encoding='utf8')as f1 ,open(full_name2,'r',encoding='euc-kr')as f2:
        for (line1,line2) in zip(f1.readlines(), f2.readlines()) :
            #print(1)
            if line1[0]=='#':            #라인의 제일 첫글자(line[0])이 '#'일 경우에 수행
                a = line1.split(" ")     #line을 공백(" ")단위로 끊어 a에 배정
                if a[1]=="sent_id":     #a의 두번째(a[1]) data의 값을 검색
                    b=a[3].rstrip()     #a의 네번째(a[3]) data를 b에 저장
                    #print(b)
                    conn.commit()
                    print(b)
            else:
                #print(line2)
                if line1[0] == '\n' :    #text파일 중간 중간에 "\n"키가 포함되어 있어 불필요한 정보 스킵
                    #print("$")
                    continue
                field1 = line1.strip().split('\t')    #line을 tab('\t')단위로 끊어 field에 배정
                #print(line2)
                field2 = line2.strip().split('\t')    #line을 tab('\t')단위로 끊어 field에 배정
                
                plusadd= field2[4].strip().split(' ')
                #print(len(plusadd))
                field2[4]=''
                for j in range(0,len(plusadd)):
                    if j != 0:
                        plusadd[j]='+'+plusadd[j]
                    #print(plusadd[j])
                    field2[4]+=plusadd[j]
                #print(field2[4]+field2[0]+str(len(plusadd)))
                with conn.cursor() as cursor:
                    cursor.execute("insert into etri_v2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (file_list1[i],b,field1[0],field1[1],field1[2],field1[3],field1[4],field1[5],field1[6],field1[7],field1[8],field1[9],b,field2[0],field2[1],field2[2],field2[3],field2[4],field2[5],field2[6],field2[7],field2[8],field2[9]))
                    #주의할 점! 마지막 misc에 삽일할 data의 길이가 너무 길어서 misc의 자료형을 변경해주었음. 에러의 요인
                #print("check")
    c=c+1
    #if c==1:
        #break
conn.close()
