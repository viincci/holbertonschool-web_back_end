#!/usr/bin/env python3
"""Module contains function that takes two integers

Imports:
    List: module for list type annotation
    wait_random: function delays for n seconds and returns n
"""
import asyncio
random_wait = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Function returns create_task

    Args:
        max_delay (int): max num to delay async function

    Returns:
        _type_: asyncio task
    """
    result = asyncio.create_task(random_wait(max_delay))
    return result
