###  模块与包
#
# 模块载入时文件将被执行，重复载入的模块仅载入一次，可使用importlib.reload()函数重新加载
# 放置在site-packages内的文件任何用户均可加载（需管理员权限）
#
# __name__    当前文件为执行文件时，值为'__main__'；当前文件作为载入模块时，值为py文件名
# __all__     包含使用from module import * 可直接导入的内容
# __init__.py 导入包及其内的任何文件均会执行
#
# 包名drawing, 目录下含colors.py、__init__.py
# colors.py:
#     import drawing                # 仅执行__init__.py文件
#     import drawing.colors         # 导入colors.py，使用全部限定名drawing.colors.TAGNAME访问变量
#     import drawing.colors as col  # 导入colors.py，使用colors.TAGNAME访问变量
#     from drawing import colors    # 导入color.py，使用colors.TAGNAME访问变量