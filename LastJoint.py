import cv2
import pandas as pd
import numpy  as np
import os
from tqdm import tqdm



boards = "C:/Users/39345/Desktop/Microtec challange/exportBrd/"
logs = "C:/Users/39345/Desktop/Microtec challange/Infologs/Infologs/logCTData@"


def lineseg_dist(p, a, b):

    # normalized tangent vector
    d = np.divide(b - a, np.linalg.norm(b - a))

    # signed parallel distance components
    s = np.dot(a - p, d)
    t = np.dot(p - b, d)

    # clamped parallel distance
    h = np.maximum.reduce([s, t, 0])

    # perpendicular distance component
    c = np.cross(p - a, d)

    return np.hypot(h, np.linalg.norm(c))


def isect_line_plane_v3(p0, p1, p_co, p_no, epsilon=1e-6):
    """
    p0, p1: Define the line.
    p_co, p_no: define the plane:
        p_co Is a point on the plane (plane coordinate).
        p_no Is a normal vector defining the plane direction;
                (does not need to be normalized).

    Return a Vector or None (when the intersection can't be found).
    """

    u = p1-p0
    dot = np.dot(p_no, u)

    if abs(dot) > epsilon:
        # The factor of the point between p0 -> p1 (0 - 1)
        # if 'fac' is between (0 - 1) the point intersects with the segment.
        # Otherwise:
        #  < 0.0: behind p0.
        #  > 1.0: infront of p1.
        w = p0-p_co
        fac = -np.dot(p_no,w)/ dot
        u = u*fac
        return p0+u

    # The segment is parallel to plane.
    return None

# # ----------------------
# # generic math functions

# def add_v3v3(v0, v1):
#     return (
#         [v0[0] + v1[0],
#         v0[1] + v1[1],
#         v0[2] + v1[2],]
#     )


# def sub_v3v3(v0, v1):
#     return (
#         [v0[0] - v1[0],
#         v0[1] - v1[1],
#         v0[2] - v1[2],]
#     )


# def dot_v3v3(v0, v1):
#     return (
#         (v0[0] * v1[0]) +
#         (v0[1] * v1[1]) +
#         (v0[2] * v1[2])
#     )


# def len_squared_v3(v0):
#     return dot_v3v3(v0, v0)


# def mul_v3_fl(v0, f):
#     return (
#         [v0[0] * f,
#         v0[1] * f,
#         v0[2] * f,]
#     )


df = pd.DataFrame(columns=["fullId","n_knots","average_radius_knot","Tot_area_knots","dist_brd_pith"])

