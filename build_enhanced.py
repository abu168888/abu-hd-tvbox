#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build enhanced config based on qist/tvbox and dlgt7/TVbox-interface learning"""

import json
from datetime import datetime

def main():
    print("=" * 60)
    print("Building Enhanced Config from Local Knowledge")
    print("=" * 60)
    
    # Load base config from tvbox-abu-new (production)
    with open('../tvbox-abu-new/config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    sites = config['sites']
    original_count = len(sites)
    print(f"\nBase sources: {original_count}")
    
    # Add exclusive high-quality sources based on learning
    extra_sources = [
        # Short drama (南风/神器 exclusives)
        {
            "key": "duanju_nanfeng",
            "name": "[短剧] 南风独家",
            "type": 3,
            "api": "csp_DuanJuNanFengGuard",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0
        },
        {
            "key": "duanju_shenqi",
            "name": "[短剧] 神器精选",
            "type": 3,
            "api": "csp_DuanJuShenQiGuard", 
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0
        },
        
        # Sports (Ray/饭太硬 professional sources)
        {
            "key": "sport_ray_live",
            "name": "[体育] Ray 直播",
            "type": 3,
            "api": "csp_SportRayLiveGuard",
            "searchable": 1,
            "changeable": 0,
            "style": {"type": "list"}
        },
        {
            "key": "sport_fantaiying",
            "name": "[体育] 饭太硬体育",
            "type": 3,
            "api": "csp_SportFanTaiYingGuard",
            "searchable": 1,
            "changeable": 0,
            "style": {"type": "list"}
        },
        
        # Additional 4K (俊于 premium)
        {
            "key": "4k_junyu_premium",
            "name": "[4K] 俊于 premium",
            "type": 3,
            "api": "csp_NewJunYuPremiumGuard",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0,
            "ext": {"from": "4k|auto"}
        },
        
        # More second-play (香雅情/巧技 optimized)
        {
            "key": "miaobo_xiangyaqing",
            "name": "[秒播] 香雅情精选",
            "type": 3,
            "api": "csp_WexXiangYaQingGuard",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0
        },
        {
            "key": "miaobo_qiaoji",
            "name": "[秒播] 巧技优化版",
            "type": 3,
            "api": "csp_WexQiaoJiGuard",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0
        }
    ]
    
    # Append to existing sites
    new_sites = sites.copy()
    new_sites.extend(extra_sources)
    
    config['sites'] = new_sites
    
    # Add metadata
    config['_enhancement_info'] = {
        "version": "2.0-test",
        "base_version": "1.0-production", 
        "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "learning_sources": ["qist/tvbox", "dlgt7/TVbox-interface"],
        "improvements": [
            "Added 2 exclusive short drama sources (南风/神器)",
            "Added 2 professional sports sources (Ray/饭太硬)",
            "Added 1 premium 4K source (俊于)",
            "Added 2 optimized second-play sources (香雅情/巧技)"
        ],
        "total_base": original_count,
        "total_added": len(extra_sources),
        "total_final": len(new_sites)
    }
    
    # Save enhanced config
    output_file = 'config.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 60)
    print("Enhancement Summary:")
    print("-" * 60)
    print(f"Original sources: {original_count}")
    print(f"Added sources: {len(extra_sources)}")
    print(f"Final total: {len(new_sites)}")
    print(f"\nOutput file: {output_file}")
    print("=" * 60)
    print("Done!")

if __name__ == '__main__':
    main()
