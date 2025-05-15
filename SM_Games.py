# from tkinter import *
import time

### 함수 정의 ############################################################################
## 기능 관련 함수 ##########
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

## 내용 관련 함수 ##########
# 인물 소개 함수
def introduce_character(name):
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
    print_list(eval(f"introduce_{name}"), 0.03)
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

##########################################################################################