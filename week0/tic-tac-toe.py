
grid = [ "-","-","-","-","-","-","-","-","-"]

def run():
    numbers_list = [0,1,2,3,4,5,6,7,8]

    got = ""
    dot = ""
    for i in range(10):
        if len(got) == 3 or len(dot) == 3:
            if got == "012" or got == "345" or got == "678" or got == "036" or got == "147" or got == "258" or got == "048" or got == "246":
                print("Player1 wins")
                break
            elif dot == "012" or dot == "345" or dot == "678" or dot == "036" or dot == "147" or dot == "258" or dot == "048" or dot == "246":
                print("Player2 wins")
                break

        display(grid)
        if i==9:
            print("Draw")
            break


        if i%2 == 0:
            cel = int(input("Enter cell(Player1): ")) - 1
            cell = str(cel)
            got+=cell
            got = ''.join(sorted(got))
            grid[cel] = "x"
        else:
            cel = int(input("Enter cell(Player2): ")) - 1
            cell = str(cel)
            dot+=cell
            dot = ''.join(sorted(dot))
            grid[cel] = "o"

def display(grid):
    print(grid[0],grid[1],grid[2])
    print(grid[3], grid[4], grid[5])
    print(grid[6], grid[7], grid[8])

run()

