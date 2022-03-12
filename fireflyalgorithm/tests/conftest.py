import logging


def pytest_configure(config):
    r"""Disable verbose output when running tests."""
    logging.basicConfig(level=logging.DEBUG)
