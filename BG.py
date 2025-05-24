from PIL import Image, ImageDraw
import random
import sys

# 获取命令行参数，如果没有提供则使用默认值
pixel_size = int(sys.argv[1]) if len(sys.argv) > 1 else 4

# 创建画布
canvas_size = 1920  # 画布大小
border_width = 0   # 边框宽度
frames = 60       # 总帧数（增加帧数使动画更流畅）
duration = 50     # 每帧持续时间（毫秒，减小使动画更快）

# 定义颜色
colors = [
    "#ff0000",  # 红色
    "#00ff00",  # 绿色
    "#0000ff",  # 蓝色
    "#ffff00",  # 黄色
    "#800080",  # 紫色
    "#000000"   # 黑色
]

# 创建帧列表
frames_list = []

# 生成帧
for frame in range(frames):
    # 创建新图像
    img = Image.new('RGB', (canvas_size, canvas_size), '#000000')
    draw = ImageDraw.Draw(img)

    # 绘制彩色方块
    for x in range(0, canvas_size, pixel_size):
        for y in range(0, canvas_size, pixel_size):
            # 随机选择一个颜色
            color = random.choice(colors)
            # 绘制方块
            draw.rectangle([
                x, y,
                x + pixel_size - border_width,
                y + pixel_size - border_width
            ], fill=color)

    # 绘制网格线
    for i in range(0, canvas_size, pixel_size):
        # 绘制水平线
        draw.line([(0, i), (canvas_size, i)], fill="#FFFFFF", width=border_width)
        # 绘制垂直线
        draw.line([(i, 0), (i, canvas_size)], fill="#FFFFFF", width=border_width)

    # 添加到帧列表
    frames_list.append(img)
    
    # 显示进度
    print(f"已生成 {frame + 1}/{frames} 帧")

# 保存为GIF
frames_list[0].save(
    'BG.gif',
    save_all=True,
    append_images=frames_list[1:],
    duration=duration,
    loop=0,  # 无限循环
    optimize=True  # 优化文件大小
)

print(f"GIF生成完成！像素大小：{pixel_size}，总帧数：{frames}，每帧时长：{duration}ms")
print("使用方法：")
print("1. 将BG.gif放在与Playing.html相同的目录下")
print("2. 刷新游戏页面即可看到动态背景")
print("3. 按ESC键可以结束游戏")