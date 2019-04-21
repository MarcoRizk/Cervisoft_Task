import csv
from.models import Email,db


def csv_to_db_mailing_list(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        line_count = 0
        for row in csv_reader:
            new_contact = Email(row['full_name'],row['user_email'])
            db.session.add(new_contact)
            line_count += 1
        db.session.commit()
        print('Loaded {0} Contacts Sucessfully into the Database.'.format(line_count))

