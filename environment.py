from dotenv import load_dotenv
import os

load_dotenv()
osversion = os.getenv('OS')
print(osversion)

seed = os.getenv('SEED')
print(seed)