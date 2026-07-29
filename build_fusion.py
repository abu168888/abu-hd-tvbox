#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""融合优化版：生产配置 + 学习成果 = 全新片源"""

import json
import re

def main():
    print("=" * 60)
    print("构建融合优化版 TVBox 配置")
    print("=" * 60)
    
    # 1. 读取生产配置（37 源，基础）
    with open('../tvbox-abu-new/config.json', 'r', encoding='utf-8') as f:
        prod_config = json.load(f)
    
    # 2. 读取完整配置（102 源，含所有类型）
    with open('../tvbox-abu-new/config_clean.json', 'r', encoding='utf-8') as f:
        clean_config = json.load(f)
    
    prod_sites = prod_config['sites']
    clean_sites = clean_config['sites']
    
    print(f"\n生产配置: {len(prod_sites)} 个源")
    print(f"完整配置: {len(clean_sites)} 个源")
    
    # 3. 按分类整理
    categories = {
        '配置中心': ['csp_WexConfigGuard'],
        '豆瓣': ['csp_NewDouBanGuard', 'csp_DouBan'],
        '4K 超清': [
            'csp_New4KZnGuard', 'csp_NewWoggGuard', 'csp_NewJuTouGuard',
            'csp_NewDuoDuoGuard', 'csp_NewMuOuGuard', 'csp_NewZhiZhenGuard',
            'csp_NewHuBanGuard', 'csp_NewGuanYingGuard', 'csp_NewErXiaoGuard',
            'csp_NewPanMe123Guard', 'csp_MyPan123Guard', 'csp_WexembyGuard',
            'csp_Duopan', 'csp_WexWo123panGuard',
        ],
        '秒播专线': [
            'csp_WexWenCaiGuard', 'csp_WexReBoGuard', 'csp_WexJianPianGuard',
            'csp_WexYiYsGuard', 'csp_WexV6DaShiXiongGuard', 'csp_WexV6TeGouGuard',
            'csp_WexHanXiaoQuanGuard', 'csp_WexDuBoKuGuard', 'csp_WexGuaZiGuard',
            'csp_WexBoBoGuard', 'csp_WexIkanBotGuard', 'csp_WexXb6vGuard',
            'csp_WexYueYueGuard', 'csp_WexTangDouGuard',
        ],
        '短剧专区': [
            'csp_DuanJuHaoKanGuard', 'csp_DuanJuHeMaGuard', 'csp_DuanJuQiMiaoGuard',
            'csp_DuanJuWeiGuanGuard', 'csp_DuanJuXingYaGuard',
            'csp_ManJuQiMaoGuard', 'csp_ManJuHuoLongGuard', 'csp_ManJuXiFanGuard',
            'csp_ManJuHongGuoGuard',
        ],
        '体育直播': [
            'csp_SportFeiQiuGuard', 'csp_SportGuaZiGuard', 'csp_SportKaFeiGuard',
            'csp_SportKanQiuTongGuard', 'csp_SportKanqiuGuard', 'csp_SportWweGuard',
            'csp_GZsportGuard', 'csp_WexGZsportGuard',
        ],
        '动漫精选': [
            'csp_AnimeFanShuGuard', 'csp_AnimeHuaziGuard', 'csp_AnimeMiaoWuGuard',
            'csp_AnimeMoDuGuard', 'csp_AnimeMiaoWuGuard',
        ],
        '搜索聚合': [
            'csp_So97SoGuard', 'csp_SoHaiYinGuard', 'csp_SoTySoGuard',
            'csp_SoBaiDuSoGuard',
        ],
        '直播频道': [
            'csp_LiveBiLiGuard', 'csp_LiveDouYuGuard', 'csp_LiveHuYaGuard',
        ],
        '其他': [
            'csp_BiliGuard', 'csp_EmbyGuard', 'csp_Gz360',
        ]
    }
    
    # 4. 构建已使用的 key 集合
    used_keys = set()
    
    # 5. 按优先级构建新 sites 列表
    new_sites = []
    added_by_category = {}
    
    for category, guards in categories.items():
        added_by_category[category] = []
        
        for site in clean_sites:
            api = site.get('api', '')
            if api in guards and site.get('key') not in used_keys:
                # 优先使用生产配置中的完整版本
                prod_match = None
                for ps in prod_sites:
                    if ps.get('api') == api:
                        prod_match = ps
                        break
                
                # 使用生产配置的版本（如果有完整配置），否则用 clean 的
                use_site = prod_match if prod_match else site
                
                # 确保有必要参数
                if use_site.get('type') == 3 and 'searchable' not in use_site:
                    use_site['searchable'] = 1
                if use_site.get('type') == 3 and 'quickSearch' not in use_site:
                    use_site['quickSearch'] = 1
                
                # 清理重复的 key
                new_sites.append(use_site)
                used_keys.add(use_site.get('key'))
                added_by_category[category].append(use_site.get('name'))
    
    # 6. 输出统计
    print("\n" + "=" * 60)
    print("融合结果统计:")
    print("-" * 60)
    total = 0
    for category in added_by_category:
        count = len(added_by_category[category])
        total += count
        if count > 0:
            print(f"  {category}: {count} 个")
    print(f"\n总计: {total} 个源")
    print("=" * 60)
    
    # 7. 构建最终配置
    final_config = {
        "spider": "https://abu168888.github.io/tvbox-config/spider.jar",
        "wallpaper": "https://jianbian.chuqiuyu.workers.dev",
        "logo": "https://storage.7x24cc.com/storage-server/presigned/ss1/a6-online-fileupload/newMediaFile/3CEAE9E_773_wexfnw_20250911190012684newMediaFile.gif",
        "sites": new_sites,
        "_version": {
            "type": "4.0-fusion-optimized",
            "created": "2026-07-29",
            "total_sources": len(new_sites),
            "description": "王二小37源精华 + 学习成果融合优化版",
            "features": [
                "保留配置中心/豆瓣/搜索",
                "保留所有体育源",
                "补全动漫/搜索/直播频道",
                "优先使用生产配置完整版本",
                "去重后保留所有可用源"
            ]
        }
    }
    
    # 8. 保存
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(final_config, f, ensure_ascii=False, indent=2)
    
    print(f"\n已生成: config.json ({len(new_sites)} 个源)")
    print("按分类排序:")
    for category in added_by_category:
        if added_by_category[category]:
            print(f"\n  === {category} ===")
            for name in added_by_category[category]:
                # 清理 emoji 打印
                clean_name = name
                for ch in clean_name:
                    if ord(ch) > 0xFFFF:
                        clean_name = clean_name.replace(ch, '')
                print(f"    - {clean_name}")
    
    print("\n" + "=" * 60)
    print("完成!")

if __name__ == '__main__':
    main()
