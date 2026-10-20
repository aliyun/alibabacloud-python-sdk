# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TextTranslateAsyncRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_name: str = None,
        format_type: str = None,
        glossary: str = None,
        source_language: str = None,
        source_text_list: List[str] = None,
        target_language: str = None,
        translate_scene: str = None,
    ):
        # The business ID of the caller. The maximum length is 128 characters. This ID is passed through in the translation results.
        self.biz_id = biz_id
        # The business name of the caller. This field represents your identity and facilitates subsequent communication. If you are an internal Alibaba organization, specify this parameter based on the actual scenario, such as BU name-product or BU name-chat. If you are an external partner, specify the full name of your company. The company name must be the same as the one used when registering your Alibaba Cloud account.
        self.biz_name = biz_name
        # The format type of the source text. Valid values: text and html.
        self.format_type = format_type
        # The ID of the intervention glossary. You must create the glossary in the console and provide its ID in the request parameters. If the intervention glossary ID is empty, the translation results are not modified.
        self.glossary = glossary
        # The source language code. For more information, see the supported language list below. If this parameter is not specified, the language is automatically detected.
        self.source_language = source_language
        # The list of texts to be translated.
        # 
        # This parameter is required.
        self.source_text_list = source_text_list
        # The target language code. For more information, see the supported language pair list below.
        # 
        # This parameter is required.
        self.target_language = target_language
        # The business scenario identifier. You can specify only one of the following values. After you specify a value, the translation engine uses the terminology library and style policy of the corresponding industry to output industry-specific translations. If this parameter is not specified or an invalid value is specified, the general translation policy is used. Valid values:
        # - e-commerce-title: Translates cross-border e-commerce product titles.
        # - e-commerce-description: Translates cross-border e-commerce product descriptions.
        # - e-commerce-chat: Translates cross-border e-commerce conversations.
        # - e-commerce-cpv: Translates cross-border e-commerce product CPV attributes.
        # - novel: Translates novels.
        # - game: Translates games.
        self.translate_scene = translate_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.format_type is not None:
            result['FormatType'] = self.format_type

        if self.glossary is not None:
            result['Glossary'] = self.glossary

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.source_text_list is not None:
            result['SourceTextList'] = self.source_text_list

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.translate_scene is not None:
            result['TranslateScene'] = self.translate_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('FormatType') is not None:
            self.format_type = m.get('FormatType')

        if m.get('Glossary') is not None:
            self.glossary = m.get('Glossary')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('SourceTextList') is not None:
            self.source_text_list = m.get('SourceTextList')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('TranslateScene') is not None:
            self.translate_scene = m.get('TranslateScene')

        return self

