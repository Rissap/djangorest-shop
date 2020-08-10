-- --------------------------------------------------------
-- Хост:                         D:\Projects\djangorest-shop\django\db.sqlite3
-- Версия сервера:               3.30.1
-- Операционная система:         
-- HeidiSQL Версия:              11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Дамп данных таблицы main.main_post: -1 rows
/*!40000 ALTER TABLE "main_post" DISABLE KEYS */;
INSERT INTO "main_post" ("id", "title") VALUES
	(1, 'Cashier'),
	(2, 'Booker'),
	(3, 'Consultant');
/*!40000 ALTER TABLE "main_post" ENABLE KEYS */;

-- Дамп данных таблицы main.main_product: -1 rows
/*!40000 ALTER TABLE "main_product" DISABLE KEYS */;
INSERT INTO "main_product" ("id", "title", "created_at", "updated_at", "price") VALUES
	(1, 'Electric Kettle', '2020-08-08 21:45:40.911612', '2020-08-08 21:45:40.911612', 126.05),
	(2, 'Steam iron dry', '2020-08-08 21:46:01.872811', '2020-08-08 21:46:01.872811', 750.5),
	(3, 'Usb lamp', '2020-08-08 21:46:14.650542', '2020-08-08 21:46:14.650542', 89),
	(4, 'Juice Blender', '2020-08-08 21:46:35.147714', '2020-08-08 21:46:35.147714', 840.49),
	(5, 'Clock', '2020-08-08 21:46:59.286095', '2020-08-08 21:47:08.850642', 25.99);
/*!40000 ALTER TABLE "main_product" ENABLE KEYS */;

-- Дамп данных таблицы main.main_sales: -1 rows
/*!40000 ALTER TABLE "main_sales" DISABLE KEYS */;
INSERT INTO "main_sales" ("id", "types", "priority", "coef") VALUES
	(1, 'old', 2, 0.8);
/*!40000 ALTER TABLE "main_sales" ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
