import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 修复网盘源的 ext 参数
pan_fixes = {
    'WexWoquark': {  # 夸克
        'ext': 'https://raw.githubusercontent.com/abu168888/tvbox-config/main/lib/quark_token.txt'
    },
    'WexWoBaidu': {  # 百度
        'ext': 'https://raw.githubusercontent.com/abu168888/tvbox-config/main/lib/baidu_token.txt'
    },
    'Wex115share': {  # 115
        'ext': ''
    },
    'WexWo189': {  # 天翼
        'ext': ''
    },
    'WexWo123': {  # 123
        'ext': ''
    },
    'WexXunLei': {  # 讯雷
        'ext': ''
    }
}

print("修复网盘源 ext 参数:")
for site in config['sites']:
    key = site['key']
    if key in pan_fixes:
        old_ext = site.get('ext', 'N/A')
        new_ext = pan_fixes[key]['ext']
        site['ext'] = new_ext
        print(f"  {key} | {site['name']} | ext: '{old_ext}' -> '{new_ext}'")

# 保存
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("\nconfig.json 已更新")
print("\n注意：如果 token 文件不存在，TVBox 会自动弹出扫码授权界面")