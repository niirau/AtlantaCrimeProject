use CrimeTimeDW

drop table dimCrime

create table dimCrime(
	CrimeTypeKey int identity primary key,
	CrimeType varchar(25),
	CrimebizKey varchar(25),
	Vehicle char(1),
	Burglary char(1),
	Robbery char(1),
	Larceny char(1),
	Violent char(1)
)
go
truncate table dimCrime

insert into dimCrime (CrimebizKey, Vehicle, Burglary, Robbery, Larceny, Violent) 
select 
	distinct crime as CrimebizKey,
	iif(crime like '%FROM VEHICLE'
		or crime like ('%AUTO THEFT'),'Y','N') as Vehicle,
	iif(crime like '%BURGLARY%', 'Y','N') as Burglary,
	iif(Crime like '%ROBBERY%', 'Y','N') as Robbery,
	iif(Crime like '%LARCENY%', 'Y', 'N') as Larceny,
	iif(Crime in ('HOMICIDE', 'RAPE', 'AGG ASSAULT'), 'Y', 'N') as Violent

from crime

select * from dimCrime