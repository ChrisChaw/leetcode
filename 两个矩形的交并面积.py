def calcu(P, G):
    pxmin, pymin, pxmax, pymax = P
    gxmin, gymin, gxmax, gymax = G
    parea = (pxmax - pxmin) * (pymax - pymin)
    garea = (gxmax - gxmin) * (gymax - gymin)

    xmin = max(pxmin, gxmin)  # 左下顶点的横坐标
    ymin = max(pymin, gymax)  # 左下顶点的纵坐标
    xmax = min(pxmax, gxmax)  # 右上顶点的横坐标
    ymax = min(pymax, gymax)  # 右上顶点的纵坐标

    # 计算相交矩形的面积
    w = xmax - xmin
    h = ymax - ymin
    if w < 0 or h < 0:
        return 0
    inter_area = w * h

    # 相并的面积 = 两个矩形的面积之和 - 相交的面积
    con_area = parea + garea - inter_area
    return inter_area, con_area
