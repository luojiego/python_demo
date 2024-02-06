# 生成60年天干地支循环列表
def generate_ganzhi_cycle():
    # 天干
    tian_gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    # 地支
    di_zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    
    # 生成60年的天干地支循环
    cycle = []
    for i in range(60):
        cycle.append(f"{i}: {tian_gan[i % 10]}{di_zhi[i % 12]}")
    
    return cycle

# 调用函数并打印结果
ganzhi_cycle = generate_ganzhi_cycle()
print(ganzhi_cycle)

