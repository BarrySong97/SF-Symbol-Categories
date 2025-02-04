import plistlib
from collections import defaultdict
import json

def process_plist():
    # 读取plist文件
    with open('symbol_categories.plist', 'rb') as fp:
        pl = plistlib.load(fp)
    
    # 使用defaultdict来按category组织icon names
    category_dict = defaultdict(list)
    
    # 遍历plist中的每个条目
    for icon_name, categories in pl.items():
        # 将每个icon添加到对应的category列表中
        for category in categories:
            category_dict[category].append(icon_name)
    
    # 将defaultdict转换为普通dict
    result = dict(category_dict)
    
    # 将结果写入JSON文件
    with open('symbol_categories.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    # 打印一些统计信息
    print(f"Total number of icons: {len(pl)}")
    print(f"Total number of categories: {len(result)}")
    for category, icons in result.items():
        print(f"{category}: {len(icons)} icons")

if __name__ == '__main__':
    process_plist() 