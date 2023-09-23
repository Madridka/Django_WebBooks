from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language, Status
# Register your models here.


# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name') #это отображение в админке
    fields = ['first_name', 'last_name',
              ('birth_date', 'death_date')] #это отображение в админке в редакторе


admin.site.register(Author, AuthorAdmin)
# admin.site.register(Book)
# admin.site.register(BookInstance)


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author') #фильтр для поиска в админке
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'inv_nom', 'status', 'borrower', 'due_back')
    list_filter = ('book', 'status', 'due_back')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Статус и окончание действия', {'fields': ('status', 'borrower', 'due_back')}),
    ) #в админке в разеделе статус отображение по field сетам


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
