import json


def create_json(result, filename="market_report.json"):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    return filename