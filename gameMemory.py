import pygame
import sys,random,time
from pygame.locals import*





def cargarTarjetasCerradas(ventana,coordenadas,nivel,tarjetaCerrada):
	ventana=ventana
	nivel=nivel
	llave=1;
	while(llave<=nivel):
		for posicion in coordenadas[llave]:
			ventana.blit(tarjetaCerrada,posicion)
		llave=llave+1
		

	return ventana
	
##Selecciona aleatoriamente y sin repetir, las imagenes que seran usadas para un nivel, returno un arreglo que contiene las imagenes seleccionadas
def seleccionarTarjetasNivel(tarjetasAbiertasCons,cantidadTarjetas):
	tarjetas=random.sample(tarjetasAbiertasCons,cantidadTarjetas)
	return tarjetas


##obtiene las coordenadas que se utilizaran para el nivel de turno, retorna un vector de tuplas
def seleccionarCoordenadas(coordenadas,nivel):
	posiciones=[]
	etapa=1
	while(etapa<=nivel):
		for pos in coordenadas[etapa]:
			posiciones.append(pos)
		etapa=etapa+1
	return posiciones

##agregar le ascocia a una imagen las dos coordenadas que ocupara en la pantalla
def iniciarImagenesCoordenadas(tarjetasNivel,coordenadasNivel):
	ancho=70
	alto=63
	tarjetas={}
	coordenadasNivel
	for indiceTarjeta in range(0,len(tarjetasNivel)):
		aux=[]
		for iteracion in range(0,2):
			indice=random.randint(0,len(coordenadasNivel)-1)
			aux.append(coordenadasNivel.pop(indice))
		aux.insert(0,tarjetasNivel[indiceTarjeta])
		aux.append(0)##status imagen 1 pos 3 // 0 es incativo y 1 es activo
		aux.append(0)##status imagen 2 pos 4 //0 es inactivo y 1 es activo
		aux.append(pygame.Rect(aux[1],(ancho,alto)))##Inicializacion del rectangulo de la imagen 1 pos 5
		aux.append(pygame.Rect(aux[2],(ancho,alto)))##Inicializacion del rectangulo de la imagen 2 pos 6
		aux.append(0)##valor que indica si la pareja de la imagen fue completada 0 es no y 1 es si
		
		tarjetas[indiceTarjeta]=aux
	return tarjetas

##imprime por pantalla las imagenes seleccionadas
def imprimirTarjetasAbiertas(escenario,tarjetas,inicio,tarjetaCerrada):
	escenario=escenario
	for i in tarjetas:
		if (inicio==True):
			escenario.blit(tarjetas[i][0],tarjetas[i][1])
			escenario.blit(tarjetas[i][0],tarjetas[i][2])
		else:
			if(tarjetas[i][3]==1):
				escenario.blit(tarjetas[i][0],tarjetas[i][1])
			else:
				escenario.blit(tarjetaCerrada,tarjetas[i][1])
			
			if(tarjetas[i][4]==1):
				escenario.blit(tarjetas[i][0],tarjetas[i][2])
			else:
				escenario.blit(tarjetaCerrada,tarjetas[i][2])
	return escenario
		
def buscarColision(posMouse,tarjetasNivel,cantidadTarjetas,cantidadParejas):
	statusCambio=[1,0]
	pareja=False
	
	for llave in tarjetasNivel:
		if(tarjetasNivel[llave][7]==0):
			if (tarjetasNivel[llave][5].collidepoint(posMouse)==True and tarjetasNivel[llave][3]==0):
				tarjetasNivel[llave][3]=statusCambio[tarjetasNivel[llave][3]]
				if(tarjetasNivel[llave][4]==1):
					tarjetasNivel[llave][7]=1
					cantidadParejas=cantidadParejas+1
					cantidadTarjetas=0
					pareja=True
				else:
					cantidadTarjetas=cantidadTarjetas+1
			if (tarjetasNivel[llave][6].collidepoint(posMouse)==True and tarjetasNivel[llave][4]==0):
				tarjetasNivel[llave][4]=statusCambio[tarjetasNivel[llave][4]]
				if(tarjetasNivel[llave][3]==1):
					tarjetasNivel[llave][7]=1
					cantidadParejas=cantidadParejas+1
					cantidadTarjetas=0
					pareja=True
				else:
					cantidadTarjetas=cantidadTarjetas+1
	return {'tarjetasNivel':tarjetasNivel,'cantidadTarjetas':cantidadTarjetas,'pareja':pareja,'cantidadParejas':cantidadParejas}
			
		
