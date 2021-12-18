# BarbersFlo

![home page all screen sizes](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/website-different-viewports.JPG)

[Link to deployed website](https://barbers-flo.herokuapp.com/)

BarbersFlo is a barbershop located in Galway City - Ireland.
On the website guests and registered users can make reservations choosing the date, time and type of treatment, selecting their favourite barber and paying for their reservation.


# Table Of Contents

-   [User Experience](#user-experience)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Testing](#testing)
-   [Deployment](#deployment)
-   [Credits](#credits)

## User Experience

-   [User Stories](#user-stories)
-   [The Scope Plane](#the-Scope-plane)
-   [The Structure Plane](#the-structure-plane)
-   [The Surface Plane](#the-surface-plane)


### User Stories

The purpose of the website is for users to make reservations with their favourite barber, at their selected time and date, for the treatment they want.
Treatments will have all the relevant information (duration, price, description).
Barbers will have a short description highlighting what they are specialised in.

| User Story ID |     AS A/AN    |                        I WANT TO BE ABLE TO...                       |                                      SO THAT I CAN...                                      |
|:--------------|:---------------|:---------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
|             1 | Customer/Guest | View a list of treatments                                            | Select the one that I want to book                                                         |
|             2 | Customer/Guest | View a calendar of available dates                                   | Select the one that I want to book                                                         |
|             3 | Customer/Guest | View a list of barbers                                               | Make a booking with my favourite one                                                       |
|             4 | Customer/Guest | View a list of available times                                       | Select the one that I want to book                                                         |
|             5 | Guest          | Easily register for an account                                       | Have a personal account and be able to view my profile                                     |
|             6 | Customer       | Easily login or logout                                               | Access my personal account information                                                     |
|             7 | Customer       | Easily recover my password in case I forget it                       | Recover access to my account                                                               |
|             8 | Customer       | Receive an email confirmation after registering                      | Verify that my account registration was successful                                         |
|             9 | Customer       | See the list of my past appointments                                 | View my personal booking history                                                           |
|            10 | Customer/Guest | Easily select the treatment, date, time and barber of my reservation | Ensure I don't accidentally select the wrong treatment, date, time and barber              |
|            11 | Customer/Guest | Easily enter my payment information                                  | Check out quickly and with no hassles                                                      |
|            12 | Customer/Guest | Feel my personal and payment information is safe and secure          | Confidently provide the needed information to make a booking                               |
|            13 | Customer/Guest | View an order confirmation after checkout                            | Verify that I haven't made any mistakes                                                    |
|            14 | Customer/Guest | Receive an email confirmation after checking out                     | Keep the confirmation of what I've booked for my records                                   |
|            15 | Shop Owner     | Add a type of treatment                                              | Make a new treatment available for booking                                                 |
|            16 | Shop Owner     | Edit/update a treatment                                              | Change treatments prices, descriptions, images and durations                               |
|            17 | Shop Owner     | Delete a treatment                                                   | Remove treatments that are no longer offered                                               |
|            18 | Shop Owner     | Add a barber                                                         | Make new hires available for booking                                                       |
|            19 | Shop Owner     | Edit/update a barber                                                 | Change an employee picture and start/end times                                             |
|            20 | Shop Owner     | Delete a barber                                                      | Make sure that people who are no longer part of the staff can't be booked for appointments |
|            21 | Shop Owner     | See a specific day's list of reservations                            | Organise the work for that day                                                             |

### The Scope Plane

Users want to be able to make a reservation with their favourite barber, at their preferred time and date, in just a few minutes.
The shop owner wants to be able to manage (add/edit/delete) treatments and barbers from the online booking system, so that their customers can only book what's available, and have all the relevant information about the session they're booking.

### The Structure Plane

The website will have the following structure for visitors (not users):
- Log-in/Register: allows the visitor to either log-in or register as a new user
- Book-now: allows users to make a reservation:
	- step 1: select treatment
	- step 2: select date
	- step 3: select barber
	- step 4: select time

On top of these pages, a user will have access to:
- My Profile: from this page, a user can manage their profile information (ph. number, first and last name) and see the last 5 reservations they've made.
- Log-out: used to simply log-out of the current session

An admin user will also have access to:
- Treatments Management: this section will allow them to create, update or delete treatments
- Barbers Management: this section will allow them to create, update or delete barbers
- Reservations: this section will allow them to see a specific day's list of reservations

The Database structure is as follows:
![DB Schema](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/db-schema.png)
- For each User, the system creates a new UserProfile (1-1 relationship) to store additional information
- Each Reservation is connected to 1 Treatment (many-1), 1 Barber (many-1) and 1 UserProfile (many-1)
- Each Availability is connected to 1 Barber (many-1)

- [Home Page Wireframe](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/home-page-wireframe.png)

### The Surface Plane

The color palette of the website will be:
![Color Palette](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/color-palette.png)
The overall look is inspired by the website [Tweed Barbers](https://tweedbarbers.com/)

## Features

-   [Existing Features](#existing-features)
-   [Features Left to Implement](#features-left-to-implement)
 
### Existing Features

| User Story ID |     AS A/AN    |                        I WANT TO BE ABLE TO...                       |                                             FEATURE                                             |
|:--------------|:---------------|:---------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
|             1 | Customer/Guest | View a list of treatments                                            | Any user can see the list of treatments by going to the Book Now section                        |
|             2 | Customer/Guest | View a calendar of available dates                                   | Any user can see the list of available dates by going to the Book Now section                   |
|             3 | Customer/Guest | View a list of barbers                                               | Any user can see the list of barbers by going to the Book Now section                           |
|             4 | Customer/Guest | View a list of available times                                       | Any user can see the list of available times by going to the Book Now section                   |
|             5 | Guest          | Easily register for an account                                       | Guests can register from the Register section                                                   |
|             6 | Customer       | Easily login or logout                                               | Customers can log-in / log-out from the log-in / log-out sections of the website                |
|             7 | Customer       | Easily recover my password in case I forget it                       | Customers can reset their password by clicking on the Forgot Password? button                   |
|             8 | Customer       | Receive an email confirmation after registering                      | A confirmation email is sent to the customer after registering                                  |
|             9 | Customer       | See the list of my past appointments                                 | From the My Profile page a customer can see their 5 most recent reservations                    |
|            10 | Customer/Guest | Easily select the treatment, date, time and barber of my reservation | Customers can go to the Book Now section and easily select Treatment, Date, Barber and Time     |
|            11 | Customer/Guest | Easily enter my payment information                                  | At the last step of the booking process, the user can enter their CC details                    |
|            12 | Customer/Guest | Feel my personal and payment information is safe and secure          | The payment is processed via Stripe which is PCI compliant Level 1 (highest)                    |
|            13 | Customer/Guest | View an order confirmation after checkout                            | After checkout, the customer is redirected to a confirmation page with the order confirmation   |
|            14 | Customer/Guest | Receive an email confirmation after checking out                     | After checkout, the customer receives a confirmation email                                      |
|            15 | Shop Owner     | Add a type of treatment                                              | From the management section, the shop owner can create new treatments                           |
|            16 | Shop Owner     | Edit/update a treatment                                              | From the management section, the shop owner can edit existing treatments                        |
|            17 | Shop Owner     | Delete a treatment                                                   | From the management section, the shop owner can delete existing treatments                      |
|            18 | Shop Owner     | Add a barber                                                         | From the management section, the shop owner can create new barbers                              |
|            19 | Shop Owner     | Edit/update a barber                                                 | From the management section, the shop owner can edit existing barbers                           |
|            20 | Shop Owner     | Delete a barber                                                      | From the management section, the shop owner can delete existing barbers                         |
|            21 | Shop Owner     | See a specific day's list of reservations                            | From the management section, the shop owner can see the list of reservations for a specific day |


### Features Left to Implement

For simplicity, the current booking system only allows to make a reservation for 1-30 days from the current date.
These should be customisable settings, but would also involve additional checks to avoid for example same day bookings for past times.
Also, allowing bookings for more than 30 days in the future would mean increasing exponentially the number of slots in the booking-availabilities table of the database, which would make queries less performing and this would be beyond the scope of this project. 
It would also be useful to implement a functionality to manage the calendar of the shop, marking barbers as off/sick or closed for bank holidays etc.


## Technologies Used

### Languages and Frameworks

- HTML for the basic structure of the website
- CSS for some custom styling of the website
- [JQuery](https://code.jquery.com/) to initiate some interactive elements of the bootstrap framework
- [Bootstrap](https://getbootstrap.com/) v5.1 for some pre-formatted styling
- [Django](https://www.djangoproject.com/) high-level Python web framework for back-end development
- [Python] language used for back-end development



### Applications

- [Gitpod](https://gitpod.io/) to develop the project
- [GitHub](https://github.com/) for version control
- [Heroku](https://www.heroku.com) to deploy the project
- [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler) to implement a daily job that creates slots for the calendar
- [Heroku Postgres](https://www.heroku.com/postgres) for the database of the deployed version on Heroku
- [Balsamiq](https://balsamiq.com/) for the wireframe of this readme.md file
- [Photopea](https://www.photopea.com/) for image editing
- [Fontawesome](https://fontawesome.com/) for the use of icons
- [Stripe](https://stripe.com/) for the payment system
- [AWS](https://aws.amazon.com/) for hosting the media used on the website
- [Tables Generator](https://www.tablesgenerator.com) to generate the tables in markdown language used in this readme
- [Coolors](https://coolors.co/) to generate the color palette used in this readme
- [DBDiagram](https://dbdiagram.io/) to generate the database schema for this readme

## Testing

The application functionalities were tested in three different scenarios:

1. Visitor
	- As a visitor, I was able to complete a reservation
		- the Stripe test card number is 4242 4242 4242 4242, any future exp. date, any CVC
	- After completing the reservation, I received the confirmation email
	- When trying to access the management pages or the profile page as a normal visitor, I am redirected to the login page
	- As a visitor I can register as a new user from the Register page

2. User
	- As a user, I can access using the login page and sign out using the logout page 
    - As a normal user, I was able to complete a reservation
	- After completing the reservation, I received the confirmation email
	- When trying to access the management pages as a normal visitor, I am redirected to the home page with an error message
	- I can access the My Profile page, see the list of up to 5 most recent reservations and update my details
	
3. Admin
	- As a user, I can access using the login page and sign out using the logout page
    - As an admin user I can make a reservation
	- As an admin user I can update my contact details
	- As an admin user I can access all pages of the website
	- As an admin user I can create/edit/delete barbers
	- As an admin user I can create/edit/delete treatments
	- If a treatment is deleted, reservations with that treatment have the field set to NULL
	- If a barber is deleted, reservations with that barber have the field set to NULL

I used the following validators to check my HTML, CSS and JavaScript code:

[HTML Validator](https://validator.w3.org/)
[CSS Validator](https://jigsaw.w3.org/css-validator/)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

They were both used on all the following pages:
- https://barbers-flo.herokuapp.com/
- https://barbers-flo.herokuapp.com/accounts/login/
- https://barbers-flo.herokuapp.com/accounts/signup/
- https://barbers-flo.herokuapp.com/booking/
- https://barbers-flo.herokuapp.com/booking/1/
- https://barbers-flo.herokuapp.com/booking/1/2022-01-14
- https://barbers-flo.herokuapp.com/booking/1/2022-01-14/3
- https://barbers-flo.herokuapp.com/checkout/1/3/3713/
- https://barbers-flo.herokuapp.com/checkout/checkout-success/12
- https://barbers-flo.herokuapp.com/profile/
- https://barbers-flo.herokuapp.com/management/reservations/
- https://barbers-flo.herokuapp.com/management/new_treatment/
- https://barbers-flo.herokuapp.com/management/get_treatment/
- https://barbers-flo.herokuapp.com/management/new_barber/
- https://barbers-flo.herokuapp.com/management/get_barber/

[JS Validator](https://jshint.com/)

[PEP8 Validator](http://pep8online.com/)

### Bugs

- When the project was started the file structure was incorrect (barbers > barbers_flo > Apps instead of barbers > Apps). The project was working fine in development but didn't work correctly once deployed because of this bug. Fixed by correcting the file structure.
- The function that makes new availability slots if needed was called every time the calendar page was loaded. If the page was loaded twice in a short timeframe, availability slots would have been created twice.
The same function was moved to a separate custom command that is run daily by Heroku Scheduler. Also, the function initially created the same slots for all barbers, so a newly created barber would only have availability slots for the end of the calendar.
- Wrongly named the constant EMAIL_HOST_PASSWORD caused emails not to be sent. Correcting the constant name fixed the issue.
- The reservations page for superusers had the date field set to gg/mm/yyyy once a date was submitted. This was due to the format of a variable (expected date, passed string instead).
- The logic of the booking system was incorrect as it would allow to book 2+ consecutive slots (e.g. for a treatment lasting 1 hour) even if only 30 minutes were available. Changed the logic to show available slots based on the duration of the chosen treatment.

## Deployment

[Link to deployed website](https://barbers-flo.herokuapp.com/)

This project was developed using GitPod, pushed to GitHub and deployed using Heroku.

To deploy to Heroku from the GitHub repository, the following steps were taken:

1. Go to heroku.com and log in
2. Click on "Create new app"
3. Go to Deploy > Deployment method > Github
4. Go to Settings > Config vars and add variables
5. Git add / commit / push Procfile and requirements.txt files
6. Enable automatic deployments from Heroku
7. Click on Deploy branch
8. Create a public bucket in Amazon Web Services (AWS) S3
9. Create user, user group and policy in AWS to allow access to the bucket 
10. Add Config Vars in Heroku to use user's credentials to access AWS

### How to run this project locally

To clone this project into Gitpod you will need:

1. A Github account
2. Use the Chrome browser

Then follow these steps:

1. Install the Gitpod Browser Extension for Chrome
2. After installation, restart the browser
3. Log into Gitpod with your gitpod account
4. Navigate to the Project GitHub repository
5. Click the green GitPod button in the top right corner of the repository
6. This will trigger a new gitpod workspace to be created

To work on the project code within a local IDE such as VSCode, Pycharm etc:

1. Follow this link to the [GitHub repository](https://github.com/matteofiorini92/barbers)
2. Click on the Code button
3. In the drop-down, copy the URL that you see in the HTTPs tab
4. In your local IDE, open the terminal
5. Change the current working directory to the location where you want the cloned directory to be made
6. Type git clone and paste the URL you copied in Step 3
7. Press Enter. Your local clone will be created.

## Credits
The content of the deployment section of this readme.md was mostly taken from [this webinar](https://www.youtube.com/watch?v=7BteidgLAyM).
The steps of the booking system are inspired by the [Resurva](https://resurva.com/) booking system for barbers used by these two websites:
The treatments name and description are inspired by [this website](https://tweedbarbers.com/)
- [CutThroat](https://cutthroatbarbershop.resurva.com/)
- [Turk's](https://turksbarbershop.ie/)


### Images
- For images and icons I used [Unsplash](https://unsplash.com/) and [Iconfinder](https://www.iconfinder.com/)
