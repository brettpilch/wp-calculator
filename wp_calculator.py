from parser import *

full = 'http://wp.advancedfootballanalytics.com/winprobcalc22.php?scorediff=0&minleft=5&sec=00&ydline=22&fldside=own&qtr=4&down=1&togo=10&preGameWP=0.50&ko1stHalf=3'
stem = 'http://wp.advancedfootballanalytics.com/winprobcalc22.php?'

# Default Values:
scorediff = '0'
qtr = '4'
timeleft = '5:00'
ydline = '22'
fldside = 'own'
down = '1'
togo = '10'
preGameWP = '0.50'
ko1stHalf = '3'

while True:
    scorediff1 = raw_input('Score Diff int(-inf, inf): ')
    if scorediff1: scorediff = scorediff1
    
    qtr1 = raw_input('Quarter int[1,7] (5: 1st OT possession, 6: OT -3 pts, 7: sudden death) ')
    if qtr1: qtr = qtr1
    
    timeleft1 = raw_input('Time Left (mm:ss <= 15:00) ')
    if timeleft1: timeleft = timeleft1
    
    ydline1 = raw_input('Yard Line int[1,50]: ')
    if ydline1: ydline = ydline1
    
    fldside1 = raw_input('Field Side [own, opp]: ')
    if fldside1: fldside = fldside1
    
    down1 = raw_input('Down int[1,4]: ')
    if down1: down = down1
    
    togo1 = raw_input('To go distance int[1,90]: ')
    if togo1: togo = togo1
    
    preGameWP1 = raw_input('Pre-game WP float[0.00,1.00): ')
    if preGameWP1: preGameWP = preGameWP1
    
    ko1stHalf1 = raw_input('Offense kicked off in 1st half? (1: yes, 2: no, 3: don\'t know) ')
    if ko1stHalf1: ko1stHalf = ko1stHalf1
    
    timelist = timeleft.split(':')

    fields = [
        ['scorediff', scorediff],
        ['minleft', timelist[0]],
        ['sec', timelist[1]],
        ['ydline', ydline],
        ['fldside', fldside],
        ['qtr', qtr],
        ['down', down],
        ['togo', togo],
        ['preGameWP', preGameWP],
        ['ko1stHalf', ko1stHalf]
        ]

    endlist = ['='.join(field) for field in fields]
    end = '&'.join(endlist)
    url = stem + end
    #print url
    #print url == full

    page = get_page(url)
    tables = get_all_tables(page)
    for table in tables:
        for row in table:
            print row
