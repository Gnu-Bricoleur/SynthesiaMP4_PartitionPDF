#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
from Tkinter import*
from PIL import Image, ImageDraw
import time

#A decommenter en "Prod"
#bashCommand = "avconv -i coldplay.mp4 -r 30 -f image2 pic/%04d.png"
#os.system(bashCommand)
#time.sleep(200000)


liste_touches = []
liste_touches_appuyes_droite = []
liste_touches_appuyes_gauche = []
debut_video = "0121"
fin_video = "0410"   #7510
liste_appuis_droite = []
liste_appuis_gauche = []
liste_sync = []

def clic(event):
	liste_touches.append([event.x, event.y])
	couleur = photo.get(event.x, event.y)
	print couleur


fen =Tk()
photo = PhotoImage(file="pic/2000.png")

canvas = Canvas(fen,width=1280, height=720)#detecter taille image
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
canvas.bind("<1>",clic)
fen.mainloop()


#points rouge + bouton fermer




print "liste des touches : " + str(liste_touches)

#A commenter en "prod" ;-)
liste_touches = [[21, 585], [32, 511], [52, 583], [83, 501], [100, 591], [148, 578], [162, 503], [183, 597], [207, 502], [229, 601], [256, 514], [270, 594], [308, 584], [329, 515], [354, 583], [379, 508], [385, 593], [436, 595], [448, 505], [475, 599], [497, 503], [521, 589], [546, 514], [550, 594], [600, 581], [619, 508], [645, 593], [666, 512], [687, 595], [723, 594], [740, 512], [771, 596], [787, 512], [817, 592], [835, 504], [857, 603], [898, 595], [909, 506], [938, 588], [959, 512], [977, 593], [1019, 598], [1032, 522], [1056, 590], [1074, 515], [1106, 596], [1127, 512], [1138, 588], [1185, 582], [1198, 510], [1222, 592], [1246, 507], [1263, 594]]

liste_touches = [[14, 461], [38, 462], [63, 462], [84, 462], [111, 466], [134, 464], [159, 466], [183, 466], [206, 470], [234, 463], [258, 466], [278, 466], [304, 464], [325, 464], [357, 465], [372, 463], [400, 465], [430, 462], [449, 462], [481, 464], [497, 462], [526, 464], [540, 463], [570, 463], [596, 457], [620, 457], [645, 454], [666, 454], [694, 454], [715, 452], [737, 450], [765, 449], [788, 457], [815, 456], [839, 454], [858, 455], [889, 449], [909, 448], [936, 451], [964, 453], [986, 448], [1006, 448], [1031, 447], [1055, 450], [1081, 448], [1104, 448], [1131, 448], [1149, 446], [1180, 443], [1205, 441], [1225, 441], [1252, 437], [1275, 432]]


#C 	D 	E 	F 	G 	A 	B
liste_notes = ["c,,", "cis,,", "d,,", "dis,,", "e,,", "f,,", "fis,,", "g,,", "gis,,", "a,,", "ais,,", "b,,", \
				"c,", "cis,", "d,", "dis,", "e,", "f,", "fis,", "g,", "gis,", "a,", "ais,", "b,", \
				"c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", \
				"c'", "cis'", "d'", "dis'", "e'", "f'", "fis'", "g'", "gis'", "a'", "ais'", "b'", \
				"c''", "cis''", "d''", "dis''", "e''"]

print len(liste_touches)
print len(liste_notes)




for nb in range(int(debut_video), int(fin_video)):
	liste_touches_appuyes_droite = []
	liste_touches_appuyes_gauche = []
	sync_droite = False
	sync_gauche = False
	print str(nb - int(debut_video)) + "/" + str (int(fin_video) - int(debut_video))
	im = Image.open("pic/" + str(nb).zfill(4) + '.png')
	draw = ImageDraw.Draw(im)
	for touche in liste_touches:
		pix = im.getpixel((touche[0], touche[1]))
		if (pix[0] < 10 and pix[1] < 10 and pix[2] < 10) or (pix[0] > 245 and pix[1] > 245 and pix[2] > 245):
			pass
		#else :
			#draw.ellipse((touche[0]-10, touche[1]-10, touche[0]+10, touche[1]+10), fill=(255,0,0,255))
			#liste_touches_appuyes_gauche.append((touche[0], touche[1]))
			#liste_touches_appuyes_droite.append((touche[0], touche[1]))
		else:
			if pix[2] > 50:
				draw.ellipse((touche[0]-10, touche[1]-10-80, touche[0]+10, touche[1]+10-80), fill=(255,0,0,255))
				liste_touches_appuyes_gauche.append((touche[0], touche[1]))
			else :
				draw.ellipse((touche[0]-10, touche[1]-10-80, touche[0]+10, touche[1]+10-80), fill=(255,255,0,255))
				liste_touches_appuyes_droite.append((touche[0], touche[1]))
	
	
	if liste_touches_appuyes_droite == []:
		liste_touches_appuyes_droite.append((0,0))
	elif liste_appuis_droite[-1] == [(0,0)]:
		sync_droite = True
	
	if liste_touches_appuyes_gauche == []:
		liste_touches_appuyes_gauche.append((0,0))
	elif liste_appuis_gauche[-1] == [(0,0)]:
		sync_gauche = True
	
	if (sync_droite == True) and (sync_gauche == True):
		liste_sync.append(len(liste_appuis_droite))
	
	liste_appuis_droite.append(liste_touches_appuyes_droite)
	liste_appuis_gauche.append(liste_touches_appuyes_gauche)
	
	im.save("pic/" + str(nb).zfill(4) + '.png',format="png")
	im.close()


