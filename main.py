from tkinter import Tk, Canvas, PhotoImage, Label, ACTIVE, DISABLED, Button, StringVar
from random import choice
import pickle

not_occupied = "NOTHING"


def index_val(seq, val):
    try:
        return seq.index(val)
    except ValueError:
        return 0


root = Tk()
root.title("Ludo")
root.config(bg="#1a1818")
canvas = Canvas(master=root, bg="#1a1818", width="735", height="735")  # 49X49 each
crt = canvas.create_rectangle
RED = "#822a2a"
BLACK = "#1a1818"
GREEN = "#184a29"
PURPLE = "#611c35"
CYAN = "#11294d"
GOLDEN = "#e65100"
green_pic = PhotoImage(file="~/Desktop/Python/Ludo/green_token.png")
purple_pic = PhotoImage(file="~/Desktop/Python/Ludo/purple_token.png")
cyan_pic = PhotoImage(file="~/Desktop/Python/Ludo/cyan_token.png")
red_pic = PhotoImage(file="~/Desktop/Python/Ludo/red_token.png")

# --------------------------------------------------Column = 1--------------------------------------------------------
r1 = [crt(0, 0, 49, 49, fill=RED), not_occupied]
r2 = [crt(49, 0, 98, 49, fill=RED), not_occupied]
r3 = [crt(98, 0, 147, 49, fill=RED), not_occupied]
r4 = [crt(147, 0, 196, 49, fill=RED), not_occupied]
r5 = [crt(196, 0, 245, 49, fill=RED), not_occupied]
r6 = [crt(245, 0, 294, 49, fill=RED), not_occupied]

b1 = [crt(294, 0, 343, 49, fill=BLACK), not_occupied]
b2 = [crt(343, 0, 392, 49, fill=BLACK), not_occupied]
b3 = [crt(392, 0, 441, 49, fill=BLACK), not_occupied]

g1 = [crt(441, 0, 490, 49, fill=GREEN), not_occupied]
g2 = [crt(490, 0, 539, 49, fill=GREEN), not_occupied]
g3 = [crt(539, 0, 588, 49, fill=GREEN), not_occupied]
g4 = [crt(588, 0, 637, 49, fill=GREEN), not_occupied]
g5 = [crt(637, 0, 686, 49, fill=GREEN), not_occupied]
g6 = [crt(686, 0, 735, 49, fill=GREEN), not_occupied]

# --------------------------------------------------Column = 2--------------------------------------------------------
r7 = [crt(0, 49, 49, 98, fill=RED), not_occupied]
r8 = [crt(49, 49, 98, 98, fill=RED), not_occupied]
r9 = [crt(98, 49, 147, 98, fill=RED), not_occupied]
r10 = [crt(147, 49, 196, 98, fill=RED), not_occupied]
r11 = [crt(196, 49, 245, 98, fill=RED), not_occupied]
r12 = [crt(245, 49, 294, 98, fill=RED), not_occupied]

b4 = [crt(294, 49, 343, 98, fill=BLACK), not_occupied]
wg1 = [crt(343, 49, 392, 98, fill=GREEN), not_occupied]
sg = [crt(392, 49, 441, 98, fill=GREEN), not_occupied]

g7 = [crt(441, 49, 490, 98, fill=GREEN), not_occupied]
g8 = [crt(490, 49, 539, 98, fill=GREEN), not_occupied]
g9 = [crt(539, 49, 588, 98, fill=GREEN), not_occupied]
g10 = [crt(588, 49, 637, 98, fill=GREEN), not_occupied]
g11 = [crt(637, 49, 686, 98, fill=GREEN), not_occupied]
g12 = [crt(686, 49, 735, 98, fill=GREEN), not_occupied]

# --------------------------------------------------Column = 3--------------------------------------------------------
r13 = [crt(0, 98, 49, 147, fill=RED), not_occupied]
r14 = [crt(49, 98, 98, 147, fill=RED), not_occupied]
r15 = [crt(98, 98, 147, 147, fill=RED), not_occupied]
r16 = [crt(147, 98, 196, 147, fill=RED), not_occupied]
r17 = [crt(196, 98, 245, 147, fill=RED), not_occupied]
r18 = [crt(245, 98, 294, 147, fill=RED), not_occupied]

b5 = [crt(294, 98, 343, 147, fill=BLACK), not_occupied]
wg2 = [crt(343, 98, 392, 147, fill=GREEN), not_occupied]
b6 = [crt(392, 98, 441, 147, fill=BLACK), not_occupied]

g13 = [crt(441, 98, 490, 147, fill=GREEN), not_occupied]
g14 = [crt(490, 98, 539, 147, fill=GREEN), not_occupied]
g15 = [crt(539, 98, 588, 147, fill=GREEN), not_occupied]
g16 = [crt(588, 98, 637, 147, fill=GREEN), not_occupied]
g17 = [crt(637, 98, 686, 147, fill=GREEN), not_occupied]
g18 = [crt(686, 98, 735, 147, fill=GREEN), not_occupied]

# --------------------------------------------------Column = 4--------------------------------------------------------
r19 = [crt(0, 147, 49, 196, fill=RED), not_occupied]
r20 = [crt(49, 147, 98, 196, fill=RED), not_occupied]
r21 = [crt(98, 147, 147, 196, fill=RED), not_occupied]
r22 = [crt(147, 147, 196, 196, fill=RED), not_occupied]
r23 = [crt(196, 147, 245, 196, fill=RED), not_occupied]
r24 = [crt(245, 147, 294, 196, fill=RED), not_occupied]

