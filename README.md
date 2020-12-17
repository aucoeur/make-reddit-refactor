# Make Reddit Refactor
- [x] Refactor to use a SQLAlchemy database instead of Mongo  
- [x] Add models for:  
    - [x] User  
    - [x] Entry  
- [x] Add login functionality using Flask-Login  
  - [x] Password hashing
- [x] Add feature to post a new entry with Flask-WTForms  
- [x] Add message flashing when a new post is posted  
- [x] Add entry to db
- [x] Populate entries on index
- [x] 'Read more' links to individual entry
- [x] Bootstrap the jinja forms
- [x] Add error handlers to redirect to index & flash error
- [ ] Implement up/down doots
- [ ] Update/Delete entries(?)

## **Instructions**

1. Clone the repository into your projects directory.
2. Run `pip3 install -r requirements.txt` to ensure that you have all required Python packages installed.
3. If db needs to be created or models changed:
   - `flask db init`  ()
   - `flask db migrate -m 'first db migration'`
   - `flask db upgrade`
4. Run the server code using `flask run`.
