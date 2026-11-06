import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

pdf_path = 'Brandable-Shopify-Product-Tagging-Guide.pdf'

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=colors.HexColor('#e11d2d'),
    alignment=TA_LEFT,
    spaceAfter=4
)

subtitle_style = ParagraphStyle(
    'DocSubtitle',
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=colors.HexColor('#212121'),
    alignment=TA_LEFT,
    spaceAfter=10
)

desc_style = ParagraphStyle(
    'DocDesc',
    fontName='Helvetica',
    fontSize=9.5,
    leading=14,
    textColor=colors.HexColor('#444444'),
    spaceAfter=12
)

h2_style = ParagraphStyle(
    'H2',
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=17,
    textColor=colors.HexColor('#212121'),
    spaceBefore=12,
    spaceAfter=6
)

table_header_style = ParagraphStyle(
    'TableHeader',
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=12,
    textColor=colors.white,
    alignment=TA_LEFT
)

table_body_style = ParagraphStyle(
    'TableBody',
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor('#212121')
)

tag_code_style = ParagraphStyle(
    'TagCode',
    fontName='Courier-Bold',
    fontSize=9.5,
    leading=12,
    textColor=colors.HexColor('#e11d2d')
)

step_num_style = ParagraphStyle(
    'StepNum',
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=colors.HexColor('#e11d2d')
)

step_text_style = ParagraphStyle(
    'StepText',
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=colors.HexColor('#333333')
)

elements = []

# Page 1: Header & Master Table
elements.append(Paragraph('BRANDABLE &bull; Corporate Gifting', title_style))
elements.append(Paragraph('Shopify Product Tagging & Category Management Guide', subtitle_style))
elements.append(HRFlowable(width='100%', thickness=2, color=colors.HexColor('#e11d2d'), spaceAfter=10))

elements.append(Paragraph(
    '<b>Purpose of this Guide:</b> To make each section of your store show only its specific products, simply add the corresponding <b>Tag</b> to your product in Shopify Admin. The theme automatically maps tags to their respective navigation links, category story circles, and builder steps.',
    desc_style
))

headers = [
    Paragraph('Storefront Section', table_header_style),
    Paragraph('Primary Tag to Add', table_header_style),
    Paragraph('Accepted Synonyms', table_header_style),
    Paragraph('Example Items', table_header_style)
]

data = [headers]

rows = [
    ('Executive Combos', 'executive-combos', 'executive, combos, luxury', 'Executive hampers, wine & cheese sets, VIP crates'),
    ('Employee Onboarding', 'employee-onboarding', 'onboarding, welcome, welcome-kit', 'Welcome kits, employee swag, starter sets'),
    ('Drinkware & Bottles', 'drinkware', 'bottle, bottles, flask, tumbler, mug', 'Temperature flasks, insulated bottles, tumblers'),
    ('Diaries & Stationary', 'diaries', 'diary, journal, notebook, stationery, pen', 'Leather journals, executive diaries, pens'),
    ('Apparel & Bags', 'apparel', 'apparel-bags, tshirt, hoodie, backpack', 'Polo t-shirts, branded hoodies, laptop bags'),
    ('Diwali & Festive', 'festive', 'diwali, diwali-festive, holiday', 'Dry fruit boxes, brass diyas, celebration crates'),
    ('Tech & Smart Gadgets', 'tech', 'tech-audio, gadgets, powerbank', 'Bluetooth speakers, wireless chargers, powerbanks'),
    ('Artisan Chocolates & Tea', 'gourmet', 'chocolates, treats, tea', 'Handcrafted Belgian chocolates, artisan coffees'),
    ('Eco & Wellness', 'eco', 'wellness, plants, bamboo', 'Air-purifying desk plants, bamboo sets, candles'),
    ('Custom Box: Packaging (Step 1)', 'custom:packaging', 'packaging', 'Rigid magnetic gift boxes, wooden crates'),
    ('Custom Box: Goodies (Step 2)', 'custom:box_item', 'box_item, goodie', 'Individual items available to put in box')
]

