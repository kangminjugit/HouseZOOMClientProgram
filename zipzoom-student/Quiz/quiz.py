from PIL import Image, ImageDraw, ImageFont
import os
import cv2
from cv2 import LINE_AA
import numpy as np


class QuizHandler:
    def __init__(self):

        # 퀴즈 시작 알리는 이미지 마스크 생성
        self.quiz_start_img = cv2.imread(
            'Quiz/quiz_start.png', cv2.IMREAD_UNCHANGED)
        # self.quiz_start_img = cv2.flip(quiz_start_img, 1)
        _, self.quiz_start_mask = cv2.threshold(
            self.quiz_start_img[:, :, 3], 1, 255, cv2.THRESH_BINARY)
        self.quiz_start_mask_inv = cv2.bitwise_not(self.quiz_start_mask)
        self.quiz_start_img = cv2.cvtColor(
            self.quiz_start_img, cv2.COLOR_BGRA2BGR)
        self.sh, self.sw, self.sc = self.quiz_start_img.shape

        # 퀴즈 문제와 이미지 합치기
        self.quiz_img = Image.open('Quiz/melon_talkBox.jpg')
        self.w, self.h = self.quiz_img.size

        # 퀴즈 답 기다리는 중 이미지
        self.quiz_submit_img = Image.open('Quiz/orange_talk_box.jpg')
        self.ww, self.wh = self.quiz_submit_img.size

        # 퀴즈 결과와 이미지 합치기
        self.quiz_result_img = Image.open('Quiz/talkBox.jpg')
        self.rw, self.rh = self.quiz_result_img.size

        # 퀴즈 문제, 결과 폰트
        self.font = ImageFont.truetype(os.path.join(
            'Quiz/Font', 'SuseongDotum.ttf'), 30, encoding="UTF-8")

    def start_quiz(self, frame):
        background_height, background_width, _ = frame.shape  # 720,1280
        # x = background_height - self.h
        y = background_width - self.sw

        roi = frame[background_height//2-self.sh//2: background_height//2-self.sh//2 +
                    self.sh, background_width//2-self.sw//2: background_width//2-self.sw//2+self.sw]

        masked_me = cv2.bitwise_and(
            self.quiz_start_img, self.quiz_start_img, None, mask=self.quiz_start_mask)
        masked_roi = cv2.bitwise_and(
            roi, roi, None, mask=self.quiz_start_mask_inv)

        result = masked_me + masked_roi

        frame[background_height//2-self.sh//2: background_height//2-self.sh//2 +
              self.sh, background_width//2-self.sw//2: background_width//2-self.sw//2+self.sw] = result

        return frame

    def set_ox_quiz(self, frame, problem):
        self.quiz_img = Image.open('Quiz/melon_talkBox.jpg')
        self.w, self.h = self.quiz_img.size
        draw = ImageDraw.Draw(self.quiz_img)

        quizText = problem + '\n'
        quizText += 'O 또는 X 표시를 해주세요\n'
        tw, th = draw.textsize(quizText, self.font)

        background_height, background_width, _ = frame.shape  # 720,1280
        self.y = background_width - self.w
        draw.text((self.w//2-tw//2, self.h//2-th//2), quizText, fill='black',
                  font=self.font, align='center')
        # self.flipped_quiz_img = self.quiz_img.transpose(Image.FLIP_LEFT_RIGHT)
        self.flipped_quiz_img = self.quiz_img

    def set_multichoice_quiz(self, frame, problem, multiChoices):
        self.quiz_img = Image.open('Quiz/melon_talkBox.jpg')
        self.w, self.h = self.quiz_img.size
        draw = ImageDraw.Draw(self.quiz_img)

        quizText = problem + '\n'
        for i in range(len(multiChoices)):
            quizText += '{} : {}\n'.format(i+1, multiChoices[i])
        tw, th = draw.textsize(quizText, self.font)

        background_height, background_width, _ = frame.shape  # 720,1280
        self.y = background_width - self.w
        draw.text((self.w//2-tw//2, self.h//2-th//2), quizText, fill='black',
                  font=self.font, align='center')
        # self.flipped_quiz_img = self.quiz_img.transpose(Image.FLIP_LEFT_RIGHT)

        self.flipped_quiz_img = self.quiz_img

    def show_quiz(self, frame):
        frame[10: 10+self.h, self.y:self.y+self.w] = self.flipped_quiz_img

        return frame

    def show_quiz_submit_msg(self, frame):
        background_height, background_width, _ = frame.shape  # 720,1280
        # x = background_height - self.h
        y = background_width - self.ww
        draw = ImageDraw.Draw(self.quiz_submit_img)

        text = '퀴즈를 제출하였습니다!\n퀴즈가 종료될 때까지 기다려주세요~'
        tw, th = draw.textsize(text, self.font)
        draw.text((self.ww//2-tw//2, self.wh//2-th//2), text, fill='black',
                  font=self.font, align='center')
        # flipped_quiz_submit_msg = self.quiz_submit_img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped_quiz_submit_msg = self.quiz_submit_img
        frame[10: 10+self.wh, y:y+self.ww] = flipped_quiz_submit_msg
        return frame

    #
    def set_quiz_result(self, answer, is_correct, is_ox):
        quiz_result_img = Image.open('Quiz/talkBox.jpg')
        self.rw, self.rh = quiz_result_img.size
        draw = ImageDraw.Draw(quiz_result_img)
        result_text = ''
        if is_correct:
            result_text += '축하합니다! 정답입니다\n'
        else:
            if is_ox:
                result_text += '아쉽게도 틀렸습니다.\n정답은 {}입니다.'.format(
                    'O' if answer else 'X')
            else:
                result_text += '아쉽게도 틀렸습니다.\n정답은 {}번입니다.'.format(answer)

        tw, th = draw.textsize(result_text, self.font)
        draw.text((self.rw//2-tw//2, self.rh//2-th//2), result_text, fill='black',
                  font=self.font, align='center')

        # self.flipped_quiz_result_img = quiz_result_img.transpose(Image.FLIP_LEFT_RIGHT)
        self.flipped_quiz_result_img = quiz_result_img

    def show_quiz_result(self, frame):
        background_height, background_width, _ = frame.shape  # 720,1280
        # x = background_height - self.h
        y = background_width - self.rw
        frame[10: 10+self.rh, y:y+self.rw] = self.flipped_quiz_result_img
        return frame