def voltearTarjetas(tarjetasNivel,cantidadTarjetas):
	
	if(cantidadTarjetas==2):
		for llave in tarjetasNivel:
			if(tarjetasNivel[llave][7]!=1):
				tarjetasNivel[llave][3]=0
				tarjetasNivel[llave][4]=0
				cantidadTarjetas=0 
	return {'tarjetasNivel':tarjetasNivel,'cantidadTarjetas':cantidadTarjetas}

def calcularTiempo(tiempoInicio,tiempoactual,escenario,numeros,coordenadas=[(155,23),(170,23),(185,23),(200,23)]):
	tiempoEntero=int(tiempoactual-tiempoInicio)
	tiempoTotal=list(str(tiempoEntero))
	if(tiempoEntero!=0):
		for i in range(0,len(tiempoTotal)):
			if(tiempoTotal[i].isdigit()):
				print "tiempo entero: ",tiempoEntero
				print "tiempo total: ",tiempoTotal
				print "index i: ",i
				print "longitud:",len(tiempoTotal)
				print "vector:",tiempoTotal
				escenario.blit(numeros[int(tiempoTotal[i])],coordenadas[i])
	return {'escenario':escenario,'tiempo':tiempoEntero}
	

		
			
		             



pygame.init()
resolucion=(442,630)

ventana=pygame.display.set_mode(resolucion)
#cargar imagenes
pygame.display.set_caption("Memory Game")

#escenario
fondo=pygame.image.load("escenario2.jpg")
##numero=pygame.image.load("1.png")

#tarjetas
tarjetasNivel=None
tarjetaCerrada=pygame.image.load("tarjetaCerrada.png")
matrizNumeros=pygame.image.load("numeros.png")
matrizTarjetas=pygame.image.load("tarjetas.png")
numeros={
           0:matrizNumeros.subsurface((40,0,9,17)),
           1:matrizNumeros.subsurface((53,0,4,17)),
           2:matrizNumeros.subsurface((0,21,9,17)),
           3:matrizNumeros.subsurface((14,0,9,17)),
           4:matrizNumeros.subsurface((0,0,10,17)),
           5:matrizNumeros.subsurface((39,21,9,17)),
           6:matrizNumeros.subsurface((0,42,9,17)),
           7:matrizNumeros.subsurface((13,21,9,17)),
           8:matrizNumeros.subsurface((26,21,9,17)),
           9:matrizNumeros.subsurface((27,0,9,17))}

tarjetasAbiertasCons=[
					matrizTarjetas.subsurface((0,0,70,63)),matrizTarjetas.subsurface((74,0,70,63)),matrizTarjetas.subsurface((148,0,70,63)),
					matrizTarjetas.subsurface((0,67,70,63)),matrizTarjetas.subsurface((74,67,70,63)),matrizTarjetas.subsurface((148,67,70,63)),
                                        matrizTarjetas.subsurface((0,134,70,63)),matrizTarjetas.subsurface((74,134,70,63)),matrizTarjetas.subsurface((148,134,70,63)),
                                        matrizTarjetas.subsurface((0,201,70,63)),matrizTarjetas.subsurface((74,201,70,63)),matrizTarjetas.subsurface((148,201,70,63)),
                                        matrizTarjetas.subsurface((0,268,70,63)),matrizTarjetas.subsurface((74,268,70,63)),matrizTarjetas.subsurface((148,268,70,63)),
                                        matrizTarjetas.subsurface((0,335,70,63)),matrizTarjetas.subsurface((74,335,70,63)),matrizTarjetas.subsurface((148,335,70,63)),
                                        matrizTarjetas.subsurface((0,402,70,63)),matrizTarjetas.subsurface((74,402,70,63)),matrizTarjetas.subsurface((148,402,70,63)),
                                        matrizTarjetas.subsurface((0,469,70,63)),matrizTarjetas.subsurface((74,469,70,63)),matrizTarjetas.subsurface((148,469,70,63)),
                                        matrizTarjetas.subsurface((0,536,70,63)),matrizTarjetas.subsurface((74,536,70,63)),matrizTarjetas.subsurface((148,536,70,63)),
                                        matrizTarjetas.subsurface((0,603,70,63)),matrizTarjetas.subsurface((74,603,70,63)),matrizTarjetas.subsurface((148,603,70,63)),
                                        matrizTarjetas.subsurface((0,670,70,63)),matrizTarjetas.subsurface((74,670,70,63)),matrizTarjetas.subsurface((148,670,70,63)),
                                        matrizTarjetas.subsurface((0,737,70,63)),matrizTarjetas.subsurface((74,737,70,63)),matrizTarjetas.subsurface((148,737,70,63)),
                                        matrizTarjetas.subsurface((0,804,70,63)),matrizTarjetas.subsurface((74,804,70,63)),matrizTarjetas.subsurface((148,804,70,63)),
                                        matrizTarjetas.subsurface((0,871,70,63)),matrizTarjetas.subsurface((74,871,70,63)),matrizTarjetas.subsurface((148,871,70,63)),
                                        matrizTarjetas.subsurface((0,938,70,63)),matrizTarjetas.subsurface((74,938,70,63)),matrizTarjetas.subsurface((148,938,70,63))
                                        
                     ]

