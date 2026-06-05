from session import session
from member import config as member_config
import os
import json
import config.config as root_config

class MemberService:
    def __init__(self):
        self.members = {}
        self.init_database()

    def sign_up(self):
        mId = input('Input ID: ')
        if mId in self.members:
            print('중복된 ID입니다.')
            return
        
        mPw = input('Input PW: ')
        mMail = input('Input Mail: ')
        mPhone = input('Input Phone: ')
    
        members = {
            'mId': mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone': mPhone
        }

        self.members[mId] = members
        self.save_members(self.members)

        print('MEMBER SIGN-UP SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members: {self.load_members()}')

    def sign_in(self):
        mId = input('Input ID: ')
        mPw = input('Input Pw: ')

        self.members = self.load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('SING-IN SUCCESS!!')
            session.setSignIneMemberId(mId)

            if root_config.DEV_MOD:
                print(f'session.signInedMemberId: {session.signInedMemberId}')
                return
            
            print('SIGN-IN FAIL!!')

    def sign_out(self):
        session.setSignIneMemberId()
        print('SIGN-OUT SUCCESS!!')

    def modify(self):
        mPw = input('Input PW: ')
        mMail = input('Input Mail: ')
        mPhone = input('Input Phone: ')

        self.members = self.load_members()
        memberModify = self.members[session.getSignIneMemberId()]

        memberModify['mPw'] = mPw
        memberModify['mMail'] = mMail
        memberModify['mPhone'] = mPhone

        self.save_members(self.members)

        print('MEMBER MODIFY SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members: {self.load_members()}')


    def delete(self):
        confirm = input('회원탈퇴 하시겠습니까? [Y] or [N]')
        if confirm == 'Y':
            self.members = self.load_members()
            del self.members[session.getSignIneMemberId()]
            self.save_members(self.members)
            session.setSignIneMemberId()
            print('DELETE SUCCESS!!')

            if root_config.DEV_MOD:
                print(f'self.load_members() = {self.load_members()}')


    def run(self):
        flag = True
        while flag:
            if session.getSignIneMemberId() == '':
                menuNum = int(input('1. SIGN-UP     2. SIGN-IN   99.SERVICE-OUT '))
            else:
                menuNum = int(input('3. SIGN-OUT    4.MODIFY    5.DELETE    99.SERVICE-OUT '))
            
            if menuNum == member_config.SIGN_UP:
                self.sign_up()

            elif menuNum == member_config.SIGN_IN:
                self.sign_in()    
            
            elif menuNum == member_config.SIGN_OUT:
                self.sign_out()
            
            elif menuNum == member_config.MODIFY:
                self.modify()
            
            elif menuNum == member_config.DELETE:
                self.delete()

            elif menuNum == member_config.SERVICE_OUT:
                flag = False

    def init_database(self):
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json' )
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):
            self.save_members(self.members)
        else:
            self.members = self.load_members()

    def save_members(self, members):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)

    def load_members(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
            

if __name__ == '__main__':
    memberService = MemberService()
    memberService.run()
