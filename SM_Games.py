# 2025-1학기 게임프로그래밍입문
# SM게임즈 - <무인도 살인사건 추리 게임>
# 소스파일: https://github.com/miles-tails-prower05/2025-1_Python_Game/blob/main/SM_Games.py


from tkinter import *
import time

##### 함수 정의 ############################################################################
### 출력 관련 함수 ##########
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
    # print("\n")

# 이미지 출력 함수
def print_image(image, W, H, title):
    root = Tk()
    root.configure(bg="white")
    root.title(title)
    root.geometry(f"{W}x{H}")

    canvas = Canvas(root, width=W, height=H)
    canvas.pack()

    img = PhotoImage(file=image).subsample(3, 3)
    canvas.create_image(0, 0, anchor=NW, image=img)

    root.mainloop()

# 선택지를 출력하고 입력받는 함수
def print_list_and_scan_input(list):
    print_list(list, 0.03, False)
    user_input = int(input("번호를 입력하고 [Enter]를 누르세요: "))
    return user_input


### 진행 관련 함수 ##########
## 인물 소개
# 인물 소개용 리스트
introduce_NaUisa = [
    "[나의사]", 
    "- 의사", 
    "- 가방 안에 다수의 약이 존재한다", 
    "- 현실적인 편", 
    "- 매우 똑똑함", 
    "- 허기씨에게 1회용 주사기를 이용해 인슐린 주사를 도움\n"
]
introduce_KimGundal = [
    "[김건달]", 
    "- 깡패", 
    "- 건들지 않으면 가만히 있음", 
    "- 말보다 행동이 앞서는 편", 
    "- 조직생활 당시 '맞은 상처가 안 보이도록 때리기'에 능숙했음", 
    "- 허기씨와 최근에 크게 싸움\n"
]
introduce_LeeBuja = [
    "[이부자]", 
    "- 사업가", 
    "- 조난 당시 가장 먼저 식량을 발견함", 
    "- 식량 관리를 담당 중임", 
    "- 계산적임\n"
]
introduce_LeeGurim = [
    "[이그림]", 
    "- 예술가", 
    "- 최소한의 식량만 챙김", 
    "- 죽음을 하나의 예술로 생각", 
    "- 사람이 죽어가는 그림을 그림", 
    "- 처음 만났을 때 대화에 따르면 조각에는 흥미가 없어 그림만 그린다고 함\n"
]
introduce_ChoiBaeksu = [
    "[최백수]", 
    "- 무직", 
    "- 긴장하면 말을 더듬음", 
    "- 무인도에서 의사 다음으로 똑똑함", 
    "- 사건 현장 최초 목격자\n"
]
introduce_LeeHuggi = [
    "[이허기]: 사망", 
    "- 당뇨병 환자", 
    "- 먹는 양이 많음", 
    "- 최근에 건달씨와 크게 싸움", 
    "- 새벽에 몰래 식량 보관소에서 음식을 먹다 걸린 적이 있음\n"
]
# 인물 소개용 함수
def introduce_character(name):
    print_list(eval(f"introduce_{name}"), 0.03)

## 행동 선택
# 선택한 행동을 입력받기 위한 리스트
action_list = [
    "\n\n\n\n무엇을 하시겠습니까?",
    "[1] 용의자 조사하기",
    "[2] 장소 조사하기",
    "[3] 범인 지목하기\n"
]
# 선택한 행동을 입력받기 위한 함수
def select_action(): 
    action = 0
    while (action != 1) and (action != 2) and (action != 3):
        action = print_list_and_scan_input(action_list)
    return action

## 용의자 조사
# 조사할 용의자를 선택하기 위한 리스트
suspect_list = [
    "\n\n\n<<<<< 용의자 조사하기 >>>>>\n", 
    "누구를 조사하시겠습니까?",
    "[1] 나의사", 
    "[2] 김건달", 
    "[3] 이부자", 
    "[4] 이그림", 
    "[5] 최백수\n"
]
# 조사할 용의자를 선택하기 위한 함수
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

