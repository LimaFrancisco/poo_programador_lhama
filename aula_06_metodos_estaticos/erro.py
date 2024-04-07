class Error:

    @staticmethod
    def error_500():
        print("Internal server error")

    @staticmethod
    def error_404():
        print("Not Found")

Error.error_404()