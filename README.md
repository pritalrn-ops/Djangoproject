Django Story Generator
Project Objective
This project is a Django web application that generates a short story, a character description, and a combined image based on a user's text prompt. The application is built to fulfill the requirements of the Phase 1 assignment, demonstrating a basic understanding of Django, AI integration, and image manipulation.

Key Features
Web Interface: A simple, clean, and responsive web interface built with Django templates and CSS.

Dynamic Text Generation: Uses a simple rule-based "AI model" to generate unique stories and character descriptions. This approach avoids external API calls, fulfilling the assignment's "free and open-source" requirement.

Image Generation: Uses the Pillow library to create and combine two placeholder images (one for the character, one for the background) into a single scene.

Image Manipulation: Demonstrates image resizing, pasting, and saving to the project's static directory.

Modular Code: The core logic for text generation and image processing is separated into distinct functions for clarity and maintainability.

Project Architecture
The application follows the Django MVT (Model-View-Template) pattern:

Model: No database models were used for this assignment as the data is not persistent.

View (storygen/views.py): This is the core logic of the application. It handles POST requests from the user's form, calls the text and image generation functions, combines the images, and renders the final index.html template with the generated content.

Template (storygen/templates/index.html): This is the front-end of the application. It contains the HTML form for user input and the display area for the generated story, character description, and combined image.

Setup and Installation
Prerequisites
Python 3.8 or higher

pip (Python package installer)

Steps
Clone the Repository: (If applicable, or assume a starting project)
git clone [your_repo_url]
cd [your_project_directory]

Create a Virtual Environment: (Optional but recommended)
python -m venv venv
venv\Scripts\activate (on Windows) or source venv/bin/activate (on macOS/Linux)

Install Dependencies:
pip install -r requirements.txt

Run Migrations:
python manage.py migrate

Start the Development Server:
python manage.py runserver

The application will now be running at http://127.0.0.1:8000/.

Author
Prital Nyamagoud
