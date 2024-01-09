def read_recipes(filename):
    recipes = {}
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()

            i += 1
            if not dish_name:
                continue

            if i >= len(lines):
                break

            ingredients_count = int(lines[i].strip())
            i += 1
            dish_ingredients = []

            for _ in range(ingredients_count):
                if i >= len(lines):
                    break
                ingredient_info = lines[i].strip().split("|")
                ingredient = {
                    "ingredient_name": ingredient_info[0].strip(),
                    "quantity": int(ingredient_info[1].strip()),
                    "measure": ingredient_info[2].strip(),
                }
                dish_ingredients.append(ingredient)
                i += 1

            recipes[dish_name] = dish_ingredients
            i += 1

    return recipes


def get_shop_list_by_dishes(culinary_book, dishes, person_count):
    shop_list_result = {}
    for dish in dishes:
        if dish in culinary_book:
            for ingredient in culinary_book[dish]:
                name = ingredient["ingredient_name"]
                measure = ingredient["measure"]
                quantity_per_person = ingredient["quantity"] * person_count
                if name not in shop_list_result:
                    shop_list_result[name] = {
                        "measure": measure,
                        "quantity": quantity_per_person,
                    }
                else:
                    shop_list_result[name]["quantity"] += quantity_per_person
    return shop_list_result


def main():
    filename = "recipes.txt"
    culinary_book = read_recipes(filename)
    if culinary_book is not None:
        print(culinary_book)

        dishes_to_cook = ["Запеченный картофель", "Омлет"]
        person_count = 2

        shop_list = get_shop_list_by_dishes(culinary_book, dishes_to_cook, person_count)
        print(shop_list)


if __name__ == "__main__":
    main()
