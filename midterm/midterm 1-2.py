# 附檔是一份紀錄某程式設計班級成績的CSV檔案，檔案敘述如下：
#
# 1.  1~10代表總共有10位學生
#
# 2.  A~G為第一次期中考各題成績，前四題(A~D)每題佔期中考成績10%，後三題(E~G) 每題佔期中考成績20%。
#
# EX:第一位學生第一次期中考成績為：60*0.1+0*0.1+0*0.1+0*0.1+40*0.2+40*0.2 + 30*0.2 = 28(分)
#
# H~N為第二次期中考成績，成績計算方式依此類推
#
# O~U為第三次期中考成績，成績計算方式依此類推，但如果他們的成績超過70分(大於等於)，那麼他們會得到額外的5分，至多就100分。
#
# 3.  V~AE為點名，0代表缺課，1代表有來上課，每次點名佔點名成績10%(即有來上課一次得點名成績10分)
# 4.  學期總成績 = 第一次期中考*0.3 + 第二次期中考*0.3 + 第三次期中考*0.3 + 點名*0.1
import numpy as np
data = np.genfromtxt('numpy_data.csv', delimiter=',')
print(data[0])
ans  = [[0]*5 for i in range(10)]
for i in range (0,10):
    ans[i][0]= i+1
for a in range(0,10):#ten student
    for i in range(0,3):#3 midterm
        sum = 0
        for j in range(0,7):
            if j <=3:
                sum = sum + data[a][i*7+j]*0.1
            else:
                sum = sum + data[a][i*7+j]*0.2
        ans[a][i+1] = sum
    attendence = 0
    for i in range(0,10):
        if data[a][21+i] == 1 :
            attendence = attendence +1
    ans[a][4] = ans[a][1]*0.3+ans[a][2]*0.3+ans[a][3]*0.3+attendence
np.savetxt('ans_1-2.csv',ans,delimiter=',')