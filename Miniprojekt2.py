import pygame

# Klasse der indeholder koden der visualisere mappet.
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_width = width // 10 # 10 kollonner
        self.cell_height = height // 10 # 10 rækker

        self.grid = [[0,1,1,0,1,1,1,1,1,1],
                     [0,0,0,0,1,1,2,2,2,1],
                     [0,2,2,0,0,1,1,2,2,1],
                     [0,0,2,2,0,0,1,1,2,2],
                     [0,0,0,0,0,0,0,0,0,2],
                     [0,0,0,0,1,1,1,0,0,0],
                     [1,0,0,0,2,2,2,0,0,1],
                     [1,1,0,0,0,0,0,0,0,1],
                     [1,2,1,0,2,2,0,0,0,0],
                     [2,2,0,0,1,1,1,0,0,1]]

    # Giv de forskellige tal i griddet farver - brug for-loop til at gennemgå alle lster (y) og celler (x)
    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = (0, 200, 50) if cell == 0 else ((0, 67, 255) if cell == 1 else (117, 117, 117))
                pygame.draw.rect(screen, color, (x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height))

    # Definer start- og slut position
    def get_start_end_positions(self):
        return (0, 0), (8, 9)

# Klasse der indeholder koden af det der foregår bag det visuelle. Koden der finder selve vejen. 
class Pathfinding:
    def __init__(self, grid):
        self.grid = grid

        self.frontier = []
        self.came_from = dict()

        self.start_pos, self.end_pos = self.grid.get_start_end_positions()

        self.frontier.append(self.start_pos)
        self.came_from[self.start_pos] = None

        #print(self.came_from)
        
    # Funktion der finder de gyldige naboer til en given position. "Valid neigbors" indeholder en liste, som retunerer de gyldige naboer.
    def neighbors(self, pos):
        x, y = pos
        possible_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                            #   (x+1,y+1), (x-1,y+1), (x+1,y-1), (x-1, y-1)] # Diagonals
        valid_neighbors = []

        for neighbor in possible_neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(self.grid.grid) and 0 <= ny < len(self.grid.grid[0]):
                if self.grid.grid[nx][ny] != 1 and self.grid.grid[nx][ny] != 2:
                    valid_neighbors.append(neighbor)

        return valid_neighbors

    # Funktion der gennemgår og tilføjer nabopositioner til frontier listen, samt registrere key og value i came_from dict.
    def find_path(self): 
        while self.frontier:
            current = self.frontier.pop()
            for next_pos in self.neighbors(current):
                if next_pos not in self.came_from:
                    self.frontier.append(next_pos)
                    self.came_from[next_pos] = current

        # Rekonstruere stien fra end_pos til start_pos og retunere den beregnede sti
        current = self.end_pos
        path = []
         
        while current != self.start_pos:
            path.append(current)
            current = self.came_from[current]

            # Vend stien om, så den går fra start_pos til end_pos
            # path.reverse()

        return path


# Hent start og slut position fra get_start_end_positions() metoden og tegn
# start og slut position som firkanter på skærmen
def draw_start_end():
            start_pos, end_pos = grid.get_start_end_positions()
            # Start position
            pygame.draw.rect(screen, (255, 67, 67), (start_pos[1] * grid.cell_width, start_pos[0] * grid.cell_height, grid.cell_width, grid.cell_height))
            # Slut posotion
            pygame.draw.rect(screen, (255, 67, 255), (end_pos[1] * grid.cell_width, end_pos[0] * grid.cell_height, grid.cell_width, grid.cell_height))

# Tegner stien ved at kalde find_path-metoden fra pathfinding-klassen/objektet
def draw_path():
            path = pathfinding.find_path()
            for pos in path:
                pygame.draw.circle(screen, (0, 0, 0), (pos[1] * grid.cell_width + grid.cell_width // 2, pos[0] * grid.cell_height + grid.cell_height // 2), 10)

# Funktion der kører og håndtere events i pygame, laver instanser af klasserne, tegner griddet, start- og slut position og stien på skærmen.
def main():
    pygame.init()

    # Angiv skærmens bredde og højde, og opret selve skræmen.
    screen_width = 600
    screen_height = 600

    global screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Miniprojekt 2")

    # Opret instanses af klasserne Grid og Pathfinding
    global grid
    grid = Grid(screen_width, screen_height)
    global pathfinding
    pathfinding = Pathfinding(grid)

    # Loopet kører så længe luk-knappen ikke klikkes.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Tegn griddet på skærmen og tegn start og slut positioner samt stien
        grid.draw(screen)
        draw_start_end()
        draw_path()

        # Opdatere skærmen
        pygame.display.flip()

    # Afslut pygame
    pygame.quit()

# Kald main-funktionen for at starte spillet
if __name__ == "__main__":
    main()
