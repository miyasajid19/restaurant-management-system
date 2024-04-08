This restaurant management system, developed using Tkinter, encompasses key functionalities such as order processing and room reservation management for existing guests in the database. Although there is potential to incorporate additional features such as integrating room details and menus into the database, the primary emphasis has been on maintaining the entirety of the project within a single file and managing code length, which exceeds 700 lines. Consequently, while the DRY (Don't Repeat Yourself) principle hasn't been fully adhered to, and the code predominantly follows a procedural paradigm. It is presumed that the requisite databases and tables have been pre-established for the program's operation.

INTERFACES

![Screenshot 2024-04-08 183950](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/56e63767-e809-45bc-8ea6-45061083011f)

![Screenshot 2024-04-08 184007](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/5cb2ca96-fbed-4364-bc1d-e5352b544236)

![Screenshot 2024-04-08 184047](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/1e89eb70-892c-4505-8bef-8c3ccf40cef9)

![Screenshot 2024-04-08 184101](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/069b2554-d9f5-46c8-b8a0-b1300bab0a6c)

![Screenshot 2024-04-08 184121](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/9e9daf51-68a1-4b14-a51e-006e4b06364c)

![Screenshot 2024-04-08 184208](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/1aa9852d-09d4-435e-befc-28340311702f)

![Screenshot 2024-04-08 184301](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/3926d479-a8fc-4afe-a53c-9d52eb622cb7)

![Screenshot 2024-04-08 184314](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/91fe59f7-d72b-4dc3-a204-65b4acefe67c)

![Screenshot 2024-04-08 184336](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/672c88bb-98ed-43e1-91e5-403276762de2)

![Screenshot 2024-04-08 184507](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/7f795e57-d3c7-4925-8011-f35403cd9168)

![Screenshot 2024-04-08 184518](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/791879bf-8068-42d3-9996-3a0608801cff)

![Screenshot 2024-04-08 184547](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/e6a62799-dac0-424c-9619-4189e13c73a4)

![Screenshot 2024-04-08 184655](https://github.com/miyasajid19/restaurant-management-system/assets/166320427/84d20aa4-b994-4ebd-b847-ffcbc64ac27b)


CREATING DATABASE

    CREATE DATABASE restaurantmanagementsystem

CREATING TABLE FOR MENU


    CREATE TABLE Menu (
        MenuItemID INT PRIMARY KEY,
        MenuItemName VARCHAR(255) NOT NULL,
        Description TEXT,
        Category VARCHAR(50),
        Price DECIMAL(10, 2),
        Ingredients TEXT,
        Availability BOOLEAN,
        PreparationTime INT,
        Calories INT,
        SpecialInformation VARCHAR(100),
        MenuItemImage VARCHAR(255),
        MenuItemRating FLOAT,
    );


INSERTING DUMMY DATA TO MENU


    INSERT INTO `menu`(`MenuItemID`, `MenuItemName`, `Description`, `Category`, `Price`, `Ingredients`, `Availability`, `PreparationTime`, `Calories`, `SpecialInformation`, `MenuItemImage`, `MenuItemRating`) VALUES
    (1, 'Spaghetti Carbonara', 'Classic Italian pasta dish with creamy sauce, bacon, and parmesan cheese', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Spaghetti, Bacon, Eggs, Parmesan Cheese, Black Pepper, Olive Oil', FLOOR(1 + RAND() * (10 - 1)), 20, 700, NULL, 'food_images/1.jpg', 4.5),
    (2, 'Caesar Salad', 'Crisp romaine lettuce with Caesar dressing, croutons, and parmesan cheese', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Romaine Lettuce, Caesar Dressing, Croutons, Parmesan Cheese', FLOOR(1 + RAND() * (10 - 1)), 10, 350, 'Vegetarian', 'food_images/2.jpg', 4.2),
    (3, 'Margherita Pizza', 'Traditional Italian pizza with tomato sauce, mozzarella cheese, and fresh basil', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Pizza Dough, Tomato Sauce, Mozzarella Cheese, Fresh Basil, Olive Oil', FLOOR(1 + RAND() * (10 - 1)), 25, 900, 'Vegetarian', 'food_images/margherita_pizza.jpeg', 4.3),
    (4, 'Chocolate Lava Cake', 'Warm chocolate cake with a gooey chocolate center, served with vanilla ice cream', 'Dessert', FLOOR(500 + RAND() * (1500 - 500)), 'Flour, Sugar, Cocoa Powder, Butter, Eggs, Vanilla Extract, Chocolate Chips, Vanilla Ice Cream', FLOOR(1 + RAND() * (10 - 1)), 15, 500, NULL, 'food_images/chocolate_lava_cake.jpg', 4.8),
    (5, 'Grilled Salmon', 'Grilled salmon fillet seasoned with herbs and lemon butter sauce', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Salmon Fillet, Lemon, Butter, Herbs, Salt, Pepper', FLOOR(1 + RAND() * (10 - 1)), 30, 600, 'Gluten-Free', 'food_images/grilled_salmon.jpg', 4.6),
    (6, 'Mushroom Risotto', 'Creamy risotto cooked with mushrooms, onions, and parmesan cheese', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Arborio Rice, Mushrooms, Onion, Parmesan Cheese, White Wine, Vegetable Broth, Olive Oil', FLOOR(1 + RAND() * (10 - 1)), 25, 800, 'Vegetarian', 'food_images/mushroom_risotto.jpg', 4.4),
    (7, 'Cheeseburger', 'Classic beef patty topped with cheddar cheese, lettuce, tomato, and pickles, served with fries', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Beef Patty, Cheddar Cheese, Lettuce, Tomato, Pickles, Burger Bun, Ketchup, Mustard, Mayonnaise, Potato Fries', FLOOR(1 + RAND() * (10 - 1)), 20, 850, NULL, 'food_images/cheeseburger.jpg', 4.7),
    (8, 'Caprese Salad', 'Fresh tomato, mozzarella cheese, and basil drizzled with balsamic glaze', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Tomato, Mozzarella Cheese, Basil, Balsamic Glaze', FLOOR(1 + RAND() * (10 - 1)), 10, 300, 'Vegetarian', 'food_images/caprese_salad.jpeg', 4.1),
    (9, 'Tiramisu', 'Classic Italian dessert made with layers of coffee-soaked ladyfingers and mascarpone cheese', 'Dessert', FLOOR(500 + RAND() * (1500 - 500)), 'Ladyfingers, Espresso, Mascarpone Cheese, Cocoa Powder, Sugar, Eggs, Marsala Wine', FLOOR(1 + RAND() * (10 - 1)), 20, 400, NULL, 'food_images/tiramisu.jpg', 4.7),
    (10, 'Chicken Alfredo Pasta', 'Creamy pasta dish with grilled chicken, Alfredo sauce, and parmesan cheese', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Fettuccine Pasta, Grilled Chicken, Alfredo Sauce, Parmesan Cheese, Garlic, Heavy Cream', FLOOR(1 + RAND() * (10 - 1)), 25, 850, NULL, 'food_images/chicken_alfredo_pasta.png', 4.5),
    (11, 'Greek Salad', 'Mixed greens with feta cheese, olives, cucumber, tomato, and Greek dressing', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Mixed Greens, Feta Cheese, Olives, Cucumber, Tomato, Greek Dressing', FLOOR(1 + RAND() * (10 - 1)), 10, 250, 'Vegetarian', 'food_images/greek_salad.jpg', 4.3),
    (12, 'Penne Arrabiata', 'Penne pasta tossed in spicy tomato sauce with garlic, chili flakes, and fresh basil', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Penne Pasta, Tomato Sauce, Garlic, Chili Flakes, Fresh Basil, Olive Oil', FLOOR(1 + RAND() * (10 - 1)), 20, 700, 'Vegetarian', 'food_images/penne_arrabiata.jpg', 4.4),
    (13, 'New York Cheesecake', 'Rich and creamy cheesecake on a graham cracker crust, topped with strawberry compote', 'Dessert', FLOOR(500 + RAND() * (1500 - 500)), 'Cream Cheese, Sugar, Eggs, Sour Cream, Vanilla Extract, Graham Crackers, Butter, Strawberry Compote', FLOOR(1 + RAND() * (10 - 1)), 15, 550, NULL, 'food_images/new_york_cheesecake.webp', 4.6),
    (14, 'Vegetable Stir Fry', 'Assorted vegetables stir-fried in a savory sauce, served with steamed rice', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Assorted Vegetables (Broccoli, Bell Peppers, Carrots, Snow Peas), Soy Sauce, Garlic, Ginger, Sesame Oil, Rice Vinegar, Steamed Rice', FLOOR(1 + RAND() * (10 - 1)), 20, 600, 'Vegan', 'food_images/vegetable_stir_fry.jpg', 4.2),
    (15, 'Spinach and Artichoke Dip', 'Creamy dip made with spinach, artichokes, and melted cheese, served with tortilla chips', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Spinach, Artichokes, Cream Cheese, Mozzarella Cheese, Parmesan Cheese, Garlic, Tortilla Chips', FLOOR(1 + RAND() * (10 - 1)), 15, 400, NULL, 'food_images/spinach_artichoke_dip.jpg', 4.5),
    (16, 'Fish and Chips', 'Battered and fried fish fillets served with crispy potato fries and tartar sauce', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Fish Fillets, Flour, Beer, Baking Powder, Potato Fries, Tartar Sauce', FLOOR(1 + RAND() * (10 - 1)), 25, 800, NULL, 'food_images/fish_and_chips.webp', 4.3),
    (17, 'Bruschetta', 'Toasted bread topped with diced tomatoes, garlic, basil, and olive oil', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Baguette, Tomatoes, Garlic, Basil, Olive Oil, Balsamic Glaze', FLOOR(1 + RAND() * (10 - 1)), 10, 300, 'Vegetarian', 'food_images/bruschetta.jpg', 4.0),
    (18, 'Lemon Garlic Shrimp Pasta', 'Pasta dish with sautéed shrimp in a lemon garlic butter sauce', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Pasta, Shrimp, Lemon, Garlic, Butter, White Wine, Parsley', FLOOR(1 + RAND() * (10 - 1)), 20, 750, NULL, 'food_images/lemon_garlic_shrimp_pasta.jpg', 4.6),
    (19, 'Cobb Salad', 'Mixed greens with grilled chicken, avocado, bacon, eggs, tomato, and blue cheese dressing', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Mixed Greens, Grilled Chicken, Avocado, Bacon, Eggs, Tomato, Blue Cheese Dressing', FLOOR(1 + RAND() * (10 - 1)), 15, 450, NULL, 'food_images/cobb_salad.jpg', 4.2),
    (20, 'Key Lime Pie', 'Refreshing pie made with tangy key lime filling in a graham cracker crust, topped with whipped cream', 'Dessert', FLOOR(500 + RAND() * (1500 - 500)), 'Key Lime Juice, Condensed Milk, Egg Yolks, Graham Cracker Crust, Whipped Cream', FLOOR(1 + RAND() * (10 - 1)), 15, 400, NULL, 'food_images/key_lime_pie.jpg', 4.7),
    (21, 'Chicken Tikka Masala', 'Tender chicken pieces cooked in a creamy tomato-based sauce with Indian spices, served with rice', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Chicken, Yogurt, Tomato Sauce, Cream, Ginger, Garlic, Indian Spices, Basmati Rice', FLOOR(1 + RAND() * (10 - 1)), 30, 900, NULL, 'food_images/chicken_tikka_masala.jpg', 4.8),
    (22, 'Vegetable Spring Rolls', 'Crispy spring rolls filled with assorted vegetables, served with sweet chili sauce', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Assorted Vegetables (Cabbage, Carrots, Bean Sprouts), Spring Roll Wrappers, Soy Sauce, Sweet Chili Sauce', FLOOR(1 + RAND() * (10 - 1)), 15, 350, 'Vegan', 'food_images/vegetable_spring_rolls.jpg', 4.4),
    (23, 'Beef Tacos', 'Soft corn tortillas filled with seasoned beef, lettuce, cheese, and salsa', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Beef, Corn Tortillas, Lettuce, Cheese, Salsa', FLOOR(1 + RAND() * (10 - 1)), 20, 700, NULL, 'food_images/beef_tacos.jpg', 4.5),
    (24, 'Pesto Pasta', 'Pasta tossed in homemade basil pesto sauce with cherry tomatoes and parmesan cheese', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Pasta, Basil Pesto Sauce, Cherry Tomatoes, Parmesan Cheese, Garlic, Pine Nuts, Olive Oil', FLOOR(1 + RAND() * (10 - 1)), 20, 650, 'Vegetarian', 'food_images/pesto_pasta.jpg', 4.3),
    (25, 'Caramel Flan', 'Smooth and creamy flan with a caramelized sugar topping', 'Dessert', FLOOR(500 + RAND() * (1500 - 500)), 'Milk, Eggs, Sugar, Vanilla Extract', FLOOR(1 + RAND() * (10 - 1)), 15, 350, NULL, 'food_images/caramel_flan.jpg', 4.6),
    (26, 'Beef Stir Fry', 'Tender beef strips stir-fried with vegetables in a savory sauce, served with steamed rice', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Beef Strips, Assorted Vegetables (Bell Peppers, Broccoli, Carrots), Soy Sauce, Garlic, Ginger, Rice Vinegar, Steamed Rice', FLOOR(1 + RAND() * (10 - 1)), 25, 800, NULL, 'food_images/beef_stir_fry.jpeg', 4.4),
    (27, 'Buffalo Wings', 'Crispy chicken wings tossed in spicy buffalo sauce, served with celery sticks and blue cheese dressing', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Chicken Wings, Buffalo Sauce, Butter, Celery Sticks, Blue Cheese Dressing', FLOOR(1 + RAND() * (10 - 1)), 15, 500, NULL, 'food_images/buffalo_wings.jpg', 4.7),
    (28, 'Vegetable Lasagna', 'Layers of pasta sheets with marinara sauce, assorted vegetables, and melted cheese', 'Main Course', FLOOR(500 + RAND() * (1500 - 500)), 'Pasta Sheets, Marinara Sauce, Assorted Vegetables (Zucchini, Bell Peppers, Mushrooms), Mozzarella Cheese, Ricotta Cheese', FLOOR(1 + RAND() * (10 - 1)), 30, 700, 'Vegetarian', 'food_images/vegetable_lasagna.jpg', 4.5),
    (29, 'Garlic Bread', 'Toasted bread slices brushed with garlic butter and herbs', 'Appetizer', FLOOR(500 + RAND() * (1500 - 500)), 'Baguette, Butter, Garlic, Parsley',  FLOOR(1 + RAND() * (10 - 1)), 10, 250, 'Vegetarian', 'food_images/garlic_bread.webp', 4.2),
    (30, 'Banoffee Pie', 'Indulgent pie with layers of bananas, toffee sauce, and whipped cream on a biscuit crust', 'Dessert', FLOOR(500 + RAND() * (1500 - 500)), 'Digestive Biscuits, Bananas, Toffee Sauce, Whipped Cream', FLOOR(1 + RAND() * (10 - 1)), 20, 450, NULL, 'food_images/banoffee_pie.jpeg', 4.8);


CREATING TABLE FOR TAKING ORDERS

    create table pending_orders (
    id int ,
    customer  varchar(255),
    contact varchar(10),
    email varchar(255),
    start time
    );

CREATING TABLE TO KEEP RECORD OF HOTEL ROOMS

    CREATE TABLE rooms (
        RoomID INT PRIMARY KEY AUTO_INCREMENT,
        RoomNumber VARCHAR(10) UNIQUE,
        RoomType VARCHAR(50),
        Capacity INT,
        Rate DECIMAL(10, 2),
        AC VARCHAR(6),
        Availability VARCHAR(5)
    );

INSERTING DUMMPY DATA OF HOTEL ROOMS

    INSERT INTO rooms (RoomNumber, RoomType, Capacity, Rate, AC, Availability) 
    VALUES 
    ('101', 'Standard', 2, 100.00, "TRUE", "TRUE"),
    ('102', 'Standard', 2, 100.00, "TRUE", "TRUE"),
    ('103', 'Deluxe', 4, 150.00, "TRUE", "TRUE"),
    ('104', 'Deluxe', 4, 150.00, "TRUE", "TRUE"),
    ('105', 'Suite', 6, 200.00, "TRUE", "TRUE"),
    ('106', 'Suite', 6, 200.00, "TRUE", "TRUE"),
    ('107', 'Economy', 1, 50.00, "FALSE", "TRUE"),
    ('108', 'Economy', 1, 50.00, "FALSE", "TRUE"),
    ('109', 'Standard', 2, 100.00, "TRUE", "TRUE"),
    ('110', 'Standard', 2, 100.00, "TRUE", "TRUE");

CREATING RECORD OF GUESTS

    CREATE TABLE Guests (
        GuestID INT PRIMARY KEY AUTO_INCREMENT,
        Name VARCHAR(255) NOT NULL,
        Contact VARCHAR(20) NOT NULL,
        RoomID INT,
        RoomName VARCHAR(50)
    );



  
