import config.config as root_config
from member import memberService
from memo import memoService

def main():
    flag = True
    while flag:
        menuNum = int(input('1.MEMBER   2.MEMO    99.SERVICE-OUT '))
        if menuNum == root_config.MEMBER_SERVICE:
            memberService.MemberService().run()

        elif menuNum == root_config.MEMO_SERVICE:
            memoService.MemoService().run()

        elif menuNum == root_config.SERVICE_OUT:
            flag = False


if __name__ == "__main__":
    main()