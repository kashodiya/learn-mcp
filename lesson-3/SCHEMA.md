# Chinook Database Schema

This document describes the schema of the Chinook SQLite database.

## Album

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| AlbumId | INTEGER | True | True |  |
| Title | NVARCHAR(160) | True | False |  |
| ArtistId | INTEGER | True | False |  |

### Foreign Keys

| Column | References | On Delete | On Update |
|--------|------------|-----------|----------|
| ArtistId | Artist(ArtistId) | NO ACTION | NO ACTION |

### Sample Data

| AlbumId | Title | ArtistId |
|---|---|---|
| 1 | For Those About To Rock We Salute You | 1 |
| 2 | Balls to the Wall | 2 |
| 3 | Restless and Wild | 2 |
| 4 | Let There Be Rock | 1 |
| 5 | Big Ones | 3 |


## Artist

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| ArtistId | INTEGER | True | True |  |
| Name | NVARCHAR(120) | False | False |  |

### Sample Data

| ArtistId | Name |
|---|---|
| 1 | AC/DC |
| 2 | Accept |
| 3 | Aerosmith |
| 4 | Alanis Morissette |
| 5 | Alice In Chains |


## Customer

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| CustomerId | INTEGER | True | True |  |
| FirstName | NVARCHAR(40) | True | False |  |
| LastName | NVARCHAR(20) | True | False |  |
| Company | NVARCHAR(80) | False | False |  |
| Address | NVARCHAR(70) | False | False |  |
| City | NVARCHAR(40) | False | False |  |
| State | NVARCHAR(40) | False | False |  |
| Country | NVARCHAR(40) | False | False |  |
| PostalCode | NVARCHAR(10) | False | False |  |
| Phone | NVARCHAR(24) | False | False |  |
| Fax | NVARCHAR(24) | False | False |  |
| Email | NVARCHAR(60) | True | False |  |
| SupportRepId | INTEGER | False | False |  |

### Foreign Keys

| Column | References | On Delete | On Update |
|--------|------------|-----------|----------|
| SupportRepId | Employee(EmployeeId) | NO ACTION | NO ACTION |

### Sample Data

| CustomerId | FirstName | LastName | Company | Address | City | State | Country | PostalCode | Phone | Fax | Email | SupportRepId |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Luís | Gonçalves | Embraer - Empresa Brasileira de Aeronáutica S.A. | Av. Brigadeiro Faria Lima, 2170 | São José dos Campos | SP | Brazil | 12227-000 | +55 (12) 3923-5555 | +55 (12) 3923-5566 | luisg@embraer.com.br | 3 |
| 2 | Leonie | Köhler | None | Theodor-Heuss-Straße 34 | Stuttgart | None | Germany | 70174 | +49 0711 2842222 | None | leonekohler@surfeu.de | 5 |
| 3 | François | Tremblay | None | 1498 rue Bélanger | Montréal | QC | Canada | H2G 1A7 | +1 (514) 721-4711 | None | ftremblay@gmail.com | 3 |
| 4 | Bjørn | Hansen | None | Ullevålsveien 14 | Oslo | None | Norway | 0171 | +47 22 44 22 22 | None | bjorn.hansen@yahoo.no | 4 |
| 5 | František | Wichterlová | JetBrains s.r.o. | Klanova 9/506 | Prague | None | Czech Republic | 14700 | +420 2 4172 5555 | +420 2 4172 5555 | frantisekw@jetbrains.com | 4 |


## Employee

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| EmployeeId | INTEGER | True | True |  |
| LastName | NVARCHAR(20) | True | False |  |
| FirstName | NVARCHAR(20) | True | False |  |
| Title | NVARCHAR(30) | False | False |  |
| ReportsTo | INTEGER | False | False |  |
| BirthDate | DATETIME | False | False |  |
| HireDate | DATETIME | False | False |  |
| Address | NVARCHAR(70) | False | False |  |
| City | NVARCHAR(40) | False | False |  |
| State | NVARCHAR(40) | False | False |  |
| Country | NVARCHAR(40) | False | False |  |
| PostalCode | NVARCHAR(10) | False | False |  |
| Phone | NVARCHAR(24) | False | False |  |
| Fax | NVARCHAR(24) | False | False |  |
| Email | NVARCHAR(60) | False | False |  |

