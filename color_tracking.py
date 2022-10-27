
# Нгуен Хоанг Нам

import cv2
import pandas as pd


img_direction = r'C:\Users\optim\Downloads\Image.jpg'
img = cv2.imread(img_direction)

# Reading csv file with pandas
idx = ['color', 'NameofColor', 'hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=idx, header=None)


# function to calculate colors and get the most matching color
def get_NameofColor(R, G, B):
    min = 999
    for i in range(len(csv)):
        distance = abs(R - int(csv.loc[i, "R"])) + abs(G -
                                                       int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if distance <= min:
            min = distance
            NameofColor = csv.loc[i, "NameofColor"]
    return NameofColor


click = False
xposition = 0
yposition = 0
r = 0
g = 0
b = 0


# function to get x,y coordinates of mouse double click
def click_function(act, x, y, flag, parameter):
    if act == cv2.EVENT_MOUSEMOVE:
        global xposition, yposition, click, b, g, r
        click = True
        yposition = y
        xposition = x
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('img')
cv2.setMouseCallback('img', click_function)

# output
while True:
    cv2.imshow('img', img)
    if click:
        # create rectangle
        cv2.rectangle(img, (150, 60), (1760, 20), (b, g, r), -1)
        # create text to display
        text = get_NameofColor(r, g, b) + ' (R=' + str(r) + \
            ' G=' + str(g) + ' B=' + str(b) + ')'
        # text position
        cv2.putText(img, text, (660, 50), 3, 1,
                    (255, 255, 255), 2, cv2.LINE_AA)
        # If light color it will display text in black color
        if r + g + b >= 600:
            cv2.putText(img, text, (660, 50), 3, 1,
                        (0, 0, 0), 2, cv2.LINE_AA)

        click = False

    # Press the Esc key to end the Loop
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
