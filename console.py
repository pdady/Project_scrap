import sys
import get

def check_is_digit(number):

    if (number.isdigit() == False and number != "exit"):
        print ('\n"' + number + '"' + ' is not a number\n')
        return (0)
    elif number == "exit":
        return (0)
    return (1)


# Get parameters on console mode
def prompt_command(
        all_products, brand):

    print("(1) Hermes\n(2) Louis Vuitton\n(3) Gucci")
    print("(4) Chanel\n(5) Prada\n(6) All")
    number = input("-->> ")
    if (check_is_digit(number) == 1):
        if (int(number) <= 0 or int(number) > len(brand)):
            print ("\nError: Bad number, please choose number between 1 and " +
                    str(len(brand)))
        else:
            print ("\n\n(1) Display mode\n(2) Write in the result.txt")
            mode = input("-->  ")
            if (check_is_digit(mode) == 1 and (mode == "1" or mode == "2")):
                max_items = input("How many items? -->> ")
                if (check_is_digit(max_items)):
                    if (max_items == "0"):
                        output_mode(mode, all_products, max_items)
                    else:
                        brand[int(number) - 1] = get.info_from_url(
                                                        brand[int(number) - 1],
                                                        all_products,
                                                        int(max_items), mode)
        prompt_command(all_products, brand, max_items)
    elif (number != "exit"):
        prompt_command(all_products, brand, max_items)


# Comand line
def get_argument(all_products, brand):

    c = 0
    nb = 0
    for i in range(len(sys.argv)):
        if i != 0:
            if "-c" == sys.argv[i]:
                c = 1
            elif "-n" == sys.argv[i] and i + 1 < len(sys.argv):
                nb = sys.argv[i + 1]
    if c == 1 and nb == 0:
            prompt_command(all_products, brand)
    elif c == 0 and nb != 0 and len(sys.argv) == 3:
        if check_is_digit(nb):
            get.info_from_url(brand[len(brand) - 1], all_products, int(nb), "1")
    else:
        print ("Usage:\n\t-c --> Console mode")
        print("\t-n --> Max number of items displayed (ex: -n 10)")