### Foreign Keys

| Column | References | On Delete | On Update |
|--------|------------|-----------|----------|
| ReportsTo | Employee(EmployeeId) | NO ACTION | NO ACTION |

### Sample Data

| EmployeeId | LastName | FirstName | Title | ReportsTo | BirthDate | HireDate | Address | City | State | Country | PostalCode | Phone | Fax | Email |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Adams | Andrew | General Manager | None | 1962-02-18 00:00:00 | 2002-08-14 00:00:00 | 11120 Jasper Ave NW | Edmonton | AB | Canada | T5K 2N1 | +1 (780) 428-9482 | +1 (780) 428-3457 | andrew@chinookcorp.com |
| 2 | Edwards | Nancy | Sales Manager | 1 | 1958-12-08 00:00:00 | 2002-05-01 00:00:00 | 825 8 Ave SW | Calgary | AB | Canada | T2P 2T3 | +1 (403) 262-3443 | +1 (403) 262-3322 | nancy@chinookcorp.com |
| 3 | Peacock | Jane | Sales Support Agent | 2 | 1973-08-29 00:00:00 | 2002-04-01 00:00:00 | 1111 6 Ave SW | Calgary | AB | Canada | T2P 5M5 | +1 (403) 262-3443 | +1 (403) 262-6712 | jane@chinookcorp.com |
| 4 | Park | Margaret | Sales Support Agent | 2 | 1947-09-19 00:00:00 | 2003-05-03 00:00:00 | 683 10 Street SW | Calgary | AB | Canada | T2P 5G3 | +1 (403) 263-4423 | +1 (403) 263-4289 | margaret@chinookcorp.com |
| 5 | Johnson | Steve | Sales Support Agent | 2 | 1965-03-03 00:00:00 | 2003-10-17 00:00:00 | 7727B 41 Ave | Calgary | AB | Canada | T3B 1Y7 | 1 (780) 836-9987 | 1 (780) 836-9543 | steve@chinookcorp.com |


## Genre

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| GenreId | INTEGER | True | True |  |
| Name | NVARCHAR(120) | False | False |  |

### Sample Data

| GenreId | Name |
|---|---|
| 1 | Rock |
| 2 | Jazz |
| 3 | Metal |
| 4 | Alternative & Punk |
| 5 | Rock And Roll |


## Invoice

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| InvoiceId | INTEGER | True | True |  |
| CustomerId | INTEGER | True | False |  |
| InvoiceDate | DATETIME | True | False |  |
| BillingAddress | NVARCHAR(70) | False | False |  |
| BillingCity | NVARCHAR(40) | False | False |  |
| BillingState | NVARCHAR(40) | False | False |  |
| BillingCountry | NVARCHAR(40) | False | False |  |
| BillingPostalCode | NVARCHAR(10) | False | False |  |
| Total | NUMERIC(10,2) | True | False |  |

### Foreign Keys

| Column | References | On Delete | On Update |
|--------|------------|-----------|----------|
| CustomerId | Customer(CustomerId) | NO ACTION | NO ACTION |

### Sample Data

| InvoiceId | CustomerId | InvoiceDate | BillingAddress | BillingCity | BillingState | BillingCountry | BillingPostalCode | Total |
|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 2009-01-01 00:00:00 | Theodor-Heuss-Straße 34 | Stuttgart | None | Germany | 70174 | 1.98 |
| 2 | 4 | 2009-01-02 00:00:00 | Ullevålsveien 14 | Oslo | None | Norway | 0171 | 3.96 |
| 3 | 8 | 2009-01-03 00:00:00 | Grétrystraat 63 | Brussels | None | Belgium | 1000 | 5.94 |
| 4 | 14 | 2009-01-06 00:00:00 | 8210 111 ST NW | Edmonton | AB | Canada | T6G 2C7 | 8.91 |
| 5 | 23 | 2009-01-11 00:00:00 | 69 Salem Street | Boston | MA | USA | 2113 | 13.86 |


