from django.shortcuts import render
from .models import Ticket
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import FileResponse
from rest_framework.response import Response
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch
from reportlab.lib import utils
import io


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        ticket = Ticket.objects.get(pk=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)


class TicketPDFView(APIView):
    def get(self, request, *args, **kwargs):
        # .get('field', 'default')
        ticket_number = request.GET.get('ticket_number', '00')  
        name = request.GET.get('name', '00')
        date = request.GET.get('date', '00') 
        time = request.GET.get('time', '00')
        ticket_type = request.GET.get('ticket_type', '00')
        price = request.GET.get('price', '00')
        order_number = request.GET.get('order_number', '00')
        order_date = request.GET.get('order_date', '00')
        location = request.GET.get('location', '00')
        custom_1 = request.GET.get('custom_1', '00')
        barcode = request.GET.get('barcode', '00')
        text_field_1 = request.GET.get('text_field_1', '00')
        text_field_2 = request.GET.get('text_field_2', '00')
        text_field_3 = request.GET.get('text_field_3', '00')
        text_field_4 = request.GET.get('text_field_4', '00')
        text_field_5 = request.GET.get('text_field_5', '00')

        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        c = canvas.Canvas(buffer, pagesize=A4)

        def resize_image(image_path, desired_width):
            img = utils.ImageReader(image_path)
            original_width, original_height = img.getSize()
            aspect_ratio = original_width / original_height
            desired_height = desired_width / aspect_ratio
            return desired_width, desired_height

        # Define the layout
        layout = [
            {'rows': 1, 'cols': [{'width': 0.75, 'image': 'static/images/zoo_logo.png'}, {'width': 0.25}], 'height': 0.10},
            {'rows': 1, 'cols': [{'width': 0.25}, {'width': 0.75}], 'height': 0.04},
            {'rows': 1, 'cols': [{'width': 0.10}, {'width': 0.40}, {'width': 0.10}, {'width': 0.40}], 'height': 0.04},
            {'rows': 1, 'cols': [{'width': 0.15}, {'width': 0.35}, {'width': 0.15}, {'width': 0.35}], 'height': 0.04},
            {'rows': 1, 'cols': [{'width': 0.15}, {'width': 0.35}, {'width': 0.15}, {'width': 0.35}], 'height': 0.04},
            {'rows': 1, 'cols': [{'width': 0.15}, {'width': 0.35}, {'width': 0.15}, {'width': 0.35}], 'height': 0.04},
            {'rows': 1, 'cols': [{'width': 1}], 'height': 0.10},
            {'rows': 1, 'cols': [{'width': 1}], 'height': 0.05},
            {'rows': 1, 'cols': [{'width': 1}], 'height': 0.06},
            {'rows': 1, 'cols': [{'width': 1}], 'height': 0.30},
            {'rows': 1, 'cols': [{'width': 1}], 'height': 0.04},
            {'rows': 1, 'cols': [{'width': 1}], 'height': 0.15},
        ]

        # Variable definitions
        zoo_blue = colors.Color(red=(0.0/255), green=(159.0/255), blue=(223.0/255))

        box_height = 22.094488188976385

        # Initialize the y-coordinate
        y = A4[1]

        # Constants for padding
        left_padding = 20  # Left padding
        right_padding = 20  # Right padding

        # Calculate the available drawing area
        drawing_width = A4[0] - left_padding - right_padding
        drawing_height = A4[1]

        # Draw the grid
        for section_index, section in enumerate(layout):
            rows = section['rows']
            section_height = drawing_height * section['height']
            cell_height = section_height  # since each section has one row
            y -= cell_height  # Move down the page by one cell

            x = left_padding  # Start drawing from the left padding

            for col_index, col in enumerate(section['cols']):
                cell_width = drawing_width * col['width']
                c.rect(x, y, cell_width, cell_height, stroke=0)  # Draw the cell

                # Insert an image in the first column of the first row
                if section_index == 0 and col_index == 0 and 'image' in col:
                	#pass
                    image_path = col['image']
                    desired_width, desired_height = resize_image(image_path, 225)

                    x_offset = (cell_width - desired_width) / 2  # Calculate the x-coordinate offset for centering
                    y_offset = (cell_height - desired_height) / 2  # Calculate the y-coordinate offset for centering

                    x_position = x + x_offset  # Calculate the x-coordinate for centering
                    y_position = y + y_offset  # Calculate the y-coordinate for centering

                    c.drawImage(image_path, x_position, y_position, width=desired_width, height=desired_height, preserveAspectRatio=True)

                # Writing text in the second column of the first row
                if section_index == 0 and col_index == 1:
                    text = 'The Calgary Zoological Society<br />1300 Zoo Road NE<br />Calgary, AB T2E 7V6<br /><u><font color="blue"><link href="http://www.calgaryzoo.com">www.calgaryzoo.com</link></font></u>'
                    style = ParagraphStyle(name='Text', fontSize=8, leading=14, textColor='black', allowWidows=1, allowOrphans=1,
                                           alignment=1, vAlign='MIDDLE')
                    p = Paragraph(text, style)
                    p.wrap(cell_width - 20, cell_height - 20)
                    p.drawOn(c, x + 10, y + 15)

                # Writing text in the first column of the second row
                if section_index == 1 and col_index == 0:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'This is your ticket for : ')

                # Adding a text box in the second column of the second row
                if section_index == 1 and col_index == 1:
                    form = c.acroForm
                    form.textfield(name=name, fillColor=zoo_blue, x=x + 10, y=y+2 , width=cell_width - 20, height=box_height)

                if section_index == 2 and col_index == 0:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'Date : ')

                if section_index == 2 and col_index == 1:
                    form = c.acroForm
                    form.textfield(name=date, fillColor=zoo_blue, x=x + 10, y=y+2 , width=cell_width - 20, height=box_height)

                if section_index == 2 and col_index == 2:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'Time : ')

                if section_index == 2 and col_index == 3:
                    form = c.acroForm
                    form.textfield(name=time, fillColor=zoo_blue, x=x + 10, y=y+2 , width=cell_width - 20, height=box_height)

                if section_index == 3 and col_index == 0:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'Price Type : ')

                if section_index == 3 and col_index == 1:
                    form = c.acroForm
                    form.textfield(name=ticket_type, fillColor=zoo_blue, x=x + 10, y=y+2, width=cell_width - 20, height=box_height)

                if section_index == 3 and col_index == 2:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'Price : ')

                if section_index == 3 and col_index == 3:
                    form = c.acroForm
                    form.textfield(name=price, fillColor=zoo_blue, x=x + 10, y=y+2 , width=cell_width - 20, height=box_height)

                if section_index == 4 and col_index == 0:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'Order Date :')

                if section_index == 4 and col_index == 1:
                    form = c.acroForm
                    form.textfield(name=order_date, fillColor=zoo_blue, x=x + 10, y=y+2 , width=cell_width - 20, height=box_height)

                if section_index == 4 and col_index == 2:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'Order # :')

                if section_index == 4 and col_index == 3:
                    form = c.acroForm
                    form.textfield(name=order_number, fillColor=zoo_blue, x=x + 10, y=y+2 , width=cell_width - 20, height=box_height)

                if section_index == 5 and col_index == 0:
                    c.drawString(x + 10, (y + cell_height / 2) - 5, 'Location : ')
            
                if section_index == 5 and col_index == 1:
                    form = c.acroForm
                    form.textfield(name=location, fillColor=zoo_blue, x=x + 6, y=y+2 , width=cell_width - 20, height=box_height)
                    
                if section_index == 5 and col_index == 2:
                    if custom_1 == "":
                        pass
                    else:
                        c.drawString(x + 10, (y + cell_height / 2) - 5, custom_1.split(',')[0])
                    
                if section_index == 5 and col_index == 3:
                    if custom_1 == "":
                        pass
                    else:
                        form = c.acroForm
                        form.textfield(name=custom_1.split(',')[1], fillColor=zoo_blue, x=x + 10, y=y, width=cell_width - 20, height=box_height)
                    
                if section_index == 6 and col_index == 0:
                    form = c.acroForm
                    section_width = layout[section_index]['cols'][col_index]['width'] * drawing_width
                    x_position = x + (section_width - 100) / 2
                    form.textfield(name=barcode, fillColor=zoo_blue, x=x_position, y=y+10, width=100, height=box_height*3)
                
                if section_index == 7 and col_index == 0:
                    text = text_field_1
                    style = ParagraphStyle(name='Text', fontSize=9, leading=14, textColor='black', allowWidows=1, allowOrphans=1,
                                           alignment=1, vAlign='TOP')
                    p = Paragraph(text, style)
                    p.wrap(cell_width - 20, cell_height - 20)
                    p.drawOn(c, x + 10, y + cell_height - p.height)
            
                if section_index == 8 and col_index == 0:
                    text = text_field_2
                    style = ParagraphStyle(name='Text', fontSize=9, leading=14, textColor='black', allowWidows=1, allowOrphans=1,
                                           alignment=1, vAlign='TOP')
                    p = Paragraph(text, style)
                    p.wrap(cell_width - 20, cell_height - 20)
                    p.drawOn(c, x + 10, y + cell_height - p.height)
                    
            
                if section_index == 9 and col_index == 0:
                    text = text_field_3
                    style = ParagraphStyle(name='Text', fontSize=9, leading=14, textColor='black', allowWidows=1, allowOrphans=1,
                                           alignment=0, vAlign='TOP', fontName='Helvetica')
                    p = Paragraph(text, style)
                    p.wrap(cell_width - 20 , cell_height - 20)
                    p.drawOn(c, x+10, y)
                    
            
                if section_index == 10 and col_index == 0:
                    text = text_field_4 + """<br /> __________________________________________________________________________"""
                    style = ParagraphStyle(name='Text', fontSize=9, leading=14, textColor='black', allowWidows=1, allowOrphans=1,
                                           alignment=1, vAlign='TOP')
                    p = Paragraph(text, style)
                    p.wrap(cell_width - 20, cell_height - 20)
                    p.drawOn(c, x + 10, y + cell_height - p.height - 10)
                    
            
                if section_index == 11 and col_index == 0:
                    text = text_field_5
                    style = ParagraphStyle(name='Text', fontSize=9, leading=14, textColor='black', allowWidows=1, allowOrphans=1,
                                           alignment=0, vAlign='TOP')
                    p = Paragraph(text, style)
                    p.wrap(cell_width - 20, cell_height - 20)
                    p.drawOn(c, x + 10, y + cell_height - p.height- 20)

                x += cell_width  # Move to the right by one cell

        c.showPage()
        c.save()

        # Close the PDF object cleanly, and ensure we've written everything out to the buffer.
        buffer.seek(0)
        # Create a FileResponse with the PDF data in the buffer, setting the correct MIME type
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')