# 용의자를 조사하기 위한 리스트
suspect_NaUisa = [
    "[나의사]: 제가 피해자를 봤을 때 입에 거품을 물고 있었어요.", 
    "          보통 이런 경우는 잘못된 음식을 먹었을 경우가 높은데 식량 관리하시는 이부자씨가 음식에 뭘 넣은 건 아닐지...", 
    "\n(의사씨 말이면 충분히 믿을만하지 부자씨한테 가봐야겠어)"
]
suspect_KimGundal = [
    "[김건달]: 내가 아무리 그 XX를 친 적이 있긴 했어도 나겠어 형씨?", 
    "          어젯밤에 난 계속 자고 있었어. 또 뭐 혼자 처먹다가 잘못 먹어서 죽은 거겠지.", 
    "          식량만 축내는 놈 죽었으니 식량도 여유 생기고 좋네.", 
    "          정 궁금하면 그림쟁이한테 가봐. 어제 보니 잠도 안 자고 그림만 그리더만.",
    "\n(흠.. 계속 잤다더니 어떻게 그림씨가 안 자는 걸 알고 있지?)"
]
suspect_LeeBuja = [
    "[이부자]: 어제 본 거 있냐고?", 
    "          식량 보관소 옆에서 자긴 했는데 뭐 딱히 본 건 없어.", 
    "          아 맞다 그러고 보니 어제 큰 소리가 한번 났던 것 같기도 한데...", 
    "          잠결에 들은 거라 몰라 난~", 
    "          허기씨도 참 딱하구먼...", 
    "          그래도 이러면 구조대 오기까지 식량은 남겠구먼.", 
    "          이 식량 다 나중에 갚아야 하는 거 알제?", 
    "\n(큰 소리...? 싸움이라도 있었던 건가)"
]
suspect_LeeGurim = [
    "[이그림]: 예술은 죽음!!! 죽음으로 이루어지지!!!", 
    "          난 그걸 봤다고!! 봤어!!!!", 
    "          신이시여!! 감사합니다! 이런 은혜를!!",
    "\n(어제 뭘 본거지? 전보다 더 이상해졌어... 더 이상의 대화는 안 통할 것 같군)"
]
suspect_ChoiBaeksu = [
    "[최백수]: 어... 어제 발견했을 때는 입에 거품을 물고 있었어요.", 
    "          근데 신기한 게 출혈이 없더라고요...", 
    "          근데 이건 왜... 저 의심하는 건 아니죠...? 전 진짜 아니에요..", 
    "          하하...", 
    "          제가 왜 사람을 죽였겠어요.. 근데 손에 이걸 들고 있었어요..",
    "\n(이건 커터칼인데... 설마 그림씨가? 근데 왜 백수 씨는 말을 떨지? 원래 안 그랬는데...)"
]
# 용의자를 조사하기 위한 함수
def investigate_suspect(name):
    if name == "ChoiBaeksu":
        print("\n\n\n")
        print_list(eval(f"suspect_{name}")[0:len(eval(f"suspect_{name}"))-1])
        print_image("image\BrokenCutter.png", 512, 341, "허기씨가 손에 들고 있던 것")
        time.sleep(0.5)
        print_sentence(eval(f"suspect_{name}")[len(eval(f"suspect_{name}"))-1])
    else:
        print("\n\n\n")
        print_list(eval(f"suspect_{name}")[0:len(eval(f"suspect_{name}"))-1])
        time.sleep(0.5)
        print_sentence(eval(f"suspect_{name}")[len(eval(f"suspect_{name}"))-1])

# 용의자를 조사한 후의 행동을 위한 리스트
after_suspect_investigation_action_list = [
    "\n\n\n그다음으로 무엇을 하시겠습니까?",
    "[1] 용의자 정보 보기",
    "[2] 다른 용의자 조사하기",
    "[3] 돌아가기\n"
]
# 용의자를 조사한 후의 행동을 위한 함수
def select_after_suspect_investigation_action():
    action = 0
    while (action != 1) and (action != 2) and (action != 3):
        action = print_list_and_scan_input(after_suspect_investigation_action_list)
    return action

# 용의자 조사를 처리하는 함수
def process_investigating_suspect():
    suspect_investigating = True
    while suspect_investigating == True: 
        suspect = select_suspect_to_investigate()
        investigate_suspect(suspect)

        after_investigation = select_after_suspect_investigation_action()
        if after_investigation == 1:
            print("\n\n\n")
            introduce_character(suspect)
            suspect_investigating = False
            continue
        elif after_investigation == 2:
            suspect_investigating = True
            continue
        elif after_investigation == 3:
            suspect_investigating = False
            continue
    
