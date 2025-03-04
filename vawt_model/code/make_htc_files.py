"""Messing around for now.

Update rotor speed: relative (initial rotor speed) AND bearing3 constraint
"""
from pathlib import Path
from lacbox.htc import HTCFile


current_dir = Path(__file__).parent.absolute()
master_dir = current_dir / '..' / 'htc_master'
htc_dir = current_dir / '..' / 'htc'

MASTER_NAME = 'mudd_vawt.htc'
master_path = master_dir / MASTER_NAME
HTC_NAME = MASTER_NAME.replace('.htc', '_5sec')

# create 5-sec files from base
htc = HTCFile(master_path)
htc.set_time(start=3, stop=5)
htc.set_name(HTC_NAME)
htc.save(filename=htc_dir / (HTC_NAME + '.htc'))
