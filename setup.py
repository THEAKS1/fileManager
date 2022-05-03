from cx_Freeze import setup, Executable

base = None    

executables = [Executable("file_explo.py", base=base)]

packages = ["idna","PyQt5","os","shutil"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "pdf_merger",
    options = options,
    version = "0.1",
    description = 'merges pdf',
    executables = executables
)