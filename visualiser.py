import sys, time, os
import pygame as p
from pygame.locals import *
import random as r
from math import *
from graphesexos import *
p.init()
temp=[]
x=[]
point = ""
liste_de_liste=[]
chaine = False
art = False
liste_ligne=[]
lettres=[]
placeholder = []
count = 0
msgcounter =0 
t = p.font.Font(None,35)
text = t.render('ajouter arete' , True , (0,0,0))
text_t = t.render('ajouter arete' , True , (250,250,250))
text2= t.render('1er point : A' , True , (0,0,0))
text3= t.render('1er point : B' , True , (0,0,0))
text4= t.render('1er point : C' , True , (0,0,0))
text5= t.render('1er point : D' , True , (0,0,0))
text6= t.render('1er point : E' , True , (0,0,0))
text7= t.render('1er point : F' , True , (0,0,0))
text8= t.render('1er point : G' , True , (0,0,0))
text9= t.render('1er point : H' , True , (0,0,0))
text_a = t.render("Chaine Eulérienne présente",True,(0,0,0))
text_b = t.render("Chaine Eulérienne pas présente",True,(0,0,0))
x3=0

taille=30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)
p.init()

dimensions = largeur, hauteur = (1200, 900)
centre=(xcentre,ycentre)=(largeur//2,hauteur//2)

fenetre = p.display.set_mode(dimensions)
fond = (  64,225,208)
couleur_passage=(r.randint(0,255),r.randint(0,255),0)
VERT      = (  255,255,255)
JAUNE     = (255,255,255)

timer = p.time.Clock()
jouer=True

def texte(message, font,couleur):
    texteSurface = font.render(message, True, couleur)
    return texteSurface, texteSurface.get_rect()
x2 = largeur//2
y2=hauteur//2

class Point:
    def __init__(self,graphe):
        self.sommets = graphe.sommets
        self.arete = graphe.voisins
    
    def placer(self,nom,x,y):
        couleur = (100,100,100)
        position = (x2+x-15,y2+y-15)
        temp.append((x+x2,y+y2))
        p.draw.circle(fenetre,couleur,(x+x2,y+y2),10)
        largeText = p.font.SysFont("Arial",25)
        TexteSurf,TextRect = texte(nom,largeText,couleur)
        TextRect.center = position
        fenetre.blit(TexteSurf,TextRect)
                   
    def afficher(self):
        r1 = 400
        r2= 200
        n = len(self.sommets)
        for i in range(n):
            self.placer(self.sommets[i],r1*cos((2*pi/n)*i),r2*sin((2*pi/n)*i))


timer = p.time.Clock()

g = GrapheLS(['A','B','C','D',"E","F","G","H"])
point1 = Point(g)
ordre = g.ordre()
text_c = t.render("Ordre du graphe : " + str(ordre),True,(0,0,0))
while jouer: 
    timer.tick(10)  
    fenetre.fill(fond)
    point1.afficher()
    keys_pressed = p.key.get_pressed()
    clavier=p.event.get()
    deg = str(g.degres())
    text_d = t.render("Degre du graphe : " + deg ,True,(100,0,36))
    fenetre.blit(text_c , (900+50,300))
    fenetre.blit(text_d , (10+50,100))
    
    if g.euler() == 1:
        chaine = True
    elif g.euler() == 0:
        chaine = False
    
    if chaine:
        fenetre.blit(text_a , (300+50,40))
    if not chaine:
        fenetre.blit(text_b , (500+50,40))

    if art ==True:
        if event.type == p.MOUSEBUTTONDOWN:
            
            print(msgcounter)
            if p.mouse.get_pos()[0] <= temp[0][0] + 20 and p.mouse.get_pos()[0] >=temp[0][0] - 10 and  p.mouse.get_pos()[1] <= temp[0][1] +20 and p.mouse.get_pos()[1] >= temp[0][1] -20:
                liste_ligne.append((temp[0][0],temp[0][1]))
                lettres.append("A")
                
                count +=1
                if msgcounter <= 1:
                    point = "A" 
                    msgcounter+=1
            if p.mouse.get_pos()[0] <= temp[1][0] + 20 and p.mouse.get_pos()[0] >=temp[1][0] - 10 and  p.mouse.get_pos()[1] <= temp[1][1] +20 and p.mouse.get_pos()[1] >= temp[1][1] -20:
                liste_ligne.append((temp[1][0],temp[1][1]))
                lettres.append("B")
                count +=1

                if msgcounter <= 1:
                    point = "B" 
                    msgcounter+=1
            if p.mouse.get_pos()[0] <= temp[2][0] + 20 and p.mouse.get_pos()[0] >=temp[2][0] - 10 and  p.mouse.get_pos()[1] <= temp[2][1] +20 and p.mouse.get_pos()[1] >= temp[2][1] -20:
                liste_ligne.append((temp[2][0],temp[2][1]))
                lettres.append("C")
                count +=1
                if msgcounter <= 1:
                    point = "C"
                    msgcounter+=1
            if p.mouse.get_pos()[0] <= temp[3][0] + 20 and p.mouse.get_pos()[0] >=temp[3][0] - 10 and  p.mouse.get_pos()[1] <= temp[3][1] +20 and p.mouse.get_pos()[1] >= temp[3][1] -20:
                liste_ligne.append((temp[3][0],temp[3][1]))
                lettres.append("D")
                count +=1

                if msgcounter <= 1:
                    point = "D" 
                    msgcounter+=1
            if p.mouse.get_pos()[0] <= temp[4][0] + 20 and p.mouse.get_pos()[0] >=temp[4][0] - 10 and  p.mouse.get_pos()[1] <= temp[4][1] +20 and p.mouse.get_pos()[1] >= temp[4][1] -20:
                liste_ligne.append((temp[4][0],temp[4][1]))
                lettres.append("E")
                count +=1
      
                if msgcounter <= 1:
                    point = "E" 
                    msgcounter+=1
            if p.mouse.get_pos()[0] <= temp[5][0] + 20 and p.mouse.get_pos()[0] >=temp[5][0] - 10 and  p.mouse.get_pos()[1] <= temp[5][1] +20 and p.mouse.get_pos()[1] >= temp[5][1] -20:
                liste_ligne.append((temp[5][0],temp[5][1]))
                lettres.append("F")
                count +=1

                if msgcounter <= 1:
                    point = "F"
                    msgcounter+=1
            if p.mouse.get_pos()[0] <= temp[6][0] + 20 and p.mouse.get_pos()[0] >=temp[6][0] - 10 and  p.mouse.get_pos()[1] <= temp[6][1] +20 and p.mouse.get_pos()[1] >= temp[6][1] -20:
                liste_ligne.append((temp[6][0],temp[6][1]))
                lettres.append("G")
                count +=1

                if msgcounter <= 1:
                    point = "G" 
                    msgcounter+=1
            if p.mouse.get_pos()[0] <= temp[7][0] + 20 and p.mouse.get_pos()[0] >=temp[7][0] - 10 and  p.mouse.get_pos()[1] <= temp[7][1] +20 and p.mouse.get_pos()[1] >= temp[7][1] -20:
                liste_ligne.append((temp[7][0],temp[7][1]))
                lettres.append("H")
                count +=1
                if msgcounter <= 1:
                    point = "H" 
                    msgcounter+=1
        p.draw.rect(fenetre,(100,250,100),[100,40,250,40])
        fenetre.blit(text , (100+50,40))
    else:      
        p.draw.rect(fenetre,(200,200,200),[100,40,250,40])
        fenetre.blit(text , (100+50,40))
    for event in clavier:
        mouse = p.mouse.get_pos()
        if event.type == p.QUIT:
            jouer=False
        if event.type == p.MOUSEBUTTONDOWN:
            print(p.mouse.get_pos())
            if 100 <= mouse[0] <= 100+250 and 40 <= mouse[1] <= 40+40:
                art = True
                print(art)
    if 100 <= mouse[0] <= 100+250 and 40<= mouse[1] <= 40+40:
        p.draw.rect(fenetre,(100,100,100),[100,40,250,40])
        fenetre.blit(text_t , (100+50,40))        
    if count == 2:
        if liste_ligne[0] != liste_ligne[1]:
            print(x.append(liste_ligne[0]))
            print(x.append(liste_ligne[1]))
            g.AjouterUneArete(lettres[0],lettres[1])
            print(g.voisins)
            lettres=[]
            msgcounter = 0
            point =""
            count=0
            liste_ligne = []
            art = False
        else:
            count=0
            lettres=[]
            liste_ligne = []
            art = False

    text_e = t.render("1er point : " + point ,True,(100,0,36))
    fenetre.blit(text_e , (600+50,700)) 
    if len(x)>0:
        p.draw.lines(fenetre,JAUNE,False,x,width=5)
    p.display.update()
    p.display.flip()
p.quit()





