from django.db import models
from core.models import Event

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    date = models.CharField(max_length=255, blank=True)
    time = models.CharField(max_length=255, blank=True)
    ticket_type = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    order_date = models.CharField(max_length=255, blank=True)
    order_number = models.CharField(max_length=255, blank=True)
    custom_1 = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    barcode = models.CharField(max_length=255, blank=True)

    text_field_1 = models.TextField(blank=True, default="""This ticket is valid for ONE (1) entry to the Wilder Institute/Calgary Zoo for the specific date listed above.<br /><b> YOU MUST
                                                            PRESENT THIS TICKET WITH VALID BARCODE FOR ENTRY INTO THE ZOO AT THE NOTED TIME.</b>""")
    text_field_2 = models.TextField(blank=True)
    text_field_3 = models.TextField(blank=True)
    text_field_4 = models.TextField(blank=True, default="""<b>Click <link href="https://www.calgaryzoo.com/events/events-at-a-glance" color="blue"><u>HERE</u></link> for more information on your experience and to plan your visit.<br />
                                                            Thank you for supporting wildlife conservation.</b>""")
    text_field_5 = models.TextField(blank=True, default="""<b>THIS IS YOUR TICKET:</b> <font color="blue">This e-ticket is valid on your phone</font>, printed in black and white or colour and MUST have a clear and valid barcode. This e-ticket is only valid for the date and time it states above.<br /><br />
                                                            <b>TICKETS ARE NON-TRANSFERABLE AND NON-REFUNDABLE.</b><br /> <font color="red"><u>Unauthorized duplication or sale of a ticket is prohibited.</u></font>The Wilder Institute/Calgary Zoo is not responsible for any inconvenience caused by unauthorized duplication and reserve the right to deny entry and/or suspend membership privileges.""")