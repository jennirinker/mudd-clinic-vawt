"""Messing around for now.
"""
from pathlib import Path
from lacbox.htc import HTCFile


current_dir = Path(__file__).parent.absolute()
master_dir = current_dir / '..' / 'htc_master'
htc_dir = current_dir / '..' / 'htc'

MASTER_NAME = 'H-rotor_3blades.htc'
master_path = master_dir / MASTER_NAME
htc_name = MASTER_NAME.replace('.htc', '_5sec.htc')

# create 5-sec files from base
htc = HTCFile(master_path)
htc.set_time(start=0, stop=5)
htc.save(filename=htc_dir / htc_name)
