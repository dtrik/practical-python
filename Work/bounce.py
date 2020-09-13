# bounce.py
#
# Exercise 1.5
def new_height(curr_height):
    return 0.6*curr_height

def main(height=100):
    for i in range(11):
        print(i,round(height,4))
        height = new_height(height)

if __name__ == "__main__":
    main(100)
