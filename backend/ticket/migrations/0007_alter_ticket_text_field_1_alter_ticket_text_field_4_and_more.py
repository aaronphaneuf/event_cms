# Generated by Django 4.1.7 on 2023-08-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_ticket_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='text_field_1',
            field=models.TextField(blank=True, default='This ticket is valid for ONE (1) entry to the Wilder Institute/Calgary Zoo for the specific date listed above.<br /><b> YOU MUST\n                                                            PRESENT THIS TICKET WITH VALID BARCODE FOR ENTRY INTO THE ZOO AT THE NOTED TIME.</b>'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='text_field_4',
            field=models.TextField(blank=True, default='<b>Click <link href="https://www.calgaryzoo.com/events/events-at-a-glance" color="blue"><u>HERE</u></link> for more information on your experience and to plan your visit.<br />\n                                                            Thank you for supporting wildlife conservation.</b>'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='text_field_5',
            field=models.TextField(blank=True, default='<b>THIS IS YOUR TICKET:</b> <font color="blue">This e-ticket is valid on your phone</font>, printed in black and white or colour and MUST have a clear and valid barcode. This e-ticket is only valid for the date and time it states above.<br /><br />\n                                                            <b>TICKETS ARE NON-TRANSFERABLE AND NON-REFUNDABLE.</b><br /> <font color="red">Unauthorized duplication or sale of a ticket is prohibited. </font>The Wilder Institute/Calgary Zoo is not responsible for any inconvenience caused by unauthorized duplication and reserve the right to deny entry and/or suspend membership privileges.'),
        ),
    ]
