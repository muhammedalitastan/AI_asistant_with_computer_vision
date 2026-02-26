# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Main3.py'],
    pathex=[],
    binaries=[],
    datas=[('intents.json', '.'), ('chat_model.h5', '.'), ('tokenizer.pkl', '.'), ('daily.json', '.'), ('schedule.json', '.'), ('Browsing.py', '.'), ("Drone'a_bağlanma.py", '.'), ('gunluk.py', '.'), ('initialize_engine.py', '.'), ('metin_girisi.py', '.'), ('metin_yazdirma.py', '.'), ('model_test.py', '.'), ('model_train.py', '.'), ('open_close_app.py', '.'), ('schedule3.py', '.'), ('social_media.py', '.'), ('tempCodeRunnerFile.py', '.'), ('utils.py', '.'), ("wi_fi'ye_bağlanma.py", '.'), ('wishMe.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='JARVIS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
