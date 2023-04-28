#第一题
score=[['Angle','0121701100106',99],['Jack','0121701100107',86],['Tom','0121701100109',65],['Smith','0121701100111',100],['Bob','0121701100115',77],['Lily','0121701100117',59]]
def ls_sort_two(n,ls):
	for i in range(len(ls)):
		for j in range(len(ls)):
			if ls[i][n]>ls[j][n]:
				swap=ls[i]
				ls[i]=ls[j]
				ls[j]=swap
ls=score
ls_sort_two(0,ls)
print("按照姓名排序：",ls)
ls_sort_two(1,ls)
print("按照学号排序：",ls)
ls_sort_two(2,ls)
print("按照成绩排序："，ls)
