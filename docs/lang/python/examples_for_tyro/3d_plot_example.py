# %%
import matplotlib.pyplot as plt
import numpy as np
import gvar as gv

color_list = ['orange','dodgerblue','blueviolet','deeppink','indigo','rosybrown','greenyellow','cyan','fuchsia','royalblue', 'red','green','orange','dodgerblue','blueviolet','deeppink','indigo','rosybrown','greenyellow','cyan','fuchsia','royalblue', 'red','green']

def renorm_pdf_3D(a_range, b_range, gv_z_dic):
    fig = plt.figure()

    # 创建 3D 图形
    ax = fig.add_subplot(111, projection='3d') # 111 表示只有一个子图

    a_ls = np.arange(0, 9.1, 0.1) # a 轴
    b_ls = np.arange(-10, 10.1, 0.1) # b 轴
    a_ls, b_ls = np.meshgrid(a_ls, b_ls) # 底面网格

    for a in a_range:
        for b in b_range:
            pdf_a = np.ones(100) * a 
            pdf_b = np.ones(100) * b 
            gv_z = gv_z_dic[str(a)][b - b_range[0]]
            pdf_v = np.linspace(gv_z.mean+gv_z.sdev, gv_z.mean-gv_z.sdev, 100)

            ax.plot3D(pdf_a, pdf_b, pdf_v, color=color_list[a]) # 3D errorbar


    val_sur = a_ls - b_ls
    ax.plot_surface(a_ls, b_ls, val_sur, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'), alpha=0.5) # 3D 曲面 plot

    ax.contourf(a_ls, b_ls, val_sur, zdir='z', offset=-1) # offset : 表示等高线图投射到z轴的某个高度

    ax.set_zlim(0, 32) # 设置 3D 图z轴高度
    ax.set_xlabel('a') 
    ax.set_ylabel('b')
    ax.set_zlabel('z')
    plt.show()

a_range = np.arange(1, 8)
b_range = np.arange(-5, 5)

gv_z_dic = {}
for a in a_range:
    gv_z_dic[str(a)] = [gv.gvar((30 - b**2), 3) for b in b_range] # 每个 a 值对应一条 b 轴上的曲线
    
renorm_pdf_3D(a_range, b_range, gv_z_dic)


# %%
