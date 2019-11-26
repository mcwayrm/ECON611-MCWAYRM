-- *** Homework 4 Answer Key ***

-- * PROBLEM 1 *

-- 1.A
--Output a table that has the columns Album Title, Artist, Track Name, Genre, Composer, Length of Song (minutes)

Select Album.Title as "Album Title", Artist.Name as "Artist Name", Track.Name as "Track Name", Genre.Name as "Genre", Track.Composer,round(Track.Milliseconds/60000.00,2) as "Lenght of Song"
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
		
-- 1.B
--Output a frequency table for how many letters are in an album title and a song title.
select A.Letter_Count_of_Title as "Letter Count of Titles", A.Album_Titles as "Number of Album Titles", B.Track_Names as "Number of Track Titles"
from
	(select 
	length(Title) as Letter_Count_of_Title, 
	count(length(Title)) as Album_Titles,
	row_number() over (order by length(Title)) as seqnum
	from Album
	group by length(Title))  A left join
	
	(select 
	length(Name) as Track_Length, 
	count(length(Name)) as Track_Names,
	row_number() over (order by length(Name)) as seqnum
	from Track
	group by length(Name)) B
	on A.seqnum=B.seqnum
	
--What is the average and range of amount of letters?	
select avg(A.Letter_Count_of_Title) as "Average Letter Count of Album Titles", avg(B.Track_Length) as "Average Letter Count of Track Titles",
	(max(A.Letter_Count_of_Title)-min(A.Letter_Count_of_Title)) as "Album Title Range", (max(B.Track_Length)-min(B.Track_Length)) as "Track Title Range"
from
	(select 
	length(Title) as Letter_Count_of_Title, 
	count(length(Title)) as Album_Titles,
	row_number() over (order by length(Title)) as seqnum
	from Album
	group by length(Title))  A left join
	
	(select 
	length(Name) as Track_Length, 
	count(length(Name)) as Track_Names,
	row_number() over (order by length(Name)) as seqnum
	from Track
	group by length(Name)) B
	on A.seqnum=B.seqnum


-- 1.C
--How many songs did each composer write? 
Select 
	Track.Composer,
	count(Track.Name)
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
group by Track.Composer


--How many artists composed their own music? 
Select sum(A.Composer_Artist_Same) as "Number of Composers of Own Songs"
from
(Select  
	Track.Composer,
	case when Track.Composer=Artist.Name then 1 end as Composer_Artist_Same
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
where Composer_Artist_Same=1
group by Track.Composer) A


--Output all of the Artists who had songs that were longer than 2.5 minutes and they did not write their own songs.
Select 
	Artist.Name as "Artist Name", 
	count(Track.Name) as "Number of Tracks",
	round(Track.Milliseconds/60000.00,2) as Length_of_Song
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId

where Length_of_Song>2.50 and Track.Composer!=Artist.Name
group by Track.Composer	
		
		
--1.D
--How many albums contain songs that only have an even number of seconds in the length of the song and the songs are all MPEG audio files?

select count(B.Number_of_Albums) as "Amount of Albums"
from
(Select (A.Album_Title) as Number_of_Albums
from
(Select 
	Album.Title as Album_Title, 
	Track.Name as "Track Name", 
	round(Track.Milliseconds/1000,2) as Seconds,
	MediaType.MediaTypeId as File_Type
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join MediaType
		on MediaType.MediaTypeId=Track.MediaTypeId
where File_Type=1 and Seconds%2=0) A
group by A.Album_Title) B


--1.E
--How large, in terms of Megabytes are each album?		

Select 
	Album.Title as "Album Title", 
	round(Track.Bytes/1000000,2) as Megabytes
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
group by Album.Title

--On average, how large, in terms of bytes, is a pop song?
select A.Genre, avg(A.Megabytes) as "Average Megabytes in Pop Song"	
from
(Select 
	Album.Title as "Album Title", 
	Track.Name as "Track Name", 
	Genre.Name as Genre, 
	round(Track.Bytes/1000000,2) as Megabytes
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre	
		on Track.GenreId=Genre.GenreId
where Genre.Name="Pop") A

