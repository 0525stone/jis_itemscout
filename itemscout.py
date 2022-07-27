"""
인섭이형 프로그램

1 itemscout.io 접속
2 카테고리 선택
3 기간 (최근 30일 또는 직접 선택 두가지 경우에 대해서)
	3-1 최근 30일
	3-2 직접 선택 => 날짜 직접 입력할 수 있게
4 BAN필터 선택후 조회하기
	4 detail : 선택 항목들이 많음 (커스텀할 수 있게 하면 좋을 듯?)
			각 선택 옵션에 대해서 접근하는 방법 구현하고, class 내에 flag 세워서 입력 받을 시 돌아가게 끔
5 엑셀 버튼 눌러서 다운 받기
6 두번째 카테고리 선택하고 같은 과정 반복
	6 카테고리 따로 선택 가능한지 확인

다음 프로세스
7 자동으로 다운로드 된 파일들을 합쳐서 하나의 엑셀 파일에 합쳐주기


구현시 신경 쓸 것

[BAN 필터 관련 정보 포함된 엑셀 파일]
정보는 각각 인섭이형한테 받아와야함

클래스 만들기
    init 에서 로그인 정보하고 전부 들어가게
    발굴탭으로 이동


"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

import argparse
import re
import time
import os


class itemscout(object):
    def __init__(self):
        self.id = 'lion12fox@gmail.com'
        self.pw = 'eoqkrdldh1!'
        

    def launch_web(self):
        # 
        pass


def main():
    ic = itemscout()
    pass



if __name__=="__main__":
    main()