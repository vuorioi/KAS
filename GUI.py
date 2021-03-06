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
        self.food_names = ["Lihis", "Ranut", "Makkaraperunat", "Sipulirenkaat", "Kinkkupizza", "Salamipizza", "foo", "foo"]
        self.food_prices = [3.0, 3.0, 3.0, 5.0, 1.0, 1.0, 1.0, 1.0]
        ######################################################################################

        self.new_serving = [0, 0, 0, 0, 0, 0, 0, 0]

        # Row 0
        self.button_order = Button(self.main_window, text="Vastaanota\ntilauksia", background="green", state=DISABLED, command=self.order, width=15)
        self.button_serve = Button(self.main_window, text="Tarjoile ruokia", background="grey", command=self.serve, width=15, height=2)
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
        food_counts = self.return_current_order_str().split(' ')
        self.label_food_1 = Label(self.main_window, text=food_counts[0])
        self.label_food_2 = Label(self.main_window, text=food_counts[1])
        self.label_food_3 = Label(self.main_window, text=food_counts[2])
        self.label_food_4 = Label(self.main_window, text=food_counts[3])
        self.label_food_5 = Label(self.main_window, text=food_counts[4])
        self.label_food_6 = Label(self.main_window, text=food_counts[5])
        self.label_food_7 = Label(self.main_window, text=food_counts[6])
        self.label_food_8 = Label(self.main_window, text=food_counts[7])
        self.label_total_text = Label(self.main_window, text="Total:")
        self.label_total = Label(self.main_window, text=(self.return_total_price_str()) + "€")
        self.label_food_1.grid(row=2, column=0)
        self.label_food_2.grid(row=2, column=1)
        self.label_food_3.grid(row=2, column=2)
        self.label_food_4.grid(row=2, column=3)
        self.label_food_5.grid(row=2, column=4)
        self.label_food_6.grid(row=2, column=5)
        self.label_food_7.grid(row=2, column=6)
        self.label_food_8.grid(row=2, column=7)
        self.label_total_text.grid(row=2, column=8)
        self.label_total.grid(row=2, column=9)
        # Row 3
        self.button_food_1_up = Button(self.main_window, text="↑", command=self.food_1_up_gui, width=10, height=6)
        self.button_food_2_up = Button(self.main_window, text="↑", command=self.food_2_up_gui, width=10, height=6)
        self.button_food_3_up = Button(self.main_window, text="↑", command=self.food_3_up_gui, width=10, height=6)
        self.button_food_4_up = Button(self.main_window, text="↑", command=self.food_4_up_gui, width=10, height=6)
        self.button_food_5_up = Button(self.main_window, text="↑", command=self.food_5_up_gui, width=10, height=6)
        self.button_food_6_up = Button(self.main_window, text="↑", command=self.food_6_up_gui, width=10, height=6)
        self.button_food_7_up = Button(self.main_window, text="↑", command=self.food_7_up_gui, width=10, height=6)
        self.button_food_8_up = Button(self.main_window, text="↑", command=self.food_8_up_gui, width=10, height=6)
        self.button_food_1_up.grid(row=3, column=0)
        self.button_food_2_up.grid(row=3, column=1)
        self.button_food_3_up.grid(row=3, column=2)
        self.button_food_4_up.grid(row=3, column=3)
        self.button_food_5_up.grid(row=3, column=4)
        self.button_food_6_up.grid(row=3, column=5)
        self.button_food_7_up.grid(row=3, column=6)
        self.button_food_8_up.grid(row=3, column=7)
        # Row 4
        self.button_food_1_down = Button(self.main_window, text="↓", command=self.food_1_down_gui, width=10, height=6)
        self.button_food_2_down = Button(self.main_window, text="↓", command=self.food_2_down_gui, width=10, height=6)
        self.button_food_3_down = Button(self.main_window, text="↓", command=self.food_3_down_gui, width=10, height=6)
        self.button_food_4_down = Button(self.main_window, text="↓", command=self.food_4_down_gui, width=10, height=6)
        self.button_food_5_down = Button(self.main_window, text="↓", command=self.food_5_down_gui, width=10, height=6)
        self.button_food_6_down = Button(self.main_window, text="↓", command=self.food_6_down_gui, width=10, height=6)
        self.button_food_7_down = Button(self.main_window, text="↓", command=self.food_7_down_gui, width=10, height=6)
        self.button_food_8_down = Button(self.main_window, text="↓", command=self.food_8_down_gui, width=10, height=6)
        self.button_submit = Button(self.main_window, text="Tarjoile", state=DISABLED, command=self.submit_serving_gui, width=15)
        self.button_food_1_down.grid(row=4, column=0)
        self.button_food_2_down.grid(row=4, column=1)
        self.button_food_3_down.grid(row=4, column=2)
        self.button_food_4_down.grid(row=4, column=3)
        self.button_food_5_down.grid(row=4, column=4)
        self.button_food_6_down.grid(row=4, column=5)
        self.button_food_7_down.grid(row=4, column=6)
        self.button_food_8_down.grid(row=4, column=7)
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
        self.button_previous.grid(row=5, column=8)
        self.button_next.grid(row=5, column=9)
        # Row 6
        self.label_spacer = Label(self.main_window, text=" ")
        self.label_spacer.grid(row=6, column=0)
        # Row 7
        self.label_order_history = Label(self.main_window, text="Tilaushistoria:")
        self.label_order_history.grid(row=7, column=0, sticky=W)
        # Rows 8-
        self.label_previous_order_10 = Label(self.main_window)
        self.label_previous_order_9 = Label(self.main_window)
        self.label_previous_order_8 = Label(self.main_window)
        self.label_previous_order_7 = Label(self.main_window)
        self.label_previous_order_6 = Label(self.main_window)
        self.label_previous_order_5 = Label(self.main_window)
        self.label_previous_order_4 = Label(self.main_window)
        self.label_previous_order_3 = Label(self.main_window)
        self.label_previous_order_2 = Label(self.main_window)
        self.label_previous_order_1 = Label(self.main_window)
        self.label_previous_order_10.grid(row=8, column=0)
        self.label_previous_order_9.grid(row=9, column=0)
        self.label_previous_order_8.grid(row=10, column=0)
        self.label_previous_order_7.grid(row=11, column=0)
        self.label_previous_order_6.grid(row=12, column=0)
        self.label_previous_order_5.grid(row=13, column=0)
        self.label_previous_order_4.grid(row=14, column=0)
        self.label_previous_order_3.grid(row=145, column=0)
        self.label_previous_order_2.grid(row=16, column=0)
        self.label_previous_order_1.grid(row=17, column=0, columnspan=10, sticky=W)
        self.update_order_history()

        self.main_window.mainloop()



    def order(self):
        self.button_order.configure(state=DISABLED, background="green")
        self.button_serve.configure(state=NORMAL, background="gray")
        self.toggle_mode()
        self.label_queue_number_text.configure(text="Number:")
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        self.label_total_text.configure(text="Total:")
        self.label_total.configure(text=(self.return_total_price_str()) + "€")
        self.label_food_1_price.configure(text=str(self.food_prices[0]) + "€")
        self.label_food_2_price.configure(text=str(self.food_prices[1]) + "€")
        self.label_food_3_price.configure(text=str(self.food_prices[2]) + "€")
        self.label_food_4_price.configure(text=str(self.food_prices[3]) + "€")
        self.label_food_5_price.configure(text=str(self.food_prices[4]) + "€")
        self.label_food_6_price.configure(text=str(self.food_prices[5]) + "€")
        self.label_food_7_price.configure(text=str(self.food_prices[6]) + "€")
        self.label_food_8_price.configure(text=str(self.food_prices[7]) + "€")
        self.button_submit.configure(state=DISABLED)
        self.button_previous.configure(state=NORMAL)
        self.button_next.configure(state=NORMAL)
        self.update_food_count_labels()


    def serve(self):
        self.button_order.configure(state=NORMAL, background="grey")
        self.button_serve.configure(state=DISABLED, background="red")
        self.toggle_mode()
        self.new_serving = [0, 0, 0, 0, 0, 0, 0, 0]
        self.update_food_count_labels()
        self.label_queue_number_text.configure(text="")
        self.label_queue_number.configure(text="")
        self.label_total_text.configure(text="")
        self.label_total.configure(text="")
        self.label_food_1_price.configure(text="")
        self.label_food_2_price.configure(text="")
        self.label_food_3_price.configure(text="")
        self.label_food_4_price.configure(text="")
        self.label_food_5_price.configure(text="")
        self.label_food_6_price.configure(text="")
        self.label_food_7_price.configure(text="")
        self.label_food_8_price.configure(text="")
        self.button_submit.configure(state=NORMAL)
        self.button_previous.configure(state=DISABLED)
        self.button_next.configure(state=DISABLED)


    def toggle_mode(self):
        if self.order_mode:
            self.order_mode = False
        else:
            self.order_mode = True


    # Up- and down-button methods - gui-side ###########################################################################
    def food_1_up_gui(self):
        if self.order_mode:
            self.food_1_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[0] += 1
            self.update_food_count_labels()


    def food_2_up_gui(self):
        if self.order_mode:
            self.food_2_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[1] += 1
            self.update_food_count_labels()

    def food_3_up_gui(self):
        if self.order_mode:
            self.food_3_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[2] += 1
            self.update_food_count_labels()

    def food_4_up_gui(self):
        if self.order_mode:
            self.food_4_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[3] += 1
            self.update_food_count_labels()

    def food_5_up_gui(self):
        if self.order_mode:
            self.food_5_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[4] += 1
            self.update_food_count_labels()

    def food_6_up_gui(self):
        if self.order_mode:
            self.food_6_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[5] += 1
            self.update_food_count_labels()

    def food_7_up_gui(self):
        if self.order_mode:
            self.food_7_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[6] += 1
            self.update_food_count_labels()

    def food_8_up_gui(self):
        if self.order_mode:
            self.food_8_up()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[7] += 1
            self.update_food_count_labels()

