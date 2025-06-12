import random


class IncrementCounterOnMatch:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "target_value": ("INT", {"default": 0}),
                "initial_counter": ("INT", {"default": 0}),
                "initial_float": ("FLOAT", {"default": 0.25}),
                "input_value": ("INT",),
            }
        }

    RETURN_TYPES = ("NUMBER", "STRING", "FLOAT")
    RETURN_NAMES = ("counter_int", "counter_str", "counter_float")
    FUNCTION = "execute"

    def execute(self, target_value, initial_counter, initial_float, input_value):
        if not hasattr(self, "counter"):
            self.counter = initial_counter
        if not hasattr(self, "float_value"):
            self.float_value = initial_float
        if input_value == target_value:
            # Set counter to a new random number between 1 and 1 trillion
            self.counter = random.randint(1, 100_000_000_000_000)
            # Increment float value by 0.15
            self.float_value += 0.15
        return (
            self.counter,
            str(self.counter),
            self.float_value,
        )


NODE_CLASS_MAPPINGS = {
    "IncrementCounterOnMatch": IncrementCounterOnMatch,
}
