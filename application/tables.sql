CREATE TABLE `quizes` (
  `quiz_id` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL
);
CREATE TABLE `questions` (
  `quiz_id` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `question_id` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `question` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ans` varchar(1) COLLATE utf8mb4_unicode_ci DEFAULT NULL
);
CREATE TABLE `choices` (
  `question_id` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `choice` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL
);
CREATE TABLE `results` (
  `quiz_id` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `a` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `b` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `c` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `d` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `grade` float DEFAULT NULL
);
INSERT INTO `quizes`
VALUES ("quiz1");
INSERT INTO `questions`
VALUES ("quiz1", "q1", "What is 2+2?", "4");
INSERT INTO `questions`
VALUES ("quiz1", "q2", "What belongs to AWS?", "EC2");
INSERT INTO `choices`
VALUES ("q1", "4");
INSERT INTO `choices`
VALUES ("q1", "5");
INSERT INTO `choices`
VALUES ("q1", "6");
INSERT INTO `choices`
VALUES ("q2", "S33");
INSERT INTO `choices`
VALUES ("q2", "Google");
INSERT INTO `choices`
VALUES ("q2", "EC2");