# Make Reddit Refactor
- [x] Refactor to use a SQLAlchemy database instead of Mongo  
- [x] Add models for:  
    - [x] User  
    - [x] Post (?)  
- [-] Add login functionality using Flask-Login  
  - [-] Password hashing
- [ ] Add feature to post a new entry with Flask-WTForms  
- [ ] Add message flashing when a new post is posted  

## **Instructions**

1. Clone the repository into your projects directory.
2. Run `pip3 install -r requirements.txt` to ensure that you have all required Python packages installed.
3. If db needs to be created:
   - `flask db init`  
   - `flask db migrate -m 'first db migration'`
   - `flask db upgrade`
4. Run the server code using `flask run`.