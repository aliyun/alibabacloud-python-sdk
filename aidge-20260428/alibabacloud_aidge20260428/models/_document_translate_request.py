# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocumentTranslateRequest(DaraModel):
    def __init__(
        self,
        file_type: str = None,
        glossary: str = None,
        target_language: str = None,
        url: str = None,
    ):
        # Supports PDF, WORD, and EXCEL formats. Use uppercase letters when specifying this parameter.
        # 
        # This parameter is required.
        self.file_type = file_type
        # ● Specify the intervention glossary ID when the intervention feature is required.   
        # ● Supports custom translation results, including:   
        # ○ Do-not-translate (ABC-ABC).   
        # ○ Specified translation (ABC-DEF).   
        # ○ Translation omission (ABC-null value).
        # This is commonly used in scenarios such as brand word protection.   
        # Example value: "glossary_1"
        self.glossary = glossary
        # The target language.
        # 
        # This parameter is required.
        self.target_language = target_language
        # The OSS URL path of the document to be translated.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.glossary is not None:
            result['Glossary'] = self.glossary

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Glossary') is not None:
            self.glossary = m.get('Glossary')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

