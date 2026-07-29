#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

def clean(s):
    return ''.join(c for c in s if ord(c) < 128)

def main():
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    sites = config['sites']
    print(f"Current sources: {len(sites)}")
    
    # 1. Fix WenCai
    for site in sites:
        if site.get('api') == 'csp_WexWenCaiGuard':
            site['ext'] = 'https://api.wenchai.net'
            site['quickSearch'] = 1
            print(f"Fixed: {clean(site.get('name', ''))}")
    
    # 2. Add missing
    missing = [
        {
            "key": "Wexconfig",
            "name": "Config Center",
            "type": 3,
            "api": "csp_WexConfigGuard",
            "searchable": 0,
            "changeable": 0,
            "indexs": 0,
            "style": {"type": "list"}
        },
        {
            "key": "NewDouBan",
            "name": "Douban Hot",
            "type": 3,
            "api": "csp_NewDouBanGuard",
            "indexs": 1,
            "searchable": 0,
            "quickSearch": 0,
            "filterable": 0,
            "ext": "https://abu168888.github.io/tvbox-config/lib/20260414181247-ae51abfbfe.txt"
        },
        {
            "key": "So97So",
            "name": "Search 97",
            "type": 3,
            "api": "csp_So97SoGuard",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0
        },
        {
            "key": "SoHaiYin",
            "name": "Search HaiYin",
            "type": 3,
            "api": "csp_SoHaiYinGuard",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0
        },
        {
            "key": "SoTySo",
            "name": "Search TySo",
            "type": 3,
            "api": "csp_SoTySoGuard",
            "searchable": 1,
            "quickSearch": 1,
            "changeable": 0
        }
    ]
    
    existing_keys = {s.get('key') for s in sites}
    added = 0
    
    for src in missing:
        if src['key'] not in existing_keys:
            sites.append(src)
            existing_keys.add(src['key'])
            added += 1
            print(f"Added: {clean(src['name'])}")
    
    config['sites'] = sites
    config['_version'] = {
        "type": "5.0-optimized",
        "created": "2026-07-29",
        "total": len(sites),
        "notes": "Added config center, douban, search. Fixed WenCai ext."
    }
    
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"Done. Total: {len(sites)} sources. Added: {added}")

if __name__ == '__main__':
    main()
