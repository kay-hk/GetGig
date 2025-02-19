DROP DATABASE IF EXISTS getgig;
CREATE DATABASE getgig;
USE getgig;

-- Genre Table
CREATE TABLE genre (
    gid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    gname VARCHAR(255)
);

-- Artist Table
CREATE TABLE artist (
    aid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    aname VARCHAR(255) NOT NULL
);

-- Artist-Genre Association Table
CREATE TABLE artist_genre (
    aid INT,
    gid INT,
    PRIMARY KEY (aid, gid),
    FOREIGN KEY (aid) REFERENCES artist(aid) ON DELETE CASCADE,
    FOREIGN KEY (gid) REFERENCES genre(gid) ON DELETE CASCADE
);

-- City Table
CREATE TABLE city (
    cid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    cname VARCHAR(255) NOT NULL
);

-- Festival Table
CREATE TABLE festival (
    fid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    fname VARCHAR(255) NOT NULL,
    cid INT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    poster VARCHAR(255),
    description VARCHAR(500),
    playlist VARCHAR(500),
    FOREIGN KEY (cid) REFERENCES city(cid) ON DELETE SET NULL
);

-- Festival-Artist Association Table
CREATE TABLE festival_artist (
    fid INT,
    aid INT,
    PRIMARY KEY (fid, aid),
    FOREIGN KEY (fid) REFERENCES festival(fid) ON DELETE CASCADE,
    FOREIGN KEY (aid) REFERENCES artist(aid) ON DELETE CASCADE
);

CREATE TABLE user_festival {
    fid int,
    uid int,
    PRIMARY KEY (fid, uid),
    FOREIGN KEY (fid) REFERENCES festival(fid),
    FOREIGN KEY (uid) REFERENCES user(id),
}

CREATE TABLE user_artist {
    aid int,
    uid int,
    PRIMARY KEY (aid, uid),
    FOREIGN KEY (aid) REFERENCES artist(aid),
    FOREIGN KEY (uid) REFERENCES user(id),
}

CREATE TABLE tickettype (
    id SERIAL PRIMARY KEY,
    ticket_type_name VARCHAR(20) UNIQUE NOT NULL,
    ticket_price DECIMAL(10,2) NOT NULL
);

CREATE TABLE ticket (
    tid SERIAL PRIMARY KEY,
    fid INT NOT NULL,
    ticket_type_id INT NULL,
    ticket_quantity INT NOT NULL DEFAULT 1,
    total_price DECIMAL(10,2) NULL,
    ticket_date DATE NULL,
    uemail INT NULL,
    FOREIGN KEY (fid) REFERENCES festival(id) ON DELETE CASCADE,
    FOREIGN KEY (ticket_type_id) REFERENCES tickettype(id) ON DELETE CASCADE,
    FOREIGN KEY (uemail) REFERENCES auth_user(id) ON DELETE CASCADE
);
