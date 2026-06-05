import cv2
import numpy as np

# 원 생성
'''
circleBG = np.zeros((450, 640, 3), dtype=np.uint8)
COLOR = (255, 255, 0)       # 색상
RADIUS = 100                # 원의 반지름
THINKNESS = 3               # 선 두께

cv2.circle(circleBG,     (150, 150), RADIUS, COLOR, THINKNESS, cv2.LINE_AA )
#        어디에 그릴거니?  원의 중심점   반지름   색상      두께        선의 타입

cv2.circle(circleBG,     (450, 150), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA )

cv2.imshow('title-circle', circleBG)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 사각형 그리기
# rectangleBG = np.zeros((450, 640, 3), dtype=np.uint8)
# COLOR = (255, 255, 0)       # 색상
# THINKNESS = 3               # 선 두께

# cv2.rectangle(rectangleBG, (50, 100), (200, 200), COLOR, THINKNESS, cv2.LINE_AA )
# #        어디에 그릴거니?       좌상단     우하단      색상      두께       선의 타입

# cv2.rectangle(rectangleBG, (300, 100), (500, 300), COLOR, cv2.FILLED, cv2.LINE_AA )

# cv2.imshow('title-circle', rectangleBG)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 다각형 그리기
# polygonBG = np.zeros((450, 640, 3), dtype=np.uint8)

# COLOR = (255, 255, 0)       # 색상
# THINKENESS = 3              # 두께

# points = np.array([
#     [50, 50],
#     [150, 150],
#     [50, 150],
# ])

# points = np.array([
#     [250, 50],
#     [350, 150],
#     [250, 150],
# ])


# # cv2.polylines(polygonBG,    [points],  False,    COLOR, THINKENESS, cv2.LINE_AA)
# #           # 어디에 그릴지?  뭐그릴거야?   열린도형     색상      두께       선의 타입
# cv2.polylines(polygonBG,    [points],  True,      COLOR, THINKENESS, cv2.LINE_AA)
#           # 어디에 그릴지?  뭐그릴거야?   닫힌도형      색상      두께       선의 타입

# cv2.imshow('title-polygonBG', polygonBG)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 이미지 복사 & 저장
# stImgGrayscale = cv2.imread('./res/img/star_wars.jpg', cv2.IMREAD_GRAYSCALE)
# stImgGrayscale = cv2.resize(stImgGrayscale, (459, 344))

# cv2.imshow('title-stImgGrayscale', stImgGrayscale)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cv2.imwrite('./save/img/star_wars_dath.jpg', stImgGrayscale)

# stImgGrayscale = cv2.imread('./res/img/star_wars.jpg', cv2.IMREAD_GRAYSCALE)
# stImgGrayscale = cv2.resize(stImgGrayscale, (459, 344))
# result = cv2.imwrite('./save/img/star_wars_dath.jpg', stImgGrayscale)
# print(f'result: {result}')

# 동영상 복사 저장
desniyMov = cv2.VideoCapture('./res/mov/desniy.mp4') # 동영상 파일 읽기

# 코덱 정의
# cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 'D', 'I', 'V', 'X'

width = int(desniyMov.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(desniyMov.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = desniyMov.get(cv2.CAP_PROP_FPS)

desniyMovOutput = cv2.VideoWriter('./save/mov/desniyMov-output.mp4', fourcc, fps, (width, height))
# 깡통파일

while desniyMov.isOpened:
    result, frame = desniyMov.read()        # 프레임 1개 읽는다.
    if not result:
        print('MOVIE END!')
        break

    desniyMovOutput.write(frame)            # 프레임을 옮긴다

    frame = cv2.resize(frame,(400, 600))
    cv2.imshow('title-desniyMov', frame)


    if cv2.waitKey(1) == ord('q'):
        print('MOVIE END!')
        break

desniyMov.release()
cv2.destroyAllWindows()