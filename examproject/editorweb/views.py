from django.shortcuts import render , redirect, get_object_or_404
from .models import Post, Person
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
#def home(request):
#    posts = Post.objects.all()
#    return render(request,'home.html',{'posts':posts})
def home(request):
    
    if request.POST:
        person = Person.objects.all()
        return render(request,'home.html',{'person': person})
    else:
        person = Person.objects.all()
        q = request.GET.get('q', '')
        if q:
            person = person.filter(subject__icontains=q) or person.filter(professor__icontains=q)

        return render(request, 'home.html', {
            'person' : person,
            'q' : q
        })

def summary(request,person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        b = str(request.POST.get('post_exam'))
        print(b)
        print(b == 'midterm')
        print("------------------------------------------------------------------")
        if b == 'midterm':
            posts = Post.objects.filter(exam__icontains="midterm")
            return render(request,'summary.html',{'posts':posts,'person':person})
        elif b == 'finalterm':
            posts = Post.objects.filter(exam__icontains="finalterm")
            return render(request,'summary.html',{'posts':posts,'person':person})
        elif b == 'quiz':
            posts = Post.objects.filter(exam__icontains="quiz")
            return render(request,'summary.html',{'posts':posts,'person':person})
        else:
            return render(request,'summary.html',{'posts':person.post_set.all,'person':person})
    else:
        return render(request,'summary.html',{'person':person,'posts':person.post_set.all})

def new(request,person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request,'new.html',{'person':person})

def create(request, person_id):

    person_id = request.POST['person_id'] 
    post = Post()
    post.exam = request.POST['post_exam']
    post.title = request.POST['post_title']
    post.body = request.POST['post_body']
    post.pub_date = timezone.datetime.now()
    if request.FILES:
      post.image = request.FILES['post_image']
    post.person = get_object_or_404(Person, pk=person_id)
    post.save()

    return redirect('summary', person_id=person_id)

#def board(request, person_id):
#  post = get_object_or_404(Post, pk=person_id)
#  return render(request, 'board.html', {'person' : person})

def createclass(request):

    person = Person()
    person.subject = request.POST['person_subject']
    person.professor = request.POST['person_professor']
    person.save()

def read(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'read.html', {'post' : post})

def renew(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'renew.html',{'post' : post})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.POST["post_title"]
    post.body = request.POST["post_body"]
    post.pub_date = timezone.datetime.now()
    if request.FILES:
      post.image = request.FILES['post_image']
    post.save()
    return redirect('read', post_id=post_id)

def delete(request, post_id):
    if request.POST:
      post = get_object_or_404(Post, pk=post_id)
      post.delete()
      return redirect('home')
    else:
      return redirect('read', post_id=post_id)




