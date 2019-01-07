from django.shortcuts import render


posts = [
            {
                'author' : 'Anubhav',
                'title' : 'Post 1',
                'content' : 'Working on new django project',
                'date_posted' : 'January 7, 2018'
            },
            {
                'author' : 'Saubhagya',
                'title' : 'Post 2',
                'content' : 'Playing PUBG',
                'date_posted' : 'January 7, 2018'
            }

]

def home(request):

    context = {
                'posts'  : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{ 'title' : 'Blog@TechnoJam - About'})