b7 = [crt(294, 147, 343, 196, fill=BLACK), not_occupied]
wg3 = [crt(343, 147, 392, 196, fill=GREEN), not_occupied]
b8 = [crt(392, 147, 441, 196, fill=BLACK), not_occupied]

g19 = [crt(441, 147, 490, 196, fill=GREEN), not_occupied]
g20 = [crt(490, 147, 539, 196, fill=GREEN), not_occupied]
g21 = [crt(539, 147, 588, 196, fill=GREEN), not_occupied]
g22 = [crt(588, 147, 637, 196, fill=GREEN), not_occupied]
g23 = [crt(637, 147, 686, 196, fill=GREEN), not_occupied]
g24 = [crt(686, 147, 735, 196, fill=GREEN), not_occupied]

# --------------------------------------------------Column = 5--------------------------------------------------------
r25 = [crt(0, 196, 49, 245, fill=RED), not_occupied]
r26 = [crt(49, 196, 98, 245, fill=RED), not_occupied]
r27 = [crt(98, 196, 147, 245, fill=RED), not_occupied]
r28 = [crt(147, 196, 196, 245, fill=RED), not_occupied]
r29 = [crt(196, 196, 245, 245, fill=RED), not_occupied]
r30 = [crt(245, 196, 294, 245, fill=RED), not_occupied]

b9 = [crt(294, 196, 343, 245, fill=BLACK), not_occupied]
wg4 = [crt(343, 196, 392, 245, fill=GREEN), not_occupied]
b10 = [crt(392, 196, 441, 245, fill=BLACK), not_occupied]

g25 = [crt(441, 196, 490, 245, fill=GREEN), not_occupied]
g26 = [crt(490, 196, 539, 245, fill=GREEN), not_occupied]
g27 = [crt(539, 196, 588, 245, fill=GREEN), not_occupied]
g28 = [crt(588, 196, 637, 245, fill=GREEN), not_occupied]
g29 = [crt(637, 196, 686, 245, fill=GREEN), not_occupied]
g30 = [crt(686, 196, 735, 245, fill=GREEN), not_occupied]

# --------------------------------------------------Column = 6--------------------------------------------------------
r31 = [crt(0, 245, 49, 294, fill=RED), not_occupied]
r32 = [crt(49, 245, 98, 294, fill=RED), not_occupied]
r33 = [crt(98, 245, 147, 294, fill=RED), not_occupied]
r34 = [crt(147, 245, 196, 294, fill=RED), not_occupied]
r35 = [crt(196, 245, 245, 294, fill=RED), not_occupied]
r36 = [crt(245, 245, 294, 294, fill=RED), not_occupied]

b11 = [crt(294, 245, 343, 294, fill=BLACK), not_occupied]
wg5 = [crt(343, 245, 392, 294, fill=GREEN), not_occupied]
b12 = [crt(392, 245, 441, 294, fill=BLACK), not_occupied]

g31 = [crt(441, 245, 490, 294, fill=GREEN), not_occupied]
g32 = [crt(490, 245, 539, 294, fill=GREEN), not_occupied]
g33 = [crt(539, 245, 588, 294, fill=GREEN), not_occupied]
g34 = [crt(588, 245, 637, 294, fill=GREEN), not_occupied]
g35 = [crt(637, 245, 686, 294, fill=GREEN), not_occupied]
g36 = [crt(686, 245, 735, 294, fill=GREEN), not_occupied]

# --------------------------------------------------Column = 7--------------------------------------------------------
b13 = [crt(0, 294, 49, 343, fill=BLACK), not_occupied]
sr = [crt(49, 294, 98, 343, fill=RED), not_occupied]
b14 = [crt(98, 294, 147, 343, fill=BLACK), not_occupied]
b15 = [crt(147, 294, 196, 343, fill=BLACK), not_occupied]
b16 = [crt(196, 294, 245, 343, fill=BLACK), not_occupied]
b17 = [crt(245, 294, 294, 343, fill=BLACK), not_occupied]

w1 = [crt(294, 294, 343, 343, fill=GOLDEN), not_occupied]
w2 = [crt(343, 294, 392, 343, fill=GOLDEN), not_occupied]
w3 = [crt(392, 294, 441, 343, fill=GOLDEN), not_occupied]

b18 = [crt(441, 294, 490, 343, fill=BLACK), not_occupied]
b19 = [crt(490, 294, 539, 343, fill=BLACK), not_occupied]
b20 = [crt(539, 294, 588, 343, fill=BLACK), not_occupied]
b21 = [crt(588, 294, 637, 343, fill=BLACK), not_occupied]
b22 = [crt(637, 294, 686, 343, fill=BLACK), not_occupied]
b23 = [crt(686, 294, 735, 343, fill=BLACK), not_occupied]

# --------------------------------------------------Column = 8--------------------------------------------------------
b24 = [crt(0, 343, 49, 392, fill=BLACK), not_occupied]
wr1 = [crt(49, 343, 98, 392, fill=RED), not_occupied]
wr2 = [crt(98, 343, 147, 392, fill=RED), not_occupied]
wr3 = [crt(147, 343, 196, 392, fill=RED), not_occupied]
wr4 = [crt(196, 343, 245, 392, fill=RED), not_occupied]
wr5 = [crt(245, 343, 294, 392, fill=RED), not_occupied]

w4 = [crt(294, 343, 343, 392, fill=GOLDEN), not_occupied]
w5 = [crt(343, 343, 392, 392, fill=GOLDEN), not_occupied]
w6 = [crt(392, 343, 441, 392, fill=GOLDEN), not_occupied]

