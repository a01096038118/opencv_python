import cv2

print(cv2.__version__)

class NaturalImg:
    def naturalImg():
        natImg = cv2.imread('./20260605ex/img/img_01.jpg')
        print(f'natImg shape: {natImg.shape}')

        natImg = cv2.resize(natImg, (630, 550))

        cv2.imshow('title-img_01',natImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
# natImg = cv2.imread('./20260605/img/img_01.jpg',cv2.IMREAD_COLOR)
