import sys
import pygame

# Con pygame la finestra viene considerata una superficie sulla quale disegnare
# nella superficie possiamo aggiungere diverse cose, tra cui immagini e bottoni

class Game:
    def __init__(self):
        # inizializza pygame
        pygame.init()

        # cambia il nome della finestra
        pygame.display.set_caption("Gioco Napoleone")

        # set_mode e' il metodo per creare la finestra
        self.screen = pygame.display.set_mode((900, 600))

        # clock si usa per impostare gli fps, o quante volte si deve ridisegnare la finestra
        self.clock = pygame.time.Clock()
        
        # di solito si usano i png perche' sono lossless
        # chiamando solo questa funzione non succede niente perche' l'immagine deve essere ancora disegnata
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        

        # self.img_pos = [160, 260]
        # self.movement = [False, False]

    def run(self):
        # crea un loop infinito per quando il gioco e' avviato
        while True:
            
            self.screen.fill("black")
            
           
            # questa funzione si usa per disegnare sulla superficie l'immagine in posizione specificata
            # l'idea dietro questa funzione e' quella di copiare un'area di memoria specificata sopra ad una superficie
            # in questo caso il programma copia l'immagine caricata precedentemente in memoria sulla finestra
            self.img = pygame.image.load("C:\\Users\\franzyfrunzyy\\Dropbox\\PC\\Documents\\Flow_Inf\\Python\\AreaDiProgetto\\data\\Images\\X tris.png")
            # carichiamo l'immagine
            self.screen.blit(self.img, self.player_pos)

            # per ogni evento generato dell'utente
            for event in pygame.event.get():
                # verifica se viene premuta la x sulla finestra e quindi se chiudere il gioco
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.player_pos.y -= 300 * dt
                if keys[pygame.K_s]:
                    self.player_pos.y += 300 * dt
                if keys[pygame.K_a]:
                    self.player_pos.x -= 300 * dt
                if keys[pygame.K_d]:
                    self.player_pos.x += 300 * dt
                """
                # questa condizione verifica se e' stato premuto un qualsiasi pulsante 
                if event.type == pygame.KEYDOWN:
                    
                    # quest'atra condizione controlla se e' stata premuta la freccia verso il basso
                    if event.key == pygame.K_UP:
                        
                        #se e' stata premuta pone il valore in posizione 0 della lista a true
                        self.movement[0] = True
                        
                    # verifica la stessa condizione di prima ma con la freccia verso il basso
                    if event.key == pygame.K_DOWN:
                        
                        # imposta il valore in posizione 1 della lista a true
                        self.movement[1] = True
                        
                # questa condizione controlla se il tasto e' stato rilasciato e non premuto
                if event.type == pygame.KEYUP:
                    
                    # questa condizione verifica se il tasto rilasciato e' la freccia verso l'alto
                    if event.key == pygame.K_UP:
                        
                        #se e' stata rilasciata pone il valore in posizione 0 della lista a true
                        self.movement[0] = False
                        
                    # verifica la stessa condizione di prima ma con la freccia verso il basso
                    if event.key == pygame.K_DOWN:
                        
                        # imposta il valore in posizione 1 della lista a false
                        self.movement[1] = False
            """
            # aggiorna la finestra
            pygame.display.flip()
            dt = self.clock.tick(60) / 1000
            self.clock.tick(60)