porte_droite = []
porte_droite.append([liste_appuis_droite[0], 1,0])
i = 1
for elt in liste_appuis_droite[1:] :
	if elt == liste_appuis_droite[i-1]:
		porte_droite[-1][1] += 1
	else:
		porte_droite.append([elt,1,i])
	i += 1


porte_gauche = []
porte_gauche.append([liste_appuis_gauche[0], 1,0])
i = 1
for elt in liste_appuis_gauche[1:] :
	if elt == liste_appuis_gauche[i-1]:
		porte_gauche[-1][1] += 1
	else:
		porte_gauche.append([elt,1,i])
	i += 1

liste_temps = []
for elt in porte_droite:
	if not( elt[1] in liste_temps ):
		liste_temps.append(elt[1])
for elt in porte_gauche:
	if not( elt[1] in liste_temps ):
		liste_temps.append(elt[1])

liste_temps.sort()
print liste_temps
print liste_sync
print porte_droite


#[1, 2, 3, 4, 5, 6, 11, 13, 20, 21, 32, 39, 89, 90]

# note plus petite 12


tab_duree = []


note_plus_courte = 12
note_plus_courte_temps = 8
tab_temps_possibles = [8, 4, 2, 1, 0]

for j in liste_temps:
	for i in range(len(tab_temps_possibles)):
		if note_plus_courte*i + note_plus_courte/2 <= j < note_plus_courte*(i+1) + note_plus_courte/2:
			if (i) <= 0:
				tab_duree.append("fermata")
			else :
				tab_duree.append(i)
	if j < note_plus_courte/2:
		tab_duree.append("rien")

tab_duree = ["rien", "rien", "rien", "rien", "rien", 8, 8, 8, 4, 4, 2, 2, 1, 1]

#ancienne version
#for j in liste_temps:
	#for i in range(note_plus_courte_temps)
		#if note_plus_courte*i + note_plus_courte/2 <= j < note_plus_courte*(i+1) + note_plus_courte/2:
			#if (note_plus_courte_temps - i) <= 0:
				#tab_duree.append("fermata")
			#else :
				#tab_duree.append(note_plus_courte_temps - i)
	#if j < note_plus_courte/2:
		#tab_duree.append("rien")

print tab_duree





os.remove("partition.ly")
fichier = open("partition.ly", "a")


fichier.write("\\version \"2.16.2\"")
#fichier.write("\\relative c")
fichier.write("\n{\n")
fichier.write("<<")
fichier.write("\\new Staff { \clef \"treble\" ")



for accord in porte_droite:
	texte = "<"
	accord_i = accord[:-2]
	print accord
	accord_i = accord[0]
	for note in accord_i:
		print note
		if note == (0,0):
			pass
		else :
			numnote = liste_touches.index([note[0],note[1]])
			texte = texte + " " + liste_notes[numnote]
	fichier.write(texte)
	fichier.write(" >")
	tps = accord[-2]
	index_tps = liste_temps.index(tps)
	if tab_duree[index_tps] == "rien":
		pass
	else:
		truc = tab_duree[index_tps]
		fichier.write(str(truc))
	fichier.write(" ")



# Ancienne version
#i = 1
#for elt in liste_appuis_droite[1:]:
	#texte = "<"
	#for note in elt:
		#if note in liste_appuis_droite[i - 1]:
			#pass
		#else:
			#numnote = liste_touches.index([note[0],note[1]])
			#texte = texte + " " + liste_notes[numnote]
	#i = i +1
	#fichier.write(texte)
	#fichier.write(" > ")

fichier.write("\n}\n")
fichier.write("\\new Staff { \clef \"bass\" ")




for accord in porte_gauche:
	texte = "<"
	accord_i = accord[:-2]
	print accord
	accord_i = accord[0]
	for note in accord_i:
		print note
		if note == (0,0):
			pass
		else :
			numnote = liste_touches.index([note[0],note[1]])
			texte = texte + " " + liste_notes[numnote]
	fichier.write(texte)
	fichier.write(" >")
	tps = accord[-2]
	index_tps = liste_temps.index(tps)
	if tab_duree[index_tps] == "rien":
		pass
	else:
		truc = tab_duree[index_tps]
		fichier.write(str(truc))
	fichier.write(" ")



# Ancienne version
#i = 1
#for elt in liste_appuis_gauche[1:]:
	#texte = "<"
	#for note in elt:
		#if note in liste_appuis_gauche[i - 1]:
			#pass
		#else:
			#numnote = liste_touches.index([note[0],note[1]])
			#texte = texte + " " + liste_notes[numnote]
	#i = i + 1
	#fichier.write(texte)
	#fichier.write(" > ")

fichier.write("\n}\n")

fichier.write(">>\n")
fichier.write("\layout{} \n \midi{}")
fichier.write("\n}")

fichier.close()

bashCommand = "lilypond partition.ly"
os.system(bashCommand)






