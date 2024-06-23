# Smart Attendance Manager and Report Generator

[click here](https://www.canva.com/design/DAGI9PXhI6E/ylUTncClPBISO625V8HQWQ/edit?utm_content=DAGI9PXhI6E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) to view the presentation of the working project.

This is a smart attendance manager and report generator, designed to streamline the attendance tracking process for educational institutions. It provides various user roles such as student, faculty, class teacher, and admin, each with specific functionalities to manage attendance and generate reports. The application is built using Python Django for the backend, and HTML, CSS, Bootstrap, and JavaScript for the frontend.


## Features

- **Student**
  - View attendance for all courses.
  - Receive notifications if listed as defaulters for any course.
  - Log in using the provided username and password.

- **Faculty**
  - Perform CRUD operations on attendance for multiple classes.
  - Log in using the provided username and password.

- **Class Teacher**
  - Download comprehensive reports for the entire class.
  - Reports include the percentage of attendance for every student in every course.
  - Log in using the provided username and password.

- **Admin**
  - Add new departments, faculty, students, courses, and more.
  - Access all functionalities available to other user roles.
  - Log in using the provided username and password.

## Technologies Used

- Backend: Python Django
- Frontend: HTML, CSS, Bootstrap, JavaScript

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python and Django installed.
3. Set up a virtual environment (optional but recommended).
4. Install the project dependencies by running `pip install -r requirements.txt`.
5. Set up the database by running `python manage.py migrate`.
6. Start the development server with `python manage.py runserver`.
7. Access the application in your browser at `http://localhost:8000`.


## Sample Usernames and Passwords

- Student:
  - Student ID: 2021300079
  - Password: 12345678

- Faculty:
  - Faculty ID: 01
  - Password: 12345678

- Class Teacher:
  - Username: 01
  - Password: 12345678

