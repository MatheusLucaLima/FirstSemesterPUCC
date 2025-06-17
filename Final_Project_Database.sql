/*CREATE DATABASE projeto_bd1;*/
/*This is the final project for Database course.
It was created by a group of 5 students, including me.
This is the original version of the project, there is not any additional changes.
*/

USE projeto_bd1;

CREATE TABLE profile (
    id_user INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(20),
    address VARCHAR(150),
    city VARCHAR(100),
    state VARCHAR(2),
    phone VARCHAR(15) UNIQUE,
    dob DATE,
    logged_devices INT
    );

CREATE TABLE movies (
	id_movie VARCHAR(5) PRIMARY KEY,
    name VARCHAR(150),
    genre VARCHAR(100),
    duration_min DECIMAL(5, 2),
    director VARCHAR(100),
    age_rating INT,
    stars_rating FLOAT,
    original_audio VARCHAR(100)
    );
    
CREATE TABLE series (
	id_series VARCHAR(5) PRIMARY KEY,
    name VARCHAR(150),
    genre VARCHAR(100),
	season INT,
    episode INT,
    director VARCHAR(100),
    age_rating INT,
    stars_rating FLOAT,
    original_audio VARCHAR(100)
    );
    
CREATE TABLE payments (
	id_payment INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT UNIQUE,
    address VARCHAR(150),
    payment_method VARCHAR(50),
    coupon VARCHAR(7) DEFAULT NULL,
    auto_pay BOOLEAN DEFAULT FALSE,
    plan VARCHAR(60),
    total DECIMAL(5,2),
    payed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_user) REFERENCES profile(id_user)
    );
    
CREATE TABLE views (
	id_view INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT,
    id_movie VARCHAR(5) DEFAULT NULL,
    id_series VARCHAR(5) DEFAULT NULL,
    time_watched_min DECIMAL(5, 2),
    completed BOOLEAN NOT NULL,
    given_review INT,
    FOREIGN KEY (id_user) REFERENCES profile(id_user),
    FOREIGN KEY (id_movie) REFERENCES movies(id_movie),
    FOREIGN KEY (id_series) REFERENCES series(id_series)
    );



