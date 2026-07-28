#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""基于真实数据的完全重建版 - 使用真实可用的 Guard 类"""

import json
from datetime import datetime

def main():
    print("=" * 60)
    print("Building REAL Fusion Config from Verified Sources")
    print("=" * 60)
    
    # Load base clean config (26KB of verified sources)
    with open('../tvbox-abu-new/config_clean.json', 'r', encoding='utf-8') as f:
        clean_config = json.load(f)
    
    clean_sites = clean_config['sites']
    print(f"\nLoaded {len(clean_sites)} verified sources from clean config")
    
    # Define REAL guard classes by category (from all_guard_classes.json)
    category_guards = {
        '4K 超清': ['csp_New4KZnGuard', 'csp_NewWoggGuard', 'csp_WexembyGuard'],
        '秒播专线': [
            'csp_WexWenCaiGuard',      # 文才
            'csp_WexReBoGuard',        # 热播
            'csp_WexJianPianGuard',    # 贱片
            'csp_WexYiYsGuard',        # 伊影
            'csp_WexV6DaShiXiongGuard', # 师兄
            'csp_WexV6TeGouGuard',     # 太狗
            'csp_WexHanXiaoQuanGuard', # 厂长
            'csp_WexDuBoKuGuard',      # 独播库
            'csp_WexGuaZiGuard',       # 瓜子
            'csp_WexBoBoGuard',        # 伯伯
            'csp_WexIkanBotGuard',     # 爱看
            'csp_WexXb6vGuard'         # XB6V
        ],
        '短剧专区': [
            'csp_DuanJuHaoKanGuard',
            'csp_DuanJuHeMaGuard',
            'csp_DuanJuQiMiaoGuard',
            'csp_DuanJuWeiGuanGuard',
            'csp_DuanJuXingYaGuard',
            'csp_ManJuHongGuoGuard',
            'csp_ManJuHuoLongGuard',
            'csp_ManJuQiMaoGuard',
            'csp_ManJuXiFanGuard'
        ],
        '体育直播': [
            'csp_SportFeiQiuGuard',
            'csp_SportGuaZiGuard',
            'csp_SportKaFeiGuard',
            'csp_SportKanQiuTongGuard',
            'csp_SportKanqiuGuard',
            'csp_SportWweGuard'
        ]
    }
    
    # Build new config using only REAL, verified sources
    new_sites = []
    added_keys = set()
    
    # Extract and organize by category
    for category, guards in category_guards.items():
        print(f"\n{category}:")
        count = 0
        
        for site in clean_sites:
            api = site.get('api', '')
            if api in guards and site.get('key') not in added_keys:
                # Clean name - remove all emojis and special chars
                import re
                orig_name = site.get('name', '')
                clean_name = re.sub(r'\x00-\x1F|\uFEFF|\U0001F300-\U0001F9FF', '', orig_name).strip()
                site['name'] = f"[{category}] {clean_name}"
                
                new_sites.append(site)
                added_keys.add(site.get('key'))
                count += 1
                print(f"  + API: {api}")
        
        print(f"  Count: {count}")
    
    # Final config
    final_config = {
        "spider": "https://abu168888.github.io/tvbox-config/spider.jar",
        "wallpaper": "https://jianbian.chuqiuyu.workers.dev",
        "logo": "https://storage.7x24cc.com/storage-server/presigned/ss1/a6-online-fileupload/newMediaFile/3CEAE9E_773_wexfnw_20250911190012684newMediaFile.gif",
        "sites": new_sites,
        "_version": {
            "type": "3.0-real-fusion",
            "created": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "total_sources": len(new_sites),
            "note": "All sources use REAL verified Guard classes"
        }
    }
    
    # Save
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(final_config, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 60)
    print(f"SUCCESS: Generated {len(new_sites)} real sources")
    print("Output: config.json")
    print("=" * 60)

if __name__ == '__main__':
    main()
