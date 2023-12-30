

def admins(admins: dict) -> str:
    """sort admins

    args:
        admins (typing.List[AdminsDatabase]): all admins crud

    returns:
    ```log
        айди: 1
        аккаунт: влад (@vladdd00)
        добавлен: 2023-06-03 20:47:39.809876
    ```
    """
    row = []

    for admin in admins["admins"]:
        id = admin["id"]
        username = admin["username"]
        full_name = admin["full_name"]
        created_at = admin["created_at"]
        row.append(
            f"айди: <code>{id}</code>\n"
            f"аккаунт: {full_name} (@{username})\n"
            f"добавлен: <code>{created_at}</code>\n",
        )
    return "\n".join(row)