INSERT INTO profile (name, email, password, address, city, state, phone, dob, logged_devices)
VALUES 
	('Ana Beatriz Silva', 'ana@uol.com.br', 'ana12345', 'Rua Almirante, 34', 'Campinas', 'SP', '(19) 99999-8888', '1977-06-18', 2),
    ('João Ferreira', 'joao@yahoo.com.br', 'joao1234', 'Av. Brasil, 35', 'São Roque', 'SP', '(15) 94444-5555', '2000-01-15', 1),
    ('Luana Pedrosa', 'luana@gmail.com', 'OvoPodre123', 'Rua Carlos Penteado, 651', 'São Paulo', 'SP', '(11) 3333-4444', '1987-05-20', 4),
    ('Fernando Maldivas', 'fernandinho21@gmail.com', 'King159', 'Rua Dr. Jucelino, 101', 'Joinville', 'SC', '(47) 96545-1015', '2008-11-28', 3),
    ('José Pereira', 'jose@hotmail.com', 'JosePereira1534', 'Rua Eduardo Fernandes, 10', 'Ponta Grossa', 'PR', '(42) 96585-1010', '1995-07-21', 4),
    ('Maria Julia Carrara', 'juju_2010@gmail.com', 'Juzinha123', 'Rua Francisco da Cunha, 568', 'Barretos', 'SP', '(17) 91342-6575', '2010-03-17', 3),
    ('Guilherme da Costa', 'guilherme@yahoo.com.br', 'Mel!1423', 'Rua Guilherme Andrade, 44', 'Rio de Janeiro', 'RJ', '(21) 96548-3025', '1998-04-23', 2),
    ('Natalino Lima', 'natal_lima@gmail.com', 'N4t4l1n0', 'Rua Heitor Penteado, 98', 'Belo Horizonte', 'MG', '(31) 97415-2016', '1973-12-24', 5),
    ('Gabriel da Cunha', 'gabriel_cunha@empresa.com.br', 'Josefina123', 'Av. Tiradentes, 186', 'São José dos Pinhais', 'PR', '(41) 91234-5432', '1989-10-31', 3),
    ('Bruna Pedrosa', 'bru_pedrosa@gmail.com', 'Durval45', 'Rua Maria Conceição, 123', 'Porto Alegre', 'RS', '(51) 98787-4245', '2005-02-26', 2),
    ('Gustavo Andrade', 'gustavinho96@hotmail.com', 'gugu4321', 'Rua Pablo Gentili, 95', 'Brasília', 'DF', '(61) 5248-6147', '1996-09-24', 2),
    ('Giovanna Fernandes', 'giovanna@gmail.com', 'Giovanna040801', 'Rua Padre José, 68', 'Salvador', 'BA', '(71) 96728-9465', '2001-08-04', 5),
    ('Matheus Oliveira', 'matheus_oliveira@gmail.com', 'T3teu5', 'Av. Norte Sul, 72', 'Olinda', 'PE', '(81) 94578-3597', '2003-05-12', 3),
    ('Bruna de Lucca', 'bruna_lucca@firma.com.br', 'Bruna123*', 'Av. Independência, 654', 'São Paulo', 'SP', '(11) 98547-1254', '2002-02-14', 4),
    ('Pedro Barbosa', 'pedro_barbosa@gmail.com', 'Pepe*95', 'Rua Francisco Pontes, 1098', 'São José dos Pinhais', 'PR', '(41) 3562-4157', '1995-11-23', 3),
    ('Mariana Pontes', 'mari_pontes@gmail.com', 'Fifi6754', 'Rua Mario José, 53', 'Campinas', 'SP', '(19) 96324-3485', '1997-12-02', 2),
    ('Lucas Rocha', 'lucas_rocha88@hotmail.com', 'Luc4a5R0ch4', 'Rua Riachuelo, 113', 'Manaus', 'AM', '(92) 98547-6790', '1988-09-21', 4),
    ('Regina Borges', 'princesa_re@uol.com.br', 'Prin86!', 'Av. Pacífico, 9845', 'Jaguariúna', 'SP', '(19) 3222-4433', '1990-10-10', 3);
  
SELECT*FROM profile;  
  
INSERT INTO movies (id_movie, name, genre, duration_min, director, age_rating, stars_rating, original_audio) 
VALUES
    ('F0001', 'The Godfather', 'Drama', 175, 'Francis Ford Coppola', 18, 4.2, 'English'),
    ('F0002', 'Interstellar', 'Science Fiction', 169, 'Christopher Nolan', 12, 3.6, 'English'),
    ('F0003', 'Parasite', 'Thriller', 132, 'Bong Joon-ho', 16, 4.5, 'Korean'),
    ('F0004', 'Fight Club', 'Drama', 139, 'David Fincher', 18, 3.8, 'English'),
    ('F0005', 'Spirited Away', 'Fantasy', 125, 'Hayao Miyazaki', 10, 4.6, 'Japanese'),
    ('F0006', 'City of God', 'Crime', 130, 'Fernando Meirelles', 18, 4.4, 'Portuguese'),
    ('F0007', 'The Lord of the Rings: The Return of the King', 'Fantasy', 201, 'Peter Jackson', 12, 4.2, 'English'),
    ('F0008', 'Pulp Fiction', 'Crime', 154, 'Quentin Tarantino', 18, 4.9, 'English'),
    ('F0009', 'The Wolf of Wall Street', 'Comedy', 180, 'Martin Scorsese', 18, 4.8, 'English'),
    ('F0010', 'Joker', 'Thriller', 122, 'Todd Phillips', 16, 3.9, 'English'),
    ('F0011', 'Forrest Gump', 'Romance', 142, 'Robert Zemeckis', 12, 3.7, 'English'),
    ('F0012', 'Matrix', 'Action', 136, 'Lana e Lilly Wachowski', 14, 4.5, 'English'),
    ('F0013', 'Titanic', 'Romance', 194, 'James Cameron', 12, 4.0, 'English'),
    ('F0014',  'The Departed', 'Thriller', 151, 'Martin Scorsese', 16, 4.4, 'English'),
    ('F0015',  'Gladiator', 'Action', 155, 'Ridley Scott', 16, 4.3, 'English'),
    ('F0016', 'Duna', 'Science Fiction', 155, 'Denis Villeneuve', 14, 3.7, 'English'),
    ('F0017', 'The Irishman', 'Drama', 209, 'Martin Scorsese', 18, 3.3, 'English'),
    ('F0018', 'Drive', 'Drama', 100, 'Nicolas Winding Refn', 18, 3.8, 'English');

