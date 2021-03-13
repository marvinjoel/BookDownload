from django.views import View

from apps.bookapp.models import CategoryModel

#Llevar en el setting , templates
# class Category_Links(View):
#     def get(self, request):
#         category = CategoryModel.objects.all()
#         return {'categories':category}


def category_links(request):
    category = CategoryModel.objects.all()
    return {'categories':category}