import datetime
from django.db import connection
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Times-New-Roman', 'TIMES.ttf'))
pdfmetrics.registerFont(TTFont('Times-New-Roman-Bold', 'TIMESBD.ttf'))


def get_concert_data_for_band_revenue(band_name):
    current_date = datetime.date.today()
    quarter_start, quarter_end = get_current_quarter_dates(current_date)

    query = """
    SELECT concert_date, concert_start_time, concert_end_time, concert_hall.concert_hall_name, 
           music_band.music_band_name, concert_hall.quantity_of_people, 
           concert_hall.avg_ticket_price, concert_hall.ticket_revenue_percent 
    FROM concert_program 
    JOIN music_band ON concert_program.music_band = music_band.music_band_id 
    JOIN concert_hall ON concert_program.concert_hall = concert_hall.concert_hall_id 
    WHERE music_band.music_band_name = %s AND concert_date BETWEEN %s AND %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [band_name, quarter_start, quarter_end])
        rows = cursor.fetchall()

    return rows

def get_concert_data_for_hall_concert(hall_name):
    current_date = datetime.date.today()
    quarter_start, quarter_end = get_current_quarter_dates(current_date)

    query = """
    SELECT concert_date, concert_start_time, concert_end_time, music_band.music_band_name 
    FROM concert_program 
    JOIN music_band ON concert_program.music_band = music_band.music_band_id 
    JOIN concert_hall ON concert_program.concert_hall = concert_hall.concert_hall_id 
    WHERE concert_hall.concert_hall_name = %s AND concert_date BETWEEN %s AND %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [hall_name, quarter_start, quarter_end])
        rows = cursor.fetchall()

    return rows

def get_concert_data_for_band_concert(band_name):
    current_date = datetime.date.today()
    quarter_start, quarter_end = get_current_quarter_dates(current_date)

    query = """
    SELECT concert_date, concert_start_time, concert_end_time, concert_hall.concert_hall_name 
    FROM concert_program 
    JOIN music_band ON concert_program.music_band = music_band.music_band_id 
    JOIN concert_hall ON concert_program.concert_hall = concert_hall.concert_hall_id 
    WHERE music_band.music_band_name = %s AND concert_date BETWEEN %s AND %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, [band_name, quarter_start, quarter_end])
        rows = cursor.fetchall()

    return rows

def get_current_quarter_dates(current_date):
    quarter = (current_date.month - 1) // 3 + 1
    quarter_start_month = 3 * quarter - 2
    quarter_end_month = 3 * quarter
    quarter_start = datetime.date(current_date.year, quarter_start_month, 1)
    if quarter_end_month == 12:
        quarter_end = datetime.date(current_date.year, 12, 31)
    else:
        quarter_end = datetime.date(current_date.year, quarter_end_month + 1, 1) - datetime.timedelta(days=1)
    return quarter_start, quarter_end

def generate_pdf(concerts, band_name):
    pdf_file = f"{band_name}_payment_report.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    c.setFont("Times-New-Roman", 14)
    c.drawString(1 * inch, 10.5 * inch, f"Payment Report for {band_name}")

    c.setFont("Times-New-Roman", 12)
    c.drawString(1 * inch, 10 * inch, "Concert Date")
    c.drawString(2.5 * inch, 10 * inch, "Start Time")
    c.drawString(4 * inch, 10 * inch, "End Time")
    c.drawString(5.5 * inch, 10 * inch, "Venue")
    c.drawString(7 * inch, 10 * inch, "Revenue")

    y = 9.5 * inch
    total_revenue = 0

    for concert in concerts:
        concert_date, start_time, end_time, hall_name, band_name, quantity, price, percent = concert
        revenue = quantity * price * (1 - percent / 100)
        total_revenue += revenue

        c.drawString(1 * inch, y, str(concert_date))
        c.drawString(2.5 * inch, y, str(start_time))
        c.drawString(4 * inch, y, str(end_time))
        c.drawString(5.5 * inch, y, hall_name)
        c.drawString(7 * inch, y, f"{revenue:,.2f} RUB")

        y -= 0.5 * inch
        if y < 1 * inch:
            c.showPage()
            c.setFont("Times-New-Roman", 12)
            y = 10 * inch

    c.setFont("Times-New-Roman-Bold", 12)
    c.drawString(1 * inch, y - 0.5 * inch, f"Total Revenue: {total_revenue:,.2f} RUB")

    c.save()
    return pdf_file

def generate_band_concerts_pdf(concerts, band_name):
    pdf_file = f"{band_name}_concert_program.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    c.setFont("Times-New-Roman", 14)
    c.drawString(1 * inch, 10.5 * inch, f"Concert Program for {band_name} for the Quarter")

    c.setFont("Times-New-Roman", 12)
    c.drawString(1 * inch, 10 * inch, "Concert Date")
    c.drawString(2.5 * inch, 10 * inch, "Start Time")
    c.drawString(4 * inch, 10 * inch, "End Time")
    c.drawString(5.5 * inch, 10 * inch, "Venue")

    y = 9.5 * inch
    concert_count = 0

    for concert in concerts:
        concert_date, start_time, end_time, hall_name = concert

        c.drawString(1 * inch, y, str(concert_date))
        c.drawString(2.5 * inch, y, str(start_time))
        c.drawString(4 * inch, y, str(end_time))
        c.drawString(5.5 * inch, y, hall_name)

        y -= 0.5 * inch
        concert_count += 1
        if y < 1 * inch:
            c.showPage()
            c.setFont("Times-New-Roman", 12)
            y = 10 * inch

    c.setFont("Times-New-Roman-Bold", 12)
    c.drawString(1 * inch, y - 0.5 * inch, f"Total number of concerts: {concert_count}")

    c.save()
    return pdf_file

def generate_hall_concerts_pdf(concerts, hall_name):
    pdf_file = f"{hall_name}_concert_program.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    c.setFont("Times-New-Roman", 14)
    c.drawString(1 * inch, 10.5 * inch, f"Concert Program for {hall_name} for the Quarter")

    c.setFont("Times-New-Roman", 12)
    c.drawString(1 * inch, 10 * inch, "Concert Date")
    c.drawString(2.5 * inch, 10 * inch, "Start Time")
    c.drawString(4 * inch, 10 * inch, "End Time")
    c.drawString(5.5 * inch, 10 * inch, "Music Band")

    y = 9.5 * inch
    concert_count = 0

    for concert in concerts:
        concert_date, start_time, end_time, band_name = concert

        c.drawString(1 * inch, y, str(concert_date))
        c.drawString(2.5 * inch, y, str(start_time))
        c.drawString(4 * inch, y, str(end_time))
        c.drawString(5.5 * inch, y, band_name)

        y -= 0.5 * inch
        concert_count += 1
        if y < 1 * inch:
            c.showPage()
            c.setFont("Times-New-Roman", 12)
            y = 10 * inch

    c.setFont("Times-New-Roman-Bold", 12)
    c.drawString(1 * inch, y - 0.5 * inch, f"Total number of concerts: {concert_count}")

    c.save()
    return pdf_file
