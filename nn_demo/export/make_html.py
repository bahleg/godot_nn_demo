from pathlib import Path
buffer = []
# ignoring teenygrad package directory 
for f in list(Path('teenygrad/teenygrad').glob('./**/*py')) + [Path('server.py')]:
        if str(f) == 'server.py':
            to_save = "/home/pyodide/server.py"
        else:
            to_save = f"/home/pyodide/{f.parent.relative_to('teenygrad')}/{f.name}"
            
        print (f'copying {f} to {to_save}')
        with open(f) as inp:
                text = inp.read().replace('`', ' ') # usually can be met in comments
         
        # inject python script to create a directory and file inside pyodide
        buffer.append(f"print('writing {to_save}')")
        buffer.append(f"""Path("{to_save}").parent.mkdir(parents=True, exist_ok=True) 
Path(f"{to_save}").write_text(\"\"\"{text}\"\"\")""")

with open('template.html') as inp:
        data = inp.read()
        
with open('filled_template.html', 'w') as out:
        # 'CODE' in our placeholder for inserting copy code  
        out.write(data.replace('CODE', "pyodide.runPython(`"+'\n'.join(buffer)+"\n`)")) 
