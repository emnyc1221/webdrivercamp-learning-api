import json

def to_json(data):
    try:
        return json.dumps(data)  # Converts Python data to a JSON-formatted string
    except TypeError:
        return None  # Or raise an exception, depending on your needs

if __name__ == "__main__":
    data_types = [[1, 2, 3, 4, 5],
                  (1, 2, 3, 4, 5),
                  "Hello World!",
                  False,
                  None,
                  123,
                  3.14,
                  {"abc": True, "Hello": "World", 10: [2, 3, 4]},
                  {"a", "b", "c"}]
    try:
        for data in data_types:
            json_data = to_json(data)
            if json_data is not None:
                print(f"{f'{data}:':40} {type(data).__name__:10} => {json_data}: {type(json_data).__name__}")
            else:
                print(f"ERROR:\n\t{data}: {type(data).__name__} => Not JSON serializable")
    except Exception as e:
        print("ERROR:")
        print(f"\t{data}: {type(data).__name__} => {e}")
