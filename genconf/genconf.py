#!/usr/bin/env python

import ConfigParser

entries = [
	# ['template', 'output_file', 'config_file', 'section'],

	# hostname config
	['input/HOSTNAME', 'output/HOSTNAME_MDF_UP1', 'config/os.conf', 'mdf_up1'],
	['input/HOSTNAME', 'output/HOSTNAME_MDF_UP2', 'config/os.conf', 'mdf_up2'],
	['input/HOSTNAME', 'output/HOSTNAME_MDF_CP1', 'config/os.conf', 'mdf_cp1'],
	['input/HOSTNAME', 'output/HOSTNAME_MDF_CP2', 'config/os.conf', 'mdf_cp2'],
	['input/HOSTNAME', 'output/HOSTNAME_MDF_DB1', 'config/os.conf', 'mdf_db1'],
	['input/HOSTNAME', 'output/HOSTNAME_MDF_DB2', 'config/os.conf', 'mdf_db2'],
]

for entry in entries:
	tpl_str = open(entry[0], 'r').read()

	config = ConfigParser.ConfigParser()
	config.read(entry[2])
	conf_dict = dict(config.items(entry[3]))

	str = tpl_str % conf_dict

	open(entry[1], 'w').write(str)
