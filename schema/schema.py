from voluptuous import Schema, PREVENT_EXTRA

create_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_successfully = Schema(
    {
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_unsuccessfully = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)