SELECT*FROM movies;  
  
INSERT INTO series (id_series, name, genre, season, episode, director, age_rating, stars_rating, original_audio) 
VALUES 
    ('S6244','Grey''s Anatomy', 'Drama', 21, 448, 'Shonda Rhimes', 14, 4.7, 'English'),
    ('S4613','Orange is the New Black', 'Drama', 7, 91, 'Piper Kerman', 18, 3.3, 'English'),
    ('S5284','Sex Education', 'Drama', 4, 32, 'Laurie Nunn', 18, 1.2, 'English'),
    ('S9401','Elite', 'Drama', 8, 64, 'Carlos Montero', 18, 1.6, 'Spanish'),
    ('S3910','Rick and Morty', 'Animation', 8, 71, 'Justin Roiland', 14, 4.4, 'English'),
    ('S5834','Pokémon', 'Animation', 20, 1315, 'Satoshi Tajiri', 0, 4.4, 'Japanese'),
    ('S8194','The Looney Tunes Show', 'Animation', 2, 52, 'Spike Brandt', 0, 4.0, 'English'),
    ('S0525','Jorel''s Brother', 'Animation', 5, 121, 'Juliano Enrico', 0, 5.0, 'Portuguese'),
    ('S7428','Carrossel', 'Soap Opera', 1, 310, 'Iris Abravanel', 10, 3.5, 'Portuguese'),
    ('S4853','Chiquititas', 'Soap Opera', 1, 545, 'Iris Abravanel', 10, 3.7, 'Portuguese'),
    ('S7319','Malhação: Viva a Diferença', 'Soap Opera', 1, 213, 'Caio Hamburgo', 12, 3.4, 'Portuguese'),
    ('S1023','Amor à Vida', 'Soap Opera', 1, 221, 'Walcyr Carrasco', 14, 4.8, 'Portuguese'),
    ('S3678','The Big Bang Theory', 'Comedy', 12, 279, 'Chuck Lorre', 12, 5.0, 'English'),
    ('S7657','Glee', 'Comedy', 6, 121, 'Ryan Murphy', 0, 1.0, 'English'),
    ('S8246','iCarly', 'Comedy', 5, 97, 'Dan Schneider', 0, 5.0, 'English'),
    ('S1823','Gossip Girl', 'Comedy', 6, 121, 'Josh Schwartz', 16, 2.4, 'English'),
    ('S8557','All of Us Are Dead', 'Horror', 1, 12, 'Chun Sung-li', 16, 2.9, 'Korean'),
    ('S4275','The Walking Dead', 'Horror', 11, 177, 'Frank Darabont', 18, 1.8, 'English'),
    ('S3551','Supermax', 'Horror', 1, 12, 'José Alvarenga Jr.', 18, 0.7, 'Portuguese'),
    ('S9285','Sweet Home', 'Horror', 3, 12, 'Kim Seol-jin', 18, 3.8, 'Korean');  
    
SELECT*FROM series;
    