wp1 = [crt(441, 343, 490, 392, fill=PURPLE), not_occupied]
wp2 = [crt(490, 343, 539, 392, fill=PURPLE), not_occupied]
wp3 = [crt(539, 343, 588, 392, fill=PURPLE), not_occupied]
wp4 = [crt(588, 343, 637, 392, fill=PURPLE), not_occupied]
wp5 = [crt(637, 343, 686, 392, fill=PURPLE), not_occupied]
b25 = [crt(686, 343, 735, 392, fill=BLACK), not_occupied]

# --------------------------------------------------Column = 9--------------------------------------------------------
b26 = [crt(0, 392, 49, 441, fill=BLACK), not_occupied]
b27 = [crt(49, 392, 98, 441, fill=BLACK), not_occupied]
b28 = [crt(98, 392, 147, 441, fill=BLACK), not_occupied]
b29 = [crt(147, 392, 196, 441, fill=BLACK), not_occupied]
b30 = [crt(196, 392, 245, 441, fill=BLACK), not_occupied]
b31 = [crt(245, 392, 294, 441, fill=BLACK), not_occupied]

w7 = [crt(294, 392, 343, 441, fill=GOLDEN), not_occupied]
w8 = [crt(343, 392, 392, 441, fill=GOLDEN), not_occupied]
w9 = [crt(392, 392, 441, 441, fill=GOLDEN), not_occupied]

b32 = [crt(441, 392, 490, 441, fill=BLACK), not_occupied]
b33 = [crt(490, 392, 539, 441, fill=BLACK), not_occupied]
b34 = [crt(539, 392, 588, 441, fill=BLACK), not_occupied]
b35 = [crt(588, 392, 637, 441, fill=BLACK), not_occupied]
sp = [crt(637, 392, 686, 441, fill=PURPLE), not_occupied]
b36 = [crt(686, 392, 735, 441, fill=BLACK), not_occupied]

# --------------------------------------------------Column = 10--------------------------------------------------------
c1 = [crt(0, 441, 49, 490, fill=CYAN), not_occupied]
c2 = [crt(49, 441, 98, 490, fill=CYAN), not_occupied]
c3 = [crt(98, 441, 147, 490, fill=CYAN), not_occupied]
c4 = [crt(147, 441, 196, 490, fill=CYAN), not_occupied]
c5 = [crt(196, 441, 245, 490, fill=CYAN), not_occupied]
c6 = [crt(245, 441, 294, 490, fill=CYAN), not_occupied]

b37 = [crt(294, 441, 343, 490, fill=BLACK), not_occupied]
wc1 = [crt(343, 441, 392, 490, fill=CYAN), not_occupied]
b38 = [crt(392, 441, 441, 490, fill=BLACK), not_occupied]

p1 = [crt(441, 441, 490, 490, fill=PURPLE), not_occupied]
p2 = [crt(490, 441, 539, 490, fill=PURPLE), not_occupied]
p3 = [crt(539, 441, 588, 490, fill=PURPLE), not_occupied]
p4 = [crt(588, 441, 637, 490, fill=PURPLE), not_occupied]
p5 = [crt(637, 441, 686, 490, fill=PURPLE), not_occupied]
p6 = [crt(686, 441, 735, 490, fill=PURPLE), not_occupied]

# --------------------------------------------------Column = 11--------------------------------------------------------
c7 = [crt(0, 490, 49, 539, fill=CYAN), not_occupied]
c8 = [crt(49, 490, 98, 539, fill=CYAN), not_occupied]
c9 = [crt(98, 490, 147, 539, fill=CYAN), not_occupied]
c10 = [crt(147, 490, 196, 539, fill=CYAN), not_occupied]
c11 = [crt(196, 490, 245, 539, fill=CYAN), not_occupied]
c12 = [crt(245, 490, 294, 539, fill=CYAN), not_occupied]

b39 = [crt(294, 490, 343, 539, fill=BLACK), not_occupied]
wc2 = [crt(343, 490, 392, 539, fill=CYAN), not_occupied]
b40 = [crt(392, 490, 441, 539, fill=BLACK), not_occupied]

p7 = [crt(441, 490, 490, 539, fill=PURPLE), not_occupied]
p8 = [crt(490, 490, 539, 539, fill=PURPLE), not_occupied]
p9 = [crt(539, 490, 588, 539, fill=PURPLE), not_occupied]
p10 = [crt(588, 490, 637, 539, fill=PURPLE), not_occupied]
p11 = [crt(637, 490, 686, 539, fill=PURPLE), not_occupied]
p12 = [crt(686, 490, 735, 539, fill=PURPLE), not_occupied]

# --------------------------------------------------Column = 12--------------------------------------------------------
c13 = [crt(0, 539, 49, 588, fill=CYAN), not_occupied]
c14 = [crt(49, 539, 98, 588, fill=CYAN), not_occupied]
c15 = [crt(98, 539, 147, 588, fill=CYAN), not_occupied]
c16 = [crt(147, 539, 196, 588, fill=CYAN), not_occupied]
c17 = [crt(196, 539, 245, 588, fill=CYAN), not_occupied]
c18 = [crt(245, 539, 294, 588, fill=CYAN), not_occupied]

b41 = [crt(294, 539, 343, 588, fill=BLACK), not_occupied]
wc3 = [crt(343, 539, 392, 588, fill=CYAN), not_occupied]
b42 = [crt(392, 539, 441, 588, fill=BLACK), not_occupied]

