# management/commands/seed_data.py
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee, Department

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        departments = [Department.objects.create(name=fake.word()) for _ in range(5)]
        
        for _ in range(30):
            Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date(),
                department=fake.random.choice(departments)
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
