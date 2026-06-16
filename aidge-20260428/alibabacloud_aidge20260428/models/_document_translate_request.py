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
        # The type of the document. Valid values: PDF and Word. Size limits: Word 200 MB/300 pages, PDF 200 MB/300 pages. The maximum size of a single file is 200 MB.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The glossary ID to use when the glossary feature is required. Supports custom translation results, including do-not-translate (ABC-ABC), specified translation (ABC-DEF), and skip translation (ABC-empty value). This is commonly used for brand name protection.
        self.glossary = glossary
        # The target language. The language code uses the two-letter ISO 639-1 standard.
        # 
        # This parameter is required.
        self.target_language = target_language
        # The OSS URL of the document to be translated.
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

