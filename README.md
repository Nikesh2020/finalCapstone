# Final Capstone
## Table of contents
1. Project name
2. Project file name
3. Project Description
4. Installation
5. Usage section
6. Credits

## 1. Project name
Inventory

## 2. Project file name
Inventory.py

## 3. Project Description
A Python program that will read from a text file inventory.txt the following information about 
the stock containined in the warehouse: -

1. country,
2. code,
3. product,
4. cost,
5. quantity.

After the program has read this information it will give the user options to perform the following 
actions on the stock items: -

1. read shoes data 
2. capture shoes 
3. view all stock 
4. re-stock minimum quatity shoes
5. seach for a shoe based on its code
6. Display Value per item of stock 
7. Find highest quantity of stock 

## 4. Installation
Please install a python IDE to compile and run this code. The 
latest verisions of either Pycharm or VScode are reccomended. 

Please install the tabulate module using the command:
pip install tabulate

## 5. Usage section 
The following is the main menu through which the user can navigate by
entering the corresponding number and pressing the enter key: -

**Main menu screen: -**<br />
Inventory.py ver 1.0<br />
Please select one of the option below and press enter:<br />
0 - Load shoe data from file.<br />
1 - Save shoe data to file.<br />
2 - View all shoes on system.<br />
3 - Search Shoe details by its code.<br />
4 - Print value of each shoe stock to screen.<br />
5 - Print highest quantity shoe stock.<br />
6 - Add shoe to file.<br />
7 - Re-stock lowest quantity shoe stock.<br />
e - Exit program.<br />
:<br />

**Option 2 screen - View all shoes on system: -**<br />
Country        Code      Product                Cost    Quantity<br />
-------------  --------  -------------------  ------  ----------<br />
South Africa   SKU44386  Air Max 90             2300          20<br />
China          SKU90000  Jordan 1               3200          50<br />
Vietnam        SKU63221  Blazer                 1700          19<br />
United States  SKU29077  Cortez                  970          60<br />
Russia         SKU89999  Air Force 1            2000          43<br />
Australia      SKU57443  Waffle Racer           2700           4<br />
Canada         SKU68677  Air Max 97             3600          13<br />
Egypt          SKU19888  Dunk SB                1500          26<br />
Britain        SKU76000  Kobe 4                 3400          32<br />
France         SKU84500  Pegasus                2490          28<br />
Zimbabwe       SKU20207  Air Presto             2999           7<br />
Morocco        SKU77744  Challenge Court        1450          11<br />
Israel         SKU29888  Air Zoom Generation    2680           6<br />
Uganda         SKU33000  Flyknit Racer          4900           9<br />
Pakistan       SKU77999  Air Yeezy 2            4389          67<br />
Brazil         SKU44600  Air Jordan 11          3870          24<br />
Columbia       SKU87500  Air Huarache           2683           8<br />
India          SKU38773  Air Max 1              1900          29<br />
Vietnam        SKU95000  Air Mag                2000           2<br />
Israel         SKU79084  Air Foamposite         2430           4<br />
China          SKU93222  Air Stab               1630          10<br />
South Korea    SKU66734  Hyperdunk              1899           7<br />
Australia      SKU71827  Zoom Hyperfuse         1400          15<br />
France         SKU20394  Eric Koston 1          2322          17<br />
Brazil         SKU88888  Nike Air Max             12          12<br />

**Option 3 Screen - Search Shoe details by its code: -**<br />
Please enter shoe-code: SKU88888<br />
Shoe Details for SKU88888:<br />
Brazil,SKU88888,Nike Air Max,12,12<br />

