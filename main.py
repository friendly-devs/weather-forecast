import sqlite3

connect = sqlite3.connect('sql.db')

arr = [
'''
DROP TABLE IF EXISTS users;
''',
'''
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  UNIQUE(username)
);
''',
'''
INSERT INTO `users` VALUES (1,'admin','123456');
''',
'''
drop table if exists `cities`;
''',
'''CREATE TABLE `cities` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar(256) NOT NULL
);
''',
'''
INSERT INTO `cities` VALUES (1,'Ha Noi'),(2,'HCM');
''',
'''
DROP TABLE IF EXISTS `weathers`;
''',
'''
CREATE TABLE `weathers` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `city_id` INTEGER NOT NULL,
  `status` varchar(256) NOT NULL,
  `day` date NOT NULL,
  `temp_min` int DEFAULT NULL,
  `temp_max` int DEFAULT NULL,
  FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`)
);
'''
]

for sql in arr:
    print(sql)
    connect.execute(sql)

connect.commit()