## 장소 조사
# 조사할 장소를 선택하기 위한 리스트
place_list = [
    "\n\n\n<<<<< 장소 조사하기 >>>>>\n", 
    "어디를 조사하시겠습니까?",
    "[1] 숲속",
    "[2] 허기씨의 가방", 
    "[3] 식량 보관소", 
    "[4] 사건 현장", 
    "[5] 바닷가",
    "[6] 그림씨의 가방\n"
]
# 조사할 장소를 선택하기 위한 함수
def select_place():
    place = 0
    while (place != 1) and (place != 2) and (place != 3) and (place != 4) and (place != 5) and (place != 6):
        place = print_list_and_scan_input(place_list)
    return place

#장소를 조사하기 위한 리스트
place_forest = [
    "\n\n\n[숲속]",
    "숲속을 한 번 찾아보자.\n\n",
    "터벅\n\n",
    "터벅\n\n",
    "이게 뭐지...", 
    "이건 종이인데.. 타버려서 어떤 종이인지는 잘 모르겠군."
]
place_Huggi_bag = [
    "\n\n\n[허기씨의 가방]",
    "가방 안에 약이 많네...", 
    "저번에 당뇨병이 있다고는 들었는데..."
]
place_storage = [
    "\n\n\n[식량 보관소]",
    "난장판이 되었군 마치 누가 싸운 듯...", 
    "허기씨는 여기서 쓰러지고 누군가가 밖으로 옮긴 걸지도 몰라."
]
place_the_scene = [
    "\n\n\n[사건 현장]",
    "이건 뭐지 다잉 메시지인가?", 
    "바닥이 모래라 일부가 지워졌군.", 
    "그래도 중요한 단서를 얻었군."
]
place_beach = [
    "\n\n\n[바닷가]",
    "여긴 단서가 없는 것 같군.", 
    "다른 곳으로 가봐야겠어."
]
place_Gurim_bag = [
    "\n\n\n[그림씨의 가방]",
    "왜 부러진 커터칼 나머지 부분이 그림씨 가방에 있는 거지?"
]
#장소를 조사하기 위한 함수
def investigate_place(place):
    if place == 1:
        print_list(place_forest[0:3])
        time.sleep(1)
        print_sentence(place_forest[3] + "\n")
        time.sleep(1)
        print_sentence(place_forest[4])
        print_image("image\BurnedPaper.png", 341, 341, "불타버린 종이")
        print_sentence(place_forest[5])
    elif place == 2:
        print_list(place_Huggi_bag)
        print_image("image\DrugAndBag.png", 341, 512, "허기씨의 가방")
    elif place == 3:
        print_list(place_storage)
        print_image("image\FoodStorage.png", 341, 341, "식량 보관소")
    elif place == 4:
        print_list(place_the_scene[0:3])
        print_image("image\TheScene.png", 341, 512, "사건 현장")
        print_sentence(place_the_scene[3])
    elif place == 5:
        print_list(place_beach)
    elif place == 6:
        print_list(place_Gurim_bag)
        print_image("image\CutterAndBag.png", 512, 341, "그림씨의 가방")

# 장소를 조사한 후의 행동을 위한 리스트
after_place_investigation_action_list = [
    "\n\n\n그다음으로 무엇을 하시겠습니까?",
    "[1] 다른 장소 조사하기",
    "[2] 돌아가기\n"
]
# 장소를 조사한 후의 행동을 위한 함수
def select_after_place_investigation_action():
    action = 0
    while (action != 1) and (action != 2):
        action = print_list_and_scan_input(after_place_investigation_action_list)
    return action

# 장소 조사를 처리하는 함수
def process_investigating_place():
    place_investigating = True
    while place_investigating == True:
        place = select_place()
        investigate_place(place)

        after_investigation = select_after_place_investigation_action()
        if after_investigation == 1:
            place_investigating = True
            continue
        elif after_investigation == 2:
            place_investigating = False
            continue

