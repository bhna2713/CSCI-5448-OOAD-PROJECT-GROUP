from django.contrib import admin
from .models import Expenses
from notes.models import Notes
from address.models import Address
from reminders.models import Reminders
from appointments.models import Appointments
admin.site.register(Expenses)
admin.site.register(Notes)
admin.site.register(Address)
admin.site.register(Reminders)
admin.site.register(Appointments)
# models.path.append( </notes/models> )

# admin.site.register(Notes)
# Register your models here.


