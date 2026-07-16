# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageTranslationStandardRequest(DaraModel):
    def __init__(
        self,
        glossary: str = None,
        image_url: str = None,
        including_product_area: bool = None,
        source_language: str = None,
        target_language: str = None,
        translating_brand_in_the_product: bool = None,
    ):
        # The ID of the intervention glossary. This parameter is optional. Create the glossary in the console and provide its ID. If the glossary ID is empty, the translation results are not modified.
        self.glossary = glossary
        # The URL of the original image. This parameter is required. Image requirements: the width and height cannot exceed 4000 × 4000 pixels, the file size cannot exceed 10 MB, and the supported formats are png, jpeg, jpg, bmp, and webp.
        # 
        # This parameter is required.
        self.image_url = image_url
        # Specifies whether to translate text on the product subject in the image. This parameter is optional. Default value: false. This helps protect information by preventing translation of embedded information such as product names.
        self.including_product_area = including_product_area
        # The source language code. This parameter is required. For supported language directions, see the supported language directions list.
        # 
        # This parameter is required.
        self.source_language = source_language
        # The target language code. This parameter is required. For supported language directions, see the supported language directions list.
        # 
        # This parameter is required.
        self.target_language = target_language
        # Specifies whether to translate brand names on the image. This parameter is optional. Default value: false. This helps protect brand name information from being translated.
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

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.including_product_area is not None:
            result['IncludingProductArea'] = self.including_product_area

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.translating_brand_in_the_product is not None:
            result['TranslatingBrandInTheProduct'] = self.translating_brand_in_the_product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Glossary') is not None:
            self.glossary = m.get('Glossary')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('IncludingProductArea') is not None:
            self.including_product_area = m.get('IncludingProductArea')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('TranslatingBrandInTheProduct') is not None:
            self.translating_brand_in_the_product = m.get('TranslatingBrandInTheProduct')

        return self

