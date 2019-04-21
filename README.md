# Project Describtion
A flask based web service to send survey emails to a mailing list and record their response through a generated form with a simple api to access the responses through the url domain/?email=email@user.com

## Important Files
- create_mailing_list.py : imports data from a csv files and stores the list into the database
- emailing.py : sends survey emails to all the contacts in the database

## Important Notes

- the settings for the mailing service are avaliable in settings.py and currently configured to gmail SMTP
- the project is currently configured for MariaDB
