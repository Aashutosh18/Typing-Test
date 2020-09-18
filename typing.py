import pygame
import sys
import time
import random

class Testing:
    def __init__(self):
        self.w=750
        self.h=750
        self.reset=true
        self.active=false
        self.input_text=''
        self.word=''
        self.time_start=0
        self.total_time=0
        self.accuracy='0%'
        self.results='time:0 accuracy:0% wpm:0'
        self.wpm=0
        self.end=false
        self.head_c=(255,213,102)
        self.text_c=(240,240,240)
        self.results_c=(255,70,70)


        pygame.init()
        self.open_image=pygame.image.load('openimage.png')
        self.open_image=pygame.transform.scale(self.open_image,(self.w,self.h))


        self.bg=pygame.image.load('background.jpg')
        self.bg=pygame.transform.scale(self.bg,(self.w,self.h))


        self.screen=pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Typing Test')

    def draw_text(self,screen,msg,y,fsize,colour):
        font=pygame.font.Font(none,fsize)
        text=font.render(msg,1,colour)
        text_rect=text.get_rect(center=(self.w/2,y))
        screen.blit(text,text_rect)#bliting=rendering
        pygame.display.update

    
    def get_sentence(self):
        f=open('sentences.txt').read()
        sentences=f.split('\n')
        sentence=random.choice(sentences)
        return sentence
        





