# from django.shortcuts import render,HttpResponse
# from .models import Listing

# def index(request):
#     trending=Listing.objects.all().filter(is_hot=True)
#     listings=Listing.objects.all()
#     context ={
#         'listings':listings,
#         'trending':trending,
#     }
#     return render(request,'pages/wishlist.html',context)

# # def about(request):
# #     listings=Listing.objects.all().filter(is_published=True)
# #     context ={
# #         'listings':listings,
# #     }
# #     return render(request,'pages/wishlist.html',context)