INSERT INTO payments (id_user, address, payment_method, coupon, auto_pay, plan, total, payed)
VALUES
 (1, 'Rua Almirante, 34', 'Payment Slip', 'SAVE10', DEFAULT, 'Standard', 0, TRUE),
 (2, 'Av. Brasil, 35', 'Debit Card', DEFAULT, TRUE, 'Premium', 0, TRUE),
 (3, 'Rua Carlos Penteado, 651', 'Gift Card', DEFAULT, DEFAULT, 'Standard with Ads', 29.90, DEFAULT),
 (4, 'Rua Dr.Jucelino, 101', 'Credit Card', 'QUERO1', DEFAULT, 'Basic with Ads', 0, TRUE),
 (5, 'Rua Eduardo Fernandes, 10', 'Debit Card', DEFAULT, TRUE, 'Premium', 179.70, DEFAULT),
 (6, 'Rua Francisco da Cunha, 568', 'Pix', DEFAULT, DEFAULT, 'Standard', 79.80, DEFAULT),
 (7, 'Rua Guilherme Andrade, 44', 'Direct Deposit', DEFAULT, TRUE, 'Standard with Ads', 0, TRUE),
 (8, 'Rua Heitor Penteado, 98', 'Credit Card', DEFAULT, DEFAULT, 'Basic with Ads', 0, TRUE),
 (9, 'Av. Tiradentes, 186', 'Payment Slip', DEFAULT, DEFAULT, 'Premium', 59.90, DEFAULT),
 (10, 'Rua Maria Conceição, 123', 'Gift Card', DEFAULT, DEFAULT, 'Basic with Ads', 19.90, DEFAULT),
 (11, 'Rua Pablo Gentili, 95', 'Pix', 'PROMO1', DEFAULT, 'Standard', 0, TRUE),
 (12, 'Rua Padre José, 68', 'Direct Deposit', DEFAULT, TRUE, 'Premium', 0, TRUE),
 (13, 'Av. Norte Sul, 72', 'Payment Slip', DEFAULT, DEFAULT, 'Standard with Ads', 59.80, DEFAULT),
 (14, 'Av, Independência, 654', 'Credit Card', 'CODIG1', DEFAULT, 'Standard', 0, TRUE),
 (15, 'Rua Francisco Pontes, 1098', 'Debit Card', DEFAULT, TRUE, 'Basic with Ads', 19.90, DEFAULT),
 (16, 'Rua Mario José, 53', 'Gift Card', DEFAULT, DEFAULT, 'Premium', 0, TRUE),
 (17, 'Rua Riachuelo, 113', 'Direct Deposit', DEFAULT, TRUE, 'Standard with Ads', 89.70, DEFAULT),
 (18, 'Av. Pacífico 9845', 'Payment Slip', DEFAULT, DEFAULT, 'Premium', 0, TRUE);

SELECT*FROM payments;

INSERT INTO views (id_user, id_movie, id_series, time_watched_min, completed, given_review)
VALUES
	(12, 'F0010', DEFAULT, 122, TRUE, 3.1), 
	(5, DEFAULT, 'S1823', 45, FALSE, 4.4), 
	(17, 'F0004', DEFAULT, 139, TRUE, 1.0), 
	(3, DEFAULT, 'S3678', 80, FALSE, 3.6), 
	(8, DEFAULT, 'S4275', 177, TRUE, 5.0), 
	(14, DEFAULT, 'S9401', 32, FALSE, 4.0), 
	(1, DEFAULT, 'S3678', 279, TRUE, 5.0), 
	(16, 'F0012', DEFAULT, 136, TRUE, 2.3), 
	(7, 'F0011', DEFAULT, 71, FALSE, 2.7), 
	(9, DEFAULT, 'S8557', 12, FALSE, 4.4), 
	(4, DEFAULT, 'S9285', 8, FALSE, 2.4), 
	(10, 'F0010', DEFAULT, 122, TRUE, 1.3), 
	(18, DEFAULT, 'S3551', 12, FALSE, 1.0), 
	(2, 'F0005', DEFAULT, 125, TRUE, 1.1), 
	(13, 'F0003', DEFAULT, 132, TRUE, 5.0), 
	(6, 'F0001', DEFAULT, 175, TRUE, 0.7), 
	(15, 'F0009', DEFAULT, 90, FALSE, 0.0), 
	(11, 'F0008', DEFAULT, 77, FALSE, 4.9); 
    
SELECT*FROM views;

/* Users that owe money */
SELECT profile.name AS user_name, payments.total AS amount_owed
FROM payments
JOIN profile ON profile.id_user = payments.id_user
WHERE total > 0;

/* Cupons used */ 
SELECT payments.coupon AS coupon, COUNT(*) total
FROM payments
GROUP BY payments.coupon;

/* Alphabetical order of users */
SELECT name
FROM profile
ORDER BY name;

/* Logged devices exceeding limits */
SELECT id_user, name, logged_devices
FROM profile
WHERE logged_devices > 4;