for section, tag, syns, ex in rows:
    data.append([
        Paragraph(f'<b>{section}</b>', table_body_style),
        Paragraph(f'<b>{tag}</b>', tag_code_style),
        Paragraph(syns, table_body_style),
        Paragraph(ex, table_body_style)
    ])

col_widths = [125, 120, 115, 160]
t = Table(data, colWidths=col_widths, repeatRows=1)
t.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e11d2d')),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('TOPPADDING', (0, 0), (-1, 0), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e0e0e0')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fcfcfc')]),
    ('TOPPADDING', (0, 1), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
]))

elements.append(t)
elements.append(Spacer(1, 14))

# Page 2: Step-by-Step Instructions & Best Practices
elements.append(PageBreak())

elements.append(Paragraph('How to Add Product Tags in Shopify Admin (5 Quick Steps)', h2_style))
elements.append(HRFlowable(width='100%', thickness=1, color=colors.HexColor('#e0e0e0'), spaceAfter=10))

steps_data = [
    [Paragraph('<b>Step 1</b>', step_num_style), Paragraph('Log in to your <b>Shopify Admin</b> panel (e.g. <code>https://admin.shopify.com</code>).', step_text_style)],
    [Paragraph('<b>Step 2</b>', step_num_style), Paragraph('In the left navigation menu, click <b>Products</b> &rarr; <b>All products</b>, then click the product you wish to organize (or click <b>Add product</b>).', step_text_style)],
    [Paragraph('<b>Step 3</b>', step_num_style), Paragraph('On the right-hand sidebar, scroll down to the <b>Product organization</b> card and locate the <b>Tags</b> field.', step_text_style)],
    [Paragraph('<b>Step 4</b>', step_num_style), Paragraph('Type the exact tag (for example: <font color="#e11d2d"><b>drinkware</b></font>) and press <b>Enter</b> on your keyboard so it appears as a tag pill.', step_text_style)],
    [Paragraph('<b>Step 5</b>', step_num_style), Paragraph('Click <b>Save</b> at the top-right corner of the page. The product will immediately appear in that specific category on the storefront!', step_text_style)]
]

steps_table = Table(steps_data, colWidths=[55, 465])
steps_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LINEBELOW', (0, 0), (-1, -2), 0.5, colors.HexColor('#f0f0f0'))
]))
elements.append(steps_table)
elements.append(Spacer(1, 12))

# Pro Tips Box
elements.append(Paragraph('Pro Tips & Best Practices for Product Organization', h2_style))
elements.append(HRFlowable(width='100%', thickness=1, color=colors.HexColor('#e0e0e0'), spaceAfter=8))

tips_text = [
    '<b>Multiple Tags on One Product:</b> A single product can have multiple tags! For example, a temperature-sensing bottle can have both <code><b>drinkware</b></code> (so it displays in the Drinkware section) and <code><b>custom:box_item</b></code> (so customers can also choose it in the Custom Box Builder).',
    '<b>Custom Box Builder Tags:</b><br/>- Tag boxes with <code><b>custom:packaging</b></code> so they appear in Step 1.<br/>- Tag goodies with <code><b>custom:box_item</b></code> so they appear in Step 2 with quantity selector pills.',
    '<b>Case-Insensitive Matching:</b> The theme is designed to be forgiving: tags like <code>drinkware</code>, <code>Drinkware</code>, or <code>DRINKWARE</code> all match seamlessly.',
    '<b>Instant Real-Time Updates:</b> Once you add a tag and save in Shopify Admin, the storefront immediately reflects the change without any code editing.'
]

for tip in tips_text:
    elements.append(Paragraph(f'&bull; {tip}', desc_style))
    elements.append(Spacer(1, 2))

elements.append(Spacer(1, 10))
elements.append(HRFlowable(width='100%', thickness=1, color=colors.HexColor('#e11d2d'), spaceAfter=8))
elements.append(Paragraph(
    '<b>Brandable Corporate Concierge:</b> Need assistance with catalog setup? Contact <b>corporate@brandable.example.com</b> | Hotline: +91 98765 43210',
    ParagraphStyle('FooterNote', fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor('#777777'), alignment=TA_CENTER)
))

doc.build(elements)
print(f'Successfully generated {pdf_path} ({os.path.getsize(pdf_path)} bytes)')
