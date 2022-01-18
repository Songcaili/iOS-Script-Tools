#!/usr/bin/python3

import os

def collectAllSDK(project_dir):
    sdks = set()
    frameworks = os.popen('find %s -name \"*.framework\"' % project_dir).read().splitlines()
    for path in frameworks:
        sdkName = path.split('/')[-1].split('.')[0]
        path = os.path.join(path, sdkName)
        if os.path.isfile(path):
            sdks.add(path)
    sdks = sdks.union(os.popen('find %s -name \"*.a\"' % project_dir).readlines())
    return sdks

def findClassSDK(project_dir):
    sdks = collectAllSDK(project_dir)

    findClass = input(
        'Please input query classname or categoryname(分类声明括号中的名字)。\n').strip()
    result = ""
    for sdk in sdks:
        sdkName = os.path.basename(sdk)
        classNameSet = set()
        lines = os.popen('/usr/bin/otool -v -s __TEXT __objc_classname %s' % sdk).readlines()
        lines = list(filter(lambda x: x[0].isdigit(), lines))
        for line in lines:
            line = line[16:].strip()
            classNameSet.add(line)
        if findClass in classNameSet:
            result = result + sdkName + " "
            if len(result) > 0:
                print("结果：" + result)
            else:
                print("没有在库中找到该符号，请检测输入类名是否正确，或者是否为项目主工程中定义的类")

if __name__ == '__main__':
    project_dir = input(
        'Please input app project root path:\n').strip()
    if not os.path.isdir(project_dir):
        exit('Error: project path error')
    findClassSDK(project_dir)
