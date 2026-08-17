# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrepaidTextTranslateShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_name: str = None,
        format_type: str = None,
        glossary: str = None,
        source_language: str = None,
        source_text_list_shrink: str = None,
        target_language: str = None,
        translate_scene: str = None,
    ):
        # The business scenario identifier. This parameter is optional. Valid values: e-commerce-title, e-commerce-description, e-commerce-chat, e-commerce-cpv, novel, game. If not specified or an invalid value is passed, the general translation strategy is used by default.
        self.biz_name = biz_name
        # The format type of the source text. This parameter is optional. Supports text (plain text format) and html (web page format, preserving HTML tags).
        self.format_type = format_type
        # The intervention glossary ID. This parameter is optional. The glossary must be created separately in the console, and its ID must be provided. If the glossary ID is empty, the translation result is not modified.
        self.glossary = glossary
        # The source language code. This parameter is optional. If not specified, the language is automatically detected. You can pass auto for language detection.
        self.source_language = source_language
        # The list of texts to translate. This parameter is required. The total character length cannot exceed 50,000, and the list length cannot exceed 50.
        # 
        # This parameter is required.
        self.source_text_list_shrink = source_text_list_shrink
        # The target language code. This parameter is required. More than 100 language directions are supported. For details, refer to the supported language directions list.
        # 
        # This parameter is required.
        self.target_language = target_language
        # The format of the translation text. html (web page format. This setting processes both the source text and translated text in HTML format) or text (text format. This setting processes both the source text and translated result as plain text without format processing).
        self.translate_scene = translate_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_name is not None:
            result['BizName'] = self.biz_name

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

        if self.translate_scene is not None:
            result['TranslateScene'] = self.translate_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

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

        if m.get('TranslateScene') is not None:
            self.translate_scene = m.get('TranslateScene')

        return self

