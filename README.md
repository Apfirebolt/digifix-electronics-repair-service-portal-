# A Web Application for a imaginary company called 'Digifix' which facilitates door to door repairing of your gadgets through online portal.

'Digifix' has an online portal where you can register and ask for a service request mentioning the type of gadget you have in possession which requires to be serviced. You can upload images of the same while registering service request.

When you request would be opened by admins, they'd assign you a reference ID and would assign a suitable engineer according to the type of problem and the device you have. Digifix would sent people at your doorstep to pick up the device. Though this reference ID you can keep track of your service request and how long would it take. A thread would be opened where you can contact with the engineer assigned to your task, post comments and pictures. After it's done and the product is returned to you, you can write a review of the service provided as 'testimonial'. Other auxiliary features like updating your account settings are provided.

This project uses custom authentication system in Django made by extending base user class. It has full CRUD functionality on user testimonials and multiple addresses which can be added for correspondence.

This project does not use any popular CSS framework, instead a custom mini framework is created entirely in CSS without using SCSS/SASS.

## Getting Started

* Create a new virtual environment and install packages specified in the requirements.txt file.

* Hook in your database of choice, make necessary database changes in the settings.py file inside the project folder. Obviously, some familiarity with Django folder structures is required for this. By default this project uses MySQL as database.

* Make migrations when you're done with the database settings and migrate.
* Run python manage.py runserver, and the application should be running on port 8000 by default.

* Please find the screenshots of the application attached below.

## Built With

* [Python Django](https://www.djangoproject.com/)
* [HTML + CSS + SCSS](https://www.w3schools.com/html/html_css.asp)

## Authors

* **Amit Prafulla (APFirebolt)** - (http://amitprafull.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Screenshots

Please find some of the screenshots of the application. Below is the screenshot depicting search pokemon page with
applied filters.

First screenshot of posting a service request.

![alt text](./screenshots/service_request1.PNG)

Another Screenshot of the service request page showing images uploaded related to the current service request. Django form sets are used to facilitate uploading several image instances at a time.

![alt text](./screenshots/service_request2.PNG)

User login page screenshot.

![alt text](./screenshots/user_login.PNG)

Home Page screenshot using custom theme.

![alt text](./screenshots/home_page.PNG)

Screenshot of the dashboard page.

![alt text](./screenshots/dashboard.PNG)

Testimonial page where users write reviews and give 1-5 ratings to the service they received.

![alt text](./screenshots/testimonial.PNG)

Screenshot showing a user changing profile settings from within the app.

 ![alt text](./screenshots/change_settings.PNG)