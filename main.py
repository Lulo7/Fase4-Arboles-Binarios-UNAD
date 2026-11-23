from views.login_view import LoginView
from views.tree_view import TreeView
from controllers.login_controller import LoginController


def main():

    login_view = LoginView()

    def open_main_window():

        login_view.withdraw()

        TreeView(login_view)

    login_controller = LoginController(
        view=login_view,
        on_success=open_main_window
    )

    login_view.set_login_command(
        login_controller.authenticate
    )

    login_view.mainloop()


if __name__ == "__main__":
    main()