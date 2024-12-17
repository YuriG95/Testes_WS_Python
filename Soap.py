import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import xml.etree.ElementTree as ET

def compare_soap_responses():
    url1 = url1_entry.get()
    headers1 = headers1_entry.get()
    body1 = body1_entry.get()
    url2 = url2_entry.get()
    headers2 = headers2_entry.get()
    body2 = body2_entry.get()

    if not url1 or not body1 or not url2 or not body2
       messagebox.showwarning ('Prencha os campos')
       return
    
    try
        