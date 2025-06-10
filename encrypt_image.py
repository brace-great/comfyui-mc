import random


class IncrementCounterOnMatch:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "target_value": ("INT", {"default": 0}),
                "initial_counter": ("INT", {"default": 0}),
                "input_value": ("INT",),
            }
        }

    RETURN_TYPES = ("NUMBER", "STRING")
    RETURN_NAMES = ("counter_int", "counter_str")
    FUNCTION = "execute"

    def execute(self, target_value, initial_counter, input_value):
        if not hasattr(self, "counter"):
            self.counter = initial_counter
        if input_value == target_value:
            # Set counter to a new random number between 1 and 1 trillion
            self.counter = random.randint(1, 100_000_000_000_000)
        return (
            self.counter,
            str(self.counter),
        )


NODE_CLASS_MAPPINGS = {
    "IncrementCounterOnMatch": IncrementCounterOnMatch,
}
