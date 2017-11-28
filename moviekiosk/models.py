# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    cid = models.IntegerField(db_column='CID', primary_key=True)  # Field name made lowercase.
    date_of_birth = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    tickets_purchased = models.IntegerField(blank=True, null=True)
    points_available = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerMoviesSeen(models.Model):
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CID', primary_key=True)  # Field name made lowercase.
    mid = models.ForeignKey('Movie', models.DO_NOTHING, db_column='MID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_movies_seen'
        unique_together = (('cid', 'mid'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Movie(models.Model):
    mid = models.IntegerField(db_column='MID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    theater_id = models.IntegerField(db_column='theater_ID', blank=True, null=True)  # Field name made lowercase.
    rating = models.CharField(max_length=5, blank=True, null=True)
    price_per_ticket = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class MovieShowtime(models.Model):
    mid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MID', primary_key=True)  # Field name made lowercase.
    showtime = models.CharField(max_length=5)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_showtime'
        unique_together = (('mid', 'showtime'),)


class PlayingInRoom(models.Model):
    mid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MID', primary_key=True)  # Field name made lowercase.
    rnum = models.ForeignKey('Room', models.DO_NOTHING, db_column='RNUM')  # Field name made lowercase.
    tid = models.ForeignKey('Theater', models.DO_NOTHING, db_column='TID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playing_in_room'
        unique_together = (('mid', 'rnum', 'tid'),)


class PurchasingTickets(models.Model):
    cid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CID', primary_key=True)  # Field name made lowercase.
    tid = models.ForeignKey('Theater', models.DO_NOTHING, db_column='TID')  # Field name made lowercase.
    mid = models.ForeignKey(Movie, models.DO_NOTHING, db_column='MID')  # Field name made lowercase.
    num_tickets = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchasing_tickets'
        unique_together = (('cid', 'tid', 'mid'),)


class Room(models.Model):
    num = models.IntegerField(db_column='NUM', primary_key=True)  # Field name made lowercase.
    total_seats = models.IntegerField(blank=True, null=True)
    num_seats_available = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Seat(models.Model):
    room_num = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_num', primary_key=True)
    seat_num = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'seat'
        unique_together = (('room_num', 'seat_num'),)


class Theater(models.Model):
    tid = models.IntegerField(db_column='TID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    opening_time = models.CharField(max_length=5, blank=True, null=True)
    closing_time = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theater'
