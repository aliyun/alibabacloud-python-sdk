# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TextTranslateShrinkRequest(DaraModel):
    def __init__(
        self,
        format_type: str = None,
        glossary: str = None,
        source_language: str = None,
        source_text_list_shrink: str = None,
        target_language: str = None,
    ):
        # The format type of the source text. Optional. Valid values: text (plain text format) and html (web page format that preserves HTML tags).
        self.format_type = format_type
        # The intervention glossary ID. Optional. Create the glossary in the console and provide its ID. If the glossary ID is empty, the translation results are not modified.
        self.glossary = glossary
        # The source language code. Optional. If not specified, the language is automatically detected. Set to auto for automatic language detection.
        self.source_language = source_language
        # The list of texts to translate. Required. The total character length cannot exceed 50,000, and the list length cannot exceed 50.
        # 
        # This parameter is required.
        self.source_text_list_shrink = source_text_list_shrink
        # The target language code. Required. More than 100 language directions are supported. For details, refer to the supported language directions list.
        # 
        # This parameter is required.
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format_type is not None:
            result['FormatType'] = self.format_type

        if self.glossary is not None:
            result['Glossary'] = self.glossary

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.source_text_list_shrink is not None:
            result['SourceTextList'] = self.source_text_list_shrink

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')

        if m.get('Glossary') is not None:
            self.glossary = m.get('Glossary')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('SourceTextList') is not None:
            self.source_text_list_shrink = m.get('SourceTextList')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        return self

