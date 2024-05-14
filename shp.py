import shapefile
import tkinter as tk
from tkinter import filedialog

# 创建 tkinter 根窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 打开选择文件对话框，选择输入的 shp 文件
input_file_path = filedialog.askopenfilename(
    title="选择 shp 文件", filetypes=[("Shapefile", "*.shp")]
)

# 打开选择文件对话框，选择输出的 txt 文件
output_file_path = filedialog.asksaveasfilename(
    title="选择输出 txt 文件",
    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt")],
)

# 确保用户选择了文件
if input_file_path and output_file_path:
    # 读取 Shapefile
    with shapefile.Reader(input_file_path) as sf:
        # 打开输出文件以写入
        with open(output_file_path, "w") as txt_file:
            # 遍历SHP文件中的每个特征（形状）
            for shape in sf.shapes():
                # 获取特征的部分类型
                part_type = shape.shapeType
                # 如果特征是折线或多边形，则遍历其部分
                if part_type == 3 or part_type == 5:  # 3代表折线，5代表多边形
                    for part in shape.parts:
                        # 获取部分的起始索引和结束索引
                        start = part
                        end = (
                            shape.parts[shape.parts.index(part) + 1]
                            if shape.parts.index(part) + 1 < len(shape.parts)
                            else len(shape.points)
                        )
                        # 写入部分的坐标点
                        for point in shape.points[start:end]:
                            txt_file.write(f"{point[0]},{point[1]}\n")
                # 如果特征是点，则直接写入坐标
                elif part_type == 1:  # 1代表点
                    txt_file.write(f"{shape.points[0][0]},{shape.points[0][1]}\n")
    print("转换完成！坐标已保存到", output_file_path)
else:
    print("用户取消了操作。")
