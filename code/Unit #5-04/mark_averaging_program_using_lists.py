# Created by: Hamza Salman
# Created on: November 2016
# Created for: ICS3U
# this program averages mark

import __future__
import ui

marks = []
	
def add_mark_button_touch_up_inside(sender):
	
    if float(view['input_textfield'].text) < 0 or float(view['input_textfield'].text) > 100:
        view['output_label'].text = 'please enter a number between 0-100'
    else:
        try:
            marks.append(float(view['input_textfield'].text))
            print(marks)
            view['marks_textview'].text = ''
            view['input_textfield'].text = ''
            for mark in marks:
                view['marks_textview'].text = view['marks_textview'].text + '\n' + str(mark)

        except:
            view['output_label'].text = 'please enter a number'
			
    if view['input_textfield'].text == '-1':
        view['output_label'].text = 'The program has been stopped'
			
def calculate_button_touch_up_inside(sender):

    average = 0
    average_max = 0
	
    if len(marks) == 0:
        view['output_label'].text = 'Add some marks first!'
    else:		
        for mark in marks:
            average = average + mark
        averageMax = float(len(marks)) * 100
        average = average / float(averageMax)
        average = average * 100
        round(average, 2)
        view['output_label'].text = ('the average of the marks is ' + str(average))
    if view['input_textfield'].text == '-1':
        view['output_label'].text = 'The program has been stopped'
		
view = ui.load_view()
view.present('fullscreen')

