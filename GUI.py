from tkinter import *
from OrderHistory import *
from Bluetooth import *


class GUI(OrderHistory):
    def __init__(self):
        super().__init__()
        self.bt = Bluetooth()
        self.main_window = Tk()
        self.order_mode = True

        ############################### Muokattavat parametrit ###############################
        self.food_names = ["Lihis", "Ranut", "Makkaraperunat", "Sipulirenkaat", "Kinkkupizza", "Salamipizza",
                           "foo", "foo"]
        self.food_prices = [3.0, 3.0, 3.0, 5.0, 1.0, 1.0, 1.0, 1.0]
        ######################################################################################

        self.new_serving = 0

        # Row 0
        self.button_order = Button(self.main_window, text="Vastaanota\ntilauksia", background="green", state=DISABLED,
                                   command=self.order, width=15)
        self.button_serve = Button(self.main_window, text="Tarjoile ruokia", background="grey", command=self.serve,
                                   width=15, height=2)
        self.label_queue_number_text = Label(self.main_window, text="Vuoronumero:", width=15)
        self.label_queue_number = Label(self.main_window, text=str(self.return_queue_number()), width=15)
        self.label_ordered_foods = Label(self.main_window, text="Tilatut ruuat:", width=15)
        self.label_ordered = Label(self.main_window, text=self.count_current_orders_str(), width=15)
        self.button_order.grid(row=0, column=0)
        self.button_serve.grid(row=0, column=1)
        self.label_queue_number_text.grid(row=0, column=2)
        self.label_queue_number.grid(row=0, column=3)
        self.label_ordered_foods.grid(row=0, column=8)
        self.label_ordered.grid(row=0, column=9)
        # Row 1
        self.label_food_1_text = Label(self.main_window, text=self.food_names[0], width=15)
        self.label_food_2_text = Label(self.main_window, text=self.food_names[1], width=15)
        self.label_food_3_text = Label(self.main_window, text=self.food_names[2], width=15)
        self.label_food_4_text = Label(self.main_window, text=self.food_names[3], width=15)
        self.label_food_5_text = Label(self.main_window, text=self.food_names[4], width=15)
        self.label_food_6_text = Label(self.main_window, text=self.food_names[5], width=15)
        self.label_food_7_text = Label(self.main_window, text=self.food_names[6], width=15)
        self.label_food_8_text = Label(self.main_window, text=self.food_names[7], width=15)
        self.label_food_1_text.grid(row=1, column=0)
        self.label_food_2_text.grid(row=1, column=1)
        self.label_food_3_text.grid(row=1, column=2)
        self.label_food_4_text.grid(row=1, column=3)
        self.label_food_5_text.grid(row=1, column=4)
        self.label_food_6_text.grid(row=1, column=5)
        self.label_food_7_text.grid(row=1, column=6)
        self.label_food_8_text.grid(row=1, column=7)

        # Row 2
        # food_counts = self.return_current_order_str().split(' ')
        # self.label_food_1 = Label(self.main_window, text=food_counts[0])
        # self.label_food_2 = Label(self.main_window, text=food_counts[1])
        # self.label_food_3 = Label(self.main_window, text=food_counts[2])
        # self.label_food_4 = Label(self.main_window, text=food_counts[3])
        # self.label_food_5 = Label(self.main_window, text=food_counts[4])
        # self.label_food_6 = Label(self.main_window, text=food_counts[5])
        # self.label_food_7 = Label(self.main_window, text=food_counts[6])
        # self.label_food_8 = Label(self.main_window, text=food_counts[7])
        # # self.label_total_text = Label(self.main_window, text="Total:")
        # self.label_total = Label(self.main_window, text=(self.return_total_price_str()) + "€")
        # self.label_food_1.grid(row=2, column=0)
        # self.label_food_2.grid(row=2, column=1)
        # self.label_food_3.grid(row=2, column=2)
        # self.label_food_4.grid(row=2, column=3)
        # self.label_food_5.grid(row=2, column=4)
        # self.label_food_6.grid(row=2, column=5)
        # self.label_food_7.grid(row=2, column=6)
        # self.label_food_8.grid(row=2, column=7)
        # self.food_count_labels = []
        # self.food_count_labels.append(self.label_food_1)
        # self.food_count_labels.append(self.label_food_2)
        # self.food_count_labels.append(self.label_food_3)
        # self.food_count_labels.append(self.label_food_4)
        # self.food_count_labels.append(self.label_food_5)
        # self.food_count_labels.append(self.label_food_6)
        # self.food_count_labels.append(self.label_food_7)
        # self.food_count_labels.append(self.label_food_8)

        # self.label_total_text.grid(row=2, column=8)
        # self.label_total.grid(row=2, column=9)
        # Row 3
        self.button_food_1 = Button(self.main_window, text="↑", command=lambda: self.select_food(1), width=10, height=6)
        self.button_food_2 = Button(self.main_window, text="↑", command=lambda: self.select_food(2), width=10, height=6)
        self.button_food_3 = Button(self.main_window, text="↑", command=lambda: self.select_food(3), width=10, height=6)
        self.button_food_4 = Button(self.main_window, text="↑", command=lambda: self.select_food(4), width=10, height=6)
        self.button_food_5 = Button(self.main_window, text="↑", command=lambda: self.select_food(5), width=10, height=6)
        self.button_food_6 = Button(self.main_window, text="↑", command=lambda: self.select_food(6), width=10, height=6)
        self.button_food_7 = Button(self.main_window, text="↑", command=lambda: self.select_food(7), width=10, height=6)
        self.button_food_8 = Button(self.main_window, text="↑", command=lambda: self.select_food(8), width=10, height=6)
        self.button_food_1.grid(row=3, column=0)
        self.button_food_2.grid(row=3, column=1)
        self.button_food_3.grid(row=3, column=2)
        self.button_food_4.grid(row=3, column=3)
        self.button_food_5.grid(row=3, column=4)
        self.button_food_6.grid(row=3, column=5)
        self.button_food_7.grid(row=3, column=6)
        self.button_food_8.grid(row=3, column=7)
        self.food_buttons = []
        self.food_buttons.append(self.button_food_1)
        self.food_buttons.append(self.button_food_2)
        self.food_buttons.append(self.button_food_3)
        self.food_buttons.append(self.button_food_4)
        self.food_buttons.append(self.button_food_5)
        self.food_buttons.append(self.button_food_6)
        self.food_buttons.append(self.button_food_7)
        self.food_buttons.append(self.button_food_8)

        # Row 4
        self.button_submit = Button(self.main_window, text="Tarjoile", state=DISABLED, command=self.submit_serving_gui,
                                    width=15)
        self.button_submit.grid(row=4, column=8, sticky=S)
        # Row 5
        self.label_food_1_price = Label(self.main_window, text=str(self.food_prices[0]) + "€")
        self.label_food_2_price = Label(self.main_window, text=str(self.food_prices[1]) + "€")
        self.label_food_3_price = Label(self.main_window, text=str(self.food_prices[2]) + "€")
        self.label_food_4_price = Label(self.main_window, text=str(self.food_prices[3]) + "€")
        self.label_food_5_price = Label(self.main_window, text=str(self.food_prices[4]) + "€")
        self.label_food_6_price = Label(self.main_window, text=str(self.food_prices[5]) + "€")
        self.label_food_7_price = Label(self.main_window, text=str(self.food_prices[6]) + "€")
        self.label_food_8_price = Label(self.main_window, text=str(self.food_prices[7]) + "€")
        self.button_previous = Button(self.main_window, text="Edellinen", command=self.previous, width=15)
        self.button_next = Button(self.main_window, text="Seuraava", command=self.next, width=15)
        self.label_food_1_price.grid(row=5, column=0)
        self.label_food_2_price.grid(row=5, column=1)
        self.label_food_3_price.grid(row=5, column=2)
        self.label_food_4_price.grid(row=5, column=3)
        self.label_food_5_price.grid(row=5, column=4)
        self.label_food_6_price.grid(row=5, column=5)
        self.label_food_7_price.grid(row=5, column=6)
        self.label_food_8_price.grid(row=5, column=7)
        self.food_price_labels = []
        self.food_price_labels.append(self.label_food_1_price)
        self.food_price_labels.append(self.label_food_2_price)
        self.food_price_labels.append(self.label_food_3_price)
        self.food_price_labels.append(self.label_food_4_price)
        self.food_price_labels.append(self.label_food_5_price)
        self.food_price_labels.append(self.label_food_6_price)
        self.food_price_labels.append(self.label_food_7_price)
        self.food_price_labels.append(self.label_food_8_price)
        self.button_previous.grid(row=5, column=8)
        self.button_next.grid(row=5, column=9)
        # Row 6
        self.label_spacer = Label(self.main_window, text=" ")
        self.label_spacer.grid(row=6, column=0)
        # Row 7
        self.label_order_history = Label(self.main_window, text="Tilaushistoria:")
        self.label_order_history.grid(row=7, column=0, sticky=W)
        # Rows 8
        self.order_history_field = Text(height=20)
        self.scrollbar = Scrollbar()
        self.order_history_field.grid(row=8, column=0, columnspan=10, sticky=E+W)
        self.scrollbar.grid(row=8, column=10, sticky=N+S)
        self.scrollbar.configure(command=self.order_history_field.yview)
        self.order_history_field.configure(yscrollcommand=self.scrollbar.set)

        self.update_order_history_field()
        self.main_window.mainloop()



    def order(self):
        self.button_order.configure(state=DISABLED, background="green")
        self.button_serve.configure(state=NORMAL, background="gray")
        self.toggle_mode()
        self.label_queue_number_text.configure(text="Number:")
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        # self.label_total_text.configure(text="Total:")
        # self.label_total.configure(text=(self.return_total_price_str()) + "€")
        for i in range(8):
            self.food_price_labels[i].configure(text=str(self.food_prices[i]) + "€")
        self.button_submit.configure(state=DISABLED)
        self.button_previous.configure(state=NORMAL)
        self.button_next.configure(state=NORMAL)
        # self.update_food_count_labels()
        self.update_logfile()
        self.update_order_history_field()


    def serve(self):
        self.button_order.configure(state=NORMAL, background="grey")
        self.button_serve.configure(state=DISABLED, background="red")
        self.toggle_mode()
        self.new_serving = 0
        # self.update_food_count_labels(0)
        self.label_queue_number_text.configure(text="")
        self.label_queue_number.configure(text="")
        # self.label_total_text.configure(text="")
        # self.label_total.configure(text="")
        for label in self.food_price_labels:
            label.configure(text="")
        self.button_submit.configure(state=NORMAL)
        self.button_previous.configure(state=DISABLED)
        self.button_next.configure(state=DISABLED)
        self.update_logfile()
        self.update_order_history_field()


    def toggle_mode(self):
        for button in self.food_buttons:
            button.configure(state=NORMAL)
        if self.order_mode:
            self.order_mode = False
        else:
            self.order_mode = True


    def select_food(self, food_num):
        # Enable all buttons
        for i in range(8):
            self.food_buttons[i].configure(state=NORMAL)
        # Disable current food button
        self.food_buttons[food_num - 1].configure(state=DISABLED)
        if self.order_mode:
            # self.update_food_count_labels(food_num)
            # self.label_total.configure(text=(str(self.food_prices[food_num])) + "€")
            self.order_history[self.return_queue_number()].food = food_num
        else:
            self.new_serving = food_num
            # self.update_food_count_labels()



