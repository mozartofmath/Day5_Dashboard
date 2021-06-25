CREATE TABLE IF NOT EXISTS `TweetInformation` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `clean_text` TEXT DEFAULT NULL,
    `polarity` FLOAT DEFAULT NULL,
    `subjectivity` FLOAT DEFAULT NULL,
    PRIMARY KEY (`id`)
);