p13 = [crt(441, 539, 490, 588, fill=PURPLE), not_occupied]
p14 = [crt(490, 539, 539, 588, fill=PURPLE), not_occupied]
p15 = [crt(539, 539, 588, 588, fill=PURPLE), not_occupied]
p16 = [crt(588, 539, 637, 588, fill=PURPLE), not_occupied]
p17 = [crt(637, 539, 686, 588, fill=PURPLE), not_occupied]
p18 = [crt(686, 539, 735, 588, fill=PURPLE), not_occupied]

# --------------------------------------------------Column = 13--------------------------------------------------------
c19 = [crt(0, 588, 49, 637, fill=CYAN), not_occupied]
c20 = [crt(49, 588, 98, 637, fill=CYAN), not_occupied]
c21 = [crt(98, 588, 147, 637, fill=CYAN), not_occupied]
c22 = [crt(147, 588, 196, 637, fill=CYAN), not_occupied]
c23 = [crt(196, 588, 245, 637, fill=CYAN), not_occupied]
c24 = [crt(245, 588, 294, 637, fill=CYAN), not_occupied]

b43 = [crt(294, 588, 343, 637, fill=BLACK), not_occupied]
wc4 = [crt(343, 588, 392, 637, fill=CYAN), not_occupied]
b44 = [crt(392, 588, 441, 637, fill=BLACK), not_occupied]

p19 = [crt(441, 588, 490, 637, fill=PURPLE), not_occupied]
p20 = [crt(490, 588, 539, 637, fill=PURPLE), not_occupied]
p21 = [crt(539, 588, 588, 637, fill=PURPLE), not_occupied]
p22 = [crt(588, 588, 637, 637, fill=PURPLE), not_occupied]
p23 = [crt(637, 588, 686, 637, fill=PURPLE), not_occupied]
p24 = [crt(686, 588, 735, 637, fill=PURPLE), not_occupied]

# --------------------------------------------------Column = 14--------------------------------------------------------
c25 = [crt(0, 637, 49, 686, fill=CYAN), not_occupied]
c26 = [crt(49, 637, 98, 686, fill=CYAN), not_occupied]
c27 = [crt(98, 637, 147, 686, fill=CYAN), not_occupied]
c28 = [crt(147, 637, 196, 686, fill=CYAN), not_occupied]
c29 = [crt(196, 637, 245, 686, fill=CYAN), not_occupied]
c30 = [crt(245, 637, 294, 686, fill=CYAN), not_occupied]

sc = [crt(294, 637, 343, 686, fill=CYAN), not_occupied]
wc5 = [crt(343, 637, 392, 686, fill=CYAN), not_occupied]
b45 = [crt(392, 637, 441, 686, fill=BLACK), not_occupied]

p25 = [crt(441, 637, 490, 686, fill=PURPLE), not_occupied]
p26 = [crt(490, 637, 539, 686, fill=PURPLE), not_occupied]
p27 = [crt(539, 637, 588, 686, fill=PURPLE), not_occupied]
p28 = [crt(588, 637, 637, 686, fill=PURPLE), not_occupied]
p29 = [crt(637, 637, 686, 686, fill=PURPLE), not_occupied]
p30 = [crt(686, 637, 735, 686, fill=PURPLE), not_occupied]

# --------------------------------------------------Column = 15--------------------------------------------------------
c31 = [crt(0, 686, 49, 735, fill=CYAN), not_occupied]
c32 = [crt(49, 686, 98, 735, fill=CYAN), not_occupied]
c33 = [crt(98, 686, 147, 735, fill=CYAN), not_occupied]
c34 = [crt(147, 686, 196, 735, fill=CYAN), not_occupied]
c35 = [crt(196, 686, 245, 735, fill=CYAN), not_occupied]
c36 = [crt(245, 686, 294, 735, fill=CYAN), not_occupied]

b46 = [crt(294, 686, 343, 735, fill=BLACK), not_occupied]
b47 = [crt(343, 686, 392, 735, fill=BLACK), not_occupied]
b48 = [crt(392, 686, 441, 735, fill=BLACK), not_occupied]

p31 = [crt(441, 686, 490, 735, fill=PURPLE), not_occupied]
p32 = [crt(490, 686, 539, 735, fill=PURPLE), not_occupied]
p33 = [crt(539, 686, 588, 735, fill=PURPLE), not_occupied]
p34 = [crt(588, 686, 637, 735, fill=PURPLE), not_occupied]
p35 = [crt(637, 686, 686, 735, fill=PURPLE), not_occupied]
p36 = [crt(686, 686, 735, 735, fill=PURPLE), not_occupied]

# --------------------------------------------------paths of player--------------------------------------------------
path_green = [
    sg, b6, b8, b10, b12, b18, b19, b20, b21, b22, b23, b25, b36, sp, b35, b34, b33, b32, b38, b40, b42,
    b44, b45, b48, b47, b46, sc, b43, b41, b39, b37, b31, b30, b29, b28, b27, b26, b24, b13, sr, b14, b15,
    b16, b17, b11, b9, b7, b5, b4, b1, b2, wg1, wg2, wg3, wg4, wg5, w2]
path_purple = [
    sp, b35, b34, b33, b32, b38, b40, b42, b44, b45, b48, b47, b46, sc, b43, b41, b39, b37, b31,
    b30, b29, b28, b27, b26, b24, b13, sr, b14, b15, b16, b17, b11, b9, b7, b5, b4, b1, b2, b3, sg,
    b6, b8, b10, b12, b18, b19, b20, b21, b22, b23, b25, wp5, wp4, wp3, wp2, wp1, w6]