--What is the range and average duration of a heavy metal song in minutes?
Select A.Genre, (max(A.Length_of_Song)-min(A.Length_of_Song)) as Range, round(avg(A.Length_of_Song),2) as "Average Length of Song"
from

(Select 
	Track.Name as "Track Name", 
	Genre.Name as Genre, 
	round(Track.Milliseconds/60000.00,2) as Length_of_Song
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre	
		on Track.GenreId=Genre.GenreId
where Genre.Name="Heavy Metal") A

	


-- * PROBLEM 2 *
		
--2.A

--Output a table that shows the number of customers in each city, and also have shows the state and country that the city is located in

select country,state,city,
	count(city) as "Number of Customers"
from customer
group by city


--2.B

--How much in total was spent on music per year? 

select substr(invoicedate,1,4) as Years, round(sum(total),2) as "Total Amount"
from invoice
group by Years

-- What is the average amount a person spent on music in a year?

select substr(invoicedate,1,4) as Years, round(avg(total),2) as "Average Spent"
from invoice
group by Years

--What is the average amount a person with a gmail account spent on music in a year?

select substr(invoice.invoicedate,1,4) as Years, round(avg(invoice.total),2) as "Average Spent By gmail users"
from invoice
	join Customer
		on Customer.CustomerId=Invoice.CustomerId

where customer.email like "%gmail%"
group by Years


--2.C

--What year-month combination had the most spending on music? 

select substr(invoicedate,1,7) as Year_month, round(sum(total),2) as Total_Amount
from invoice
group by Year_month 
order by Total_Amount desc

--Which year-month combi- nation had the most money spent on pop music?


select substr(invoice.invoicedate,1,7) as Year_month, round(sum(Invoice.Total),2) as Total_Spent,Genre.name
from invoice
	join InvoiceLine	
		on InvoiceLine.InvoiceId=InvoiceLine.InvoiceId
	join Track 
		on Track.TrackId=InvoiceLine.TrackId
	join Genre	
		on Genre.GenreId=Track.GenreId	
where Genre.name="Pop"
group by Year_month		
order by Total_spent desc 		


--2.D

--What Artist has the most songs bought that are in the pop genre? 

Select Artist.Name as "Artist Name", count(Track.Name) as "Number of Tracks", Genre.Name as "Genre"
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
	join InvoiceLine
		on InvoiceLine.TrackId=Track.TrackId
where genre.name="Pop"		
group by Artist.Name
order by count(Track.Name) desc

--What is the total money spent on these songs? 

Select Artist.Name as "Artist Name", count(Track.Name) as "Number of Tracks", round(sum(Invoice.Total),2) as "Total Spent", Genre.Name as "Genre"
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
	join InvoiceLine
		on InvoiceLine.TrackId=Track.TrackId
	join Invoice	
		on Invoice.InvoiceId=InvoiceLine.InvoiceId
where genre.name="Pop"		
group by Artist.Name
order by count(Track.Name) desc

--Which customer is spending the most on pop songs?

Select customer.LastName||", "||customer.FirstName as Customer_Name, Artist.Name as "Artist Name", count(Track.Name) as "Number of Tracks", round(sum(Invoice.Total),2) as Total_Spent, Genre.Name as "Genre"
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
	join InvoiceLine
		on InvoiceLine.TrackId=Track.TrackId
	join Invoice	
		on Invoice.InvoiceId=InvoiceLine.InvoiceId
	join Customer	
		on customer.CustomerId=Invoice.CustomerId
where genre.name="Pop"		
group by Customer_Name
order by Total_Spent desc


--2.E

--Output how many songs each artist is selling in each country?

Select Customer.country, Artist.Name as "Artist Name", count(Track.Name) as "Number of Tracks"
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
	join InvoiceLine
		on InvoiceLine.TrackId=Track.TrackId
	join Invoice	
		on Invoice.InvoiceId=InvoiceLine.InvoiceId
	join Customer	
		on customer.CustomerId=Invoice.CustomerId	
group by Customer.country,Artist.Name


--Who is selling the most outside of the US?

