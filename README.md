### Usage

1. Download the project
   > git clone  https://github.com/Ma4eteS/PaySystemDjango
2. Create a [stripe](https://dashboard.stripe.com/test/dashboard) account, get and put your STRIPE_PUBLISHABLE_KEY and STRIPE_SECRET_KEY in .env file or set it as env variables
3. Install [docker](https://docs.docker.com/engine/install/ubuntu/#set-up-the-repository)
4. Run command to start containers:
   > sudo docker compose up
5. Add a superuser in your database
   > docker exec -it paysystemdjango-web-1 bash
   >
   > python manage.py createsuperuser

Quit the container with press ctrl+p, ctrl+q

6. Go to your [admin page](http://0.0.0.0:8000/admin/stripe_api/item/) and add a couple of items

7. Add the same items in your [stripe account](https://dashboard.stripe.com/test/products/)

9. Test payment system of [your shop](http://0.0.0.0:8000/) 
