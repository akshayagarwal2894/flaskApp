CREATE DATABASE appname;

/* Create tables as required */
CREATE TABLE `appname`.`tbl_user` (
  `user_id` BIGINT AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` text NULL,
  `user_password` text NULL,
  PRIMARY KEY (`user_id`));

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(20),
    IN p_username text,
    IN p_password text
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;