path_cyan = [
    sc, b43, b41, b39, b37, b31, b30, b29, b28, b27, b26, b24, b13, sr, b14, b15, b16, b17,
    b11, b9, b7, b5, b4, b1, b2, b3, sg, b6, b8, b10, b12, b18, b19, b20, b21, b22, b23, b25,
    b36, sp, b35, b34, b33, b32, b38, b40, b42, b44, b45, b48, b47, wc5, wc4, wc3, wc2, wc1, w8]
path_red = [
    sr, b14, b15, b16, b17, b11, b9, b7, b5, b4, b1, b2, b3, sg, b6, b8, b10, b12, b18, b19, b20, b21,
    b22, b23, b25, b36, sp, b35, b34, b33, b32, b38, b40, b42, b44, b45, b48, b47, b46, sc, b43, b41,
    b39, b37, b31, b30, b29, b28, b27, b26, b24, wr1, wr2, wr3, wr4, wr5, w4]
# --------------------------------------------------RED LOGIC------------------------------------------------------
pr1 = [Label(canvas, image=red_pic), "HOME", r8, r8]  # [label(), state, position, initial position]
pr2 = [Label(canvas, image=red_pic), "HOME", r10, r10]
pr3 = [Label(canvas, image=red_pic), "HOME", r20, r20]
pr4 = [Label(canvas, image=red_pic), "HOME", r22, r22]

choice_red = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
result_red = None
vr = StringVar()
vr.set("0")


def binder_red():
    global result_red
    save_game.config(state=ACTIVE)
    result_red = choice(choice_red)
    vr.set(str(result_red))
    if (pr1[1] == "HOME" or pr1[1] == "WON") and (pr2[1] == "HOME" or pr2[1] == "WON") and (
            pr3[1] == "HOME" or pr3[1] == "WON") and (pr4[1] == "HOME" or pr4[1] == "WON") and result_red != 6:
        button_red.config(state=DISABLED)
        button_green.config(state=ACTIVE)
    elif pr1[1] == "WON" and pr2[1] == "WON" and pr3[1] == "WON" and pr4[1] == "WON":
        button_red.config(state=DISABLED)
        button_green.config(state=ACTIVE)
    elif (index_val(path_red, pr1[2]) + result_red >= len(path_red)) and (
            index_val(path_red, pr2[2]) + result_red >= len(path_red)) and (
            index_val(path_red, pr3[2]) + result_red >= len(path_red)) and (
            index_val(path_red, pr4[2]) + result_red >= len(path_red)):
        button_red.config(state=DISABLED)
        button_green.config(state=ACTIVE)
    else:
        button_red.config(state=DISABLED)
        pr1[0].bind("<Button-1>",
                    lambda event: general_move(pr1, pr2, pr3, pr4, path_red, result_red, button_red, button_green, sr))
        pr2[0].bind("<Button-1>",
                    lambda event: general_move(pr2, pr1, pr3, pr4, path_red, result_red, button_red, button_green, sr))
        pr3[0].bind("<Button-1>",
                    lambda event: general_move(pr3, pr1, pr2, pr4, path_red, result_red, button_red, button_green, sr))
        pr4[0].bind("<Button-1>",
                    lambda event: general_move(pr4, pr1, pr2, pr3, path_red, result_red, button_red, button_green, sr))


button_red = Button(root, textvariable=vr, command=binder_red, height=5, width=5, bg=RED, fg="white",
                    activebackground=RED, activeforeground="white", font=("Comic Sans", 10, "bold"))
button_red.place(x=246, y=18)
# --------------------------------------------------GREEN LOGIC---------------------------------------------------
pg1 = [Label(canvas, image=green_pic), "HOME", g8, g8]  # [label(), state, position, initial position]
pg2 = [Label(canvas, image=green_pic), "HOME", g10, g10]
pg3 = [Label(canvas, image=green_pic), "HOME", g20, g20]
pg4 = [Label(canvas, image=green_pic), "HOME", g22, g22]

choice_green = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
result_green = None

vg = StringVar()
vg.set("0")


def binder_green():
    global result_green
    save_game.config(state=DISABLED)
    result_green = choice(choice_green)
    vg.set(str(result_green))
    if (pg1[1] == "HOME" or pg1[1] == "WON") and (pg2[1] == "HOME" or pg2[1] == "WON") and (
            pg3[1] == "HOME" or pg3[1] == "WON") and (pg4[1] == "HOME" or pg4[1] == "WON") and result_green != 6:
        button_green.config(state=DISABLED)
        button_purple.config(state=ACTIVE)
    elif pg1[1] == "WON" and pg2[1] == "WON" and pg3[1] == "WON" and pg4[1] == "WON":
        button_green.config(state=DISABLED)
        button_purple.config(state=ACTIVE)
    elif (index_val(path_green, pg1[2]) + result_green >= len(path_green)) and (
            index_val(path_green, pg2[2]) + result_green >= len(path_green)) and (
            index_val(path_green, pg3[2]) + result_green >= len(path_green)) and (
            index_val(path_green, pg4[2]) + result_green >= len(path_green)):
        button_green.config(state=DISABLED)
        button_purple.config(state=ACTIVE)
    else:
        button_green.config(state=DISABLED)
        pg1[0].bind("<Button-1>", lambda event: general_move(pg1, pg2, pg3, pg4, path_green, result_green, button_green,
                                                             button_purple, sg))
        pg2[0].bind("<Button-1>", lambda event: general_move(pg2, pg1, pg3, pg4, path_green, result_green, button_green,
                                                             button_purple, sg))
        pg3[0].bind("<Button-1>", lambda event: general_move(pg3, pg2, pg1, pg4, path_green, result_green, button_green,
                                                             button_purple, sg))
        pg4[0].bind("<Button-1>", lambda event: general_move(pg4, pg2, pg3, pg1, path_green, result_green, button_green,
                                                             button_purple, sg))


