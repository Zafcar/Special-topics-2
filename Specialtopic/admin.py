from django.contrib import admin
from  django.contrib.auth.models  import  Group
#new commit!!!
# this import from models.py file which stores all the sql tables.
from .models import Student_database, System_database


# This class is to display all the values in the Student_database table.
class  Student_databaseAdmin(admin.ModelAdmin):
    list_display=("USN", "Student_name")
    

# This class is to display all the values in the System_database table.
class  System_databaseAdmin(admin.ModelAdmin):
    list_display=("Date", "Student_name", "Branch", "USN", "System_no", "Time_in", "Time_out")
    # creates a filter to sort by. 
    list_filter = ("Date",)


# This adds both the tables from models.py into admin site for viewing or adding.
admin.site.register(Student_database, Student_databaseAdmin)
admin.site.register(System_database, System_databaseAdmin)


# Changes the name of the header, title and index.
admin.site.site_title  =  "System Assign Admin"
admin.site.site_header  =  "System Assign Admin" 
admin.site.index_title  =  "Admin Controls"

# Removes all default groups.
admin.site.unregister(Group)