## InvoiceLine

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| InvoiceLineId | INTEGER | True | True |  |
| InvoiceId | INTEGER | True | False |  |
| TrackId | INTEGER | True | False |  |
| UnitPrice | NUMERIC(10,2) | True | False |  |
| Quantity | INTEGER | True | False |  |

### Foreign Keys

| Column | References | On Delete | On Update |
|--------|------------|-----------|----------|
| TrackId | Track(TrackId) | NO ACTION | NO ACTION |
| InvoiceId | Invoice(InvoiceId) | NO ACTION | NO ACTION |

### Sample Data

| InvoiceLineId | InvoiceId | TrackId | UnitPrice | Quantity |
|---|---|---|---|---|
| 1 | 1 | 2 | 0.99 | 1 |
| 2 | 1 | 4 | 0.99 | 1 |
| 3 | 2 | 6 | 0.99 | 1 |
| 4 | 2 | 8 | 0.99 | 1 |
| 5 | 2 | 10 | 0.99 | 1 |


## MediaType

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| MediaTypeId | INTEGER | True | True |  |
| Name | NVARCHAR(120) | False | False |  |

### Sample Data

| MediaTypeId | Name |
|---|---|
| 1 | MPEG audio file |
| 2 | Protected AAC audio file |
| 3 | Protected MPEG-4 video file |
| 4 | Purchased AAC audio file |
| 5 | AAC audio file |


## Playlist

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| PlaylistId | INTEGER | True | True |  |
| Name | NVARCHAR(120) | False | False |  |

### Sample Data

| PlaylistId | Name |
|---|---|
| 1 | Music |
| 2 | Movies |
| 3 | TV Shows |
| 4 | Audiobooks |
| 5 | 90’s Music |


## PlaylistTrack

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| PlaylistId | INTEGER | True | True |  |
| TrackId | INTEGER | True | True |  |

### Foreign Keys

| Column | References | On Delete | On Update |
|--------|------------|-----------|----------|
| TrackId | Track(TrackId) | NO ACTION | NO ACTION |
| PlaylistId | Playlist(PlaylistId) | NO ACTION | NO ACTION |

### Sample Data

| PlaylistId | TrackId |
|---|---|
| 1 | 3402 |
| 1 | 3389 |
| 1 | 3390 |
| 1 | 3391 |
| 1 | 3392 |


## Track

### Schema

| Column | Type | Not Null | Primary Key | Default |
|--------|------|----------|-------------|--------|
| TrackId | INTEGER | True | True |  |
| Name | NVARCHAR(200) | True | False |  |
| AlbumId | INTEGER | False | False |  |
| MediaTypeId | INTEGER | True | False |  |
| GenreId | INTEGER | False | False |  |
| Composer | NVARCHAR(220) | False | False |  |
| Milliseconds | INTEGER | True | False |  |
| Bytes | INTEGER | False | False |  |
| UnitPrice | NUMERIC(10,2) | True | False |  |

### Foreign Keys

| Column | References | On Delete | On Update |
|--------|------------|-----------|----------|
| MediaTypeId | MediaType(MediaTypeId) | NO ACTION | NO ACTION |
| GenreId | Genre(GenreId) | NO ACTION | NO ACTION |
| AlbumId | Album(AlbumId) | NO ACTION | NO ACTION |

### Sample Data

| TrackId | Name | AlbumId | MediaTypeId | GenreId | Composer | Milliseconds | Bytes | UnitPrice |
|---|---|---|---|---|---|---|---|---|
| 1 | For Those About To Rock (We Salute You) | 1 | 1 | 1 | Angus Young, Malcolm Young, Brian Johnson | 343719 | 11170334 | 0.99 |
| 2 | Balls to the Wall | 2 | 2 | 1 | None | 342562 | 5510424 | 0.99 |
| 3 | Fast As a Shark | 3 | 2 | 1 | F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman | 230619 | 3990994 | 0.99 |
| 4 | Restless and Wild | 3 | 2 | 1 | F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider & W. Hoffman | 252051 | 4331779 | 0.99 |
| 5 | Princess of the Dawn | 3 | 2 | 1 | Deaffy & R.A. Smith-Diesel | 375418 | 6290521 | 0.99 |


