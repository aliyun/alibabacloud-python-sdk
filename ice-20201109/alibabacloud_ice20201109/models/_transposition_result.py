# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TranspositionResult(DaraModel):
    def __init__(
        self,
        target_language: str = None,
        translated_text: str = None,
    ):
        self.target_language = target_language
        self.translated_text = translated_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.translated_text is not None:
            result['TranslatedText'] = self.translated_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('TranslatedText') is not None:
            self.translated_text = m.get('TranslatedText')

        return self

