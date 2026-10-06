import re
from motrix_envs import registry as env_registry

path = r"D:\MotrixArena\MotrixLab\motrix_rl\src\motrix_rl\cfgs.py"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 获取已注册的环境名
registered = set(env_registry._envs.keys())

# 找出 cfgs.py 中所有 @rlcfg 引用的环境名
refs = set(re.findall(r'@rlcfg\("([^"]+)"', content))

# 找出引用了但未注册的环境
missing = refs - registered

print("=" * 60)
print("cfgs.py 引用但未注册的环境：")
for m in sorted(missing):
    print("  -", m)
print("=" * 60)

# 逐个删除对应的配置类
for env_name in missing:
    pattern = rf'(\s*@rlcfg\("{re.escape(env_name)}"\).*?)(?=\s*@rlcfg\(|\Z)'
    content = re.sub(pattern, "", content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("已删除未注册的配置类，保存完成。")