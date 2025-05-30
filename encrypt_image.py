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

    RETURN_TYPES = ("NUMBER", "STRING")  # Changed from ("INT", "STRING")
    RETURN_NAMES = ("counter_int", "counter_str")
    FUNCTION = "execute"

    def execute(self, target_value, initial_counter, input_value):
        if not hasattr(self, "counter"):
            self.counter = initial_counter
        if input_value == target_value:
            self.counter += 10
        return (
            self.counter,
            str(self.counter),
        )  # counter is still an integer, compatible with NUMBER


NODE_CLASS_MAPPINGS = {
    "IncrementCounterOnMatch": IncrementCounterOnMatch,
}
