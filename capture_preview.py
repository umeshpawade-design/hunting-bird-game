import os
import sys
import pygame

# Force dummy video driver so we can render without a real display.
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from core.engine import Game  # noqa: E402

pygame.init()

game = Game(width=1280, height=720, fullscreen=False, headless=False)

# Let the game render a few frames to settle into the menu state.
for _ in range(5):
    game._handle_events()
    game._update(1 / 60.0)
    game._draw()

# Save the rendered game surface.
if game.game_surface is not None:
    out_path = os.path.join(os.path.dirname(__file__), "preview.bmp")
    size = game.game_surface.get_size()
    raw = pygame.image.tostring(game.game_surface, "RGB")
    save_surface = pygame.image.fromstring(raw, size, "RGB")
    pygame.image.save(save_surface, out_path)
    print(f"Saved preview to {out_path}")
else:
    print("No game_surface to save")

pygame.quit()
