from datetime import datetime, timezone
import logging


logging.basicConfig(level=logging.ERROR)

logger = logging.getLogger(__name__)

print('Hello world!')
print('Learning Git!')
print('This is my third change...')

logger.debug("Debug message")
logger.info("Application started")
logger.warning("This is a warning")
logger.error("This is an error")

# name = input("What is your name? ")

current_time = datetime.now(timezone.utc)


print('This is another Sunday evening print statement!')

print(f'The time is {current_time}')

print('Some more functionality for a Sunday evening before I go for a run!!')

print('My last print statement before I go for a run')

print('This is another print statement... this time from Wednesday!!!!!')

print('Last Wednesday evening greeting')

print('First Thursday evening update')

print('Second Thursday evening update')

print('First Saturday evening update')

print('This is another Saturday evening update')

print('Third saturday evening update')

print('FOURTH Saturday evening update')

print('First Sunday evening update...........')

print('This is an update on Tuesday evening!')

print('Friday evening update.......!')

print('Minor change')

print('Another small Friday evening update!')

def greet(name: str) -> str:
	return f"Hello, {name}!"
















