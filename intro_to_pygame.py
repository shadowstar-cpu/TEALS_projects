from sys import exit
import pygame
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()
        walk_1 = pygame.image.load('Final_pygame/graphics/Player/player_walk_1.png').convert_alpha()
        walk_2 = pygame.image.load('Final_pygame/graphics/Player/player_walk_2.png').convert_alpha()
        self.walk = [walk_1, walk_2]
        self.index = 0
        self.jump = pygame.image.load('Final_pygame/graphics/Player/jump.png').convert_alpha()
        self.image = self.walk[self.index]
        self.rect = self.image.get_rect(midbottom = (200, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation(self):
        pass

    def update(self):
        self.player_input()
        self.apply_gravity()


def display_score():
    global current_time
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surf = pixel_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

def final_score():
    final_score_surf = pixel_font.render(f'Last score: {final_time}', False, '#D4AF37')
    final_score_rect = final_score_surf.get_rect(midbottom = (400, 320))
    screen.blit(final_score_surf, final_score_rect)
'''
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)

            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]
'''
def init():
    global pixel_font, screen, sky_surf, ground_surf, title_surf, title_rect, instruct1_surf, instruct1_rect, instruct2_rect, instruct2_surf, instruct3_rect, instruct3_surf, clock, game_active, final_time, obstacle_timer, obstacle_rect_list, start_time, snail_animation_timer, fly_animation_timer, player, player_stand, player_stand_rect
    pygame.init()
    width = 800
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Runner')
    clock = pygame.time.Clock()
    pixel_font = pygame.font.Font('Final_pygame/font/Pixeltype.ttf', 50)
    game_active = False
    start_time = 0
    final_time = 0
    obstacle_rect_list = []

    '''
    test_surface = pygame.Surface((100,200))
    test_surface.fill('Red')
    '''
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    
    sky_surf = pygame.image.load('Final_pygame/graphics/Background/Sky.png').convert()
    ground_surf = pygame.image.load('Final_pygame/graphics/Background/ground.png').convert()

    '''
    score_surf = pixel_font.render('My game', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    '''
    '''
    snail_frame_1 = pygame.image.load('Final_pygame/graphics/Snail/snail1.png').convert_alpha()
    snail_frame_2 = pygame.image.load('Final_pygame/graphics/Snail/snail2.png').convert_alpha()
    snail_frames = [snail_frame_1, snail_frame_2]
    snail_frame_index = 0
    snail_surf = snail_frames[snail_frame_index]
    
    fly_frame_1 = pygame.image.load('Final_pygame/graphics/Fly/Fly1.png').convert_alpha()
    fly_frame_2 = pygame.image.load('Final_pygame/graphics/Fly/Fly2.png').convert_alpha()
    fly_frames = [fly_frame_1, fly_frame_2]
    fly_frame_index = 0
    fly_surf = fly_frames[fly_frame_index]
    
    player_walk_1 = pygame.image.load('Final_pygame/graphics/Player/player_walk_1.png').convert_alpha()
    player_walk_2 = pygame.image.load('Final_pygame/graphics/Player/player_walk_2.png').convert_alpha()
    player_walk = [player_walk_1, player_walk_2]
    player_index = 0
    player_jump = pygame.image.load('Final_pygame/graphics/Player/jump.png').convert_alpha()
    player_surf = player_walk[player_index]
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    player_grav = 0
    '''
    player_stand = pygame.image.load('Final_pygame/graphics/Player/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center = (400, 200))


    title_surf = pixel_font.render('Jump Around', False, '#02c1de')
    title_rect = title_surf.get_rect(midtop = (400, 50))

    instruct1_surf = pixel_font.render('Press R to begin', False, (151, 184, 240))
    instruct1_rect = instruct1_surf.get_rect(bottomleft = (0, 400))
    instruct2_surf = pixel_font.render('Press Space to Jump', False, (151, 184, 240))
    instruct2_rect = instruct2_surf.get_rect(bottomright = (800, 405))
    instruct3_surf = pixel_font.render('Avoid the snail!!', False, (151, 184, 240))
    instruct3_rect = instruct3_surf.get_rect(bottomleft = (255, 375))

    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1500)

    snail_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(snail_animation_timer, 500)

    fly_animation_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(fly_animation_timer, 200)

init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        '''

        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse down')

        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('collision')

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                        player_grav = -15
            
            if event.type == pygame.KEYDOWN:
                #print('key down')
                if event.key == pygame.K_SPACE and player_rect.bottom >=300:
                        player_grav = -15

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.KEYUP:
                print('key up')

            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))
            
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]
            '''
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                #player_rect.bottom = 300
                #snail_rect.left = 800
                #player_grav = 0
                start_time = pygame.time.get_ticks()
                game_active = True
            
            if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            
    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        '''
        pygame.draw.rect(screen, '#c0e8ec', score_rect.inflate(10,10), border_radius = 3)
        pygame.draw.line(screen, 'Gold', (0, 0), (800, 400), 10)
        pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))
        screen.blit(score_surf, score_rect)
        '''
        display_score()

        '''
        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)
        '''

        '''
        player_grav += .5
        player_rect.y += player_grav
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)'''
        
        player.draw(screen)
        player.update()
        '''
        if snail_rect.colliderect(player_rect):
            final_time = (pygame.time.get_ticks() - start_time) // 1000
            game_active = False
  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print('jump')

        if player_rect.colliderect(snail_rect):
            print('collision')

        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            pygame.mouse.get_pressed()
        '''

        '''
        if not collisions(player_rect, obstacle_rect_list):
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_grav = 0
        final_time = (pygame.time.get_ticks() - start_time) // 1000
        game_active = False'''

        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    else:
        screen.fill((30, 4, 56))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_surf, title_rect)
        screen.blit(instruct1_surf, instruct1_rect)
        screen.blit(instruct2_surf, instruct2_rect)
        screen.blit(instruct3_surf, instruct3_rect)        
        final_score()

    pygame.display.update()
    clock.tick(60)
