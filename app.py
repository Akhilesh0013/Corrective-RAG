import nest_asyncio
nest_asyncio.apply()

from dotenv import load_dotenv
load_dotenv()

import logging
import sys
import os
import asyncio
import streamlit as st
import qdrant_client
import base64
import gc
import tempfile
import uuid
import time
from IPython.display import Markdown, display
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.core import Settings
from workflow import CorrectiveRAGWorkflow
import io
from contextlib import redirect_stdout



st.set_page_config(page_title="Corrective RAG Demo", layout="wide")

if "id" not in st.session_state:
    st.session_state.id = uuid.uuid4()
    st.session_state.file_cache = {}
    
if "workflow" not in st.session_state:
    st.session_state.workflow = None
    
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "workflow_logs" not in st.session_state:
    st.session_state.workflow_logs = []

session_id = st.session_state.id