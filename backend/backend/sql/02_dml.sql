INSERT INTO genre (gname)
VALUES ('Pop'),
    ('Rock'),
    ('Metal'),
    ('Punk'),
    ('Electronic'),
    ('Hip-Hop'),
    ('Indie'),
    ('Folk'),
    ('Reggae'),
    ('World'),
    ('R&B'),
    ('Alternative'),
    ('Jazz'),
    ('Soul');
insert into city (cname)
values -- download
    ('Donington'), -- isle of wight
    ('Newport'),
    -- reading
    ('Reading'),
    -- latitude
    ('Southwold'),
    -- boomtown
    ('Winchester'),
    -- kendall calling
    ('Penrith'),
    -- terminal v 
    ('Edinburgh'),
    -- brick lane jazz 
    ('London'),
    -- victorious
    ('Portsmouth'),
    -- trnsmt
    ('Glasgow');
INSERT INTO artist (aname)
VALUES -- download
    ('Green Day'),
    ('Sleep Token'),
    ('Korn'),
    -- isle of wight
    ('Sting'), -- latitude
    ('Stereophonics'),
    ('Justin Timberlake'),
    -- reading 
    ('Travis Scott'),
    ('Chappell Roan'),
    ('Bring Me The Horizon'),
    ('Hozier'),
    -- latitude
    ('Fatboy Slim'), -- kendall calling
    ('Snow Patrol'), -- trnsmt
    ('Basement Jaxx'),
    ('Elbow'),
    -- boomtown fair
    ('Maribou State'),
    ('Sean Paul'),
    ('Sex Pistols featuring Frank Carter'),
    -- kendall calling
    ('Kaiser Chiefs'),
    ('Courteeners'),
    ('The Prodigy'),
    -- terminal v
    ('999999999'),
    ('AK Sports'),
    ('Adrian Mills'),
    -- brick lane jazz
    ('Laraaji'),
    ('Adi Oasis'),
    ('Ragz Originale'),
    -- victorious
    ('Queens of the Stone Age'),
    ('Vampire Weekend'),
    ('Kings of Leon'),
    -- trnsmt
    ('50 Cent'),
    ('Biffy Clyro');
INSERT INTO artist_genre (aid, gid)
VALUES -- download
    (1, 2),
    -- Green Day mapped to Rock
    (1, 4),
    -- Green Day mapped to Punk
    (2, 3),
    -- Sleep Token mapped to Metal
    (2, 2),
    -- Sleep Token mapped to Rock
    (3, 3),
    -- Korn mapped to Metal
    (3, 2),
    -- Korn mapped to Rock
    -- isle of wight
    (4, 1),
    (4, 2),
    (5, 2),
    (5, 7),
    (6, 1),
    (6, 11),
    -- reading
    (7, 6),
    (8, 1),
    (9, 1),
    (9, 2),
    (10, 7),
    (10, 8),
    -- latitude
    (11, 5),
    (12, 2),
    (12, 7),
    (13, 5),
    (14, 2),
    (14, 12),
    -- boomtown fair 
    (15, 5),
    (16, 9),
    (16, 11),
    (17, 2),
    (17, 4),
    -- kendall calling
    (18, 2),
    (18, 7),
    (19, 7),
    (20, 5),
    (20, 12),
    -- terminal v
    (21, 5),
    (22, 5),
    (23, 5),
    -- brick lane jazz
    (24, 13),
    (25, 11),
    (25, 14),
    (26, 6),
    (26, 11),
    -- victorious
    (27, 2),
    (27, 12),
    (28, 1),
    (28, 7),
    (29, 2),
    (29, 12),
    -- trnsmt
    (30, 6),
    (31, 2),
    (31, 12);

insert into festival (fname, cid, start_date, end_date, poster, description, playlist) values
('DOWNLOAD', 1, '2025-06-13', '2025-06-15',
 'https://downloadfestival.co.uk/wp-content/uploads/2024/11/DXXII-admat-900x1273.jpg',
 'Set against the legendary backdrop of Donington Park, Download Festival transforms the historic motorsport circuit into a seismic stage where earth‐shattering rock and metal acts ignite the crowd and unbridled, rebellious energy unites fans for an unforgettable, headbanging celebration.',
 'https://open.spotify.com/embed/playlist/5qvf0i5CfUV0X3GChlj8Pl?utm_source=generator'),
('ISLE OF WIGHT', 2, '2025-06-19', '2025-06-22',
 'https://cdn.isleofwightfestival.com/assets/images/gallery/IOW2025-Anno-4x5-Web_2025-01-29-080905_xmpg.png',
 'Escape to the Isle of Wight for a festival packed with legendary artists, beautiful scenery, and an unforgettable seaside vibe. A true summer celebration!',
 'https://open.spotify.com/embed/playlist/4zJm1vHL6owBFKpsv6RJw0?utm_source=generator'),
