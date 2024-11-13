import hashlib
import time


# Класс для пользователей
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хэширование пароля
        self.age = age

    def __str__(self):
        return f"User(nickname={self.nickname}, age={self.age})"


# Класс для видео
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"


# Класс для платформы UrTube
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        # Поиск пользователя по nickname и password
        for user in self.users:
            if user.nickname == nickname and user.password == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                print(f"Добро пожаловать, {self.current_user.nickname}!")
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        # Проверка на существующего пользователя
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add(self, *videos):
        for video in videos:
            if all(v.title != video.title for v in self.videos):  # Проверка на уникальность названия
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    def get_videos(self, search_word):
        # Поиск видео по ключевому слову
        search_word = search_word.lower()
        return [v.title for v in self.videos if search_word in v.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Поиск видео по точному названию
        video = next((v for v in self.videos if v.title == title), None)

        if not video:
            print(f"Видео '{title}' не найдено")
            return

        # Проверка на возрастное ограничение
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Воспроизведение видео
        for i in range(video.duration):
            print(i + 1, end=" ", flush=True)
            time.sleep(1)  # Эмуляция воспроизведения (паузу можно регулировать по необходимости)
        print("\nКонец видео")

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')