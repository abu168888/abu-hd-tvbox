import json
from datetime import datetime

# 配置参数
REPO_NAME = "abu-hd-tvbox"
SPIDER_URL = "https://raw.githubusercontent.com/abu168888/tvbox-config/main/spider.jar"
WALLPAPER = "https://jianbian.chuqiuyu.workers.dev"
LOGO = "https://storage.7x24cc.com/storage-server/presigned/ss1/a6-online-fileupload/newMediaFile/3CEAE9E_773_wexfnw_20250911190012684newMediaFile.gif"

# 高清影视源列表（精选 4K/蓝光/高码率）
hd_sources = [
    # ===== 引导配置 =====
    {
        "key": "DoubanHD",
        "name": "阿不 HD┃【更新于{DATE}】",
        "type": 3,
        "api": "csp_NewDouBanGuard",
        "indexs": 1,
        "searchable": 0,
        "quickSearch": 0,
        "filterable": 0,
        "ext": "https://abu168888.github.io/abu-hd-tvbox/lib/hd_sites.txt"
    },
    
    # ===== 4K 源（最高优先级） =====
    {
        "key": "WexEmby",
        "name": "🀄️Emby┃4K🀄️",
        "type": 3,
        "api": "csp_WexembyGuard",
        "searchable": 1,
        "changeable": 1
    },
    {
        "key": "NewPanMe123",
        "name": "💓123┃4K💓",
        "type": 3,
        "api": "csp_NewPanMe123Guard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "原盘",
        "name": "💓原盘┃4K💓‍",
        "type": 3,
        "api": "csp_New4KZnGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "阿不",
        "name": "💓指南┃4K‍",
        "type": 3,
        "api": "csp_NewErXiaoGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "玩偶",
        "name": "💓玩偶┃4K💓‍",
        "type": 3,
        "api": "csp_NewWoggGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "NewJuTou",
        "name": "💓剧透┃4K💓",
        "type": 3,
        "api": "csp_NewJuTouGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "NewDuoDuo",
        "name": "💓多多┃4K💓",
        "type": 3,
        "api": "csp_NewDuoDuoGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "NewMuOu",
        "name": "💓木偶┃4K💓",
        "type": 3,
        "api": "csp_NewMuOuGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "NewZhiZhen",
        "name": "💓至臻┃4K💓",
        "type": 3,
        "api": "csp_NewZhiZhenGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "NewHuBan",
        "name": "💓虎斑┃4K💓",
        "type": 3,
        "api": "csp_NewHuBanGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    {
        "key": "NewGuanYing",
        "name": "💓观影┃4K💓",
        "type": 3,
        "api": "csp_NewGuanYingGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0,
        "timeout": 120
    },
    
    # ===== 秒播影视（高清优先） =====
    {
        "key": "WexBoBo",
        "name": "🎇伯伯┃秒播🎇",
        "type": 3,
        "api": "csp_WexBoBoGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "新 6V",
        "name": "🎇新 6V┃磁力🎇",
        "type": 3,
        "api": "csp_WexXb6vGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexIkanBot",
        "name": "🎇爱看┃采集🎇",
        "type": 3,
        "api": "csp_WexIkanBotGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexYiYs",
        "name": "💥伊影┃秒播💥",
        "type": 3,
        "api": "csp_WexYiYsGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexV6TeGou",
        "name": "💥太狗┃秒播💥",
        "type": 3,
        "api": "csp_WexV6TeGouGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexV6DaShiXiong",
        "name": "💥师兄┃秒播💥",
        "type": 3,
        "api": "csp_WexV6DaShiXiongGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexWenCai",
        "name": "💥文才┃秒播💥",
        "type": 3,
        "api": "csp_WexWenCaiGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 1
    },
    {
        "key": "WexReBo",
        "name": "💥热播┃秒播💥",
        "type": 3,
        "api": "csp_WexReBoGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexDuBoKu",
        "name": "💥独播┃秒播💥",
        "type": 3,
        "api": "csp_WexDuBoKuGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexGuaZi",
        "name": "💥瓜子┃秒播💥",
        "type": 3,
        "api": "csp_WexGuaZiGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "贱片",
        "name": "💥贱片┃秒播💥",
        "type": 3,
        "api": "csp_WexJianPianGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    {
        "key": "WexHanjp",
        "name": "💥韩剧┃秒播💥",
        "type": 3,
        "api": "csp_WexHanjpGuard",
        "searchable": 1,
        "quickSearch": 1,
        "changeable": 0
    },
    
    # ===== 网盘源（高清首选） =====
    {
        "key": "WexWoquark",
        "name": "💓我的┃夸克💓",
        "type": 3,
        "api": "csp_WexWoquarkpanGuard",
        "searchable": 1,
        "changeable": 1,
        "timeout": 50,
        "style": {"type": "list"},
        "ext": ""
    },
    {
        "key": "WexWoBaidu",
        "name": "💓我的┃百度💓‍",
        "type": 3,
        "api": "csp_WexWoBaiduPanGuard",
        "searchable": 1,
        "changeable": 1,
        "timeout": 50,
        "style": {"type": "list"},
        "ext": ""
    },
    {
        "key": "Wex115share",
        "name": "💓我的┃115💓‍",
        "type": 3,
        "api": "csp_Wex115shareGuard",
        "searchable": 1,
        "changeable": 1,
        "timeout": 50,
        "style": {"type": "list"}
    },
    {
        "key": "WexWo189",
        "name": "💓我的┃天翼💓‍",
        "type": 3,
        "api": "csp_WexWo189Guard",
        "searchable": 1,
        "changeable": 1,
        "timeout": 50,
        "style": {"type": "list"}
    },
    {
        "key": "WexWo123",
        "name": "💓我的┃123💓‍",
        "type": 3,
        "api": "csp_WexWo123panGuard",
        "searchable": 1,
        "changeable": 1,
        "timeout": 50,
        "style": {"type": "list"}
    },
    {
        "key": "WexXunLei",
        "name": "💓我的┃讯雷💓‍",
        "type": 3,
        "api": "csp_WexWoXunLeiPanGuard",
        "searchable": 1,
        "changeable": 1,
        "timeout": 50,
        "style": {"type": "list"}
    },
    
    # ===== 短剧源 =====
    {
        "key": "Wexduanjuvop",
        "name": "🅰️短剧┃秒播🅰️",
        "type": 3,
        "api": "csp_WexduanjuvopGuard",
        "searchable": 1,
        "changeable": 1
    },
    {
        "key": "Wexduanjusuipian",
        "name": "🅱️短剧┃速播🅱️",
        "type": 3,
        "api": "csp_WexduanjusuipianGuard",
        "searchable": 1,
        "changeable": 1
    },
    {
        "key": "Wexduanjuvmp",
        "name": "🅾️短剧┃瞬播🅾️",
        "type": 3,
        "api": "csp_WexduanjuvmpGuard",
        "searchable": 1,
        "changeable": 1
    },
    {
        "key": "Wexduanjuhema",
        "name": "🅲短剧┃仙品🅲",
        "type": 3,
        "api": "csp_WexduanjuhemaGuard",
        "searchable": 1,
        "changeable": 1
    },
    {
        "key": "Wexduanju001",
        "name": "🅳短剧┃神品🅳",
        "type": 3,
        "api": "csp_Wexduanju001Guard",
        "searchable": 1,
        "changeable": 1
    },
    
    # ===== 体育源 =====
    {
        "key": "SportGuaZi",
        "name": "🌐瓜子┃体育🌐",
        "type": 3,
        "api": "csp_SportGuaZiGuard",
        "searchable": 1,
        "changeable": 0,
        "style": {"type": "list"}
    },
    {
        "key": "GuaziKQ",
        "name": "🌐瓜子┃体育🌐",
        "type": 3,
        "api": "csp_WexGZsportGuard",
        "searchable": 1,
        "changeable": 0,
        "style": {"type": "list"}
    },
    
    # ===== 听书源 =====
    {
        "key": "Wexlaobaitingshu",
        "name": "💥白兔┃听书💥",
        "type": 3,
        "api": "csp_WexlaobaitingshuGuard",
        "searchable": 1,
        "changeable": 0
    },
    {
        "key": "Wex275tingshu",
        "name": "💥极品┃听书💥",
        "type": 3,
        "api": "csp_Wex275tingshuGuard",
        "searchable": 1,
        "changeable": 0
    },
    
    # ===== 直播源 =====
    {
        "key": "WexNewBiLiLive",
        "name": "哔哩┃直播⚡",
        "type": 3,
        "api": "csp_WexNewBiLiLiveGuard",
        "searchable": 1,
        "changeable": 1
    },
    {
        "key": "Auto_LiveDouYu",
        "name": "⚡斗鱼┃直播⚡",
        "type": 3,
        "api": "csp_LiveDouYuGuard",
        "searchable": 1,
        "changeable": 0
    },
    {
        "key": "Auto_LiveHuYa",
        "name": "⚡虎牙┃直播⚡",
        "type": 3,
        "api": "csp_LiveHuYaGuard",
        "searchable": 1,
        "changeable": 0
    },
    
    # ===== B 站源 =====
    {
        "key": "Auto_Bili",
        "name": "♨️哔哩┃合集♨️",
        "type": 3,
        "api": "csp_BiliGuard",
        "searchable": 1,
        "changeable": 0
    },
    {
        "key": "Auto_Emby",
        "name": "♨️Emby┃影音♨️",
        "type": 3,
        "api": "csp_EmbyGuard",
        "searchable": 1,
        "changeable": 0
    },
    
    # ===== 动漫源 =====
    {
        "key": "Auto_AnimeMiaoWu",
        "name": "🎬动漫┃喵屋🎬",
        "type": 3,
        "api": "csp_AnimeMiaoWuGuard",
        "searchable": 1,
        "changeable": 0
    },
    
    # ===== 搜索聚合 =====
    {
        "key": "Auto_So97So",
        "name": "🔍九七┃搜索🔍",
        "type": 3,
        "api": "csp_So97SoGuard",
        "searchable": 1,
        "changeable": 0
    },
    {
        "key": "Auto_SoHaiYin",
        "name": "🔍海音┃搜索🔍",
        "type": 3,
        "api": "csp_SoHaiYinGuard",
        "searchable": 1,
        "changeable": 0
    }
]

