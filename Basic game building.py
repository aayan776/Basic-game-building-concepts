import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))
Green = (0, 255, 0)
pygame.display.update()
done = False
while not done:
  for event in pygame.event.get():
    if event == pygame.QUIT:
      done = True
  pygame.draw.circle(screen, Green, (50, 50), 20)
  pygame.draw.circle(screen, Green, (100, 100), 20, 3)
  pygame.display.flip()
#Rectangle
'''
import pygame  
pygame.init()  
screen = pygame.display.set_mode((400, 300))  
done = False  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))    
    pygame.display.flip()  
'''
'''
import pygame
def main():
  pygame.init()
  screen_width, screen_height = 500, 500
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Color changing sprite")
  color = {'red' : pygame.Color('red'), 'blue' : pygame.Color('blue'), 'green' : pygame.Color('green')
  , 'yellow' : pygame.Color('yellow'), 'white' : pygame.Color('white'), }
  current_color = color['white']
  x, y = 30, 30
  sprite_width, sprite_height = 60, 60
  clock = pygame.time.Clock()
  done = False
  while not done:
    for event in pygame.event.get():
      if event == pygame.QUIT:
        done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
      x -= 3
    if pressed[pygame.K_RIGHT]:
      x += 3
    if pressed[pygame.K_UP]:
      y += 3
    if pressed[pygame.K_DOWN]:
      y -= 3
    x = min(max(0, x), screen_width - sprite_width)
    y = min(max(0, x), screen_height - sprite_height)
    if x == 0:
      current_color = color['blue']
      print("touched left boundary")
    elif x == screen_width - sprite_width:
      current_color = color['yellow']
    elif y == 0:
      current_color = color['red']
      print("touched top boundary")
    elif y == screen_height - sprite_height:
      current_color = color['green']
    else:
      current_color = color['white']
    screen.fill((0,0,0))
    pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()
if __name__ == "__main__":
  main()
'''
