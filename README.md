
# Python Flask App for testing

```powershell
docker run -p 5000:5000 \
-e WRITE_DB_USER='your_write_db_user' \
-e WRITE_DB_PASSWORD='your_write_db_password' \
-e WRITE_DB_HOST='your_write_db_endpoint' \
-e READ_DB_USER='your_read_db_user' \
-e READ_DB_PASSWORD='your_read_db_password' \
-e READ_DB_HOST='your_read_db_endpoint' \
-e DB_NAME='webappdb' \
flask-webapp
```