# 构建 config
config = {
    "spider": SPIDER_URL,
    "wallpaper": WALLPAPER,
    "logo": LOGO,
    "sites": hd_sources,
    "parses": [
        {"name": "解析 1", "url": "https://jx.m3u8.tv/jiexi/?url="},
        {"name": "解析 2", "url": "https://www.yemu.xyz/home/vod?url="}
    ],
    "lives": [
        {"name": "直播 1", "url": "https://live.fanmingming.cn/tv/m3u/ipv6.m3u"}
    ],
    "doh": [
        {"name": "Google", "url": "https://dns.google/dns-query", "ips": ["8.8.4.4", "8.8.8.8"]},
        {"name": "Cloudflare", "url": "https://cloudflare-dns.com/dns-query", "ips": ["1.1.1.1", "1.0.0.1"]}
    ],
    "rules": [],
    "ads": []
}

# 更新日期替换
for site in config['sites']:
    if 'DATE' in site.get('name', ''):
        site['name'] = site['name'].replace('{DATE}', datetime.now().strftime('%Y%m%d'))

# 保存
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print(f"✅ config.json 生成成功")
print(f"总源数：{len(config['sites'])}")

# 分类统计
cats = {}
for s in config['sites']:
    name = s.get('name', '')
    if '4K' in name or '玩偶' in name or '原盘' in name:
        category = '4K 源'
    elif '秒播' in name or '文才' in name or '贱片' in name:
        category = '秒播影视'
    elif '短剧' in name:
        category = '短剧源'
    elif '我的┃' in name or '网盘' in name:
        category = '网盘源'
    elif '体育' in name:
        category = '体育源'
    elif '听书' in name:
        category = '听书源'
    elif '直播' in name:
        category = '直播源'
    elif '哔哩' in name or '动漫' in name:
        category = 'B 站/动漫'
    elif '搜索' in name:
        category = '搜索聚合'
    else:
        category = '其他'
    
    cats[category] = cats.get(category, 0) + 1

print("\n分类统计:")
for k, v in sorted(cats.items()):
    print(f"  {k}: {v}")
