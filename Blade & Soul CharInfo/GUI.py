from info_crawl import info_call
from tkinter import *
import pandas as pd

global dat

dat = pd.read_excel("dic.xlsx")


# 사전에서 단어를 찾아 뜻을 보여준다.
def click():
    word = entry.get()  # 우리가 입력한 단어.

    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지(END) 지우겠다.
    output.delete(0.0, END)  # (결과) 텍스트 박스을 지워준다.
    output1.delete(0.0, END)

    try:
        # def_word = dict_all[word]
        # def_word = dat.loc[행, 열]
        kor_def = dat.loc[dat['한글단어이름'] == word, '한글내용'].values[0]
        eng_word = dat.loc[dat['한글단어이름'] == word, '영어단어이름'].values[0]

    except:
        kor_def = "단어의 뜻을 찾을 수 없습니다."
        eng_word = 'No such word has founded'

    # END : 문자열이 입력된 최종 지점을 의미한다.
    output.insert(END, kor_def)
    output1.insert(END, eng_word)


def click_eng():
    word = entry.get()  # 우리가 입력한 단어.

    output.delete(0.0, END)  # (결과) 텍스트 박스을 지워준다.
    output1.delete(0.0, END)

    try:
        kor_def = dat.loc[dat['한글단어이름'] == word, '영어내용'].values[0]
        eng_word = dat.loc[dat['한글단어이름'] == word, '영어단어이름'].values[0]

    except:
        kor_def = "ERROR : No such Korean word has founded"
        eng_word = 'No such Korean word has founded'

    # END : 문자열이 입력된 최종 지점을 의미한다.
    output.insert(END, kor_def)
    output1.insert(END, eng_word)


def press_ent(event):
    word = entry.get()
    output.delete(0.0, END)
    output1.delete(0.0, END)

    try:
        kor_def = dat.loc[dat['한글단어이름'] == word, '한글내용'].values[0]
        eng_word = dat.loc[dat['한글단어이름'] == word, '영어단어이름'].values[0]

    except:
        kor_def = "단어의 뜻을 찾을 수 없습니다."
        eng_word = 'No such word has founded'

    output.insert(END, kor_def)
    output1.insert(END, eng_word)


# 메인
w = Tk()
w.title("My Dictionary")

# 설명 레이블
label = Label(w, text="단어 검색 [엔터키 입력시 한글 검색] : ")
label.grid(row=0, column=0, sticky=W)

# 입력 상자(텍스트 입력) - Entry
entry = Entry(w, width=15, bg="light yellow")
entry.grid(row=1, column=0, sticky=W)

# '단어 뜻 확인'  버튼 추가
btn = Button(w, text="한국어", width=5, command=click)
btn.grid(row=2, column=0, sticky=W)

# '단어 뜻 확인'  버튼 추가
btn = Button(w, text="ENG", width=5, command=click_eng)
btn.grid(row=2, column=0)

# 설명(뜻 보여주는 상자에 대한) 레이블
label2 = Label(w, text="\n단어 정의[def.]:")
label2.grid(row=3, column=0, sticky=W)

# 한글 정의 출력 상자
output = Text(w, width=50, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

label3 = Label(w, text="\n영어 단어:")
label3.grid(row=5, column=0, sticky=W)

# 영단어 출력 상자
output1 = Text(w, width=50, height=6, wrap=WORD, background="light green")
output1.grid(row=6, column=0, columnspan=2, sticky=W)

w.bind('<Return>', press_ent)

w.mainloop()
