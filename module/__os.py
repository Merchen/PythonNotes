import os

# 执行程序，受限于空白(必须使用双引号包围)，
os.system(r'C:\"Program Files"\"Internet Explorer"\iexplore.exe')

# 执行程序，不受限空白
os.startfile(r'C:\Program Files\Internet Explorer\iexplore.exe')

# 获取目录下的全部文件名称
os.listdir('.')

# 递归获取目录下所有文件和目录名称，返回元组path, dirnames, filenames
os.path.walk('.')

# 返回当前文件名称
os.path.basename(__file__)

# 返回当前文件所在目录（不含文件名）
os.path.dirname(__file__)

# 返回当前文件绝地路径（含文件名）
os.path.abspath(__file__)
# 返回父级目录绝对路径
os.path.abspath('..')
# 返回父级目录绝对路径
os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))