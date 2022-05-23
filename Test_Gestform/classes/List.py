from Test_Gestform.functions.functions import is_5_mult, is_3_mult, randomList


class List:
    L = []
    L_string = []
    L_printed = []
    n = 0
    index = -1
    string = ""
    genreated = False

    def __init__(self):
        pass

    #initialize the current string into an attribute
    def set_string(self, n):
        if is_3_mult(n) and is_5_mult(n):
            self.string = "GestForm"
        elif is_3_mult(n):
            self.string = "Geste"
        elif is_5_mult(n):
            self.string = "Forme"
        else:
            self.string = str(n)

    #initialize the list of numbers
    def init_list(self, n):
        self.n = n
        self.L = randomList(n)
        self.L_printed = []
        self.set_string(n)
        self.genreated = True
        self.init_list_string()

    #initialize the list of strings results
    def init_list_string(self):
        for i in self.L:
            if is_3_mult(i) and is_5_mult(i):
                self.L_string.append("GestForm")
            elif is_3_mult(i):
                self.L_string.append("Geste")
            elif is_5_mult(i):
                self.L_string.append("Forme")
            else:
                self.L_string.append(str(i))


    #print rectangles where the list will be shown
    def printList(self, master, point, size):
        top_left_corner_x = point[0]
        top_left_corner_y = point[1]
        bottom_right_corner_x = top_left_corner_x + size
        bottom_right_corner_y = top_left_corner_y + size

        for i in range(3):
            case = master.create_rectangle(
                top_left_corner_x,
                top_left_corner_y,
                bottom_right_corner_x,
                bottom_right_corner_y
            )
            if i+self.index < self.n and i+self.index > -1:
                master.create_text(top_left_corner_x + size / 2, top_left_corner_y + size / 2, text=self.L[i+self.index], font="Corbel 20")
                master.create_text(top_left_corner_x + size / 2, top_left_corner_y + size+5,text=self.index+i, font="Corbel 10")

                if i == 1:
                    master.itemconfig(case, fill='green')

            else:
                master.itemconfig(case, fill='black')

            self.L_printed.append(case)
            top_left_corner_x += size
            bottom_right_corner_x += size

    #move the index in direction of the end of the list and update the current string attribute
    def navigate_forward(self, master):
        if self.index+2 < self.n:
            self.index += 1
        self.printList(master, (150, 15), 100)
        self.set_string(self.L[self.index+1])

    #move the index in direction of the begening of the list and update the current string attribute
    def navigate_backward(self, master):
        if self.index-2 < self.n and self.index >= 0:
            self.index -= 1
        self.printList(master, (150, 15), 100)
        self.set_string(self.L[self.index+1])
