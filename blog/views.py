from django.shortcuts import render

posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'Jan 27, 2022'
	},
	{
		'author': 'Waters',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'Jan 28, 2022'
	},
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
	
