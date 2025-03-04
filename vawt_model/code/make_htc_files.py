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

# create 5-sec files from base
HTC_NAME = MASTER_NAME.replace('.htc', '_5sec')
htc = HTCFile(master_path)
htc.set_time(start=3, stop=5)
htc.set_name(HTC_NAME)
htc.save(filename=htc_dir / (HTC_NAME + '.htc'))

# create a 5-sec file with a new rotor speed
tsr, wsp = 5.2, 4
omega = tsr * wsp / 0.7874  # rad/s
HTC_NAME = MASTER_NAME.replace('.htc', f'_tsr{tsr}')
htc = HTCFile(master_path)
htc.set_time(start=3, stop=5)
htc.wind.wsp = wsp  # set the wind speed
htc.new_htc_structure.orientation.relative.mbdy2_ini_rotvec_d1 = [0.0, 0.0, 1.0, omega]  # init. rotor speed
htc.new_htc_structure.constraint.bearing3.omegas = omega  # constrained rotor speed
htc.set_name(HTC_NAME)
htc.save(filename=htc_dir / (HTC_NAME + '.htc'))
