#油品类
class Oil:
    def __init__(self,name,density,IBP,FBP,FP,CN,price):
        self.name=name
        self.density=density
        self.IBP=IBP
        self.FBP=FBP
        self.FP=FP
        self.CN=CN
        self.price=price

#油品实例
oil1=Oil("国五",0.831,162,266,69,52,4900)
oil2=Oil("煤油",0.79,145,200,53,47,4530)
oil3=Oil("循环油",0.85,150,250,60,42,4330)

#参数
T_IBP = 158
T_IBP_DEVIATION = 2
T_FBP = 250
T_FBP_DEVIATION = 2
T_FP  = 55
T_FP_DEVIATION = 1
T_CN  = 46
T_CN_DEVIATION = 1
T_DENSITY = 0.84
T_DENSITY_DEVIATION = 0
n = 0#精确率到小数点后N位，单位为%


#修正
N = 100*pow(10,n)
T_IBP_MAX = (T_IBP+T_IBP_DEVIATION)*N
T_IBP_MIN = (T_IBP-T_IBP_DEVIATION)*N
T_IBP = T_IBP*N
T_FBP_MAX = (T_FBP+T_FBP_DEVIATION)*N
T_FBP_MIN = (T_FBP-T_FBP_DEVIATION)*N
T_FBP = T_FBP*N
T_FP_MAX  = (T_FP + T_FP_DEVIATION)*N
T_FP_Min  = (T_FP - T_FP_DEVIATION)*N
T_FP = T_FP*N 
T_CN_MAX  = (T_CN + T_CN_DEVIATION)*N
T_CN_MIN  = (T_CN - T_CN_DEVIATION)*N
T_CN = T_CN*N
T_DENSITY_MAX = (T_DENSITY+T_DENSITY_DEVIATION)*N
T_DENSITY_MIN = (T_DENSITY-T_DENSITY_DEVIATION)*N
T_DENSITY = T_DENSITY*N


#计算
count=0
success=0
M = N+1
k = N/100
for z in range(0,M):
    for y in range(0,M-z):
        x = N-z-y
        count+=1
        if oil1.IBP*x+oil2.IBP*y+oil3.IBP*z > T_IBP:
            if oil1.FBP*x+oil2.FBP*y+oil3.FBP*z > T_FBP:
                if oil1.FP*x+oil2.FP*y+oil3.FP*z > T_FP:
                    if oil1.CN*x+oil2.CN*y+oil3.CN*z > T_CN:
                        if oil1.density*x+oil2.density*y+oil3.density*z < T_DENSITY:
                            success+=1
                            print("第%s组比例为：%s%%的%s，%s%%的%s和%s%%的%s成功"%(count,x/k,oil1.name,y/k,oil2.name,z/k,oil3.name))
        #                 else :
        #                     print("第%s组密度不对"%(count))
        #             else:
        #                 print("第%s组十六烷值不对"%(count))
        #         else:
        #             print("第%s组闪点不对"%(count))
        #     else:
        #         print("第%s组终馏值不对"%(count))
        # else:
        #     print("第%s组初馏值不对"%(count))
print("一共有%s组配搭成功,N为%s"%(success,N))
            
                
      


                            


    



