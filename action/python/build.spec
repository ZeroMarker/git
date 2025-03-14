# -*- mode: python ; coding: utf-8 -*-

block_cipher = None  # For encryption (optional)

# Main analysis configuration
a = Analysis(
    ['src/main.py'],  # Your main script
    pathex=['/path/to/your/project'],  # Project root directory
    binaries=[],  # External binaries (.dll, .so, etc.)
    datas=[
        ('assets/images/*.png', 'assets/images'),  # Include image folder
        ('config/settings.json', 'config')  # Include config file
    ],
    hiddenimports=[  # Force-include modules PyInstaller might miss
        'sklearn.utils._weight_vector',
        'pandas._libs.tslibs'
    ],
    hookspath=[],  # Custom hooks directory
    hooksconfig={},  # Hook configuration overrides
    runtime_hooks=[],
    excludes=[],  # Exclude unnecessary modules to reduce size
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,  # Set to True for debug
)

# Bundle Python files into a .pyz archive
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

# Executable configuration
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='MyAwesomeApp',  # Output executable name
    icon='assets/icons/app_icon.ico',  # Application icon
    debug=False,  # Set to True for development
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Use UPX compression (requires UPX installed)
    upx_exclude=[],
    runtime_tmpdir=None,  # Temp directory (use for onefile mode)
    console=False,  # Set to True for console applications
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,  # macOS code signing
    entitlements_file=None,  # macOS entitlements
)

# For one-file builds (optional)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MyAwesomeApp',  # Folder name for one-dir builds
)