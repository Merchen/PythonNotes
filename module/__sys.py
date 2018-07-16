import sys

###  环境变量
#
# sys.path包含编译系统环境变量，放置在site-packages内的文件任何用户均可加载（需管理员权限）
# 添加sys.path.append()添加自定义环境变量，此方法仅一次有效
#
# windows新建系统环境变量:
#     variable name: PYTHONPATH, 变量中添加路径即可，永久有效


sys.argv()  # 包含向Python解释器传递的参数，包括脚本名
# sys.exit()                    # 退出主程序
sys.path.append('../')  # 加入上级目录至编译器环境变量