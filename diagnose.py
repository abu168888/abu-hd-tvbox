#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复配置中心、豆瓣、文才和 4K 问题"""

import json
import time
import requests

def check_url(url, desc):
    """检查 URL 是否可访问"""
    try:
        r = requests.head(url, timeout=5, allow_redirects=True)
        print(f"✅ {desc}: {url} → {r.status_code}")
        return r.status_code == 200
    except Exception as e:
        print(f"❌ {desc}: {url} → {e}")
        return False

def main():
    print("=" * 60)
    print("诊断配置加载问题")
    print("=" * 60)
    
    # 1. 检查 spider.jar
    print("\n[1] 检查 spider.jar:")
    spider_url = "https://abu168888.github.io/tvbox-config/spider.jar"
    spider_ok = check_url(spider_url, "Spider.jar")
    
    # 2. 检查豆瓣 ext 文件
    print("\n[2] 检查豆瓣 ext 文件:")
    douban_ext = "https://abu168888.github.io/tvbox-config/lib/20260414181247-ae51abfbfe.txt"
    douban_ext_ok = check_url(douban_ext, "Douban ext")
    
    # 3. 读取配置并检查
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    sites = config['sites']
    print(f"\n[3] 配置中共 {len(sites)} 个源")
    
    # 检查配置中心
    print("\n[4] 检查配置中心:")
    for s in sites:
        if 'Config' in s.get('name', '') or s.get('key') == 'Wexconfig':
            print(f"  找到: {s}")
            # 问题: searchable=0, changeable=0, indexs=0 会导致不显示
            print("  问题: searchable=0 且 indexs=0 导致不显示")
    
    # 检查豆瓣
    print("\n[5] 检查豆瓣:")
    for s in sites:
        if 'DouBan' in str(s.get('api', '')) or '豆瓣' in str(s.get('name', '')):
            print(f"  找到: {s}")
            if douban_ext_ok:
                print("  ✅ ext 文件存在")
            else:
                print("  ❌ ext 文件不存在")
    
    # 检查文才
    print("\n[6] 检查文才:")
    for s in sites:
        if 'WenCai' in str(s.get('api', '')) or '文才' in str(s.get('name', '')):
            print(f"  找到: {s}")
            if s.get('ext'):
                print(f"  ext: {s['ext']}")
                check_url(s['ext'], "WenCai API")
    
    # 检查 4K Emby
    print("\n[7] 检查 4K Emby:")
    for s in sites:
        if 'Wexemby' in str(s.get('api', '')) or 'emby' in str(s.get('name', '')):
            print(f"  找到: {s}")
    
    print("\n" + "=" * 60)
    print("诊断完成")
    print("=" * 60)

if __name__ == '__main__':
    main()
