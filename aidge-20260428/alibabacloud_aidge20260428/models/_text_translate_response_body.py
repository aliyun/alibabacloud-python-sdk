# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class TextTranslateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TextTranslateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value "success" is returned for a successful call.
        self.code = code
        # The translation result data, which contains the translation list and usage information.
        self.data = data
        # The error message. The value "Success" is returned for a successful call. For a failed call, a specific error message is returned, such as "The parameters contain sensitive information. Try other input.".
        self.message = message
        # The request ID, which uniquely identifies the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values: true and false.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.TextTranslateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TextTranslateResponseBodyData(DaraModel):
    def __init__(
        self,
        translations: List[main_models.TextTranslateResponseBodyDataTranslations] = None,
        usage_map: Dict[str, int] = None,
    ):
        # The list of translation results. Each element corresponds to a translation result for an entry in the input text list.
        self.translations = translations
        # The usage information, including the number of input characters.
        self.usage_map = usage_map

    def validate(self):
        if self.translations:
            for v1 in self.translations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Translations'] = []
        if self.translations is not None:
            for k1 in self.translations:
                result['Translations'].append(k1.to_map() if k1 else None)

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.translations = []
        if m.get('Translations') is not None:
            for k1 in m.get('Translations'):
                temp_model = main_models.TextTranslateResponseBodyDataTranslations()
                self.translations.append(temp_model.from_map(k1))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class TextTranslateResponseBodyDataTranslations(DaraModel):
    def __init__(
        self,
        characters: int = None,
        detected_language: str = None,
        translated_text: str = None,
    ):
        # The number of characters in the source text.
        self.characters = characters
        # The automatically detected source language code.
        self.detected_language = detected_language
        # The translated text.
        self.translated_text = translated_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.characters is not None:
            result['Characters'] = self.characters

        if self.detected_language is not None:
            result['DetectedLanguage'] = self.detected_language

        if self.translated_text is not None:
            result['TranslatedText'] = self.translated_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Characters') is not None:
            self.characters = m.get('Characters')

        if m.get('DetectedLanguage') is not None:
            self.detected_language = m.get('DetectedLanguage')

        if m.get('TranslatedText') is not None:
            self.translated_text = m.get('TranslatedText')

        return self

