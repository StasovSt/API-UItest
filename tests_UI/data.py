
class AuthData:
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