/* New movie watched*/
INSERT INTO views (id_user, id_movie, id_series, time_watched_min, clompleted, given_review)
VALUES (6, 'F0008', DEFAULT, 154, TRUE, 4.8);

/* Show only under 18 rated movies to minors */
SELECT movies.name AS movie, movies.age_rating AS rating
FROM movies
WHERE age_rating < 18;

/* Show only under 18 rated series to minors */
SELECT series.name AS series, series.age_rating AS rating
FROM series
WHERE age_rating < 18;

/* Watch again list for 'João Ferreira' */
SELECT movies.name AS movie, series.name AS series
FROM views
LEFT JOIN movies ON movies.id_movie = views.id_movie
LEFT JOIN series ON series.id_series = views.id_series
JOIN profile ON profile.id_user = views.id_user
WHERE views.completed = TRUE AND profile.name = 'João Ferreira';

/* Counting types of plans */
SELECT payments.plan AS plan, COUNT(*) AS total
FROM payments
GROUP BY payments.plan
ORDER BY total DESC;

/* New movies in streaming */
INSERT INTO movies (id_movie, name, genre, duration_min, director, age_rating, stars_rating, original_audio) 
VALUES
	('F0019', 'I`m still here', 'Biography', 135, 'Walter Salles', 14, 5, 'Portuguese'),
	('F0020', 'Emilia Pérez', 'Musical', 130, 'Jacques Audiard', 16, 1.7, 'Spanish'),
	('F0021', 'REC', 'Horror', 78, 'Jaume Balagueró', 16, 1.7, 'Spanish'),
	('F0022', 'Central Station', 'Drama', 115, 'Walter Salles', 14, 4.9, 'Portuguese'),
	('F0023', 'Vitória', 'Biography', 112, 'Andrucha Waddington', 14, 4.7, 'Portuguese'),
	('F0024', 'The Substance', 'Horror', 101, 'Coralie Fargeat', 14, 4.5, 'English'),
	('F0025', 'A Minecraft Movie', 'Comedy', 140, 'Jared Hess', 10, 3.2, 'English');

/* Users that haven't finished watching movies/series */
SELECT id_user, id_movie, id_series
FROM views
WHERE completed = FALSE;

/* Continue watching for 'Gustavo Andrade' */
SELECT movies.name AS movie, series.name AS series
FROM views
LEFT JOIN movies ON movies.id_movie = views.id_movie
LEFT JOIN series ON series.id_series = views.id_series
JOIN profile ON profile.id_user = views.id_user
WHERE views.completed = FALSE AND profile.name = 'Gustavo Andrade';

/* Series with higher ratings */
SELECT series.name AS series, series.stars_rating AS rating
FROM series
WHERE stars_rating > 4;

/* Movies by genre */
SELECT movies.genre AS genre, COUNT(*) AS total
FROM movies
GROUP BY movies.genre
ORDER BY total DESC; 

/* Series by genre */
SELECT series.genre AS genre, COUNT(*) AS total
FROM series
GROUP BY series.genre
ORDER BY total DESC;

/* New users */
INSERT INTO profile(name, email, password, address, city, state, phone, dob, logged_devices)
VALUES
    ('Eduardo Souza', 'duardo_01@gmail.com', 'dudu0109', 'Rua Maranhão, 694', 'Ubatatuba', 'SP', '(12) 98764-5324', '1998-02-11',3),
    ('Leandro Albuquerque', 'leandro_albu@hotmail.com', '1811leandro', 'Rua Buenos Aires, 300', 'Sumaré', 'SP', '(19) 98412-2425', '1994-01-18',1),
    ('Daniel Batista', 'danibati@yahoo.com.br', 'b4tist489', 'Rua José Albino, 542', 'São José dos Campos', 'SP', '(12) 95421-6675', '1970-08-30',4);

/* New payment registrations */
INSERT INTO payments (id_user, address, payment_method, coupon, auto_pay, plan, total, payed)
VALUES 
	(19, 'Rua Maranhão, 694', 'Pix', DEFAULT, FALSE, 'Premium', 59.90, FALSE),
    (20, 'Rua Buenos Aires, 300', 'Debit card', 'SAVE10', TRUE, 'Standard with Adds', 0, TRUE),
    (21, 'Rua José Albino, 542', 'Direct Deposit', DEFAULT, TRUE, 'Basic with Adds', 0, TRUE);

