"""
第一周 线性代数练习：向量运算
每个函数对应一个核心知识点，手动实现并对比NumPy结果

知识点清单：
  1. 向量加法 —— 力的合成（平行四边形法则）
  2. 标量乘法 —— 缩放力的大小
  3. 点积 (Dot Product) —— 计算做功、判断两向量夹角
  4. 叉积 (Cross Product) —— 计算力矩、表面法线、旋转方向
"""
import numpy as np

print("=" * 60)
print("第一周 向量运算练习")
print("=" * 60)

# ===== 知识点1：向量加法 =====
# 物理意义：两个力的合成（平行四边形法则）
print("\n--- 知识点1：向量加法（力的合成）---")


def vector_add(v1, v2):
    """手动实现向量加法"""
    return [v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]]


force_wind = [1.0, 0.0, 0.0]       # 风力：沿X轴正方向，1N
force_gravity = [0.0, -9.8, 0.0]    # 重力：沿Y轴向下，9.8N
force_total = vector_add(force_wind, force_gravity)
print(f"风力:        {force_wind}")
print(f"重力:        {force_gravity}")
print(f"合力(手动):  {force_total}")
print(f"合力(NumPy): {np.add(force_wind, force_gravity)}")

# ===== 知识点2：标量乘法 =====
# 物理意义：缩放力的大小（或反向）
print("\n--- 知识点2：标量乘法（缩放力的大小）---")


def scalar_multiply(s, v):
    """手动实现标量乘法"""
    return [s * v[0], s * v[1], s * v[2]]


force_double = scalar_multiply(2.0, force_wind)
force_half = scalar_multiply(0.5, force_gravity)
force_reverse = scalar_multiply(-1.0, force_wind)
print(f"2倍风力:     {force_double}")
print(f"0.5倍重力:   {force_half}")
print(f"反向风力:    {force_reverse}")

# ===== 知识点3：点积 (Dot Product) =====
# 物理意义1：力·位移 = 做功
# 物理意义2：判断两向量夹角 cosθ = a·b / (|a||b|)
print("\n--- 知识点3：点积（做功 + 夹角判断）---")


def dot_product(v1, v2):
    """手动实现点积"""
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


# 用途A：计算做功 W = F·d
force = [0.0, 0.0, 10.0]         # 10N沿Z轴
displacement = [0.0, 0.0, 5.0]    # 物体移动5米沿Z轴
work = dot_product(force, displacement)
print(f"力:          {force}")
print(f"位移:        {displacement}")
print(f"做功(手动):  {work} 焦耳")
print(f"做功(NumPy): {np.dot(force, displacement)} 焦耳")

# 力与位移垂直时不做功
force_perp = [10.0, 0.0, 0.0]     # 力沿X轴
displacement_perp = [0.0, 5.0, 0.0]  # 位移沿Y轴
work_perp = dot_product(force_perp, displacement_perp)
print(f"\n垂直力·位移: {work_perp} 焦耳 (力⊥位移，不做功)")

# 用途B：判断两向量夹角
a = np.array([1, 0, 0])   # X轴方向
b = np.array([0, 1, 0])   # Y轴方向
c = np.array([1, 1, 0])   # 45°方向
cos_angle_ab = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
cos_angle_ac = np.dot(a, c) / (np.linalg.norm(a) * np.linalg.norm(c))
angle_ab = np.degrees(np.arccos(cos_angle_ab))
angle_ac = np.degrees(np.arccos(cos_angle_ac))
print(f"\na=(1,0,0) 与 b=(0,1,0) 夹角: {angle_ab:.0f}° (正交)")
print(f"a=(1,0,0) 与 c=(1,1,0) 夹角: {angle_ac:.0f}° (45°)")

# 点积为正 → 夹角<90°（同向趋势）
# 点积为零 → 夹角=90°（正交）
# 点积为负 → 夹角>90°（反向趋势）
d = np.array([-1, 0, 0])
cos_ad = np.dot(a, d) / (np.linalg.norm(a) * np.linalg.norm(d))
print(f"a=(1,0,0) 与 d=(-1,0,0) 点积: {np.dot(a,d):.0f} → 夹角: {np.degrees(np.arccos(cos_ad)):.0f}° (反向)")

# ===== 知识点4：叉积 (Cross Product) =====
# 物理意义1：力矩 = 力臂 × 力
# 物理意义2：计算三角形面法线
print("\n--- 知识点4：叉积（力矩 + 法线计算）---")


def cross_product(v1, v2):
    """手动实现叉积 a×b"""
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0],
    ]


# 用途A：计算力矩 τ = r × F
lever_arm = [1.0, 0.0, 0.0]    # 力臂：沿X轴1米
force = [0.0, 0.0, 10.0]        # 力：沿Z轴10N
torque_manual = cross_product(lever_arm, force)
torque_np = np.cross(lever_arm, force)
print(f"力臂(r):     {lever_arm}")
print(f"力(F):       {force}")
print(f"力矩(手动):  {torque_manual}  N·m")
print(f"力矩(NumPy): {list(torque_np)}  N·m")
print("→ 力矩沿Y轴负方向，物体会绕Y轴旋转")

# 用途B：计算三角形面法线
# 三个顶点定义一个三角形
p1 = np.array([0, 0, 0])
p2 = np.array([1, 0, 0])
p3 = np.array([0, 1, 0])
edge1 = p2 - p1  # 边1：沿X轴
edge2 = p3 - p1  # 边2：沿Y轴
normal = np.cross(edge1, edge2)
normal_normalized = normal / np.linalg.norm(normal)
print(f"\n三角形顶点: p1={p1}, p2={p2}, p3={p3}")
print(f"边1(edge1): {edge1}")
print(f"边2(edge2): {edge2}")
print(f"面法线:      {normal_normalized}")
print("→ 法线指向Z轴正方向，三角形正面朝上")

# 叉积的大小 |a×b| = |a||b|sinθ —— 等于两向量围成的平行四边形面积
area_parallelogram = np.linalg.norm(np.cross(edge1, edge2))
area_triangle = area_parallelogram / 2
print(f"\n平行四边形面积: {area_parallelogram:.2f}")
print(f"三角形面积:     {area_triangle:.2f}")

# ===== 知识点5：右手定则演示 =====
# 叉积方向由右手定则确定
print("\n--- 知识点5：右手定则验证 ---")
x_axis = np.array([1, 0, 0])
y_axis = np.array([0, 1, 0])
z_axis = np.array([0, 0, 1])

print(f"X × Y = {np.cross(x_axis, y_axis)}  (应等于Z轴正方向)")
print(f"Y × X = {np.cross(y_axis, x_axis)}  (应等于Z轴负方向，反交换律!)")
print(f"Y × Z = {np.cross(y_axis, z_axis)}  (应等于X轴正方向)")
print(f"Z × X = {np.cross(z_axis, x_axis)}  (应等于Y轴正方向)")
print("\n→ 叉积满足反交换律: a×b = -(b×a)")

print("\n" + "=" * 60)
print("向量运算练习完成！")
print("=" * 60)
