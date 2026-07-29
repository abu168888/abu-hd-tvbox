#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""混合架构最终版 - 35 源 + 自主采集 API"""

import json

def get_order(site):
    """获取排序顺序"""
    api = site.get('api', '')
    name = site.get('name', '')
    
    if 'Wexconfig' in name or 'Config' in name:
        return 0
    if 'DouBan' in api or '豆瓣' in name:
        return 1
    if '4K' in api or '4K' in name:
        return 2
    if 'WenCai' in api or 'ReBo' in api or 'BoBo' in api or 'YiYs' in api or 'GuaZi' in api or 'JianPian' in api:
        return 3
    if 'DuanJu' in api or 'ManJu' in api:
        return 4
    if 'Sport' in api:
        return 5
    if 'Search' in name or '九七' in name or 'So97' in api or 'SoHai' in api or 'SoTy' in api:
        return 6
    if 'Self' in api:
        return 7
    return 8

def main():
    print("=" * 60)
    print("混合架构最终版配置")
    print("=" * 60)
    
    # 读取现有 35 源
    with open('config.json', 'r', encoding='utf-8') as f:
        current_config = json.load(f)
    
    sites = current_config['sites']
    print(f"\n现有源: {len(sites)} 个")
    
    # 添加自主采集 API 源
    autonomous_sources = [
        {
            "key": "SelfShortDrama",
            "name": "🎬短剧┃自主采集",
            "type": 3,
            "api": "csp_SelfShortDrama",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0,
            "ext": "http://192.168.1.100:5000/api/v1/short_drama"
        },
        {
            "key": "SelfVariety",
            "name": "📺综艺┃自主采集",
            "type": 3,
            "api": "csp_SelfVariety",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0,
            "ext": "http://192.168.1.100:5000/api/v1/variety"
        },
        {
            "key": "SelfHot",
            "name": "🔥热门┃自主采集",
            "type": 3,
            "api": "csp_SelfHot",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0,
            "ext": "http://192.168.1.100:5000/api/v1/hot"
        }
    ]
    
    # 合并
    all_sites = sites + autonomous_sources
    
    # 排序
    all_sites.sort(key=lambda x: get_order(x))
    
    # 统计
    print("\n分类统计:")
    categories = {}
    for site in all_sites:
        order = get_order(site)
        cat_names = {
            0: '配置中心',
            1: '豆瓣',
            2: '4K 超清',
            3: '秒播专线',
            4: '短剧专区',
            5: '体育直播',
            6: '搜索',
            7: '自主采集'
        }
        cat_name = cat_names.get(order, '其他')
        categories[cat_name] = categories.get(cat_name, 0) + 1
    
    for cat, count in categories.items():
        if count > 0:
            print(f"  {cat}: {count} 个")
    
    total = sum(categories.values())
    print(f"\n总计: {total} 个源")
    
    # 保存最终配置
    final_config = {
        "spider": "https://abu168888.github.io/tvbox-config/spider.jar",
        "wallpaper": "https://jianbian.chuqiuyu.workers.dev",
        "logo": "https://storage.7x24cc.com/storage-server/presigned/ss1/a6-online-fileupload/newMediaFile/3CEAE9E_773_wexfnw_20250911190012684newMediaFile.gif",
        "sites": all_sites,
        "_version": {
            "type": "6.0-hybrid-architecture",
            "created": "2026-07-29",
            "total_sources": total,
            "description": "混合架构 - 35 源 + 3 自主采集 API",
            "features": [
                "配置中心",
                "豆瓣热门",
                "4K 超清",
                "秒播专线",
                "短剧专区",
                "体育直播",
                "搜索聚合",
                "自主采集（短剧/综艺/热门）"
            ],
            "autonomous_api": {
                "base_url": "http://192.168.1.100:5000",
                "docs": "/api/v1",
                "health": "/health",
                "collectors": ["short_drama", "variety", "hot"]
            }
        }
    }
    
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(final_config, f, ensure_ascii=False, indent=2)
    
    print(f"\n生成完成: {total} 个源")

if __name__ == '__main__':
    main()
