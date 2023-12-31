# REST API Документация

Данный репозиторий содержит код для REST API, который предоставляет функциональность для управления каталогом продуктов, корзиной покупок, заказами и профилями пользователей.

## Каталог Продуктов

### Получение списка всех категорий
- URL: `/categories/`
- Метод: `GET`
- Описание: Получение списка всех категорий продуктов.

### Получение списка продуктов с фильтрами
- URL: `/catalog/`
- Метод: `GET`
- Описание: Получение списка продуктов с фильтрами по категории и цене.

### Получение списка популярных продуктов
- URL: `/catalog/popular/`
- Метод: `GET`
- Описание: Получение списка популярных продуктов.

### Получение списка продуктов с ограниченным количеством
- URL: `/catalog/limited/`
- Метод: `GET`
- Описание: Получение списка продуктов с ограниченным количеством.

### Получение списка продуктов со скидкой
- URL: `/sales/`
- Метод: `GET`
- Описание: Получение списка продуктов со скидкой.

### Получение списка баннерных продуктов
- URL: `/banners/`
- Метод: `GET`
- Описание: Получение списка баннерных продуктов.

### Получение списка всех тегов продуктов
- URL: `/tags/`
- Метод: `GET`
- Описание: Получение списка всех тегов продуктов.

### Получение детальной информации о продукте
- URL: `/product/<id>/`
- Метод: `GET`
- Описание: Получение детальной информации о продукте по его идентификатору.

### Добавление отзыва о продукте
- URL: `/product/<id>/review/`
- Метод: `POST`
- Описание: Добавление отзыва о продукте и обновление рейтинга продукта.

## Управление Корзиной и Заказами

### Получение содержимого корзины
- URL: `/basket/`
- Метод: `GET`
- Описание: Получение содержимого корзины пользователя.

### Создание заказа в корзине
- URL: `/basket/`
- Метод: `POST`
- Описание: Создание заказа в корзине.

### Очистка корзины
- URL: `/basket/`
- Метод: `DELETE`
- Описание: Очистка корзины пользователя.

### Получение списка заказов
- URL: `/orders/`
- Метод: `GET`
- Описание: Получение списка заказов.

### Создание нового заказа
- URL: `/orders/`
- Метод: `POST`
- Описание: Создание нового заказа.

### Получение, обновление и удаление детальной информации о заказе
- URL: `/orders/<order_id>/`
- Методы: `GET`, `PUT`, `DELETE`
- Описание: Получение, обновление и удаление детальной информации о заказе по его идентификатору.

## Аутентификация и Профили Пользователей

### Аутентификация пользователя
- URL: `/sign-in/`
- Метод: `POST`
- Описание: Аутентификация пользователя по логину и паролю.

### Регистрация нового пользователя
- URL: `/sign-up/`
- Метод: `POST`
- Описание: Регистрация нового пользователя.

### Выход пользователя
- URL: `/sign-out/`
- Метод: `POST`
- Описание: Выход пользователя из системы.

### Получение и обновление профиля пользователя
- URL: `/profile/`
- Методы: `GET`, `POST`
- Описание: Получение и обновление информации о профиле пользователя.

### Смена пароля пользователя
- URL: `/change-password/`
- Метод: `POST`
- Описание: Смена пароля пользователя.

## Оплата заказов

### Обработка платежа для заказа
- URL: `/payment/`
- Метод: `POST`
- Описание: Обработка платежа для заказа.

## Сериализаторы

В репозитории также содержатся сериализаторы для различных моделей, которые описывают, как данные сериализуются и десериализуются.

- `CategorySerializer`: Сериализатор для категорий продуктов.
- `SubcategorySerializer`: Сериализатор для подкатегорий продуктов.
- `ProductSerializer`: Сериализатор для продуктов.
- `ReviewSerializer`: Сериализатор для отзывов о продуктах.
- `SpecificationSerializer`: Сериализатор для характеристик продуктов.
- `TagSerializer`: Сериализатор для тегов продуктов.
- `OrderSerializer`: Сериализатор для заказов.
- `BasketSerializer`: Сериализатор для корзины покупок.
- `SignInSerializer`: Сериализатор для аутентификации.