button_green = Button(root, textvariable=vg, command=binder_green, height=5, width=5, bg=GREEN, fg="white",
                      activebackground=GREEN, activeforeground="white", font=("Comic Sans", 10, "bold"), state=DISABLED)
button_green.place(x=1050, y=18)
# --------------------------------------------------PURPLE LOGIC--------------------------------------------------
pp1 = [Label(canvas, image=purple_pic), "HOME", p14, p14]  # [label(), state, position, initial position]
pp2 = [Label(canvas, image=purple_pic), "HOME", p16, p16]
pp3 = [Label(canvas, image=purple_pic), "HOME", p26, p26]
pp4 = [Label(canvas, image=purple_pic), "HOME", p28, p28]

choice_purple = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
result_purple = None

vp = StringVar()
vp.set("0")


def binder_purple():
    global result_purple
    save_game.config(state=DISABLED)
    result_purple = choice(choice_purple)
    vp.set(str(result_purple))
    if (pp1[1] == "HOME" or pp1[1] == "WON") and (pp2[1] == "HOME" or pp2[1] == "WON") and (
            pp3[1] == "HOME" or pp3[1] == "WON") and (pp4[1] == "HOME" or pp4[1] == "WON") and result_purple != 6:
        button_purple.config(state=DISABLED)
        button_cyan.config(state=ACTIVE)
    elif pp1[1] == "WON" and pp2[1] == "WON" and pp3[1] == "WON" and pp4[1] == "WON":
        button_purple.config(state=DISABLED)
        button_cyan.config(state=ACTIVE)
    elif (index_val(path_purple, pp1[2]) + result_purple >= len(path_purple)) and (
            index_val(path_purple, pp2[2]) + result_purple >= len(path_purple)) and (
            index_val(path_purple, pp3[2]) + result_purple >= len(path_purple)) and (
            index_val(path_purple, pp4[2]) + result_purple >= len(path_purple)):
        button_purple.config(state=DISABLED)
        button_cyan.config(state=ACTIVE)
    else:
        button_purple.config(state=DISABLED)
        pp1[0].bind("<Button-1>",
                    lambda event: general_move(pp1, pp2, pp3, pp4, path_purple, result_purple, button_purple,
                                               button_cyan, sp))
        pp2[0].bind("<Button-1>",
                    lambda event: general_move(pp2, pp1, pp3, pp4, path_purple, result_purple, button_purple,
                                               button_cyan, sp))
        pp3[0].bind("<Button-1>",
                    lambda event: general_move(pp3, pp2, pp1, pp4, path_purple, result_purple, button_purple,
                                               button_cyan, sp))
        pp4[0].bind("<Button-1>",
                    lambda event: general_move(pp4, pp2, pp3, pp1, path_purple, result_purple, button_purple,
                                               button_cyan, sp))


button_purple = Button(root, textvariable=vp, command=binder_purple, height=5, width=5, bg=PURPLE, fg="white",
                       activebackground=PURPLE, activeforeground="white", font=("Comic Sans", 10, "bold"),
                       state=DISABLED)
button_purple.place(x=1050, y=641)
# --------------------------------------------------CYAN LOGIC-----------------------------------------------------
pc1 = [Label(canvas, image=cyan_pic), "HOME", c14, c14]  # [label(), state, position, initial position]
pc2 = [Label(canvas, image=cyan_pic), "HOME", c16, c16]
pc3 = [Label(canvas, image=cyan_pic), "HOME", c26, c26]
pc4 = [Label(canvas, image=cyan_pic), "HOME", c28, c28]

choice_cyan = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
result_cyan = None

vc = StringVar()
vc.set("0")


def binder_cyan():
    global result_cyan
    save_game.config(state=DISABLED)
    result_cyan = choice(choice_cyan)
    vc.set(str(result_cyan))
    if (pc1[1] == "HOME" or pc1[1] == "WON") and (pc2[1] == "HOME" or pc2[1] == "WON") and (
            pc3[1] == "HOME" or pc3[1] == "WON") and (pc4[1] == "HOME" or pc4[1] == "WON") and result_cyan != 6:
        button_cyan.config(state=DISABLED)
        button_red.config(state=ACTIVE)
    elif pc1[1] == "WON" and pc2[1] == "WON" and pc3[1] == "WON" and pc4[1] == "WON":
        button_cyan.config(state=DISABLED)
        button_red.config(state=ACTIVE)
    elif (index_val(path_cyan, pc1[2]) + result_cyan >= len(path_cyan)) and (
            index_val(path_cyan, pc2[2]) + result_cyan >= len(path_cyan)) and (
            index_val(path_cyan, pc3[2]) + result_cyan >= len(path_cyan)) and (
            index_val(path_cyan, pc4[2]) + result_cyan >= len(path_cyan)):
        button_cyan.config(state=DISABLED)
        button_red.config(state=ACTIVE)
    else:
        button_cyan.config(state=DISABLED)
        pc1[0].bind("<Button-1>",
                    lambda event: general_move(pc1, pc2, pc3, pc4, path_cyan, result_cyan, button_cyan, button_red, sc))
        pc2[0].bind("<Button-1>",
                    lambda event: general_move(pc2, pc1, pc3, pc4, path_cyan, result_cyan, button_cyan, button_red, sc))
        pc3[0].bind("<Button-1>",
                    lambda event: general_move(pc3, pc2, pc1, pc4, path_cyan, result_cyan, button_cyan, button_red, sc))
        pc4[0].bind("<Button-1>",
                    lambda event: general_move(pc4, pc2, pc3, pc1, path_cyan, result_cyan, button_cyan, button_red, sc))