########################################################################################################################

    def return_total_price_str(self):
        return str(self.current_order)


    # def update_food_count_labels(self, food_num):
    #     if self.order_mode:
    #         for i in range(8):
    #             self.food_count_labels[i].configure(text="")
    #     else:
    #         for i in range(8):
    #             self.food_count_labels[i].configure(text=self.new_serving[food_num])


    def submit_serving_gui(self):
        order_num = self.find_serving_number(self.new_serving)
        # If no servable order (should not happen)
        if order_num == 0:
            return
        self.popup(order_num)
        self.submit_new_serving(self.new_serving)
        self.label_ordered.configure(text=self.count_current_orders_str())
        self.new_serving = 0
        self.update_order_history_field()
        for button in self.food_buttons:
            button.configure(state=NORMAL)
        self.update_logfile()
        # self.update_food_count_labels()
        # self.bt.send_foods(self.count_current_orders())


    def popup(self, order_num):
        popup = Toplevel()
        popup.title("!")
        message = Message(popup, text=str(order_num), font=("", 30))
        message.pack()
        button = Button(popup, text="Ok", command=popup.destroy)
        button.pack()


    def previous(self):
        self.previous_order()
        self.update_logfile()
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        self.label_ordered.configure(text=self.count_current_orders_str())
        self.update_order_history_field()
        # Enable all buttons
        for button in self.food_buttons:
            button.configure(state=NORMAL)
        self.food_buttons[self.order_history[self.return_queue_number()].food - 1].configure(state=DISABLED)


    def next(self):
        self.next_order()
        self.update_logfile()
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        self.label_ordered.configure(text=self.count_current_orders_str())
        # self.bt.send_foods(self.count_current_orders())
        self.update_order_history_field()
        # Enable all buttons
        for button in self.food_buttons:
            button.configure(state=NORMAL)
        # Disable button of ordered food
        food_num = self.order_history[self.return_queue_number()].food
        if food_num >= 0:
            self.food_buttons[food_num].configure(state=DISABLED)


    def update_order_history_field(self):
        text = ""
        for order in self.order_history:
            served = "F"
            if order.served:
                served = "T"
            text += str(order.number) + " " + str(order.food) + " " + served + '\n'
        self.order_history_field.delete(1.0, END)
        self.order_history_field.insert(INSERT, text)
        self.order_history_field.see(END)

        # buf = self.return_order(self.current_queue_number - 1)
        # text = str(self.current_queue_number) + "                "
        # for i in range(8):
        #     text += str(buf[i]) + "                               "
        # # self.label_previous_order_1.configure(text=text)


    def exit(self):
        self.main_window.destroy()
