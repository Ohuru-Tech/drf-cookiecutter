profile_update_200_example = {
    "application/json": {
        "id": 1,
        "name": "Test developer",
        "profile_pic": "/some_pic.jpg"
    },
}

profile_update_401_example = {
    "application/json": {
        "error": "NotAuthenticated",
        "detail": "Incorrect authentication credentials.",  # noqa
    }
}

profile_update_403_example = {
    "application/json": {
        "error": "PermissionDenied",
        "detail": "You do not have permission to perform this action."
    }
}