/* See how many users have each city/state */
SELECT profile.city AS city, profile.state AS state, COUNT(*) AS total
FROM profile
GROUP BY profile.city, profile.state
ORDER BY total DESC;


/* New series */
INSERT INTO series (id_series, name, genre, season, episode, director, age_rating, stars_rating, original_audio) 
VALUES 
    ('S2834','Crash Landing on You', 'Drama', 1, 16, 'Park Ji-eun', 12, 4.3, 'Korean'),
    ('S6432','Squid Game', 'Horror', 2, 16, 'Hwang Dong-hyuk', 18, 2.3, 'Korean'),
    ('S5632','Violetta', 'Soap Opera', 3, 240, 'Jorge Nisco', 0, 1.2, 'Spanish'),
    ('S3832','Usurper', 'Soap Opera', 1, 120, 'Carlos Romero', 14, 3.3, 'Spanish'),
    ('S4932','Back to 15', 'Drama', 3, 120, 'Bruna Vieira', 12, 4.7, 'Portuguese');
    
/* New views */
INSERT INTO views (id_user, id_movie, id_series, time_watched_min, completed, given_review)
VALUES
	(2, 'F0013', DEFAULT, 97, FALSE, 1.1), 
	(11, DEFAULT, 'S4613', 45, FALSE, 4.9), 
	(13, DEFAULT, 'S5284', 16, FALSE, 5.0), 
	(7, 'F0012', DEFAULT, 68, FALSE, 2.7), 
	(5, 'F0015', DEFAULT, 155, TRUE, 4.7), 
	(12, DEFAULT, 'S3910', 35, FALSE, 3.1), 
	(3, 'F0003', DEFAULT, 66, FALSE, 3.6), 
	(16, 'F0002', DEFAULT, 84, FALSE, 2.3), 
	(10, 'F0006', DEFAULT, 130, TRUE, 1.3), 
	(4, 'F0010', DEFAULT, 61, FALSE, 2.4), 
	(14, 'F0016', DEFAULT, 77, FALSE, 4.0), 
	(9, 'F0017', DEFAULT, 104, FALSE, 4.4), 
	(1, 'F0007', DEFAULT, 100, FALSE, 4.5), 
	(8, 'F0008', DEFAULT, 77, FALSE, 5.0), 
	(17, DEFAULT, 'S3551', 6, FALSE, 1.0), 
	(6, DEFAULT, 'S7428', 155, FALSE, 0.7), 
	(15, DEFAULT, 'S1023', 110, TRUE, 4.2), 
	(18, 'F0013', DEFAULT, 97, FALSE, 1.0), 
	(2, DEFAULT, 'S6244', 150, FALSE, 1.1), 
	(1, DEFAULT, 'S6244', 224, FALSE, 5.0), 
	(17, 'F0018', DEFAULT, 100, TRUE, 1.0);

/* Most watched movies and series */
SELECT movies.name AS movie, series.name AS series
FROM views
LEFT JOIN movies ON movies.id_movie = views.id_movie
LEFT JOIN series ON series.id_series = views.id_series
WHERE views.completed = TRUE;

/* Latin movies */ 
SELECT movies.name AS movie, movies.stars_rating AS stars, movies.original_audio AS language
FROM movies
WHERE movies.original_audio LIKE 'Portuguese' OR movies.original_audio LIKE 'Spanish';

/* Latin series */ 
SELECT series.name AS series, series.stars_rating AS stars, series.original_audio AS language
FROM series
WHERE series.original_audio LIKE 'Portuguese' OR series.original_audio LIKE 'Spanish';

/* Short movies (less than 120 min) */ 
SELECT movies.name AS movie, movies.duration_min AS total
FROM movies
WHERE duration_min < 120
ORDER BY duration_min DESC;

/* Series with higher ratings */
SELECT movies.name AS movie, movies.stars_rating AS rating
FROM movies
WHERE stars_rating > 4;

