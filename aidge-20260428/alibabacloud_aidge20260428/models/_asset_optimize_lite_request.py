# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssetOptimizeLiteRequest(DaraModel):
    def __init__(
        self,
        glossary: str = None,
        including_product_area: bool = None,
        need_trans: bool = None,
        product_url: str = None,
        source_language: str = None,
        source_platform: str = None,
        target_language: str = None,
        target_platform: str = None,
        translating_brand_in_the_product: bool = None,
    ):
        # Custom glossary
        self.glossary = glossary
        # Whether to include product region translation
        self.including_product_area = including_product_area
        # Whether translation is required
        # 
        # This parameter is required.
        self.need_trans = need_trans
        # Product Link URL
        # 
        # This parameter is required.
        self.product_url = product_url
        # Source language code, e.g., zh
        self.source_language = source_language
        # Source platform, e.g., 1688
        # 
        # This parameter is required.
        self.source_platform = source_platform
        # Target language code, e.g., en
        self.target_language = target_language
        # Target platform, e.g., temu
        # 
        # This parameter is required.
        self.target_platform = target_platform
        # Whether to translate brand names in images, default false
        self.translating_brand_in_the_product = translating_brand_in_the_product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.glossary is not None:
            result['Glossary'] = self.glossary

        if self.including_product_area is not None:
            result['IncludingProductArea'] = self.including_product_area

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

        if self.translating_brand_in_the_product is not None:
            result['TranslatingBrandInTheProduct'] = self.translating_brand_in_the_product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Glossary') is not None:
            self.glossary = m.get('Glossary')

        if m.get('IncludingProductArea') is not None:
            self.including_product_area = m.get('IncludingProductArea')

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

        if m.get('TranslatingBrandInTheProduct') is not None:
            self.translating_brand_in_the_product = m.get('TranslatingBrandInTheProduct')

        return self

