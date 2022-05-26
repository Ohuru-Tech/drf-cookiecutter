# TODO change this when we cumpolsate email confirmation
user_registration_201_example = {
    "application/json": {
        "key": "2e9d235fa499d7e52a5bffe9879897989",
        "user": {
            "id": 1,
            "name": "John Doe",
            "email": "user@example.com",
            "account_type": "general",
            "profile_pic": "some_name.jpg",
        },
    }
}

user_registration_400_example = {
    "application/json": {
        "email": ["A user is already registered with this e-mail address"],
        "password1": ["This password is too common."],
    }
}


user_login_400_example = {
    "application/json": {
        "non_field_errors": ["Unable to log in with provided credentials."]
    }
}

user_login_200_example = {
    "application/json": {
        "key": "2e9d235fa499d7e52a5bffe9879897989",
        "user": {
            "id": 1,
            "name": "John Doe",
            "email": "user@example.com",
            "account_type": "general",
            "profile_pic": "some_name.jpg",
        },
    }
}

user_logout_200_example = {
    "application/json": {"detail": "Successfully logged out."}
}

user_logout_401_example = {"application/json": {"detail": "Invalid token."}}

user_password_reset_200_example = {
    "application/json": {"detail": "Password reset e-mail has been sent"}
}

user_password_reset_400_example = {
    "application/json": {
        "detail": "The user with the given email does not exist"
    }
}

user_password_reset_confirm_200_example = {
    "application/json": {
        "detail": "Password has been reset with the new password."
    }
}

user_password_reset_confirm_400_example = {
    "application/json": {"token": ["Invalid Value"]}
}


user_password_set_200_example = {
    "application/json": {"detail": "New password has been saved."}
}

user_password_set_401_example = {
    "application/json": {"detail": "Invalid token"}
}
