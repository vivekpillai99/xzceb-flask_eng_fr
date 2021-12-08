"""
    Author: Vivek Pillai
    Project: IBM_Developer, Language Translator
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey=os.environ["apikey"]
url=os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    Function to translate from english text to french text
    """
    translation_response = language_translator.translate(text=english_text, \
        model_id='en-fr')
    translation = translation_response.get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text

def frenchToEnglish(french_text):
    """
    Function to translate from french text to english text
    """
    translation_response = language_translator.translate(text=french_text, \
        model_id='fr-en')
    translation = translation_response.get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
