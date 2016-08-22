import shutil, os, re

datePattern = re.compile(r'''^(.*?) # all text before the date
((0|1)?\d)-                         # one or two digits for the month
((0|1|2|3)?\d)-                     # one or two digits for the day
((19|20)\d\d)                       # four digits for the year
(.*?)$                              # all text after the date
''', re.VERBOSE)

for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    euroFileName = '{}{}-{}-{}{}'.format(beforePart, dayPart, monthPart,
                                         yearPart, afterPart)

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # Rename the files.
    print('Rename "{}" to "{}"...'.format(amerFileName, euroFileName))
    shutil.move(amerFileName, euroFileName)
