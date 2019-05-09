use kimtest;


-- create a comic book 
-- table with 6 fields
CREATE TABLE comic_books_${PUT_YOUR_FNAME_HERE} (
	primary_id int auto_increment primary key,
    comic_title varchar(255),
    comic_issue int,
    comic_publisher_id int,
    comic_value decimal,
--     `value` float --opt alt version of comic_value
    issue_date date
) engine=INNODB;

