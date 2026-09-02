Sandwich Maker API

A RESTful API for creating, viewing, updating, and deleting sandwich records. The project was built with FastAPI and SQLAlchemy and uses MySQL for persistent data storage. Automated tests are written with pytest.

Features
Create new sandwiches
Retrieve all sandwiches
Retrieve a sandwich by ID
Update existing sandwiches
Delete sandwiches
Persistent data storage with MySQL
SQLAlchemy ORM for database interactions
Automated API testing with pytest
Interactive API documentation through FastAPI
Tech Stack
Python
FastAPI — API framework
SQLAlchemy — ORM and database management
MySQL — relational database
pytest — automated testing
API Endpoints
Method	Endpoint	Description
GET	/sandwiches	Retrieve all sandwiches
GET	/sandwiches/{id}	Retrieve a sandwich by ID
POST	/sandwiches	Create a new sandwich
PUT	/sandwiches/{id}	Update a sandwich
DELETE	/sandwiches/{id}	Delete a sandwich
Example Sandwich
{
  "name": "Turkey Club",
  "bread": "Wheat",
  "protein": "Turkey",
  "cheese": "Cheddar",
  "toppings": ["Lettuce", "Tomato", "Bacon"]
}
Getting Started
1. Clone the repository
git clone https://github.com/ALchemistAero/sandwich-maker-api.git
cd Assignment-5
2. Create a virtual environment
python -m venv venv

Activate the virtual environment:

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure the database

Create a MySQL database and configure the application's database connection with your MySQL credentials.

Example:

DATABASE_URL=mysql+pymysql://username:password@localhost/sandwich_db

Do not commit database passwords, API keys, or other credentials to the repository.

5. Start the API
uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000
API Documentation

FastAPI automatically provides interactive API documentation.

Once the server is running, visit:

http://127.0.0.1:8000/docs

You can use the Swagger UI to test the API endpoints directly from your browser.

Running Tests

Run the test suite with:

pytest
What I Learned

Through this project, I practiced:

Designing RESTful API endpoints
Working with relational databases
Using SQLAlchemy to interact with a database
Implementing CRUD operations
Writing automated API tests
Using FastAPI's interactive documentation
Structuring a backend application
Future Improvements

Potential improvements include:

Add user authentication and authorization
Add pagination for sandwich results
Add input validation and more detailed error handling
Add Docker support
Deploy the API to a cloud platform
Expand the test suite