for board in tqdm(os.listdir(boards)):
    
    images = []
    images = cv2.imreadmulti(mats = images, filename = boards + board, flags = cv2.IMREAD_ANYCOLOR + cv2.IMREAD_ANYDEPTH)
    # print(len(images))
    Xbrd=np.matrix(np.array(images[1][0]))
    Ybrd=np.matrix(np.array(images[1][1]))
    Zbrd=np.matrix(np.array(images[1][2]))
    valid=np.where(Zbrd>0)
    # print(np.shape(valid))
    startBrd = valid[1][0]
    endBrd = valid[1][np.shape(valid)[1]-1]
    Brd_len_z = abs(Zbrd[0,endBrd]-Zbrd[0,startBrd])
    Brd_width_x_start = abs(Xbrd[7,startBrd]-Xbrd[2,startBrd])
    Brd_height_y_start = abs(Ybrd[1,startBrd]-Ybrd[4,startBrd])
    Brd_width_x_end = abs(Xbrd[7,endBrd]-Xbrd[2,endBrd])
    Brd_height_y_end = abs(Ybrd[1,endBrd]-Ybrd[4,endBrd])
    # print(Brd_width_x_start)
    # print(Brd_width_x_end)
    # print(Brd_height_y_start)
    # print(Brd_height_y_end)
    # break

    x_right_start= (Xbrd[1,startBrd]+Xbrd[2,startBrd]+Xbrd[3,startBrd]+Xbrd[4,startBrd])/4
    x_left_start = (Xbrd[5,startBrd]+Xbrd[6,startBrd]+Xbrd[7,startBrd]+Xbrd[0,startBrd])/4
    y_right_start = (Ybrd[1,startBrd]+Ybrd[2,startBrd]+Ybrd[3,startBrd]+Ybrd[4,startBrd])/4
    y_left_start = (Ybrd[5,startBrd]+Ybrd[6,startBrd]+Ybrd[7,startBrd]+Ybrd[0,startBrd])/4
    z_right_start = (Zbrd[1,startBrd]+Zbrd[2,startBrd]+Zbrd[3,startBrd]+Zbrd[4,startBrd])/4
    z_left_start = (Zbrd[5,startBrd]+Zbrd[6,startBrd]+Zbrd[7,startBrd]+Zbrd[0,startBrd])/4
    
    right_start = np.array([x_right_start,y_right_start,z_right_start])
    left_start = np.array([x_left_start,y_left_start,z_left_start])
    
    x_right_end= (Xbrd[1,endBrd]+Xbrd[2,endBrd]+Xbrd[3,endBrd]+Xbrd[4,endBrd])/4
    x_left_end = (Xbrd[5,endBrd]+Xbrd[6,endBrd]+Xbrd[7,endBrd]+Xbrd[0,endBrd])/4
    y_right_end = (Ybrd[1,endBrd]+Ybrd[2,endBrd]+Ybrd[3,endBrd]+Ybrd[4,endBrd])/4
    y_left_end = (Ybrd[5,endBrd]+Ybrd[6,endBrd]+Ybrd[7,endBrd]+Ybrd[0,endBrd])/4
    z_right_end= (Zbrd[1,endBrd]+Zbrd[2,endBrd]+Zbrd[3,endBrd]+Zbrd[4,endBrd])/4
    z_left_end = (Zbrd[5,endBrd]+Zbrd[6,endBrd]+Zbrd[7,endBrd]+Zbrd[0,endBrd])/4
    
    right_end = np.array([x_right_end,y_right_end,z_right_end])
    left_end = np.array([x_left_end,y_left_end,z_left_end])
    
    
    logid = board.split("2022")[1]
    size = len(logid)
    fullLogId = int(logid[:size-5])
    logid = logid[:size-7]
    
    log = logs+logid+".tiff"
    images_log = []
    images_log = cv2.imreadmulti(mats = images_log, filename = log, flags = cv2.IMREAD_ANYCOLOR + cv2.IMREAD_ANYDEPTH)
    knots = images_log[1][4]
    n_knots = len(knots[:,0])
    knot_x_start=knots[:,1]
    knot_y_start=knots[:,2]
    knot_z_start=knots[:,3]
    knot_x_end=knots[:,4]
    knot_y_end=knots[:,5]
    knot_z_end=knots[:,6]
    knot_dead_knot_border=knots[:,7]
    knot_radius=knots[:,8]
    knot_length=knots[:,9]
    
    pith = images_log[1][3]
    x_pith = pith[:,0]/10
    y_pith = pith[:,1]/10
    
    pith_start_coord = np.array([x_pith[startBrd],y_pith[startBrd],10])
    pith_end_coord = np.array([x_pith[endBrd],y_pith[endBrd],np.shape(x_pith)[0]*10])

    
    dist_brd_pith_start = lineseg_dist(pith_start_coord,right_start,left_start)
    dist_brd_pith_end = lineseg_dist(pith_end_coord,right_end,left_end)
    dist_brd_pith = (dist_brd_pith_start+dist_brd_pith_end)/2
    

    ux, uy, uz = u = left_start-right_start
    vx, vy, vz = v = right_end-right_start

    u_cross_v = [uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx]
    u_no = np.array(u_cross_v)
    u_co = right_start
    
    n_inter_knots = 0
    sum_rad_inter_knots = 0
    tot_area_knots = 0
    for k in range(n_knots):
        
        p0 = np.array([knot_x_start[k],knot_y_start[k],knot_z_start[k]])
        p1 = np.array([knot_x_end[k],knot_y_end[k],knot_z_end[k]])

        out = isect_line_plane_v3(p0,p1,u_co,u_no)
        if out is not None:
            
            #checks for intersection between knot and board
            diff1 = left_start-right_start
            diff2 = right_end-right_start
            d1 = np.dot(right_start,diff1)
            d2 = np.dot(out,diff1)
            d3 = np.dot(left_start,diff1)
            e1 = np.dot(right_start,diff2)
            e2 = np.dot(out,diff2)
            e3 = np.dot(right_end,diff2)
            
            if d1<d2<d3 and e1<e2<e3:
                n_inter_knots+=1
                sum_rad_inter_knots+=knot_radius[k]
                tot_area_knots+=((knot_radius[k])**2)*np.pi
                # print(n_inter_knots)
                # print(sum_rad_inter_knots)
            
    # print(np.round(sum_rad_inter_knots/n_inter_knots,5))
    
    if n_inter_knots!=0:
        avg_knot_rad = np.round(sum_rad_inter_knots/n_inter_knots,5)
    else: avg_knot_rad=0
    
    dict = {"fullId":[fullLogId],"n_knots":[n_inter_knots],"average_radius_knot":[avg_knot_rad],"Tot_area_knots":tot_area_knots,"dist_brd_pith":dist_brd_pith}
    new_row = pd.DataFrame.from_dict(dict)
    df = pd.concat([df,new_row])


    
final = pd.read_csv(r"C:\Users\39345\Desktop\Microtec challange\final2.csv")
df = pd.merge(df,final,on="fullId",how="inner")
df.to_csv("final3.csv")
    
    





