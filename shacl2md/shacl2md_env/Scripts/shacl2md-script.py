#!c:\users\itsd\documents\github\tooling-evaluation\shacl2md\shacl2md_env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'shacl2md==0.0.0','console_scripts','shacl2md'
__requires__ = 'shacl2md==0.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('shacl2md==0.0.0', 'console_scripts', 'shacl2md')()
    )
