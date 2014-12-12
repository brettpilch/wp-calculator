from parser import *
from Tkinter import *

# Advanced Football Analysis API stem:
stem = 'http://wp.advancedfootballanalytics.com/winprobcalc22.php?'

# Default Values:
scorediff_default = '0'
qtr_default = '1'
qtr_values = ['1','2','3','4','1st OT Poss', 'OT down by 3', 'OT sudden death']
minleft_default = '5'
secleft_default = '00'
ydline_default = '22'
fldside_default = 'own'
fldside_values = ['own', 'opp']
down_default = '1'
togo_default = '10'
preGameWP_default = '0.50'
ko1stHalf_default = '3' #don't know

#Initialize GUI window:
app = Tk()
app.title("NFL Win Probability Calculator")
app.geometry("600x500+10+10")

#Instantiate empty StringVars to hold output values:
wp = StringVar()
awp = StringVar()
ep = StringVar()
first_prob = StringVar()
td_prob = StringVar()
fg_prob = StringVar()

def calculate_wp():
    """
    This function is called when the submit button is clicked.
    It constructs the API call from user input values.
    WP data is retrieved from API and displayed in GUI labels.
    """
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
    #print url

    page = get_page(url)
    table = get_all_tables(page)[0]
    wp.set(table[0][0] + ' ' + table[0][1])
    awp.set(table[1][0] + ' ' + table[1][1])
    ep.set(table[2][0] + ' ' + table[2][1])
    first_prob.set(table[3][0] + ' ' + table[3][1])
    td_prob.set(table[4][0] + ' ' + table[4][1])
    fg_prob.set(table[5][0] + ' ' + table[5][1])

# Add each frame to the GUI packed from top to bottom:
score_frame = Frame(app)
score_frame.pack()

# Add each GUI element (label, button, etc.) to the appropriate frame from left to right:
scorediff_label = Label(score_frame, text = 'Score Difference:')
scorediff_label.pack(side=LEFT)

scorediff = StringVar()
scorediff.set(scorediff_default)
scorediff_entry = Entry(score_frame, textvariable = scorediff, width=4)
scorediff_entry.pack(side=LEFT)

qtr_frame1 = Frame(app)
qtr_frame1.pack()
qtr_frame2 = Frame(app)
qtr_frame2.pack()
qtr_label = Label(qtr_frame1, text = 'Quarter:')
qtr_label.pack(side=LEFT)
qtr = StringVar()
qtr_b1 = Radiobutton(qtr_frame1, text="1", variable=qtr, value='1')
qtr_b1.pack(side=LEFT)
qtr_b1.select()
Radiobutton(qtr_frame1, text="2", variable=qtr, value='2').pack(side=LEFT)
Radiobutton(qtr_frame1, text="3", variable=qtr, value='3').pack(side=LEFT)
Radiobutton(qtr_frame1, text="4", variable=qtr, value='4').pack(side=LEFT)
Radiobutton(qtr_frame2, text="1st OT poss", variable=qtr, value='5').pack(side=LEFT)
Radiobutton(qtr_frame2, text="OT down 3 pts", variable=qtr, value='6').pack(side=LEFT)
Radiobutton(qtr_frame2, text="OT sudden death", variable=qtr, value='7').pack(side=LEFT)

timeleft_frame = Frame(app)
timeleft_frame.pack()
timeleft_label = Label(timeleft_frame, text = 'Time Remaining:')
timeleft_label.pack(side=LEFT)

minleft = StringVar()
minleft.set(minleft_default)
minleft_entry = Entry(timeleft_frame, textvariable = minleft, width=3)
minleft_entry.pack(side=LEFT)

secleft_label = Label(timeleft_frame, text = ':')
secleft_label.pack(side=LEFT)

secleft = StringVar()
secleft.set(secleft_default)
secleft_entry = Entry(timeleft_frame, textvariable = secleft, width=3)
secleft_entry.pack(side=LEFT)

ydline_frame = Frame(app)
ydline_frame.pack()
ydline_label = Label(ydline_frame, text = 'Yard Line:')
ydline_label.pack(side=LEFT)

ydline = StringVar()
ydline.set(ydline_default)
ydline_entry = Entry(ydline_frame, textvariable = ydline, width=3)
ydline_entry.pack(side=LEFT)

fldside = StringVar()
fldside_b1 = Radiobutton(ydline_frame, text="Own", variable=fldside, value='own')
fldside_b1.pack(side=LEFT)
fldside_b1.select()
Radiobutton(ydline_frame, text="Opponent's", variable=fldside, value='opp').pack(side=LEFT)

down_frame = Frame(app)
down_frame.pack()
down_label = Label(down_frame, text = 'Down:')
down_label.pack(side=LEFT)

down = StringVar()
down_b1 = Radiobutton(down_frame, text="1st", variable=down, value='1')
down_b1.pack(side=LEFT)
down_b1.select()
Radiobutton(down_frame, text="2nd", variable=down, value='2').pack(side=LEFT)
Radiobutton(down_frame, text="3rd", variable=down, value='3').pack(side=LEFT)
Radiobutton(down_frame, text="4th", variable=down, value='4').pack(side=LEFT)

togo_frame = Frame(app)
togo_frame.pack()
togo_label = Label(togo_frame, text = 'To go distance:')
togo_label.pack(side=LEFT)

togo = StringVar()
togo.set(togo_default)
togo_entry = Entry(togo_frame, textvariable = togo, width=3)
togo_entry.pack(side=LEFT)

pregame_frame = Frame(app)
pregame_frame.pack()
preGameWP_label = Label(pregame_frame, text = 'Pre-game win probability:')
preGameWP_label.pack(side=LEFT)

preGameWP = StringVar()
preGameWP.set(preGameWP_default)
preGameWP_entry = Entry(pregame_frame, textvariable = preGameWP, width=7)
preGameWP_entry.pack(side=LEFT)

ko_frame = Frame(app)
ko_frame.pack()
ko1stHalf_label = Label(ko_frame, text = 'Offense kicked off in first half?')
ko1stHalf_label.pack(side=LEFT)
ko1stHalf = StringVar()
Radiobutton(ko_frame, text="yes", variable=ko1stHalf, value='1').pack(side=LEFT)
Radiobutton(ko_frame, text="no", variable=ko1stHalf, value='2').pack(side=LEFT)
ko1stHalf_b1 = Radiobutton(ko_frame, text="don't know", variable=ko1stHalf, value='3')
ko1stHalf_b1.pack(side=LEFT)
ko1stHalf_b1.select()

submit_button = Button(app, text = 'Calculate Win Probability', width = 40, command = calculate_wp)
submit_button.pack()

separator = Frame(app, height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

# Add all output labels to the bottom of the window.
# These are initially empty, so they can't be seen in the window:
wp_label = Label(app, textvariable = wp)
wp_label.pack()
awp_label = Label(app, textvariable = awp)
awp_label.pack()
ep_label = Label(app, textvariable = ep)
ep_label.pack()
first_label = Label(app, textvariable = first_prob)
first_label.pack()
td_label = Label(app, textvariable = td_prob)
td_label.pack()
fg_label = Label(app, textvariable = fg_prob)
fg_label.pack()

app.mainloop()
