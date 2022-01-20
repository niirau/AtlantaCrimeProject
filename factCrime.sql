create table factCrime(
	crimeEventId int identity primary key,
	crimeTypeKey int,
	dateKey int,
	weatherKey int,
	neighborhoodKey int,
	lat float,
	long float,
	beat int,
	npu varchar(5)
)

truncate table factCrime
insert into factCrime (crimeTypeKey, weatherKey, dateKey, neighborhoodKey, lat, long, beat, npu)
select
	dimCrime.CrimeTypeKey,
	dimWeather.WeatherKey,
	dimDate.datekey,
	crime.neighborhoodkey,
	crime.lat,
	crime.long,
	crime.beat,
	crime.npu
from crime  
join dimCrime on crime.crime = dimCrime.CrimeBizKey
join dimNeighborhood on dimNeighborhood.NeighborhoodKey = crime.neighborhoodkey
join dimDate on dimDate.date = cast(crime.date as date)
left join weather on weather.DateKey = cast(crime.date as date)
left join dimWeather on weather.description = dimWeather.Weather




