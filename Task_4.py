import doctest


class SocialNetworks:
    """
    Базовый класс для социальных сетей.
    """

    def __init__(self, name: str, platform: str):
        """
        Инициализирует экземпляр социальной сети.

        Args:
            name (str): Название социальной сети.
            platform (str): Платформа, на которой работает социальная сеть.
        """
        self.name = name
        self.platform = platform

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.

        Returns:
            str: Строковое представление социальной сети.
        """
        return f"{self.name} - {self.platform}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление социальной сети.

        Returns:
            str: Строковое представление социальной сети.
        """
        return f"{self.__class__.__name__}(name='{self.name}', platform='{self.platform}')"


class VK(SocialNetworks):
    """
    Дочерний класс, представляющий социальную сеть ВКонтакте.
    """

    def __init__(self, name: str, platform: str, username: str):
        """
        Инициализирует экземпляр ВКонтакте.

        Args:
            name (str): Название социальной сети.
            platform (str): Платформа, на которой работает социальная сеть.
            username (str): Имя пользователя, связанное с аккаунтом ВКонтакте.
        """
        super().__init__(name, platform)
        self.username = username

    def create_post(self, content: str):
        """
        Создает новый пост на стене ВКонтакте.

        Args:
            content (str): Содержимое поста.

        Example:
            vk = VK('ВКонтакте', 'Web', 'user123')
            vk.create_post('Привет, мир!')
        """
        print(f"Создание нового поста на стене ВКонтакте от имени пользователя {self.username}")

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети ВКонтакте.

        Returns:
            str: Строковое представление социальной сети ВКонтакте.
        """
        return f"{self.name} - {self.platform} (Имя пользователя: {self.username})"


class Facebook(SocialNetworks):
    """
    Дочерний класс, представляющий социальную сеть Facebook.
    """

    def __init__(self, name: str, platform: str, user_id: str):
        """
        Инициализирует экземпляр Facebook.

        Args:
            name (str): Название социальной сети.
            platform (str): Платформа, на которой работает социальная сеть.
            user_id (str): Идентификатор пользователя, связанный с аккаунтом Facebook.
        """
        super().__init__(name, platform)
        self.user_id = user_id

    def create_post(self, content: str):
        """
        Создает новый пост на стене Facebook.

        Args:
            content (str): Содержимое поста.

        Example:
            fb = Facebook('Facebook', 'Web', '1234567890')
            fb.create_post('Hello, world!')
        """
        print(f"Creating a new post on Facebook wall with user ID: {self.user_id}")

    def get_friends(self) -> list:
        """
        Возвращает список друзей пользователя на Facebook.

        Returns:
            list: Список друзей пользователя.

        Example:
            fb = Facebook('Facebook', 'Web', '1234567890')
            friends = fb.get_friends()
            print(friends)
        """
        friends = ["Friend 1", "Friend 2", "Friend 3"]
        return friends

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети Facebook.

        Returns:
            str: Строковое представление социальной сети Facebook.
        """
        return f"{self.name} - {self.platform}(Пользовательский код для создания и использования объектов)"


"""

vk = VK('ВКонтакте', 'Web', 'user123')
print(vk)  # ВКонтакте - Web (Имя пользователя: user123)
vk.create_post('Привет, мир!')
# Создание нового поста на стене ВКонтакте от имени пользователя user123

fb = Facebook('Facebook', 'Web', '1234567890')
print(fb)  # Facebook - Web
friends = fb.get_friends()
print(friends)  # ['Friend 1', 'Friend 2', 'Friend 3']
fb.create_post('Hello, world!')
# Creating a new post on Facebook wall with user ID: 1234567890

"""

if __name__ == "__main__":
    doctest.testmod()
    pass