('READING AND LEEDS', 3, '2025-08-21', '2025-08-24',
 'https://www.readingfestival.com/wp-content/uploads/2024/12/Reading25-Portrait-Web-900x1125.jpg',
 'Join one of the UK''s most iconic music festivals, featuring top rock, alternative, and pop acts. Experience three days of incredible performances and an electrifying atmosphere.',
 'https://open.spotify.com/embed/playlist/1cqpAb6sBZ5H45DhQXTeVs?utm_source=generator'),
('LATITUDE', 4, '2025-07-24', '2025-07-27',
 'https://www.latitudefestival.com/wp-content/uploads/2025/01/LAT25_Third-Announcement_14-01-1200x2133.png',
 'Discover a mix of music, arts, and comedy at Latitude Festival, set in the picturesque Suffolk countryside. Perfect for the whole family!',
 'https://open.spotify.com/embed/playlist/6YFXo6EyLb96lB3DI36bxT?utm_source=generator'),
('BOOMTOWN FAIR', 5, '2025-08-06', '2025-08-10',
 'https://cdn.prod.website-files.com/66fbea41b5ef08dc592dbf06/6798b3749907301a7267643b_small.jpg',
 'Immerse yourself in the unique world of Boomtown Fair, where music, theatre, and art collide to create an unforgettable experience like no other.',
 'https://open.spotify.com/embed/playlist/3yZyHIPVPorLcqlgYCGJHq?utm_source=generator'),
('KENDAL CALLING', 6, '2025-07-31', '2025-08-03',
 'https://cdn.kendalcalling.co.uk/KC25-4X5-7am.png',
 'Set in the Lake District, Kendal Calling combines great music, stunning scenery, and a warm community spirit for an unforgettable festival experience.',
 'https://open.spotify.com/embed/playlist/3cJDTjMh0eUw52Kam3IhBy?utm_source=generator'),
('TERMINAL V', 7, '2025-04-19', '2025-04-20',
 'https://terminalv.co.uk/festival/wp-content/uploads/sites/4/2025/01/Lineup-Story-3.jpg',
 'Terminal V transforms the Scottish festival experience into an immersive journey through techno''s past, present, and future. Set in Edinburgh at The Royal Highland Centre, Terminal V blends cutting-edge electronic music with vibrant art, intimate boat parties, and legendary after-hours gatherings – all amidst Scotland''s dynamic urban backdrop for an unforgettable celebration of sound and community.',
 'https://open.spotify.com/embed/playlist/1Q8uMRbE5HEwL8Zp8LqAs8?utm_source=generator'),
('BRICK LANE JAZZ', 8, '2025-04-25', '2025-04-27',
 '_',
 'Bringing together London''s vibrant underground music community for three days at the iconic Truman Brewery site and beyond, Brick Lane Jazz Festival will return in 2025, showcasing some of the most exciting new and established acts on the scene today.',
 'https://open.spotify.com/embed/playlist/2JvPBCJVVQzcRjsB5pwHgy?utm_source=generator'),
('VICTORIOUS', 9, '2025-08-22', '2025-08-24',
 'https://d2utmtmc4jckg3.cloudfront.net/wp-content/uploads/2025/02/VF25_Release-2_4x5.png',
 'Set against the stunning backdrop of Portsmouth''s Southsea Common, Victorious Festival transforms the iconic seaside venue into a vibrant celebration where world-class music, comedy, and family-friendly entertainment merge with coastal charm to create an unforgettable experience.',
 'https://open.spotify.com/embed/playlist/6BQLKKEnSgstCf8ERb2Pnb?utm_source=generator'),
('TRANSMT', 10, '2025-07-11', '2025-07-13',
 'https://trnsmt-dev.ams3.cdn.digitaloceanspaces.com/theme/images/site/2025/T25-LINEUP-WEB-POSTER.jpg',
 'Set in the heart of Glasgow, TRNSMT transforms the iconic Glasgow Green into a dynamic stage where cutting-edge music, urban energy, and deep-rooted Scottish pride converge to create an unforgettable festival experience.',
 'https://open.spotify.com/embed/playlist/6ZQuYeeifxYy5nZ86NF1VH?utm_source=generator');

insert into festival_artist (fid,aid) values
(1,1),
(1,2),
(1,3),
(2,4),
(2,5),
(2,6),
(3,7),
(3,8),
(3,9),
(3,10),
(4,4),
(4,11),
(4,12),
(4,13),
(4,14),
(5,15),
(5,16),
(5,17),
(6,11),
(6,18),
(6,19),
(6,20),
(7,21),
(7,22),
(7,23),
(8,24),
(8,25),
(8,26),
(9,27),
(9,28),
(9,29),
(10,12),
(10,30),
(10,31);

insert into tickettype (ticket_type_name,ticket_price) values
('Camping',50),
('Non-Camping',30),
('VIP',100);