#pie de pagina
logoPython=pygame.image.load("python.png")
banderaVenezuela=pygame.image.load("bandera.png")

nivel=1
coordenadasNivel=None
iniciar=True
tiempoEspera=5000
cantidadT=0
pareja=False
contadorParejas=0
tiempo=0

#almacenar coordenadas
coordenadas={
                         1:[(150,258),(150,324),(224,258),(224,324)],
			 2:[(150,192),(224,192),(150,390),(224,390)],
			 3:[(150,457),(150,126),(224,126),(224,457)],
			 4:[(75,258),(75,324),(300,258),(300,324)],
			 5:[(75,390),(300,390),(75,457),(300,457)],
			 6:[(75,192),(75,126),(300,126),(300,192)],
                         7:[(75,523),(150,523),(224,523),(300,523)],
                         8:[(75,59),(150,59),(224,59),(300,59)]
}


cantidadParejas={1:2,2:4,3:6,4:8,5:10,6:12,7:14,8:16}


while True:
	escenario=fondo.copy()
	escenario.blit(numeros[nivel],(383,25))	
	if(tiempo==0):
		escenario.blit(numeros[0],(165,23))
	for event in pygame.event.get():
	
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		else:
			
			
			
			
			if (iniciar==True):
				tarjetas=seleccionarTarjetasNivel(tarjetasAbiertasCons,cantidadParejas[nivel])
				coordenadasNivel=seleccionarCoordenadas(coordenadas,nivel)
				tarjetasNivel=iniciarImagenesCoordenadas(tarjetas,coordenadasNivel)
				escenario=imprimirTarjetasAbiertas(escenario,tarjetasNivel,True,tarjetaCerrada)
				escenario.blit(logoPython,(20,604))
				escenario.blit(banderaVenezuela,(400,608))
				ventana.blit(escenario,(-5,-15))
				pygame.display.flip()
				
				pygame.time.delay(4000)
				tiempoInicio=time.clock()
				escenario=cargarTarjetasCerradas(escenario,coordenadas,nivel,tarjetaCerrada)
				ventana.blit(escenario,(-5,-15))
				
				
				iniciar=False
			elif(iniciar==False):
				if(event.type==MOUSEBUTTONUP):
					if(event.button==1):
						aux=buscarColision(event.pos,tarjetasNivel,cantidadT,contadorParejas)
						tarjetasNivel=aux['tarjetasNivel']
						cantidadT=aux['cantidadTarjetas']
						pareja=aux['pareja']
						contadorParejas=aux['cantidadParejas']
						
			
						
				
				
			
		
		
			
			
				

	
	escenario=imprimirTarjetasAbiertas(escenario,tarjetasNivel,False,tarjetaCerrada)
						
	escenario.blit(logoPython,(20,604))
	escenario.blit(banderaVenezuela,(400,608))
	tiempoTotal=time.clock()
	aux=calcularTiempo(tiempoInicio,tiempoTotal,escenario,numeros)
	escenario=aux['escenario']
	tiempo=aux['tiempo']
	ventana.blit(escenario,(-5,-15))				
	pygame.display.flip()
						
						
						
	if pareja==False and cantidadT==2:
		pygame.time.delay(800)
		aux=voltearTarjetas(tarjetasNivel,cantidadT)
		tarjetasNivel=aux['tarjetasNivel']
		cantidadT=aux['cantidadTarjetas']
		escenario=imprimirTarjetasAbiertas(escenario,tarjetasNivel,False,tarjetaCerrada)
		pygame.display.flip()
	elif pareja==True and cantidadParejas[nivel]==contadorParejas:
		iniciar=True
		contadorParejas=0
		cantidadT=0
		nivel=nivel+1
		pygame.time.delay(3000)	
		tiempo=0