#############

    def food_1_down_gui(self):
        if self.order_mode:
            self.food_1_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[0] -= 1
            self.update_food_count_labels()

    def food_2_down_gui(self):
        if self.order_mode:
            self.food_2_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[1] -= 1
            self.update_food_count_labels()

    def food_3_down_gui(self):
        if self.order_mode:
            self.food_3_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[2] -= 1
            self.update_food_count_labels()

    def food_4_down_gui(self):
        if self.order_mode:
            self.food_4_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[3] -= 1
            self.update_food_count_labels()

    def food_5_down_gui(self):
        if self.order_mode:
            self.food_5_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[4] -= 1
            self.update_food_count_labels()

    def food_6_down_gui(self):
        if self.order_mode:
            self.food_6_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[5] -= 1
            self.update_food_count_labels()

    def food_7_down_gui(self):
        if self.order_mode:
            self.food_7_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[6] -= 1
            self.update_food_count_labels()

    def food_8_down_gui(self):
        if self.order_mode:
            self.food_8_down()
            self.update_food_count_labels()
            self.label_total.configure(text=(self.return_total_price_str()) + "€")
        else:
            self.new_serving[7] -= 1
            self.update_food_count_labels()
########################################################################################################################

    def return_total_price_str(self):
        price = 0
        for i in range(8):
            price += self.current_order[i] * self.food_prices[i]
        return str(price)


    def update_food_count_labels(self):
        if self.order_mode:
            food_counts = self.return_current_order_str().split(' ')
            self.label_food_1.configure(text=food_counts[0])
            self.label_food_2.configure(text=food_counts[1])
            self.label_food_3.configure(text=food_counts[2])
            self.label_food_4.configure(text=food_counts[3])
            self.label_food_5.configure(text=food_counts[4])
            self.label_food_6.configure(text=food_counts[5])
            self.label_food_7.configure(text=food_counts[6])
            self.label_food_8.configure(text=food_counts[7])
        else:
            self.label_food_1.configure(text=self.new_serving[0])
            self.label_food_2.configure(text=self.new_serving[1])
            self.label_food_3.configure(text=self.new_serving[2])
            self.label_food_4.configure(text=self.new_serving[3])
            self.label_food_5.configure(text=self.new_serving[4])
            self.label_food_6.configure(text=self.new_serving[5])
            self.label_food_7.configure(text=self.new_serving[6])
            self.label_food_8.configure(text=self.new_serving[7])


    def submit_serving_gui(self):
        self.submit_new_serving(self.new_serving)
        self.label_ordered.configure(text=self.count_current_orders_str())
        self.new_serving = [0, 0, 0, 0, 0, 0, 0, 0]
        self.update_food_count_labels()
        self.bt.send_foods(self.count_current_orders())


    def previous(self):
        self.previous_order()
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        self.update_food_count_labels()
        self.label_total.configure(text=(self.return_total_price_str()) + "€")
        self.label_ordered.configure(text=self.count_current_orders_str())
        self.update_order_history()


    def next(self):
        self.next_order()
        self.update_logfile()
        self.label_queue_number.configure(text=str(self.return_queue_number()))
        self.update_food_count_labels()
        self.label_total.configure(text=(self.return_total_price_str()) + "€")
        self.label_ordered.configure(text=self.count_current_orders_str())
        self.bt.send_foods(self.count_current_orders())
        self.update_order_history()


    def update_order_history(self):
        buf = self.return_order(self.current_queue_number - 1)
        text = str(self.current_queue_number) + "                "
        for i in range(8):
            text += str(buf[i]) + "                               "
        self.label_previous_order_1.configure(text=text)


    def exit(self):
        self.main_window.destroy()