button_cyan = Button(root, textvariable=vc, command=binder_cyan, height=5, width=5, bg=CYAN, fg="white",
                     activebackground=CYAN, activeforeground="white", font=("Comic Sans", 10, "bold"), state=DISABLED)
button_cyan.place(x=246, y=641)


# ------------------------------------------------SAVE, LOAD, NEW GAME LOGIC------------------------------

def save():
    with open("/home/adeed/Desktop/Python/Ludo/data.dat", "wb") as data:
        pickle.dump(pr1[1], data)
        pickle.dump([i for i, j in globals().items() if j == pr1[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pr1[2][1]][0], data)

        pickle.dump(pr2[1], data)
        pickle.dump([i for i, j in globals().items() if j == pr2[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pr2[2][1]][0], data)

        pickle.dump(pr3[1], data)
        pickle.dump([i for i, j in globals().items() if j == pr3[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pr3[2][1]][0], data)

        pickle.dump(pr4[1], data)
        pickle.dump([i for i, j in globals().items() if j == pr4[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pr4[2][1]][0], data)

        # -------------------------------------------------------------------------------------
        pickle.dump(pg1[1], data)
        pickle.dump([i for i, j in globals().items() if j == pg1[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pg1[2][1]][0], data)

        pickle.dump(pg2[1], data)
        pickle.dump([i for i, j in globals().items() if j == pg2[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pg2[2][1]][0], data)

        pickle.dump(pg3[1], data)
        pickle.dump([i for i, j in globals().items() if j == pg3[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pg3[2][1]][0], data)

        pickle.dump(pg4[1], data)
        pickle.dump([i for i, j in globals().items() if j == pg4[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pg4[2][1]][0], data)
        # -------------------------------------------------------------------------------------

        pickle.dump(pp1[1], data)
        pickle.dump([i for i, j in globals().items() if j == pp1[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pp1[2][1]][0], data)

        pickle.dump(pp2[1], data)
        pickle.dump([i for i, j in globals().items() if j == pp2[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pp2[2][1]][0], data)

        pickle.dump(pp3[1], data)
        pickle.dump([i for i, j in globals().items() if j == pp3[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pp3[2][1]][0], data)

        pickle.dump(pp4[1], data)
        pickle.dump([i for i, j in globals().items() if j == pp4[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pp4[2][1]][0], data)
        # -------------------------------------------------------------------------------------

        pickle.dump(pc1[1], data)
        pickle.dump([i for i, j in globals().items() if j == pc1[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pc1[2][1]][0], data)

        pickle.dump(pc2[1], data)
        pickle.dump([i for i, j in globals().items() if j == pc2[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pc2[2][1]][0], data)

        pickle.dump(pc3[1], data)
        pickle.dump([i for i, j in globals().items() if j == pc3[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pc3[2][1]][0], data)

        pickle.dump(pc4[1], data)
        pickle.dump([i for i, j in globals().items() if j == pc4[2]][0], data)
        pickle.dump([i for i, j in globals().items() if j == pc4[2][1]][0], data)


save_game = Button(root, text="Save Game", command=save, state=DISABLED)
save_game.place(x=150, y=50)


def new():
    with open("/home/adeed/Desktop/Python/Ludo/data.dat", "wb") as clear:
        clear.writable()
        pass


new_game = Button(root, text="New Game", command=new)
new_game.place(x=150, y=100)


def load_game():
    try:
        with open("/home/adeed/Desktop/Python/Ludo/data.dat", "rb") as file:
            pr1[1] = pickle.load(file)
            pr1[2] = globals()[pickle.load(file)]
            pr1[2][1] = globals()[pickle.load(file)]

            pr2[1] = pickle.load(file)
            pr2[2] = globals()[pickle.load(file)]
            pr2[2][1] = globals()[pickle.load(file)]

            pr3[1] = pickle.load(file)
            pr3[2] = globals()[pickle.load(file)]
            pr3[2][1] = globals()[pickle.load(file)]

            pr4[1] = pickle.load(file)
            pr4[2] = globals()[pickle.load(file)]
            pr4[2][1] = globals()[pickle.load(file)]

            pg1[1] = pickle.load(file)
            pg1[2] = globals()[pickle.load(file)]
            pg1[2][1] = globals()[pickle.load(file)]

            pg2[1] = pickle.load(file)
            pg2[2] = globals()[pickle.load(file)]
            pg2[2][1] = globals()[pickle.load(file)]

            pg3[1] = pickle.load(file)
            pg3[2] = globals()[pickle.load(file)]
            pg3[2][1] = globals()[pickle.load(file)]

            pg4[1] = pickle.load(file)
            pg4[2] = globals()[pickle.load(file)]
            pg4[2][1] = globals()[pickle.load(file)]

            pp1[1] = pickle.load(file)
            pp1[2] = globals()[pickle.load(file)]
            pp1[2][1] = globals()[pickle.load(file)]

            pp2[1] = pickle.load(file)
            pp2[2] = globals()[pickle.load(file)]
            pp2[2][1] = globals()[pickle.load(file)]

            pp3[1] = pickle.load(file)
            pp3[2] = globals()[pickle.load(file)]
            pp3[2][1] = globals()[pickle.load(file)]

            pp4[1] = pickle.load(file)
            pp4[2] = globals()[pickle.load(file)]
            pp4[2][1] = globals()[pickle.load(file)]

            pc1[1] = pickle.load(file)
            pc1[2] = globals()[pickle.load(file)]
            pc1[2][1] = globals()[pickle.load(file)]

            pc2[1] = pickle.load(file)
            pc2[2] = globals()[pickle.load(file)]
            pc2[2][1] = globals()[pickle.load(file)]

            pc3[1] = pickle.load(file)
            pc3[2] = globals()[pickle.load(file)]
            pc3[2][1] = globals()[pickle.load(file)]

            pc4[1] = pickle.load(file)
            pc4[2] = globals()[pickle.load(file)]
            pc4[2][1] = globals()[pickle.load(file)]
    except EOFError:
        pass


load_game()
pr1[0].place(x=canvas.coords(pr1[2][0])[0], y=canvas.coords(pr1[2][0])[1])
pr2[0].place(x=canvas.coords(pr2[2][0])[0], y=canvas.coords(pr2[2][0])[1])
pr3[0].place(x=canvas.coords(pr3[2][0])[0], y=canvas.coords(pr3[2][0])[1])
pr4[0].place(x=canvas.coords(pr4[2][0])[0], y=canvas.coords(pr4[2][0])[1])

pg1[0].place(x=canvas.coords(pg1[2][0])[0], y=canvas.coords(pg1[2][0])[1])
pg2[0].place(x=canvas.coords(pg2[2][0])[0], y=canvas.coords(pg2[2][0])[1])
pg3[0].place(x=canvas.coords(pg3[2][0])[0], y=canvas.coords(pg3[2][0])[1])
pg4[0].place(x=canvas.coords(pg4[2][0])[0], y=canvas.coords(pg4[2][0])[1])

pp1[0].place(x=canvas.coords(pp1[2][0])[0], y=canvas.coords(pp1[2][0])[1])
pp2[0].place(x=canvas.coords(pp2[2][0])[0], y=canvas.coords(pp2[2][0])[1])
pp3[0].place(x=canvas.coords(pp3[2][0])[0], y=canvas.coords(pp3[2][0])[1])
pp4[0].place(x=canvas.coords(pp4[2][0])[0], y=canvas.coords(pp4[2][0])[1])

pc1[0].place(x=canvas.coords(pc1[2][0])[0], y=canvas.coords(pc1[2][0])[1])
pc2[0].place(x=canvas.coords(pc2[2][0])[0], y=canvas.coords(pc2[2][0])[1])
pc3[0].place(x=canvas.coords(pc3[2][0])[0], y=canvas.coords(pc3[2][0])[1])
pc4[0].place(x=canvas.coords(pc4[2][0])[0], y=canvas.coords(pc4[2][0])[1])


# --------------------------------------------------PLAYER MOVE LOGIC---------------------------------------------------
def general_move(main_p, side_p1, side_p2, side_p3, path_fol, result, main_b, next_b, first_pos):
    save_game.config(state=DISABLED)
    try:
        final_pos = path_fol[index_val(path_fol, main_p[2]) + result]  # returns the complete board var(ex-r8)
    except IndexError:
        final_pos = None
    if final_pos is None:
        pass
    elif main_p[1] == "WON":
        pass
    elif main_p[1] == "HOME":
        if result == 6:
            main_p[0].place(x=canvas.coords(first_pos[0])[0], y=canvas.coords(first_pos[0])[1])
            main_p[1] = "ON_BOARD"
            main_p[2] = first_pos
            main_p[0].unbind("<Button-1>")
            side_p1[0].unbind("<Button-1>")
            side_p2[0].unbind("<Button-1>")
            side_p3[0].unbind("<Button-1>")
            main_b.config(state=ACTIVE)
    elif (final_pos[1] == side_p1) or (final_pos[1] == side_p2) or (final_pos[1] == side_p3):
        pass
    else:
        if final_pos[1] == not_occupied:
            main_p[2][1] = not_occupied
            main_p[0].place(x=canvas.coords(final_pos[0])[0], y=canvas.coords(final_pos[0])[1])
            main_p[2] = final_pos
            if main_p[2] == path_fol[len(path_fol) - 1]:
                main_p[1] = "WON"
            else:
                main_p[1] = "ON_BOARD"
            main_p[0].unbind("<Button-1>")
            side_p1[0].unbind("<Button-1>")
            side_p2[0].unbind("<Button-1>")
            side_p3[0].unbind("<Button-1>")
            if index_val(path_fol, final_pos) <= index_val(path_fol, path_fol[-6]):
                final_pos[1] = main_p
            if result == 6:
                main_b.config(state=ACTIVE)
            else:
                next_b.config(state=ACTIVE)
        else:
            main_p[2][1] = not_occupied
            final_pos[1][0].place(x=canvas.coords(final_pos[1][3][0])[0], y=canvas.coords(final_pos[1][3][0])[1])
            final_pos[1][1] = "HOME"
            final_pos[1][2] = final_pos[1][3]
            main_p[0].place(x=canvas.coords(final_pos[0])[0], y=canvas.coords(final_pos[0])[1])
            main_p[1] = "ON_BOARD"
            main_p[2] = final_pos
            main_p[0].unbind("<Button-1>")
            side_p1[0].unbind("<Button-1>")
            side_p2[0].unbind("<Button-1>")
            side_p3[0].unbind("<Button-1>")
            final_pos[1] = main_p
            if result == 6:
                main_b.config(state=ACTIVE)
            else:
                next_b.config(state=ACTIVE)


canvas.pack(pady=18)
root.mainloop()
