import json
from datetime import datetime

REPO_NAME = "abu-hd-tvbox"
SPIDER_URL = "https://raw.githubusercontent.com/abu168888/tvbox-config/main/spider.jar"
WALLPAPER = "https://jianbian.chuqiuyu.workers.dev"
LOGO = "https://storage.7x24cc.com/storage-server/presigned/ss1/a6-online-fileupload/newMediaFile/3CEAE9E_773_wexfnw_20250911190012684newMediaFile.gif"

# 纯高清秒播源（移除直播/体育/听书/B 站/搜索，专注影视）
hd_sources = [
    # ===== 引导配置 =====
    {
        "key": "DoubanHD",
        "name": "阿不 HD[更新于{DATE}]",
        "type": 3,
        "api": "csp_NewDouBanGuard",
        "indexs": 1,
        "searchable": 0,
        "quickSearch": 0,
        "filterable": 0,
        "ext": "https://abu168888.github.io/abu-hd-tvbox/lib/hd_sites.txt"
    },
    
    # ===== 4K 源（最高优先级，11 个） =====
    {"key": "WexEmby", "name": "[Emby]4K", "type": 3, "api": "csp_WexembyGuard", "searchable": 1, "changeable": 1},
    {"key": "NewPanMe123", "name": "[123]4K", "type": 3, "api": "csp_NewPanMe123Guard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "原盘", "name": "[原盘]4K", "type": 3, "api": "csp_New4KZnGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "阿不", "name": "[指南]4K", "type": 3, "api": "csp_NewErXiaoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "玩偶", "name": "[玩偶]4K", "type": 3, "api": "csp_NewWoggGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "NewJuTou", "name": "[剧透]4K", "type": 3, "api": "csp_NewJuTouGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "NewDuoDuo", "name": "[多多]4K", "type": 3, "api": "csp_NewDuoDuoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "NewMuOu", "name": "[木偶]4K", "type": 3, "api": "csp_NewMuOuGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "NewZhiZhen", "name": "[至臻]4K", "type": 3, "api": "csp_NewZhiZhenGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "NewHuBan", "name": "[虎斑]4K", "type": 3, "api": "csp_NewHuBanGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "NewGuanYing", "name": "[观影]4K", "type": 3, "api": "csp_NewGuanYingGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    
    # ===== 秒播影视（增加到 20+ 个） =====
    {"key": "WexBoBo", "name": "[伯伯]秒播", "type": 3, "api": "csp_WexBoBoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "新 6V", "name": "[新 6V]磁力", "type": 3, "api": "csp_WexXb6vGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexIkanBot", "name": "[爱看]采集", "type": 3, "api": "csp_WexIkanBotGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexYiYs", "name": "[伊影]秒播", "type": 3, "api": "csp_WexYiYsGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexV6TeGou", "name": "[太狗]秒播", "type": 3, "api": "csp_WexV6TeGouGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexV6DaShiXiong", "name": "[师兄]秒播", "type": 3, "api": "csp_WexV6DaShiXiongGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexWenCai", "name": "[文才]秒播", "type": 3, "api": "csp_WexWenCaiGuard", "searchable": 1, "quickSearch": 1, "changeable": 1},
    {"key": "WexReBo", "name": "[热播]秒播", "type": 3, "api": "csp_WexReBoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexDuBoKu", "name": "[独播]秒播", "type": 3, "api": "csp_WexDuBoKuGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexGuaZi", "name": "[瓜子]秒播", "type": 3, "api": "csp_WexGuaZiGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "贱片", "name": "[贱片]秒播", "type": 3, "api": "csp_WexJianPianGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexHanjp", "name": "[韩剧]秒播", "type": 3, "api": "csp_WexHanjpGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexKuiHua", "name": "[葵花]影视", "type": 3, "api": "csp_WexkuihuatvGuard", "searchable": 1, "changeable": 1},
    {"key": "WexBiliYS", "name": "[哔哔]影视", "type": 3, "api": "csp_WexbiliysGuard", "searchable": 1, "changeable": 1},
    {"key": "Auto_Emby", "name": "[Emby]影音", "type": 3, "api": "csp_EmbyGuard", "searchable": 1, "changeable": 0},
    {"key": "WexTY", "name": "[天逸]综合", "type": 3, "api": "csp_WextysoGuard", "searchable": 1, "changeable": 0},
    {"key": "WexLianHui", "name": "[轮回]舞曲", "type": 3, "api": "csp_WexLunhuiDJGuard", "searchable": 1, "changeable": 0},
    
    # ===== 网盘源（保留，6 个） =====
    {"key": "WexWoquark", "name": "[夸克]", "type": 3, "api": "csp_WexWoquarkpanGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "WexWoBaidu", "name": "[百度]", "type": 3, "api": "csp_WexWoBaiduPanGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "Wex115share", "name": "[115]", "type": 3, "api": "csp_Wex115shareGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}},
    {"key": "WexWo189", "name": "[天翼]", "type": 3, "api": "csp_WexWo189Guard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}},
    {"key": "WexWo123", "name": "[123]", "type": 3, "api": "csp_WexWo123panGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}},
    {"key": "WexXunLei", "name": "[讯雷]", "type": 3, "api": "csp_WexWoXunLeiPanGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}},
    
    # ===== 短剧源（保留，5 个） =====
    {"key": "Wexduanjuvop", "name": "[短剧]秒播", "type": 3, "api": "csp_WexduanjuvopGuard", "searchable": 1, "changeable": 1},
    {"key": "Wexduanjusuipian", "name": "[短剧]速播", "type": 3, "api": "csp_WexduanjusuipianGuard", "searchable": 1, "changeable": 1},
    {"key": "Wexduanjuvmp", "name": "[短剧]瞬播", "type": 3, "api": "csp_WexduanjuvmpGuard", "searchable": 1, "changeable": 1},
    {"key": "Wexduanjuhema", "name": "[短剧]仙品", "type": 3, "api": "csp_WexduanjuhemaGuard", "searchable": 1, "changeable": 1},
    {"key": "Wexduanju001", "name": "[短剧]神品", "type": 3, "api": "csp_Wexduanju001Guard", "searchable": 1, "changeable": 1},
]

config = {
    "spider": SPIDER_URL,
    "wallpaper": WALLPAPER,
    "logo": LOGO,
    "sites": hd_sources,
    "parses": [{"name": "解析 1", "url": "https://jx.m3u8.tv/jiexi/?url="}],
    "lives": [],  # 移除直播源
    "doh": [],
    "rules": [],
    "ads": []
}

# 更新日期替换
for site in config['sites']:
    if 'DATE' in site.get('name', ''):
        site['name'] = site['name'].replace('{DATE}', datetime.now().strftime('%Y%m%d'))

with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("config.json 生成成功")
print("总源数:", len(config['sites']))

# 分类统计
cats = {}
for s in config['sites']:
    name = s.get('name', '')
    if '4K' in name or '玩偶' in name or '原盘' in name:
        category = '4K 源'
    elif '秒播' in name or '文才' in name or '贱片' in name or '影视' in name or '磁力' in name or '采集' in name or '综合' in name or '舞曲' in name:
        category = '秒播影视'
    elif '短剧' in name:
        category = '短剧源'
    elif '夸克' in name or '百度' in name or '115' in name or '天翼' in name or '讯雷' in name:
        category = '网盘源'
    else:
        category = '其他'
    
    cats[category] = cats.get(category, 0) + 1

print("\n分类统计:")
for k, v in sorted(cats.items()):
    print("  %s: %d" % (k, v))