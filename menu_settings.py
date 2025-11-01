import pygame as pg
import sys

pg.init()

button_font = pg.font.Font(None, 60)
WHITE = (255, 255, 255)

volume = 50
difficulty = "Normal"
fullscreen = False

def menu_settings(screen, bg_image, WIDTH, HEIGHT, Button):
    global volume, difficulty, fullscreen
    clock = pg.time.Clock()
    running = True

    def exit_settings():
        nonlocal running
        running = False

    back_button = Button("Back", WIDTH//2 - 150, HEIGHT - 120, 300, 80, exit_settings)

    while running:
        screen.blit(bg_image, (0, 0))

        vol_text = button_font.render(f"Volume: {volume}%", True, WHITE)
        diff_text = button_font.render(f"Difficulty: {difficulty}", True, WHITE)
        full_text = button_font.render(f"Fullscreen: {'On' if fullscreen else 'Off'}", True, WHITE)

        screen.blit(vol_text, (WIDTH//2 - vol_text.get_width()//2, 150))
        screen.blit(diff_text, (WIDTH//2 - diff_text.get_width()//2, 250))
        screen.blit(full_text, (WIDTH//2 - full_text.get_width()//2, 350))

        back_button.draw(screen)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    volume = max(0, volume - 5)
                    pg.mixer.music.set_volume(volume / 100)
                elif event.key == pg.K_RIGHT:
                    volume = min(100, volume + 5)
                    pg.mixer.music.set_volume(volume / 100)
                elif event.key == pg.K_d:
                    difficulty = "Easy" if difficulty == "Normal" else "Hard" if difficulty == "Easy" else "Normal"
                elif event.key == pg.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
                    else:
                        screen = pg.display.set_mode((WIDTH, HEIGHT))
            back_button.check_click(event)

        clock.tick(60)