Select Artist.Name as "Artist Name", count(Track.Name) as "Number of Tracks Sold"
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
	join InvoiceLine
		on InvoiceLine.TrackId=Track.TrackId
	join Invoice	
		on Invoice.InvoiceId=InvoiceLine.InvoiceId
	join Customer	
		on customer.CustomerId=Invoice.CustomerId	
where Customer.country!="USA"
group by Artist.Name
order by count(Track.Name) desc

--On average, how many songs is each artist selling outside of the US?
select round(avg(A.Number_of_Tracks_Sold),2) as "Average Tracks Sold Outside of US"
from
(Select Artist.Name as "Artist Name", count(Track.Name) as Number_of_Tracks_Sold
from Album
	join Artist
		on Artist.ArtistId=Album.ArtistId
	join Track	
		on Track.AlbumId=Album.AlbumId
	join Genre
		on Genre.GenreId=Track.GenreId
	join InvoiceLine
		on InvoiceLine.TrackId=Track.TrackId
	join Invoice	
		on Invoice.InvoiceId=InvoiceLine.InvoiceId
	join Customer	
		on customer.CustomerId=Invoice.CustomerId	
where Customer.country!="USA"
group by Artist.Name
order by count(Track.Name) desc) A


-- * PROBLEM 3 *

--3.A

--Return a list of Customers that assigns a sequential integer to each customer and resets the number when the country of the customer changes for Customers are not from Canada and Brazil and whose email address have yahoo or `gmail'

select *
from (
SELECT
        ROW_NUMBER () OVER (PARTITION BY Country ORDER BY FirstName) RowNum,
        FirstName,
        LastName,
        country, Email
    FROM
        customer)
where Country not in ('Canada', 'Brazil') and (Email like '%gmail%' or Email like '%yahoo%') 

--3.B

--Compute the rank for each track in each album based on the track’s length, then append all the tracks that have a lengthrank of 2 and 4

select *
    from (
SELECT
            AlbumId,
            Name,
            Milliseconds,
            DENSE_RANK () OVER ( 
        PARTITION BY AlbumId 
        ORDER BY Milliseconds 
    ) LengthRank
        FROM
            track)
    where LengthRank=2
union ALL
    select *
    from (
SELECT
            AlbumId,
            Name,
            Milliseconds,
            DENSE_RANK () OVER ( 
        PARTITION BY AlbumId 
        ORDER BY Milliseconds 
    ) LengthRank
        FROM
            track)
    where LengthRank=4

    

-- * BONUS *

-- ** HERE THIS WAS USED IN JUPYTER LAB **

!pip install ipython-sql
%load_ext sql
%sql sqlite://

%%sql   
CREATE TABLE STUDENT(firstname varchar(50),lastname varchar(50), Hours_Studied varchar(50), Hours_Slept varchar(50), Grade varchar(50));  
INSERT INTO STUDENT VALUES('Tom','Mitchell',15, 8, .95);  
INSERT INTO STUDENT VALUES('Jack','Ryan',10, 12, .87);
INSERT INTO STUDENT VALUES('Matt','Smith',11, 9, .90);
INSERT INTO STUDENT VALUES('Sally','Rose',20, 8, .97);
INSERT INTO STUDENT VALUES('Alex','Carl',18, 7, .95);
INSERT INTO STUDENT VALUES('Barry','Marx',17, 10, .91);
INSERT INTO STUDENT VALUES('Eric','Prince',4, 10, .74);
INSERT INTO STUDENT VALUES('Rick','Perry',13, 6, .94);
INSERT INTO STUDENT VALUES('Jessica','Ryans',7, 9, .85);
INSERT INTO STUDENT VALUES('Robert','Carlos',11, 7, .86);

 %sql SELECT * from STUDENT;  

--Calculation 1: Average Hours Studied

 %sql SELECT avg(Hours_studied) from STUDENT;  

--Calculation 2: Average Hours Studied for those who have an A

 %sql SELECT round(avg(Hours_studied),2) as "Average Hours Studied" from STUDENT where Grade>=0.9
 
 --Calculation 3: Biggest difference between Hours Studied and Hours Slept
 
%sql SELECT (Hours_studied-Hours_slept) as Difference_Between_Study_and_Sleep_Hours, Grade from STUDENT order by Difference_Between_Study_and_Sleep_Hours desc 
