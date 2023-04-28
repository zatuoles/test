#第二题
def write_file(ls,new_file):
	with open(new_file,'w',encoding='utf-8') as text:
		[file.writelines(','.join(x)+'\n')for x in ls]
def sort_list(ls):
	
	
