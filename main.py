import youtube


def compile_id_string(id_set):
    id_string = ""

    for link_id in id_set:
        id_string += link_id + ","

    return id_string


if __name__ == '__main__':

    ids_to_validate = {
        "g_FTlm3sdq12tdoU",
        "g_FTlm3tdoU"
    }

    youtube_service = youtube.dev_auth("config/dev_key.txt")

    request = youtube_service.videos().list(
        part="player",
        id=compile_id_string(ids_to_validate)
    )

    response = request.execute()

    valid_ids = set()
    for item in response.get("items"):
        valid_ids.add(item.get("id"))

    invalid_ids = set.difference(ids_to_validate, valid_ids)
    print(f"These are invalid ids : {invalid_ids}")
