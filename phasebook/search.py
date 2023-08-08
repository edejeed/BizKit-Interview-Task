from flask import Blueprint, request, jsonify

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    search_result = search_users(request.args.to_dict())
    return jsonify(search_result), 200

def search_users(args):
    filtered_users = []

    if "id" in args:
        user_with_id = next((user for user in USERS if user["id"] == args["id"]), None)
        if user_with_id:
            filtered_users.append(user_with_id)

    if "name" in args:
        name_filter = args["name"].lower()
        filtered_users.extend(user for user in USERS if name_filter in user["name"].lower())

    if "age" in args:
        age_filter = int(args["age"])
        filtered_users.extend(user for user in USERS if age_filter - 1 <= user["age"] <= age_filter + 1)

    if "occupation" in args:
        occupation_filter = args["occupation"].lower()
        filtered_users.extend(user for user in USERS if occupation_filter in user["occupation"].lower())

    # Remove duplicates from the filtered_users list
    unique_filtered_users = []
    for user in filtered_users:
        if user not in unique_filtered_users:
            unique_filtered_users.append(user)

    # Sort the unique_filtered_users list based on priority
    sorted_users = sorted(unique_filtered_users, key=lambda user: (
        "id" in args and user["id"] == args["id"],
        "name" in args and name_filter in user["name"].lower(),
        "age" in args and age_filter - 1 <= user["age"] <= age_filter + 1,
        "occupation" in args and occupation_filter in user["occupation"].lower()
    ), reverse=True)

    return sorted_users
