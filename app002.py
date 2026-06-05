# opencv 모듈 가져오기
import cv2

# 버전 확인
print(cv2.__version__)

# 이미지 불러와서 출력하기

# stImg = cv2.imread('./res/img/star_wars.jpg')        # 이미지 읽기
# print(f'stImg shape: {stImg.shape}')                 # 이미지 크기 출력 --> (3448(세로), 4592(가로), 3(BGR컬러))

# stImg = cv2.resize(stImg, (459, 344))                # 이미지 크기 변경 --> ((가로, 세로), 3)

# cv2.imshow('title-starwars', stImg)                  # 이미지 출력
# # cv2.imshow('윈도우이름', 출력할이미지)
# # cv2.waitKey(1000 * 3)                              # 3초동안 출력이 된다. 단위가 ms 이다.
# cv2.waitKey(0)                                       # 키보드 키 아무거나 누를때 창이 닫힌다.
# cv2.destroyAllWindows()                              # 모든 창 닫기


# 이미지 읽기 옵션
stImgColor = cv2.imread('./res/img/star_wars.jpg', cv2.IMREAD_COLOR)        # BGR 유지
stImgColor = cv2.resize(stImgColor, (459, 344))

stImgGray = cv2.imread('./res/img/star_wars.jpg', cv2.IMREAD_COLOR)         # GRAYSCALE
stImgGray = cv2.resize(stImgGray, (459, 344))

stImgUnchanged = cv2.imread('./res/img/star_wars.jpg', cv2.IMREAD_COLOR)    # ALPHA 유지
stImgUnchanged = cv2.resize(stImgUnchanged, (459, 344))


cv2.imshow('title-stImgColor', stImgColor)
cv2.imshow('title-stImgGray', stImgGray)
cv2.imshow('title-stImgUnchanged', stImgUnchanged)


cv2.waitKey(0)            # 외부자원 해제
cv2.destroyAllWindows()   # 윈도우 창 닫기

# 동영상 불러와서 출력하기
# Opencv에서 동영상을 불러온다는 것은 동영상 -> 프레임(frame) 추출 -> 이미지화 -> 출력

# desniyMov = cv2.VideoCapture('./res/mov/desniy.mp4')
# while desniyMov.isOpened():                             # 동영상 파일이 연결되어 있다면,
#     result, frame = desniyMov.read()                    # result: read 성공여부, frame: 받아온 이미지(프레임)
#     if not result:
#         print('END FRAME')
#         break


#     # 사이즈 조정
#     frame = cv2.resize(frame, (400, 600))


#     print(f'frame: {frame}')
#     cv2.imshow('title-desniyFrame', frame)              # 매우 빠르게 frame(이미지)가 출력 된다. 
#     if cv2.waitKey(1) == ord('q'):                      # 1ms동안 기다린다. 사용자가 'q'를 입력하면 중단한다.
#         break 

# desniyMov.release()                                     # 외부자원 해제
# cv2.destroyAllWindows()                                 # 윈도우 창 닫기


# # 캠에서 동영상 실시간으로 불러오기
# desniyMov = cv2.VideoCapture(0)
# while desniyMov.isOpened():                             # 동영상 파일이 연결되어 있다면,
#     result, frame = desniyMov.read()                    # result: read 성공여부, frame: 받아온 이미지(프레임)
#     if not result:
#         print('END FRAME')
#         break


#     # 사이즈 조정
#     frame = cv2.resize(frame, (400, 600))


#     print(f'frame: {frame}')
#     cv2.imshow('title-desniyFrame', frame)              # 매우 빠르게 frame(이미지)가 출력 된다. 
#     if cv2.waitKey(1) == ord('q'):                      # 1ms동안 기다린다. 사용자가 'q'를 입력하면 중단한다.
#         break 

# desniyMov.release()                                     # 외부자원 해제
# cv2.destroyAllWindows()                                 # 윈도우 창 닫기