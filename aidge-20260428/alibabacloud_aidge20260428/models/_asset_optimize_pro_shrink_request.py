# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssetOptimizeProShrinkRequest(DaraModel):
    def __init__(
        self,
        column_name_list_shrink: str = None,
        glossary: str = None,
        including_product_area: bool = None,
        language_model: str = None,
        need_trans: bool = None,
        product_url: str = None,
        source_language: str = None,
        source_platform: str = None,
        target_language: str = None,
        target_platform: str = None,
        threshold: float = None,
        translating_brand_in_the_product: bool = None,
    ):
        # The list of column names to be recognized in the size chart. This parameter is optional.
        self.column_name_list_shrink = column_name_list_shrink
        # The ID of the intervention glossary. This parameter is optional. You must create the glossary in the console and provide its ID. If this parameter is left empty, the translation results are not modified.
        self.glossary = glossary
        # Specifies whether to translate the text on the main subject of the image. This helps protect embedded information such as product names from being translated. Default value: false.
        self.including_product_area = including_product_area
        # The output language format for the size chart. If this parameter is left empty, the original language is used. Valid values: en for English, cn for Chinese.
        self.language_model = language_model
        # Specifies whether translation is required. Valid values: true and false. If this parameter is set to true, SourceLanguage and TargetLanguage are required.
        # 
        # This parameter is required.
        self.need_trans = need_trans
        # The product URL. This parameter is required. Currently, only 1688 product links are supported.
        # 
        # This parameter is required.
        self.product_url = product_url
        # The source language code. This parameter is optional. For supported language pairs, see the list of supported translation languages. This parameter is required if NeedTrans is set to true.
        self.source_language = source_language
        # The source platform. Currently, only 1688 is supported.
        # 
        # This parameter is required.
        self.source_platform = source_platform
        # The target language code. This parameter is optional. For supported language pairs, see the list of supported translation languages. This parameter is required if NeedTrans is set to true.
        self.target_language = target_language
        # The target platform for product listing. Currently, only TEMU is supported.
        # 
        # This parameter is required.
        self.target_platform = target_platform
        # The confidence threshold for size chart detection. Default value: 0.4. If this parameter is set to 0, all images are considered size charts. If this parameter is set to 1, no images are considered size charts.
        self.threshold = threshold
        # Specifies whether to translate brand names in images. This parameter is optional. Default value: false. This helps protect brand names from being translated.
        self.translating_brand_in_the_product = translating_brand_in_the_product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name_list_shrink is not None:
            result['ColumnNameList'] = self.column_name_list_shrink

        if self.glossary is not None:
            result['Glossary'] = self.glossary

        if self.including_product_area is not None:
            result['IncludingProductArea'] = self.including_product_area

        if self.language_model is not None:
            result['LanguageModel'] = self.language_model

        if self.need_trans is not None:
            result['NeedTrans'] = self.need_trans

        if self.product_url is not None:
            result['ProductUrl'] = self.product_url

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.source_platform is not None:
            result['SourcePlatform'] = self.source_platform

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.target_platform is not None:
            result['TargetPlatform'] = self.target_platform

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.translating_brand_in_the_product is not None:
            result['TranslatingBrandInTheProduct'] = self.translating_brand_in_the_product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnNameList') is not None:
            self.column_name_list_shrink = m.get('ColumnNameList')

        if m.get('Glossary') is not None:
            self.glossary = m.get('Glossary')

        if m.get('IncludingProductArea') is not None:
            self.including_product_area = m.get('IncludingProductArea')

        if m.get('LanguageModel') is not None:
            self.language_model = m.get('LanguageModel')

        if m.get('NeedTrans') is not None:
            self.need_trans = m.get('NeedTrans')

        if m.get('ProductUrl') is not None:
            self.product_url = m.get('ProductUrl')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('SourcePlatform') is not None:
            self.source_platform = m.get('SourcePlatform')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('TargetPlatform') is not None:
            self.target_platform = m.get('TargetPlatform')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('TranslatingBrandInTheProduct') is not None:
            self.translating_brand_in_the_product = m.get('TranslatingBrandInTheProduct')

        return self

