import pandas as pd


# Load the JSON file into a DataFrame
df = pd.read_json('ExampleFile/v2_Cards.json')


def populate_item_dict(df):
    df = df.transpose()

    id_to_name = df['InternalName'].to_dict()

    name_to_id = {v: k for k, v in id_to_name.items()}
    df = df.transpose()

    return name_to_id, id_to_name

name_to_id, id_to_name = populate_item_dict(df)

def get_card_obj_by_name(name):
    card_id = name_to_id[name]

    card_obj = df[card_id]

    return card_obj

print(get_card_obj_by_name('Rainbow Potion'))


