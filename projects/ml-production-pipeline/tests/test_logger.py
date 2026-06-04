import logging

from src.utils.logger import get_logger


def test_get_logger_returns_logger_with_expected_name():
    logger = get_logger("test_logger")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"


def test_get_logger_does_not_add_duplicate_handlers():
    logger = get_logger("duplicate_handler_test")
    initial_handler_count = len(logger.handlers)

    same_logger = get_logger("duplicate_handler_test")

    assert same_logger is logger
    assert len(same_logger.handlers) == initial_handler_count


def test_get_logger_disables_propagation():
    logger = get_logger("propagation_test")

    assert logger.propagate is False
