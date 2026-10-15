# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageTranslationPlusAsyncRequest(DaraModel):
    def __init__(
        self,
        glossary: str = None,
        image_url: str = None,
        including_product_area: bool = None,
        source_language: str = None,
        target_language: str = None,
        translating_brand_in_the_product: bool = None,
        use_image_editor: bool = None,
    ):
        # The intervention glossary ID. The intervention glossary ID must be created separately and provided in the input parameters. If the provided intervention glossary ID is empty, the translation results will not be modified.
        self.glossary = glossary
        # • Image URL: Must be publicly accessible.    
        # • Format: PNG, JPEG, JPG, BMP, or WEBP.    
        # • Pixels: Both width and height must not exceed 4,000.   
        # • File size: The original file must be less than or equal to 10 MB.
        # 
        # This parameter is required.
        self.image_url = image_url
        # Specifies whether to translate the text on the image subject. This helps you protect information and prevent embedded information, such as product names, from being translated. In the example image, the text in the red box represents the text on the subject, and the text in the blue box represents the text not on the subject.
        self.including_product_area = including_product_area
        # The source language code. The value auto is supported for automatic detection.
        # 
        # This parameter is required.
        self.source_language = source_language
        # The target language code. The 12 minor language pairs listed above are recommended.
        # 
        # This parameter is required.
        self.target_language = target_language
        # Specifies whether to translate brand names in the image. This prevents brand names from being translated. Default value: false, which indicates that brand names are not translated. In the example image, \\"懒角落\\" represents a brand name.
        self.translating_brand_in_the_product = translating_brand_in_the_product
        # Specifies whether to return layout information such as the position, font, and color of the text. This can be used to obtain data when integrating the image editor for secondary editing. You can call the image translation result query API to obtain the complete parameter information.
        self.use_image_editor = use_image_editor

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

        if self.use_image_editor is not None:
            result['UseImageEditor'] = self.use_image_editor

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

        if m.get('UseImageEditor') is not None:
            self.use_image_editor = m.get('UseImageEditor')

        return self

