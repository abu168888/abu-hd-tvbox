import json
from datetime import datetime

# 使用旧仓库验证过的完整配置
verified_config = {
  "spider": "https://abu168888.github.io/abu-hd-tvbox/spider.jar",
  "wallpaper": "https://jianbian.chuqiuyu.workers.dev",
  "logo": "https://storage.7x24cc.com/storage-server/presigned/ss1/a6-online-fileupload/newMediaFile/3CEAE9E_773_wexfnw_20250911190012684newMediaFile.gif",
  "sites": [
    {"key": "DoubanHD", "name": "[阿不 HD] 更新于{DATE}", "type": 3, "api": "csp_NewDouBanGuard", "indexs": 1, "searchable": 0, "quickSearch": 0, "filterable": 0, "ext": "https://abu168888.github.io/abu-hd-tvbox/lib/20260414181247-ae51abfbfe.txt"},
    {"key": "WexEmby", "name": "[emby]4K", "type": 3, "api": "csp_WexembyGuard", "searchable": 1, "changeable": 1},
    {"key": "NewPanMe123", "name": "[123]4K", "type": 3, "api": "csp_NewPanMe123Guard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "原盘", "name": "[原盘]4K", "type": 3, "api": "csp_New4KZnGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "阿不", "name": "[指南]4K", "type": 3, "api": "csp_NewErXiaoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "玩偶", "name": "[玩偶]4K", "type": 3, "api": "csp_NewWoggGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "NewJuTou", "name": "[剧透]4K", "type": 3, "api": "csp_NewJuTouGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "NewDuoDuo", "name": "[多多]4K", "type": 3, "api": "csp_NewDuoDuoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "NewMuOu", "name": "[木偶]4K", "type": 3, "api": "csp_NewMuOuGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "NewZhiZhen", "name": "[至臻]4K", "type": 3, "api": "csp_NewZhiZhenGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "NewHuBan", "name": "[虎斑]4K", "type": 3, "api": "csp_NewHuBanGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "NewGuanYing", "name": "[观影]4K", "type": 3, "api": "csp_NewGuanYingGuard", "searchable": 1, "quickSearch": 1, "changeable": 0, "timeout": 120},
    {"key": "Auto_Bili", "name": "秒播 [Bili]", "type": 3, "api": "csp_BiliGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "Auto_Emby2", "name": "秒播 [Emby]", "type": 3, "api": "csp_EmbyGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "SportGuaZi", "name": "[瓜子] 体育", "type": 3, "api": "csp_SportGuaZiGuard", "searchable": 1, "changeable": 0, "style": {"type": "list"}},
    {"key": "GuaziKQ", "name": "[瓜子] 体育 2", "type": 3, "api": "csp_WexGZsportGuard", "searchable": 1, "changeable": 0, "style": {"type": "list"}},
    {"key": "WexBoBo", "name": "[伯伯] 秒播", "type": 3, "api": "csp_WexBoBoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "新 6V", "name": "[新 6V] 磁力", "type": 3, "api": "csp_WexXb6vGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexIkanBot", "name": "[爱看] 采集", "type": 3, "api": "csp_WexIkanBotGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexYiYs", "name": "[伊影] 秒播", "type": 3, "api": "csp_WexYiYsGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexV6TeGou", "name": "[太狗] 秒播", "type": 3, "api": "csp_WexV6TeGouGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexV6DaShiXiong", "name": "[师兄] 秒播", "type": 3, "api": "csp_WexV6DaShiXiongGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexWenCai", "name": "[文才] 秒播", "type": 3, "api": "csp_WexWenCaiGuard", "searchable": 1, "quickSearch": 1, "changeable": 1},
    {"key": "WexReBo", "name": "[热播] 秒播", "type": 3, "api": "csp_WexReBoGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexDuBoKu", "name": "[独播] 秒播", "type": 3, "api": "csp_WexDuBoKuGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexGuaZi", "name": "[瓜子] 秒播", "type": 3, "api": "csp_WexGuaZiGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "贱片", "name": "[贱片] 秒播", "type": 3, "api": "csp_WexJianPianGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexYueYue", "name": "[闪电] 秒播", "type": 3, "api": "csp_WexYueYueGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexHanXiaoQuan", "name": "[韩剧] 秒播", "type": 3, "api": "csp_WexHanXiaoQuanGuard", "searchable": 1, "quickSearch": 1, "changeable": 0},
    {"key": "WexWoquark", "name": "[夸克]", "type": 3, "api": "csp_WexWoquarkpanGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "WexWoBaidu", "name": "[百度]", "type": 3, "api": "csp_WexWoBaiduPanGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "Wex115share", "name": "[115]", "type": 3, "api": "csp_Wex115shareGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "WexWo189", "name": "[天翼]", "type": 3, "api": "csp_WexWo189Guard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "WexWo123", "name": "[123]", "type": 3, "api": "csp_WexWo123panGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "WexXunLei", "name": "[讯雷]", "type": 3, "api": "csp_WexWoXunLeiPanGuard", "searchable": 1, "changeable": 1, "timeout": 50, "style": {"type": "list"}, "ext": ""},
    {"key": "DuanJuHaoKan", "name": "[短剧] 好看", "type": 3, "api": "csp_DuanJuHaoKanGuard", "searchable": 1, "changeable": 0},
    {"key": "DuanJuQiMiao", "name": "[短剧] 小猫", "type": 3, "api": "csp_DuanJuQiMiaoGuard", "searchable": 1, "changeable": 0},
    {"key": "BookYueTing", "name": "[悦庭] 听书", "type": 3, "api": "csp_BookYueTingGuard", "searchable": 1, "changeable": 0, "timeout": 120},
    {"key": "BookShiJie", "name": "[极品] 听书", "type": 3, "api": "csp_BookShiJieGuard", "searchable": 1, "changeable": 0},
    {"key": "KanQiu", "name": "[88] 体育", "type": 3, "api": "csp_KanqiuGuard", "searchable": 1, "changeable": 0, "style": {"type": "list"}},
    {"key": "SportWwe", "name": "[WWE] 体育", "type": 3, "api": "csp_SportWweGuard", "searchable": 1, "changeable": 0, "style": {"type": "list"}},
    {"key": "push_agent", "name": "推送", "type": 3, "api": "csp_PushGuard", "searchable": 1, "changeable": 0}
  ],
  "parses": [{"name": "解析 1", "url": "https://jx.m3u8.tv/jiexi/?url="}],
  "lives": [],
  "doh": [{"name": "Google", "url": "https://dns.google/dns-query", "ips": ["8.8.4.4", "8.8.8.8"]}],
  "rules": [],
  "ads": []
}

# 更新日期替换
for site in verified_config['sites']:
    if 'DATE' in site.get('name', ''):
        site['name'] = site['name'].replace('{DATE}', datetime.now().strftime('%Y%m%d'))

with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(verified_config, f, ensure_ascii=False, indent=2)

print("已成功复制已验证配置")
print(f"总源数：{len(verified_config['sites'])}")

# 分类统计
cats = {}
for s in verified_config['sites']:
    name = s.get('name', '')
    if '4K' in name or '玩偶' in name:
        category = '4K 源'
    elif '秒播' in name:
        category = '秒播影视'
    elif '短剧' in name:
        category = '短剧源'
    elif '夸克' in name or '百度' in name or '网盘' in name:
        category = '网盘源'
    elif '体育' in name:
        category = '体育源'
    elif '听书' in name:
        category = '听书源'
    else:
        category = '其他'
    
    cats[category] = cats.get(category, 0) + 1

print("\n分类统计:")
for k, v in sorted(cats.items()):
    print(f"  {k}: {v}")