## 범인 지목
# 범인 지목을 위한 리스트
criminal_list = [
    "\n\n\n<<<<< 범인 지목하기 >>>>>\n", 
    "누구를 지목하시겠습니까?",
    "[1] 나의사", 
    "[2] 김건달", 
    "[3] 이부자", 
    "[4] 이그림", 
    "[5] 최백수\n"
]
# 범인 지목을 위한 함수
def select_criminal():
    criminal = 0
    while (criminal != 1) and (criminal != 2) and (criminal != 3) and (criminal != 4) and (criminal != 5):
        criminal = print_list_and_scan_input(criminal_list)

    name_list = ["나의사", "김건달", "이부자", "이그림", "최백수"]
    return name_list[criminal-1]

# 범인 지목과 엔딩을 처리하기 위한 리스트
ending_good = [
    "\n\n\n\n\n범인은 당신이야!\n", 
    "허기씨의 당뇨병을 이용해 인슐린을 과다 투여하여 사망시키다니... 당신을 격리하겠습니다!\n",
    "나의사: 어떻게....", 
    "        난 해야 할 일을 했을 뿐이야...", 
    "        쟤가 있었으면 식량은 부족했을 거라고!!", 
    "        난 무죄야 난 무죄라고!!!!"
]
ending_bad = [
    "\n\n\n\n\n범인은 당신입니다! 당신을 격리시키도록 하죠.\n\n", 
    ": 억울해요.. 전 아니에요!!\n\n\n",
    "그날 밤\n\n",
    "뭐지... 왜 이렇게 아프지..? 어라 내 몸이 왜 이래!\n",
    "???: 일어나셨네 형사양반 당신이 마지막이야..", 
    "     그러게 추리를 잘 좀 하시지... 다음 생에는 만나지 말자고~\n",
    "으아아악!!!"
]
credit = [
    "< 무인도 살인사건 추리 게임 >",
    "",
    "제작: SM게임즈",
    "      - 팀장: 한승원", 
    "      - 기획, 이미지 제작: 신동규", 
    "      - 코딩: 박건우", 
    "",
    "      - 발표: 한승원", 
    "      - 발표 자료 제작: 신동규", 
    "",
    "",
    "플레이해 주셔서 감사합니다."
]
# 범인 지목과 엔딩을 처리하기 위한 함수
def process_ending():
    criminal = select_criminal()

    if criminal == "나의사":
        print_list(ending_good)
    else:
        print_sentence(ending_bad[0])
        print(f"{criminal}{ending_bad[1]}")

        for x in range(5):
            print(". ", end="")
            time.sleep(0.4)
        
        print_list(ending_bad[2:])

    time.sleep(0.4)
    for y in range(10):
        print("")
        time.sleep(0.2)
    print_list(credit)
##########################################################################################


##### 게임 코드 ############################################################################
intro_story = [
    "한 비행기가 운행 중 갑작스러운 난기류에 휩쓸려 추락하게 된다.", 
    "이로 인해 비행기 안에 있던 대부분의 사람은 사망하고 말았지만, 일부는 사고로 인한 큰 부상이 없었던 [나의사]의 도움으로 목숨을 구할 수 있었다.", 
    "그들은 비행기 안에 있는 식량과 무인도에 있는 각종 과일로 하루하루를 버티고 있었지만 점차 식량은 부족해지기 시작한다.", 
    "그러던 어느 날 밤. 당신은 잠을 자던 중 큰 비명소리에 눈을 떴고 비명소리가 난 곳으로 가보니...", 
    "", 
    "사람들이 모여있고 그 가운데에는 한 사람이 죽어 있었다.", 
    "전직 형사였던 당신. 살아있는 사람들의 안전을 위해 살인범을 찾아 격리시키려고 한다.", 
    "과연 당신은 범인을 찾고 사람들을 구할 수 있을까?"
]
print_list(intro_story, newline=True)

print("\n\n<<<<< 인물 소개 >>>>>\n")
for name in ["NaUisa", "KimGundal", "LeeBuja", "LeeGurim", "ChoiBaeksu", "LeeHuggi"]: 
    introduce_character(name)

while True:
    action = select_action()

    if action == 1:
        process_investigating_suspect()
    elif action == 2: 
        process_investigating_place()
    elif action == 3:
        process_ending()
        break
##########################################################################################