import os
import json
from session import session
from memo import config as memo_config
import config.config as root_config
import cv2
from imgex import imgex



class MemoService:
    def __init__(self):
        self.memos = {}
        self.init_database()

    def init_database(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        self.imgFile = os.path.join(ROOT_DIR, 'img', 'img_01.jpg')
        print(f'self.imgFile: {self.imgFile}')
        
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'memos.json')
        print(f'self.dbFile: {self.dbFile}')
        
        if not os.path.exists(self.dbFile):
            self.save_memos(self.memos)
        else:
            self.memos = self.load_memos()
            

    def save_memos(self, memos):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)
            
    def load_memos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def isMyMemos(self):
        allMemos = self.load_memos()
        if session.getSignIneMemberId() in allMemos:
            return True
        
        return False
    
    def run(self):
        if session.getSignIneMemberId() == '':
            print('Please SIGN-IN!!')

    

        flag = True
        while flag:

            if not self.isMyMemos():
                self.memos[session.getSignIneMemberId()] = []
                self.save_memos(self.memos)

            menuNum = int(input('1.WRITE    2.READ     3.UPDATE     4.DELETE    99.SERVICE-OUT '))
            if menuNum == memo_config.WRITE:
                newMemo = input('Write memo: ')

                self.memos = self.load_memos()
                myMemos = self.memos[session.getSignIneMemberId()]
                myMemos.insert(0, newMemo)

                self.save_memos(self.memos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')

            elif menuNum == memo_config.READ:
                self.memos = self.load_memos()
                myMemos = self.memos[session.getSignIneMemberId()]
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx + 1}] {memo}')

                
                natImg = cv2.imread(self.imgFile)
                if natImg is None:
                    print('이미지 로드 실패')
                    return
                print(f'natImg shape: {natImg.shape}')

                    # print(natImg)

                natImg = cv2.resize(natImg, (630, 550))


                cv2.putText(
                    natImg,
                    memo,
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2
                )
                    

                cv2.imshow('title-img_01',natImg,)
                cv2.waitKey(0)
                cv2.destroyAllWindows()


            elif menuNum == memo_config.UPDATE:
                self.memos = self.load_memos()
                myMemos = self.memos[session.getSignIneMemberId()]
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx + 1}] {memo}')

                selectedNumber = int(input('select the number to modify: '))
                memo = input('Edit memo: ')
                myMemos[selectedNumber -1] = memo

                self.save_memos(self.memos)
                print('MODIFY SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')

            elif menuNum == memo_config.DELETE:
                self.memos = self.load_memos()
                myMemos = self.memos[session.getSignIneMemberId()]
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx + 1}] {memo}')

                selectedNumber = int(input('select the number to delete: '))
                myMemos.pop(selectedNumber -1)
                self.save_memos(self.memos)

                if root_config.DEV_MOD:
                    print(f'self.load_memos(): {self.load_memos()}')


            elif menuNum == memo_config.SERVICE_OUT:
                flag = False





if __name__ == '__main__':
    memoService = MemoService()
    memoService.run()