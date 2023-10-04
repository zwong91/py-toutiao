#encoding=utf8
import xlwt
def set_style(name,height,bold=False):
	style = xlwt.XFStyle() # 初始化样式

	font = xlwt.Font() # 为样式创建字体
	font.name = name # 'Times New Roman'
	font.bold = bold
	font.color_index = 4
	font.height = height

	# borders= xlwt.Borders()
	# borders.left= 6
	# borders.right= 6
	# borders.top= 6
	# borders.bottom= 6

	style.font = font
	# style.borders = borders

	return style
def write_excel(filename, row, data_dict):
	f = xlwt.Workbook()
	'''
	创建第一个sheet:
	sheet1
	'''
	sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet

	#生成第一行
	for i in range(0,len(row)):
		sheet1.write(0,i,row[i],set_style('Times New Roman',220,True))
		
	#写入数据
	i = 1
	for (key, arr) in data_dict.items():
		sheet1.write(i, 0, key)
		for j in range(0, len(arr)):
			sheet1.write(i, j+1, arr[j])
		i+=1
	f.save(filename)

if __name__ == '__main__':
	#demo
	row = [u'业务',u'状态',u'合计']
	data_dict = {}
	data_dict[u'10001'] = [u'成功', u'success']
	data_dict[u'10002'] = [u'失败', u'failed']
	write_excel('玩家充值信息.xls', row, data_dict)
