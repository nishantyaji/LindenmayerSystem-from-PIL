import ImageTrtl as turtle

class LindenMayerSystem:

    def __init__(self, start_string='', iterations=1, rules_dict={}, measures_dict={}, fn_dict={}):
        self.rules_dict = rules_dict
        self.state_string = start_string
        self.iterations = iterations
        self.fn_dict = fn_dict

    def set_rules_dict(self, rules_dict):
        self.rules_dict = rules_dict

    def display(self, turtle1=turtle.ImageTrtl()):
        for _ in range(0, self.iterations):
            self.__apply_rules()
        self.__draw_turtle_fn(turtle1)
        turtle1.show()

    def __apply_rules(self):
        new_state = ''
        for char in self.state_string:
            translated_chars = self.rules_dict[char] if char in self.rules_dict else char
            new_state = new_state + translated_chars
        self.state_string = new_state

    def __draw_turtle_fn(self, turtle1):
        for char in self.state_string:
            if char in self.fn_dict:
                fn = self.fn_dict[char]
                fn(turtle1)
