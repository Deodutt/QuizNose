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
