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

insert into factCrime (crimeTypeKey, dateKey, neighborhoodKey, lat, long, beat, npu)
select
	dimCrime.CrimeTypeKey,
	dimDate.datekey,
	crime.neighbourhoodkey,
	crime.lat,
	crime.long,
	crime.beat,
	crime.npu
from crime  
join dimCrime on crime.crime = dimCrime.CrimeBizKey
join dimNeighborhood on dimNeighborhood.NeighborhoodKey = crime.neighbourhoodkey
join dimDate on dimDate.date = cast(crime.date as date)

select top 50 * from factCrime
where datekey is null
or neighborhoodKey is null
or crimeTypeKey is null