**Option 4 screen - Print value of each shoe stock to screen: -**<br />
Values per Item:<br />
────────────────────────────────────────────────────────────────────────────────<br />
South Africa,SKU44386,Air Max 90,2300,20<br />
value = 46000<br />
────────────────────────────────────────────────────────────────────────────────<br />
China,SKU90000,Jordan 1,3200,50<br />
value = 160000<br />
────────────────────────────────────────────────────────────────────────────────<br />
Vietnam,SKU63221,Blazer,1700,19<br />
value = 32300<br />
────────────────────────────────────────────────────────────────────────────────<br />
United States,SKU29077,Cortez,970,60<br />
value = 58200<br />
────────────────────────────────────────────────────────────────────────────────<br />
Russia,SKU89999,Air Force 1,2000,43<br />
value = 86000<br />
────────────────────────────────────────────────────────────────────────────────<br />
Australia,SKU57443,Waffle Racer,2700,4<br />
value = 10800<br />
────────────────────────────────────────────────────────────────────────────────<br />
Canada,SKU68677,Air Max 97,3600,13<br />
value = 46800<br />
────────────────────────────────────────────────────────────────────────────────<br />
Egypt,SKU19888,Dunk SB,1500,26<br />
value = 39000<br />
────────────────────────────────────────────────────────────────────────────────<br />
Britain,SKU76000,Kobe 4,3400,32<br />
value = 108800<br />
────────────────────────────────────────────────────────────────────────────────<br />
France,SKU84500,Pegasus,2490,28<br />
value = 69720<br />
────────────────────────────────────────────────────────────────────────────────<br />
Zimbabwe,SKU20207,Air Presto,2999,7<br />
value = 20993<br />
────────────────────────────────────────────────────────────────────────────────<br />
Morocco,SKU77744,Challenge Court,1450,11<br />
value = 15950<br />
────────────────────────────────────────────────────────────────────────────────<br />
Israel,SKU29888,Air Zoom Generation,2680,6<br />
value = 16080<br />
────────────────────────────────────────────────────────────────────────────────<br />
Uganda,SKU33000,Flyknit Racer,4900,9<br />
value = 44100<br />
────────────────────────────────────────────────────────────────────────────────<br />
Pakistan,SKU77999,Air Yeezy 2,4389,67<br />
value = 294063<br />
────────────────────────────────────────────────────────────────────────────────<br />
Brazil,SKU44600,Air Jordan 11,3870,24<br />
value = 92880<br />
────────────────────────────────────────────────────────────────────────────────<br />
Columbia,SKU87500,Air Huarache,2683,8<br />
value = 21464<br />
────────────────────────────────────────────────────────────────────────────────<br />
India,SKU38773,Air Max 1,1900,29<br />
value = 55100<br />
────────────────────────────────────────────────────────────────────────────────<br />
Vietnam,SKU95000,Air Mag,2000,2<br />
value = 4000<br />
────────────────────────────────────────────────────────────────────────────────<br />
Israel,SKU79084,Air Foamposite,2430,4<br />
value = 9720<br />
────────────────────────────────────────────────────────────────────────────────<br />
China,SKU93222,Air Stab,1630,10<br />
value = 16300<br />
────────────────────────────────────────────────────────────────────────────────<br />
South Korea,SKU66734,Hyperdunk,1899,7<br />
value = 13293<br />
────────────────────────────────────────────────────────────────────────────────<br />
Australia,SKU71827,Zoom Hyperfuse,1400,15<br />
value = 21000<br />
────────────────────────────────────────────────────────────────────────────────<br />
France,SKU20394,Eric Koston 1,2322,17<br />
value = 39474<br />
────────────────────────────────────────────────────────────────────────────────<br />
Brazil,SKU88888,Nike Air Max,12,12<br />
value = 144<br />
────────────────────────────────────────────────────────────────────────────────<br />

**Option 5 screen - Print highest quantity shoe stock as being on sale: -**<br />
The following shoe has the largest quantity in stock and is on sale:<br />
Pakistan,SKU77999,Air Yeezy 2,4389,67<br />

**Option 6 screen - Add shoe to file: -**<br />
Please enter the product details<br />
Please enter the product country: Brazil<br />
Please enter the product code: SKU88888<br />
Please enter the product name: Nike Air Max II<br />
Please enter the product cost: 39474<br />
Please enter the quantity: 12<br />
Product added to File successfully!<br />

**Option 7 screen- Re-stock lowest quantity shoe stock: -**<br />
Minimum quantity stock is: Vietnam,SKU95000,Air Mag,2000,2<br />
Would you like to add quantity to this stock? [y or n] :y<br />
Please enter how many items you would like to add to this stock: 12<br />
Stock updated successfully<br />
Would you like to add quantity to this stock? [y or n] :n<br />

## 6. Credits
**Author:** Nikesh Chavda<br />
**Special mentions:** HyperionDev for designing the task.<br />
