# from tkinter import *
import time

### 함수 정의 ############################################################################
## 출력 관련 함수 ##########
# 문장 출력 함수
def print_sentence(sentence, timesl=0.06):      # https://yanoos.tistory.com/10 참고하였음
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)

# 리스트의 문장을 출력하는 함수
def print_list(list, timesl=0.06, newline=False):
    for sentence in list:
        print_sentence(sentence, timesl)
        if newline == True:
            print("\n")
        else:
            print("")
    print("\n")

# 이미지 출력 함수
def print_image(image, title):
    root = Tk()
    root.configure(bg="white")
    root.title(title)
    root.geometry("700x700")

    canvas = Canvas(root, width=700, height=700)
    canvas.pack()

    root.mainloop()

# 선택지를 출력하고 입력받는 함수
def print_list_and_scan_input(list):
    print_list(list, 0.03, False)
    user_input = int(input("번호를 입력하고 [Enter]를 누르세요: "))
    return user_input


## 진행 관련 함수 ##########
# 인물 소개용 리스트와 함수
introduce_NaUisa = [
    "[나의사]", 
    "- 의사", 
    "- 가방안에 다수의 약이 존재한다", 
    "- 현실적인편", 
    "- 매우 똑똑함", 
    "- 허기씨에게 1회용 주사기를 이용해 인슐린 주사를 도움"
]
introduce_KimGundal = [
    "[김건달]", 
    "- 깡패", 
    "- 건들지 않으면 가만히있음", 
    "- 말보다 행동이 앞서는 편", 
    "- 조직생활 당시 맞은 상처가 안보이도록 때리기에 능숙했음", 
    "- 허기씨와 최근에 크게 싸움"
]
introduce_LeeBuja = [
    "[이부자]", 
    "- 사업가", 
    "- 조난 당시 가장 먼저 식량을 발견함", 
    "- 식량 관리를 담당중임", 
    "- 계산적임"
]
introduce_LeeGurim = [
    "[이그림]", 
    "- 예술가", 
    "- 최소한의 식량만 챙김", 
    "- 죽음을 하나의 예술로 생각", 
    "- 사람이 죽어가는 그림을 그림", 
    "- 처음 만났을때 대화에 따르면 조각에는 흥미가 없어 그림만 그린다고 함"
]
introduce_ChoiBaeksu = [
    "[최백수]", 
    "- 무직", 
    "- 긴장하면 말을 절음", 
    "- 무인도에서 의사 다음으로 똑똑함", 
    "- 사건현장 최초 목격자"
]
introduce_LeeHuggi = [
    "[이허기]", 
    "- 당뇨병 환자", 
    "- 먹는 양이 많음", 
    "- 최근에 건달씨와 크게 싸움", 
    "- 새벽에 몰래 식량보관소에서 음식을 먹다 걸린적이 있음"
]
def introduce_character(name):
    print_list(eval(f"introduce_{name}"), 0.03)

# 조사할 용의자를 선택하기 위한 리스트와 함수
suspect_list = [
    "\n\n<<<<< 용의자 조사하기 >>>>>\n", 
    "누구를 조사하시겠습니까?",
    "[1] 나의사", 
    "[2] 김건달", 
    "[3] 이부자", 
    "[4] 이그림", 
    "[5] 최백수"
]
def select_suspect_to_investigate():
    suspect = 0
    while (suspect != 1) and (suspect != 2) and (suspect != 3) and (suspect != 4) and (suspect != 5):
        suspect = print_list_and_scan_input(suspect_list)

        if suspect == 1:
            return "NaUisa"
        elif suspect == 2:
            return "KimGundal"
        elif suspect == 3:
            return "LeeBuja"
        elif suspect == 4:
            return "LeeGurim"
        elif suspect == 5:
            return "ChoiBaeksu"
        else: 
            continue

