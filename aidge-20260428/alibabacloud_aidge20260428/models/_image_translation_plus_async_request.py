# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageTranslationPlusAsyncRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        glossary: str = None,
        image_url: str = None,
        including_product_area: bool = None,
        source_language: str = None,
        target_language: str = None,
        translating_brand_in_the_product: bool = None,
        use_image_editor: bool = None,
    ):
        # The business order ID of the caller. This ID is recorded when the request is accepted and returned as is when you query the asynchronous task result.
        self.biz_id = biz_id
        # The intervention glossary ID. You must create the intervention glossary separately and provide its ID in the input parameters. If the provided intervention glossary ID is empty, the translation results are not modified.
        self.glossary = glossary
        # * Image URL: The image must be accessible over the Internet.    
        # * Format: PNG, JPEG, JPG, BMP, or WEBP.    
        # * Resolution: The width and height cannot exceed 4,000 pixels.   
        # * File size: The original file size cannot exceed 10 MB.
        # 
        # This parameter is required.
        self.image_url = image_url
        # Specifies whether to translate the text on the image subject. This helps you protect information and prevent embedded information, such as the product name, from being translated. In the example image, the text in the red box represents the text on the subject, and the text in the blue box represents the text not on the subject.
        self.including_product_area = including_product_area
        # The source language code. The value auto is supported for automatic detection.
        # 
        # This parameter is required.
        self.source_language = source_language
        # The target language code. We recommend that you use the 12 minor language pairs listed above.
        # 
        # This parameter is required.
        self.target_language = target_language
        # Specifies whether to translate the brand name in the image. This prevents the brand name from being translated. Default value: false. In the example image, \\"懒角落\\" represents the brand name.
        self.translating_brand_in_the_product = translating_brand_in_the_product
        # Specifies whether to return layout information such as the position, font, and color of the text. This can be used to obtain data when you integrate the image editor for secondary editing. You can call the image translation result data query API operation to obtain the complete parameter information.
        self.use_image_editor = use_image_editor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

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
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

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

