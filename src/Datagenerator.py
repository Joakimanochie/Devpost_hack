import os
import traceback
from dotenv import load_dotenv
from src.utils import get_data
from src.utils import logging


from langchain_google_genai import ChatGoogleGenerativeAI