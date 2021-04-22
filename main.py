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
DROP TABLE IF EXISTS `cities`;
''',
    '''CREATE TABLE `cities` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL
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
  `status` TEXT NOT NULL,
  `day` TEXT NOT NULL,
  `temp_min` INTEGER DEFAULT NULL,
  `temp_max` INTEGER DEFAULT NULL,
  FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`)
);
''',
    '''
PRAGMA foreign_keys = ON;
'''
]

for sql in arr:
    print(sql)
    connect.execute(sql)

connect.commit()
