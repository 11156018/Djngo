from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, MessageForm
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.decorators import login_required

def hello(request):
    return HttpResponse(request, "hello world")

def homepage(request):
    posts = Post.objects.all() 
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "homepage.html", {'list_posts': list_posts, 'now': now})

def ntub(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "ntub.html", {'list_posts': list_posts, 'now': now})

def ntut(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body        
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "ntut.html", {'list_posts': list_posts, 'now': now})

def ntuh(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date        
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "ntuh.html", {'list_posts': list_posts, 'now': now})

def ntust(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "ntust.html", {'list_posts': list_posts, 'now': now})

def others(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "others.html", {'list_posts': list_posts, 'now': now})

def mood(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "mood.html", {'list_posts': list_posts, 'now': now})

def tech(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "tech.html", {'list_posts': list_posts, 'now': now})

def note(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        sub_data["slug"] = i.slug
        sub_data["pub_date"] = i.pub_date
        list_posts.append(sub_data)
    now = datetime.now()
    return render(request, "note.html", {'list_posts': list_posts, 'now': now})

def list_posts(request):
    posts = Post.objects.all()
    list_posts = []
    for i in posts:
        sub_data = {}
        sub_data["title"] = i.title
        sub_data["body"] = i.body
        list_posts.append(sub_data)
    list_posts = [f'No. {count}: {post.title}: {post.body} <br>' for count, post in enumerate(posts)]
    return HttpResponse(request, list_posts)

def urltest(request, year, month, words):
    print(f'year: {year}, month: {month}, words: {words}')
    #return HttpResponse(f'year: {year}, month: {month}, words: {words}')
    return render(request, "urltest.html", locals())

def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, "post.html", locals())
        #get預設取得一筆資料
    except Exception as e:
        print(e)
        return HttpResponse('錯誤')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '註冊成功！')
            return redirect('message_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('message_list')

def message_list(request):
    messages_list = Message.objects.order_by('-created_at')
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, '請先登入')
            return redirect('login')
        
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            messages.success(request, '留言成功！')
            return redirect('message_list')
    else:
        form = MessageForm()
    
    return render(request, 'message_list.html', {
        'messages_list': messages_list, 
        'form': form
    })

@login_required
def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, user=request.user)
    
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, '留言已更新')
            return redirect('message_list')
    else:
        form = MessageForm(instance=message)
    
    return render(request, 'edit_message.html', {
        'form': form, 
        'message': message
    })

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, user=request.user)
    
    if request.method == 'POST':
        message.delete()
        messages.success(request, '留言已刪除')
        return redirect('message_list')
    
    return render(request, 'delete_message.html', {'message': message})

from .forms import UserProfileForm

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '個人資訊已更新！')
            return redirect('edit_profile')  # 假設有一個顯示個人資料的頁面
    else:
        form = UserProfileForm(instance=user)
    
    return render(request, 'edit_profile.html', {'form': form})