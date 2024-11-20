from django.urls import path 
from .views import*
#,PostDatail,SignupPage,LogoutUser,loginPage,contactPage
urlpatterns=[
    path('',HomePage,name='home'),

    path('post_detail/',PostDetail, name='post_detail'),  # 'post_detail' nomi
    # path('signup/',SignupPage,name='signup'),
    # path('logout/',LogoutUser,name="logout"),
    # path('login/',loginPage,name='login'),
    # path('contact/',contactPage,name='contact')

]

