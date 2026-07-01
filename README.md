# Slingshot Empire: Invasion Overdrive Pro

A professional, premium, cross-platform Pygame slingshot action game rebuilt for desktop and Android. Designed to feel like a polished mobile title ready for Google Play Store.

## Features

- **Premium UI/UX**: redesigned menus, panels, buttons, HUD, and overlays with glow, gradients, shadows, and smooth animations.
- **Multiple screens**: Main Menu, How to Play, Settings, Shop, Pause, Game Over, and Victory.
- **Modern controls**: drag-to-aim, trajectory preview, touch + mouse support, haptic feedback.
- **Gameplay**: slingshot physics, combos, power-ups, boss waves, weapon upgrades, and progression to level 100.
- **Ads**: AdMob-ready Banner, Interstitial, and Rewarded ads with test IDs and graceful offline fallback.
- **Performance**: cached surfaces, object pooling-friendly entities, capped dt, and optional FPS display.
- **Save/Load**: profile persistence with atomic writes and backups, plus settings persistence.
- **Audio**: procedural SFX and music (no external assets required), volume controls.
- **Custom art**: drop PNG files into `assets/images/` to override any generated sprite.

## Run on desktop

```bash
cd artifacts/slingshot-empire
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

Optional flags:

```bash
python src/main.py --windowed --width 1280 --height 720
python src/main.py --headless      # for CI / screenshot generation
```

## Controls

- **Drag** from the slingshot to aim, **release** to shoot.
- **Weapon tabs** on the right switch ammo (Plasma/Ballista are only available during boss fights).
- **SHOP** and **PAUSE** buttons in the HUD.
- **ESC** toggles pause / back (desktop).
- **Settings** lets you toggle music, SFX, vibration, particles, glow, FPS, and ads.

## Build for Android (Google Play Store)

### 1. Install Buildozer and dependencies

```bash
pip install buildozer cython
sudo apt update && sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libffi-dev libssl-dev libltdl-dev
```

### 2. Set your AdMob App ID (required for release)

For development, the game uses Google's test IDs automatically. Before release, either:

- Set the environment variable: `export ADMOB_APP_ID=ca-app-pub-XXXXXXXX~XXXXXXXX`
- Or edit `buildozer.spec` and replace `${ADMOB_APP_ID}` with your real ID.

### 3. Add an AdMob recipe (optional for test builds)

To show real ads on Android, add a python-for-android recipe such as **KivMob** or **KivAds** to your `buildozer.spec`:

```ini
p4a.local_recipes = ./recipes
```

The game already provides a safe `AdManager` facade that will work once the recipe is present. Without a recipe, ads are silently disabled and the game continues to run.

### 4. Build the APK

```bash
cd artifacts/slingshot-empire
buildozer -v android debug
```

### 5. Release build

```bash
buildozer -v android release
```

Make sure to update `buildozer.spec` with your final package name, version, and signing keystore before Play Store upload.

## Project structure

```text
artifacts/slingshot-empire/
├── src/
│   ├── main.py              # Entry point
│   ├── config.py            # Constants, theme, difficulty settings
│   ├── core/
│   │   └── engine.py        # Main game loop, state manager
│   ├── entities/
│   │   ├── bird.py          # Enemy birds (normal, alpha, golden)
│   │   ├── boss.py          # Boss waves and projectiles
│   │   ├── arrow.py         # Player arrows / slingshot physics
│   │   └── particle.py      # Particle effects and trails
│   ├── systems/
│   │   ├── physics.py       # Collision, movement, gameplay logic
│   │   ├── audio.py         # Procedural sound effects + music
│   │   ├── save_manager.py  # JSON profile + settings persistence
│   │   ├── sprite_atlas.py  # Runtime sprite generation + asset loading
│   │   ├── vibration.py     # Cross-platform haptic feedback
│   │   └── ads.py           # AdMob integration facade
│   ├── ui/
│   │   ├── widgets.py       # Premium buttons, labels, panels, toggles
│   │   ├── screens.py       # Menu, Shop, Pause, Game Over, Victory, Settings, Tutorial
│   │   └── hud.py           # Heads-up display
│   └── utils/
│       └── helpers.py       # Fonts, gradients, effects, utilities
├── assets/
│   ├── images/              # Optional custom sprite overrides
│   └── ad_config.json       # AdMob test IDs and policy
├── buildozer.spec           # Android packaging config
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── CHANGES.md               # Detailed changelog
```

## AdMob integration details

- **Banner ads**: shown on the Main Menu, Shop/Pause, and Game Over screens.
- **Interstitial ads**: shown at Game Over, capped to avoid policy violations.
- **Rewarded ads**: available in the Shop to grant +50 coins; rewarded even if ads are offline so the game never feels broken.
- **Test IDs**: `assets/ad_config.json` contains Google's official AdMob test IDs.
- **Error handling**: all ad calls are wrapped in try/except; the game never crashes if an ad fails to load.

## Performance notes

- All gradients, shadows, and panels are cached by size.
- Particle system uses a shared scratch surface.
- `dt` is capped to prevent physics spikes on lag frames.
- Enable **Low Quality** in Settings to disable glow and particles on older devices.

## License

This project is for educational / publishing by the owner. Replace placeholder art and ad IDs with your own before commercial release.
