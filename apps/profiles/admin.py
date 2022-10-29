from django.contrib import admin

from .models import ReaderProfile, LibrarianProfile


class LibrarianProfileAdmin(admin.ModelAdmin):
    """
    -------------------------
    Custom View Profile Admin
    -------------------------
    """

    list_display = ["id", "pkid", "user", "phone_number", "gender", "country", "city"]
    list_filter = ["gender", "country", "city"]
    list_display_links = ["id", "pkid", "user"]

class ReaderProfileAdmin(admin.ModelAdmin):
    """
    -------------------------
    Custom View Profile Admin
    -------------------------
    """

    list_display = ["id", "pkid", "user", "phone_number", "gender", "country", "city", "total_books_borrowed", "current_books_borrowed", "status"]
    list_filter = ["gender", "country", "city", "status"]
    list_display_links = ["id", "pkid", "user"]


admin.site.register(LibrarianProfile, LibrarianProfileAdmin)
admin.site.register(ReaderProfile, ReaderProfileAdmin)