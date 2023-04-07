class URL:
    BASE_URL = "https://qastand.valhalla.pw/"
    LOGIN_URL = f"{BASE_URL}login"
    MAIN_URL = f"{BASE_URL}profile"


class AuthData:
    VALID_AUTH_DATA = {
        "login": "qa_test@test.ru",
        "password": "!QAZ2wsx"
    }

    INVALID_AUTH_DATA = [
        ("", "!QAZ2wsx"),
        ("qa_test@test.ru", ""),
        ("qa_testtest.ru", "!QAZ2wsx"),
        ("qwerty@qwerty.com", "dsfsdfbihew")
    ]

    NEGATIVE_TESTS_IDS = [
        "empty_login",
        "empty_password",
        "no @ in email",
        "don't registration user"
    ]