# 용의자를 조사하기 위한 리스트와 함수
suspect_NaUisa = [
    "\n[나의사]: 제가 피해자를 봤을 때 입에 거품을 물고 있었어요.", 
    "          보통 이런경우는 잘못된 음식을 먹었을 경우가 높은데 식량 관리 하시는 이부자씨가 음식에 뭘 넣은건 아닐지... ", 
    "(의사씨 말이면 충분히 믿을만하지 부자씨한테 가봐야겠어)"
]
suspect_KimGundal = [
    "\n[김건달]: 내가 아무리 그 XX를 친적이 있긴 했어도 나겠어 형씨?", 
    "          어제밤에 난 계속 자고 있었어. 또 뭐 혼자 쳐먹다가 잘못먹어서 죽은거겠지.", 
    "          식량만 축내는놈 죽었으니 식량도 여유생기고 좋네.", 
    "          정 궁금하면 그림쟁이한테 가봐. 어제보니 잠도 안자고 그림만 그리더만.",
    "(흠.. 계속 잤다더니 어떻게 그림씨가 안자는걸 알고있지?)"
]
suspect_LeeBuja = [
    "\n[이부자]: 어제 본거있냐고?", 
    "          식량 보관소 옆에서 자긴했는데 뭐 딱히 본 건 없어.", 
    "          아 맞다 그러고보니 어제 큰 소리가 한번 났던것 같기도 한데...", 
    "          잠결에 들은거라 몰라 난~ 허기씨도 참 딱하구먼...", 
    "          그래도 이러면 구조대 오기까지 식량은 남겠구먼 이 식량 다 나중에 갚아야 하는거 알제?", 
    "(큰 소리...? 싸움이라도 있었던건가)"
]
suspect_LeeGurim = [
    "\n[이그림]: 예술은 죽음!!! 죽음으로 이루어지지!!!", 
    "          난 그걸 봤다고!! 봤어!!!!", 
    "          신이시여!! 감사합니다! 이런 은혜를!!",
    "(어제 뭘본거지? 전보다 더 이상해졌어... 더이상의 대화는 안통할 것 같군)"
]
suspect_ChoiBaeksu = [
    "\n[최백수]: 어... 어제 발견했을때는 입에 거품을 물고 있었어요.", 
    "          근데 신기한게 출혈이 없더라고요...", 
    "          근데 이건 왜... 저 의심하는건 아니죠...? 전 진짜 아니에요..", 
    "          하하... 제가 왜 사람을 죽였겠어요.. 근데 손에 이걸 들고 있었어요..",
    "(이건 커터칼 인데... 설마 그림씨가? 근데 왜 백수씨는 말을 떨지? 원래 안그랬는데...)"
]
def investigate_suspect(name):
    if name == "ChoiBaeksu":
        print_list(eval(f"suspect_{name}")[0:len(eval(f"suspect_{name}"))-1])
        # 여기에 사진 출력 코드 삽입
        time.sleep(0.5)
        print_sentence(eval(f"suspect_{name}")[len(eval(f"suspect_{name}"))-1])
    else:
        print_list(eval(f"suspect_{name}")[0:len(eval(f"suspect_{name}"))-1])
        time.sleep(0.5)
        print_sentence(eval(f"suspect_{name}")[len(eval(f"suspect_{name}"))-1])


# 선택한 행동을 입력받기 위한 리스트와 함수
action_list = [
    "\n\n무엇을 하시겠습니까?",
    "[1] 용의자 조사하기",
    "[2] 장소 조사하기",
    "[3] 범인 지목하기"
]
def select_action(): 
    action = 0
    while (action != 1) and (action != 2) and (action != 3):
        action = print_list_and_scan_input(action_list)
    
    start_action(action)

# 선택한 행동을 실행하는 함수
def start_action(action):
    if action == 1:
        suspect = select_suspect_to_investigate()
        investigate_suspect(suspect)
    # elif action == 2: # 마저 작성하기

##########################################################################################


### 게임 코드 ############################################################################
intro_story = [
    "한 비행기가 운행 중 갑작스러운 난기류에 휩쓸리게 된다.", 
    "이로 인해 비행기 안에 있던 대부분의 사람은 사망하고 말았지만 일부 사람들은 사고로 인한 큰 부상이 없었던 [나의사]의 도움으로 목숨을 구할 수 있었다.", 
    "그들은 비행기 안에 있는 식량과 무인도에 있는 각종 과일로 하루하루를 버티고 있었지만 점차 식량은 부족해지기 시작한다.", 
    "그러던 어느날 밤 당신은 잠을 자던 중 큰 비명소리에 눈을 떴고 비명소리가 난 곳으로 가보니...", 
    "", 
    "사람들이 모여있고 그 가운데에는 한 사람이 죽어 있었다.", 
    "전직 형사였던 당신. 살아있는 사람들의 안전을 위해 살인범을 찾아 격리시키려고 한다.", 
    "과연 당신은 범인을 찾고 사람들을 구할 수 있을까?"
]
print_list(intro_story, newline=True)

print("\n\n<<<<< 인물 소개 >>>>>\n")
for name in ["NaUisa", "KimGundal", "LeeBuja", "LeeGurim", "ChoiBaeksu", "LeeHuggi"]: 
    introduce_character(name)

# 테스트용 코드
#investigate_suspect("KimGundal")

while True:
    action = select_action()
    start_action(action)
    
    break
##########################################################################################