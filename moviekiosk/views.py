from django.shortcuts import render
from django.http import HttpResponse
from moviekiosk.models import Movie
from django.template import loader
from django.db import connection
import datetime

# Create your views here.
def dictfetchall(cursor):
	"Return all rows from a cursor as a dict"
	columns = [col[0] for col in cursor.description]
	return [
		dict(zip(columns, row))
		for row in cursor.fetchall()
	]

def index(request, theater_id):
	now = datetime.datetime.now()
	with connection.cursor() as cursor:
		cursor.execute('SELECT MID, name, rating, price_per_ticket, poster_title FROM movie WHERE theater_id = %s' % theater_id)
		movie_list = dictfetchall(cursor)
		cursor.execute('SELECT TID, name FROM theater WHERE TID = %s' % theater_id)
		theater_name = dictfetchall(cursor)
	context = {
		'movie_list': movie_list,
		'theater_name': theater_name,
	}
	return render(request, 'moviekiosk/index.html', context)

def detail(request, theater_id, movie_id):
	with connection.cursor() as cursor:
		cursor.execute('SELECT MID, name, rating, price_per_ticket, poster_title FROM movie WHERE theater_id = ' + theater_id + ' AND MID = ' + movie_id)
		movie_info = dictfetchall(cursor)
		cursor.execute('SELECT MID, showtime FROM movie_showtime WHERE MID = %s' % movie_id)
		time_info = dictfetchall(cursor)
	context = {
		'movie_info': movie_info[0],
		'time_info': time_info,
	}
	return render(request, 'moviekiosk/moviePage.html', context)

def confirmTicket(request, theater_id, movie_id):
	if request.method == "POST":
		with connection.cursor() as cursor:
			cursor.execute('SELECT TID, name FROM theater WHERE TID = %s' % theater_id)
			theater_name = dictfetchall(cursor)
			cursor.execute('SELECT CID, name, date_of_birth FROM customer WHERE name = "' + request.POST['name'] + '" AND date_of_birth = "' + request.POST['dob'] + '"')
			if cursor.rowcount != 0:
				temp_info = dictfetchall(cursor)
				cursor.execute('UPDATE customer SET tickets_purchased = tickets_purchased + 1 WHERE CID = ' + str(temp_info[0]['CID']))
			else:
				cursor.execute('INSERT INTO customer (date_of_birth, name, phone, address, tickets_purchased, points_available) VALUES ("' + request.POST['dob'] + '", "' + request.POST['name'] + '", "' + request.POST['phone'] + '", "' + request.POST['address'] + '", 1, 100)')
			cursor.execute('SELECT MID, name, price_per_ticket FROM movie WHERE theater_id = ' + theater_id + ' AND MID = ' + movie_id)
			movie_info = dictfetchall(cursor)
			cursor.execute('SELECT MID, RNUM, TID FROM playing_in_room WHERE TID = ' + theater_id + ' AND MID = ' + movie_id)
			room_info = dictfetchall(cursor)
			cursor.execute('SELECT MID, showtime, date FROM movie_showtime WHERE MID = ' + movie_id + ' AND showtime = "' + request.POST['time_label'].split('_')[1] + '"')
			show_time_info = dictfetchall(cursor)

		context = {
			'theater_name': theater_name,
			'movie_info': movie_info,
			'room_info': room_info,
			'show_time_info': show_time_info,
			'user_name': request.POST['name'],
		}
		return render(request, 'moviekiosk/ticket.html', context)
	else:
		return HttpResponse("Try again later")