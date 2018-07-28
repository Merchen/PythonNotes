模块与包
===

    模块在import时执行初始化，仅载入一次
    可使用importlib.reload()函数重新加载
    
    __init__.py在导入包时自动执行

    放置在site-packages内的文件任何用户均可加载（需管理员权限）
    
    注释：
        package为特殊目录(包), 包含__init__.py
        directory为一般目录, 不含__init__.py
        module为模块, 即xxx.py文件
<br>

> ## import package
    以package.xxx形式引用
    xxx: module/__init__文件中定义的函数和变量及导入的所有对象
    
    不能访问package下的package或directory(若未在__init__中导入)
    如import concurrent, 其__init__文件为空, 则只能访问concurrent下的module
<br>

> ## import module
    以module.xxx形式引用
    xxx: 内部定义的function/tag/模块导入的任何对象如package、module、funtion、tag
<br>

> ## import xxx.yyy
    以xxx.yyy全名称形式引用
    
    import package.package/module/funtion/tag
    # funtion/tag为__init__文件中的函数和变量及导入的所有对象
    
    import directory.package/module
    import module.fuction/tag/package/module
    
    yyy = directory无效
    import directory无效
    以directory.xxx访问不到任何对象
<br> 

> ## from xxx import yyy
    以yyy形式引用
    
    from package import module/package/function/tag
    from directory import package/module
    from module import function/tag/package/module
   
    yyy = *表示导入所有对象, 并以无前缀(命名空间)的方式引用yyy中的模块/函数/变量
<br> 


\_\_name__
---
    当前文件为执行文件时，__name__ = '__main__'；
    当前文件作为载入模块时，__name__ = 文件名

     
\_\_all__
---  
    包含使用from module import * 导入的内容

