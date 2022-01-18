# iOS-Script-Tools
a script tool set for iOS OC

## find_sdk_use_classname.py
python3 find_sdk_use_classname.py

在项目的迭代的过程中，我们需要不断解决线上的crash问题，而有些crash可能是我们接入的一些SDK引起的，有时候单从名字上我们无法判断出crash是属于哪个SDK的。所以经常会遇到需要向所有合作的三方SDK进行询问来找到crash的来源。
该脚本，支持传入类名/分类名，来查找是哪个SDK使用的，帮助我们找到crash来源。
