import pygame
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

# Start point for the arms
start_point = (320, 240) 

# Length of the second arm
length_1 = 190  

# Length of the minute arm
length_2 = 170

# Length of the hour arm
length_3 = 130

# Font for displaying numbers (ChatGPT)
font = pygame.font.Font(None, 40)

# Loop
while True:
    screen.fill((255, 255, 255))
    current_time = datetime.now()

    # Black circle around the clock
    pygame.draw.circle(screen, (0, 0, 0), ((320,240)),((225)))

    # Green circle under small lines (on top of the black circle)
    pygame.draw.circle(screen, (88, 188, 69), ((320,240)),((220)))
    
    # Radiating lines
    start_position = (320,240)

    # small lines (Every minute)
    radius = 220
    for angle in range(0, 360, 6):
        end_offset = [radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle))]
        end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
        pygame.draw.line(screen, (0,0,0), start_position, end_position, 3)
    
    # Green circle to make the minute lines shorter
    pygame.draw.circle(screen, (88, 188, 69), ((320,240)),((210)))

    # big lines (every hour)
    radius = 220
    for angle in range(0, 360, 30):
        end_offset = [radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle))]
        end_position = (start_position[0]+end_offset[0], start_position[1]+end_offset[1])
        pygame.draw.line(screen, (0,0,0), start_position, end_position, 5)
    
    # make the line rotate clockwise pr. minute
    angle = math.radians((current_time.minute + current_time.second / 60)*6-90) 
    end_x = start_point[0] + length_2 * math.cos(angle) 
    end_y = start_point[1] + length_2 * math.sin(angle)
    end_point = (int(end_x), int(end_y))
    pygame.draw.circle(screen, (88, 188, 69), ((320,240)),((205)))
    pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)
    
    # make the line rotate clockwise pr. hour
    angle = math.radians((current_time.hour % 12 + current_time.minute / 60)*30-90) 
    end_x = start_point[0] + length_3 * math.cos(angle)
    end_y = start_point[1] + length_3 * math.sin(angle)
    end_point = (int(end_x), int(end_y))
    pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

    # make the line rotate clockwise pr. second
    angle = math.radians(current_time.second*6-90) 
    end_x = start_point[0] + length_1 * math.cos(angle)
    end_y = start_point[1] + length_1 * math.sin(angle)
    end_point = (int(end_x), int(end_y))
    pygame.draw.line(screen, (214, 19, 36), start_point, end_point, 5) 

   # Draw numbers around the clock (ChatGPT)
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)  # Calculate angle for each number
        num_x = start_point[0] + 185 * math.cos(angle)  # Adjust position
        num_y = start_point[1] + 185 * math.sin(angle)  # Adjust position
        number_surface = font.render(str(i), True, (0, 0, 0))
        number_rect = number_surface.get_rect(center=(num_x, num_y))
        screen.blit(number_surface, number_rect)

    # Updates the entire display. 
    pygame.display.flip() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()