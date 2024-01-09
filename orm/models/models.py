from django.db import models
from django.db.models import Q
import datetime


class Author(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	address = models.CharField(max_length=200, null=True)
	zipcode = models.IntegerField(null=True)
	telephone = models.CharField(max_length=100, null=True)
	recommendedby = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='recommended_authors', related_query_name='recommended_authors', null=True)
	joindate = models.DateField()
	popularity_score = models.IntegerField()
	followers = models.ManyToManyField('User', related_name='followed_authors', related_query_name='followed_authors')

	def __str__(self):
		return self.firstname + ' ' + self.lastname


class Books(models.Model):
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=200)
	price = models.IntegerField(null=True)
	published_date = models.DateField()
	author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', related_query_name='books')
	publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', related_query_name='books')
	
	def __str__(self):
	    return self.title


class Publisher(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	recommendedby = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True)
	joindate = models.DateField()
	popularity_score = models.IntegerField()

	def __str__(self):
		return self.firstname + ' ' + self.lastname


class User(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def get_object():
		pass

	def __str__(self):
		return self.username


ans1 = Books.objects.all()
ans2 = Books.objects.all().values_list('title', 'publiched_date')
ans3 = Author.objects.all().filter(popularity_score=0).values_list('firstname', 'lastname')
ans4 = Author.objects.all().filter(firstname_startswith='a', popularity_score__gte=8).values_list('firstname', 'lastname')
ans5 = Author.objects.all().filter(firstname__icontains='aa').values_list('firstname', 'lastname')
ans6 = Author.objects.all().filter(pk__in=[1, 3, 23, 43, 134, 25])
ans7 = Publisher.objects.all().filter(joindate__gte=datetime.date(year=2012, month=9, day=1)).order_by('joindate').values_list('firstname', 'joindate')
ans8 = Publisher.objects.all().order_by('lastname').values_list('lastname').distinct()[:10]
ans9 = [
  Author.objects.all().order_by('joindate').last(),
  Publisher.objects.all().order_by('-joindate').first()
]
ans10 = Author.objects.all().order_by('-joindate').values_list('firstname', 'lastname', 'joindate').first()
ans11 = Author.objects.all().filter(joindate__year__gte=2013)
ans12 = Books.objects.all().filter(author__popularity_score__gte=7).aggregate(total_books_price=sum('prices'))
ans13 = Books.objects.all().filter(author__startswith='A').values_list('title', flat=True)
ans14 = Books.objects.all().filter(author__pk__in=[1,3,4]).aggregate(total_book_price_2=sum('prices'))
ans15 = Books.objects.all().values_list('author', 'recommendedby__firstname')
# ans16 = Author.objets.all().order_by('firstname').filter(books__pk=1)
ans16 = Authors.objects.all().filter(books__publisher__pk=1)
user1 = Users.objects.create(username='user1', email='abc@abc.en')
user2 = Users.objects.create(username='user2', email='efg@efg.en')
user3 = Users.objects.create(username='user3', email='efg@efg.en')
ans17 = Authors.objects.get(pk=1).followers.add(user1, user2, user3)
ans18 = Authors.obects.get(pk=2).followers.set(user1)
ans19 = Authors.objects.get(pk=1).followers.add(user4)
ans20 = Authors.objects.get(pk=1).followers.remove(user1) 
ans21 = User.objects.all(pk=1).follower_authors.all().values_list('firstname', flat=True)
ans22 = Authors.objects.all().filter(books__title__icontains='tle')
ans23 = Authors.objects.filter(Q(firstname__istartswith='a') and ( Q(popularity_score__gt=5) or Q(joindate__year__gt=2014)))
ans24 = Authors.objects.get(pk=1)
ans25 = Authors.objects.all()[:10]
# qs = Authors.objects.filter(popularity_score=7)
# author2 = qs[1] 
# author1 = qs[0]
qs = Authors.objetcts.filter(popularity_score=7)
author1 = qs.first()
author2 = qs.last()
ans27 = Authors.objects.filter(
	pupularity_score__gte=4, 
	joindate_year__gte=2012, 
	joindate_year___gte=12, 
	firstname__istartswith='A'
	)
# ans28 = Authors.objects.filter(datetime__year_ne=2012)
ans28 = Authors.objects.exclude(joindate_year=2012)


oldest_author = Authors.objects.latest('datetime')
newest_author = Authors.objects.newest('datetime')
authors_score = Authors.objects.filter('popularity_score')

def calculate_avg_score_authors(authors_score):
	if not authors_score:
		return None
	else: 
		average = sum(authors_score) / len(authors_score)
		return average

sum_all_price = Books.objects.all().aggregate(sum('price'))
# sum_all_price = Books.objects.all().sum(('price'))	