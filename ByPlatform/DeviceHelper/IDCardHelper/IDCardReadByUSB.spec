# -*- mode: python -*-

block_cipher = None


a = Analysis(['IDCardReadByUSB.py'],
             pathex=['D:\\Work\\SVNRep\\BYSmartPlatform\\4.Code\\Smart\\Platform\\ByPlatform\\DeviceHelper\\IDCardHelper'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='IDCardReadByUSB',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
