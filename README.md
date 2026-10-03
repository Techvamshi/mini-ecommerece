# Healthify (Django, black & white)

1. Copy your six images into `shop/static/shop/images/`:
   fresh_fruits.jpg, green_smoothie.jpg, mixed_nuts.jpg, oats_bowl.jpg, quinoa_salad.jpg, wheat_bread.jpg
2. Run:

       python -m venv venv
       source venv/bin/activate        # Windows: venv\Scripts\activate
       pip install -r requirements.txt
       python manage.py migrate        # also loads the 6 sample products
       python manage.py runserver

Open http://127.0.0.1:8000/

Products are managed only in the admin panel (/admin/) - run `python manage.py createsuperuser` first.
Images are shown in grayscale to keep the UI black and white (remove `filter: grayscale(1)` in style.css for colour).
