# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TextCorrectRequest(DaraModel):
    def __init__(
        self,
        source_language: str = None,
        source_text: str = None,
    ):
        # Source language code. Required. You can pass "auto" for automatic language detection. Supports 14 languages.
        # 
        # This parameter is required.
        self.source_language = source_language
        # Text to be corrected. Required.
        # 
        # This parameter is required.
        self.source_text = source_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.source_text is not None:
            result['SourceText'] = self.source_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')

        return self

