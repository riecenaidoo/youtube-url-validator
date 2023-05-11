import youtube


def compile_id_string(id_set):
    id_string = ""

    for link_id in id_set:
        id_string += link_id + ","

    return id_string


def check_response_for_valid_ids(response):

    valid_ids = set()
    for item in response.get("items"):
        valid_ids.add(item.get("id"))
    return valid_ids


def send_request(ids_to_validate):

    youtube_service = youtube.dev_auth("config/dev_key.txt")

    request = youtube_service.videos().list(
        part="player",
        id=compile_id_string(ids_to_validate)
    )
    response = request.execute()
    return response


def final_validation(ids_to_validate):
    response = send_request(ids_to_validate)
    valid_ids = check_response_for_valid_ids(response)
    invalid_ids = set.difference(ids_to_validate, valid_ids)
    print(f"These are invalid ids : {invalid_ids}")


