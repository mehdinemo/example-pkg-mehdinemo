from datetime import datetime


class SampleClass:
    def __init__(self, test_string, core_numbers):
        self.test_string = test_string
        self.core_numbers = core_numbers

    def method1(self, messages: str) -> dict:
        print(messages)
        results = {'input': messages}
        return results

    def print_time(self) -> str:
        message = "current time is:\t" + str(datetime.now())
        return message
