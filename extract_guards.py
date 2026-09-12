import zipfile
import re

z = zipfile.ZipFile('spider.jar')
content = z.read('assets/wexshinidie.guard').decode('utf-8', errors='replace')

# 提取所有类名（JSON key "xxx": {）
guards = re.findall(r'"([^"]+)"\s*:\s*\{', content)
unique = sorted(set(guards))
print(f"Found {len(unique)} guards")
for g in unique:
    print(g)
