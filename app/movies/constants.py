from django.core.validators import MaxValueValidator, MinValueValidator

default_parameters = {"blank": True, "null": True}

blank_null_str = {}
blank_null_str.update(default_parameters)
blank_null_str["default"] = ""

blank_null_none = {}
blank_null_none.update(default_parameters)
blank_null_none["default"] = None

rating_validator = [MinValueValidator(0), MaxValueValidator(100)]

# --------------------------------------------

MAX_LENGTH = 255
SCHEMA = "content"
