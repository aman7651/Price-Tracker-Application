import time
from celery import shared_task
from .models import Item
from tracker.views import crawl_data


@shared_task
def track_for_discount():
    items = Item.objects.all()
    for item in items:
        data = crawl_data(item.url)
        if data['last_price'] < item.requested_price:
            print(f'Discount for {data["title"]}')
            item_discount = Item.objects.get(id=item.id)
            item_discount.discount_price = f'DISCOUNT! The price is {data["last_price"]}'
            item_discount.save()
            send_mail()
@shared_task
                  
def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('aman765180@gmail.com', 'Neesu@123')
        subject = "Price of your Flipkart item has fallen down"
        body = "Hey  \User The price of Flipkart product has reached at your requested price     
           : "
        msg = f"Subject: {subject} \n\n {body} "
        server.sendmail(
            'aman765180@gmail.com',
            'Abhishek7071631646@gmail.com', msg
        )
        ,#print("HEY Rahul, EMAIL HAS BEEN SENT SUCCESSFULLY.")
        server.quit()
        
@shared_task
def track_for_not_discount():
    items = Item.objects.all()
    for item in items:
        data = crawl_data(item.url)
        if data["last_price"] > item.requested_price:
            print(f'Discount finished for {data["title"]}')
            item_discount_finished = Item.objects.get(id=item.id)
            item_discount_finished.discount_price = 'No Discount Yet'
            item_discount_finished.save()

while True:
    track_for_discount()
    time.sleep(10)
    track_for_not_discount()
    time.sleep(10) 

        
