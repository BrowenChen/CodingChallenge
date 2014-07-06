import gdata.calendar.service
import gdata.calendar
import atom

cal_client = gdata.calendar.service.CalendarService()
cal_client.email = 'owenchen93@gmail.com'
cal_client.password = 'Mindtr1ck'

def initiateCal():
	cal_client.ProgrammaticLogin()



def add_to_gcal(item):
	initiateCal()
	event = gdata.calendar.CalendarEventEntry()
	event.content = atom.Content(text=item)
	event.quick_add = gdata.calendar.QuickAdd(value='true');

	new_event = cal_client.InsertEvent(event, '/calendar/feeds/hqun5dji8sttvs5nrncadbbnb8%40group.calendar.google.com/private/full')


def get_cal_list():
	initiateCal()
	return cal_client.GetOwnCalendarsFeed()

# def _InsertSingleEvent(self, title='One-time Tennis with Beth',
#   content='Meet for a quick lesson', where='On the courts',
#   start_time=None, end_time=None):
#     """Uses the _InsertEvent helper method to insert a single event which
#     does not have any recurrence syntax specified."""

#     new_event = self._InsertEvent(title, content, where, start_time, end_time,
#         recurrence_data=None)

#     print 'New single event inserted: %s' % (new_event.id.text,)
#     print '\tEvent edit URL: %s' % (new_event.GetEditLink().href,)
#     print '\tEvent HTML URL: %s' % (new_event.GetHtmlLink().href,)

#     return new_event



add_to_gcal('Dentist Appt today at 4pm')
# cal_client._InsertSingleEvent("Lolz")

print "Your event was created"

