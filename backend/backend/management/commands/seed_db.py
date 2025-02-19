from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection, transaction
from pathlib import Path

class Command(BaseCommand):
    help = "Creates a superuser and seeds the database with initial data."

    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        User = get_user_model()
        admin_username = "tribbl3"
        admin_email = "tribbl3@gmail.com"
        admin_password = "password"
        
        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password
            )
            self.stdout.write(self.style.SUCCESS("Superuser created."))
        else:
            self.stdout.write("Superuser already exists.")

        # Determine the SQL file path
        base_dir = Path(__file__).resolve().parent.parent.parent  # Moves up 3 levels
        sql_file = base_dir / "sql" / "02_dml.sql"

        if not sql_file.exists():
            self.stderr.write(self.style.ERROR(f"SQL file not found: {sql_file}"))
            return

        try:
            with sql_file.open("r") as file:
                sql_statements = file.read()

            with connection.cursor() as cursor:
                # Disable foreign key checks
                cursor.execute("SET FOREIGN_KEY_CHECKS=0;")

                # Execute each SQL statement
                for statement in sql_statements.split(";"):
                    statement = statement.strip()
                    if statement:
                        cursor.execute(statement)

                # Re-enable foreign key checks
                cursor.execute("SET FOREIGN_KEY_CHECKS=1;")

                # Commit the transaction
                transaction.commit()

            self.stdout.write(self.style.SUCCESS("Database seeded successfully."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error seeding database: {e}"))
