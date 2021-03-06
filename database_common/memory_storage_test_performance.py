import logging

from config.config import TestPerformanceConfig
from utils.boolean_utils import to_bool
from utils.to_number import to_float

logger = logging.getLogger("MemoryStoragePerformance")


class MemoryStoragePerformance:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MemoryStoragePerformance.__instance == None:
            MemoryStoragePerformance()
        return MemoryStoragePerformance.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self.calculate_performance = to_bool(TestPerformanceConfig.CALCULATE_PERFORMANCE)
        if MemoryStoragePerformance.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MemoryStoragePerformance.__instance = self
        self.storage = {}

    def set(self, key, value):
        if not self.calculate_performance:
            return 0
        self.storage[key] = value

    def get(self, key):
        if not self.calculate_performance:
            return 0
        try:
            return self.storage[key]
        except Exception as e:
            logger.warning(f"key {e} not found")
            return 0

    def set_calculate_performance(self, calculate_performance=True):
        self.calculate_performance = calculate_performance

    def get_calculate_performance(self):
        return self.calculate_performance

    def get_keys(self):
        return self.storage.keys()

    def accumulate_to_key(self, key, amount):
        if not self.calculate_performance:
            return 0
        try:
            self.storage[key] += amount
        except Exception as e:
            logger.warning(f"key {e} created")
            self.storage[key] = to_float(amount)
