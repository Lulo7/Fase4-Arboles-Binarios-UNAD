class LoginController:

    PASSWORD = "UNAD"

    def __init__(self, view, on_success):
        self.view = view
        self.on_success = on_success

    def authenticate(self):

        password = self.view.get_password()

        if password == self.PASSWORD:

            self.view.show_success(
                "Access granted successfully."
            )

            self.on_success()

        else:

            self.view.show_error(
                "Incorrect password. Please try again."
            )