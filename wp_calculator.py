from parser import *
from Tkinter import *

full = 'http://wp.advancedfootballanalytics.com/winprobcalc22.php?scorediff=0&minleft=5&sec=00&ydline=22&fldside=own&qtr=4&down=1&togo=10&preGameWP=0.50&ko1stHalf=3'
stem = 'http://wp.advancedfootballanalytics.com/winprobcalc22.php?'

# Default Values:
scorediff_default = '0'
qtr_default = '4'
qtr_values = ['1','2','3','4','1st OT Poss', 'OT down by 3', 'OT sudden death']
minleft_default = '5'
secleft_default = '00'
ydline_default = '22'
fldside_default = 'own'
fldside_values = ['own', 'opp']
down_default = '1'
togo_default = '10'
preGameWP_default = '0.50'
ko1stHalf_default = '3'

app = Tk()
app.title("NFL Win Probability Calculator")
app.geometry("600x800+10+10")

wp = StringVar()

def calculate_wp():
    fields = [
        ['scorediff', scorediff.get()],
        ['minleft', minleft.get()],
        ['sec', secleft.get()],
        ['ydline', ydline.get()],
        ['fldside', fldside.get()],
        ['qtr', qtr.get()],
        ['down', down.get()],
        ['togo', togo.get()],
        ['preGameWP', preGameWP.get()],
        ['ko1stHalf', ko1stHalf.get()]
        ]

    endlist = ['='.join(field) for field in fields]
    end = '&'.join(endlist)
    url = stem + end
    print url
    #print url == full

    page = get_page(url)
    table = get_all_tables(page)[0]
    wp.set('Win Probability: ' + table[0][1])

scorediff_label = Label(app, text = 'Score Difference:')
scorediff_label.pack()

scorediff = StringVar()
scorediff.set(scorediff_default)
scorediff_entry = Entry(app, textvariable = scorediff)
scorediff_entry.pack()

qtr_label = Label(app, text = 'Quarter:')
qtr_label.pack()

qtr = StringVar()
qtr.set(qtr_default)
qtr_dropdown = OptionMenu(app, qtr, *qtr_values) # need callback function?
qtr_dropdown.pack()

minleft_label = Label(app, text = 'Minutes:')
minleft_label.pack()

minleft = StringVar()
minleft.set(minleft_default)
minleft_entry = Entry(app, textvariable = minleft)
minleft_entry.pack()

secleft_label = Label(app, text = 'Seconds:')
secleft_label.pack()

secleft = StringVar()
secleft.set(secleft_default)
secleft_entry = Entry(app, textvariable = secleft)
secleft_entry.pack()

ydline_label = Label(app, text = 'Yard Line:')
ydline_label.pack()

ydline = StringVar()
ydline.set(ydline_default)
ydline_entry = Entry(app, textvariable = ydline)
ydline_entry.pack()

fldside_label = Label(app, text = 'Field Side:')
fldside_label.pack()

fldside = StringVar()
Radiobutton(app, text="Own", variable=fldside, value='own').pack()
Radiobutton(app, text="Opponent's", variable=fldside, value='opp').pack()

down_label = Label(app, text = 'Down:')
down_label.pack()

down = StringVar()
Radiobutton(app, text="1st", variable=down, value='1').pack()
Radiobutton(app, text="2nd", variable=down, value='2').pack()
Radiobutton(app, text="3rd", variable=down, value='3').pack()
Radiobutton(app, text="4th", variable=down, value='4').pack()

togo_label = Label(app, text = 'To go distance:')
togo_label.pack()

togo = StringVar()
togo.set(togo_default)
togo_entry = Entry(app, textvariable = togo)
togo_entry.pack()

preGameWP_label = Label(app, text = 'Pre-game win probability:')
preGameWP_label.pack()

preGameWP = StringVar()
preGameWP.set(preGameWP_default)
preGameWP_entry = Entry(app, textvariable = preGameWP)
preGameWP_entry.pack()

ko1stHalf_label = Label(app, text = 'Offense kicked off in first half?')
ko1stHalf_label.pack()

ko1stHalf = StringVar()
Radiobutton(app, text="yes", variable=ko1stHalf, value='1').pack()
Radiobutton(app, text="no", variable=ko1stHalf, value='2').pack()
Radiobutton(app, text="don't know", variable=ko1stHalf, value='3').pack()

submit_button = Button(app, text = 'Calculate Win Probability', width = 40, command = calculate_wp)
submit_button.pack()

wp.set('Win Probability: 0.50')
wp_label = Label(app, textvariable = wp)
wp_label.pack()

app.mainloop()

##
##while True:
##    scorediff1 = raw_input('Score Diff int(-inf, inf): ')
##    if scorediff1: scorediff = scorediff1
##    
##    qtr1 = raw_input('Quarter int[1,7] (5: 1st OT possession, 6: OT -3 pts, 7: sudden death) ')
##    if qtr1: qtr = qtr1
##    
##    timeleft1 = raw_input('Time Left (mm:ss <= 15:00) ')
##    if timeleft1: timeleft = timeleft1
##    
##    ydline1 = raw_input('Yard Line int[1,50]: ')
##    if ydline1: ydline = ydline1
##    
##    fldside1 = raw_input('Field Side [own, opp]: ')
##    if fldside1: fldside = fldside1
##    
##    down1 = raw_input('Down int[1,4]: ')
##    if down1: down = down1
##    
##    togo1 = raw_input('To go distance int[1,90]: ')
##    if togo1: togo = togo1
##    
##    preGameWP1 = raw_input('Pre-game WP float[0.00,1.00): ')
##    if preGameWP1: preGameWP = preGameWP1
##    
##    ko1stHalf1 = raw_input('Offense kicked off in 1st half? (1: yes, 2: no, 3: don\'t know) ')
##    if ko1stHalf1: ko1stHalf = ko1stHalf1
##    
##    timelist = timeleft.split(':')
##
##    fields = [
##        ['scorediff', scorediff],
##        ['minleft', timelist[0]],
##        ['sec', timelist[1]],
##        ['ydline', ydline],
##        ['fldside', fldside],
##        ['qtr', qtr],
##        ['down', down],
##        ['togo', togo],
##        ['preGameWP', preGameWP],
##        ['ko1stHalf', ko1stHalf]
##        ]
##
##    endlist = ['='.join(field) for field in fields]
##    end = '&'.join(endlist)
##    url = stem + end
##    #print url
##    #print url == full
##
##    page = get_page(url)
##    tables = get_all_tables(page)
##    for table in tables:
##        for row in table:
##            print row
