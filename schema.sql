DROP TABLE IF EXISTS guestbook;

CREATE TABLE guestbook (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    sentiment TEXT NOT NULL
);
