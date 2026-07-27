import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 修复豆瓣热搜的 ext 参数
for site in config['sites']:
    if site['key'] == 'DoubanHD':
        # 使用标准的豆瓣热搜 API
        site['ext'] = 'https://raw.githubusercontent.com/abu168888/tvbox-config/main/lib/20260414181247-ae51abfbfe.txt'
        print("已修复 DoubanHD ext 参数")
        break

# 保存
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("config.json 已更新")

# 验证网盘源 ext 状态
print("\n网盘源 ext 检查:")
for site in config['sites']:
    name = site.get('name', '')
    if any(k in name for k in ['夸克', '百度', '115', '天翼', '讯雷']):
        ext = site.get('ext', 'N/A')
        changeable = site.get('changeable', 'N/A')
        print(f"  {site['key']} | {name} | ext: '{ext}' | changeable: {changeable}")