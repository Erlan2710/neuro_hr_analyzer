import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

import re
import time
import json
import codecs
import pathlib
import tempfile
import warnings
import logging
import requests
from datetime import timedelta
from pathlib import Path

from tqdm.auto import tqdm

# LangChain и OpenAI
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma, FAISS
from langchain.prompts import PromptTemplate

import tiktoken

