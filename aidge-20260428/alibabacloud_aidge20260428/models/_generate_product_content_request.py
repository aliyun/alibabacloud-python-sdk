# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateProductContentRequest(DaraModel):
    def __init__(
        self,
        bullet_point_count: int = None,
        content_type: str = None,
        enable_translation: bool = None,
        max_length: int = None,
        min_length: int = None,
        operation: str = None,
        platform: str = None,
        product_attributes: str = None,
        product_category: str = None,
        source_language: str = None,
        source_text: str = None,
        target_language: str = None,
    ):
        # Takes effect only when contentType is set to bulletPoint. Valid values: 1 to 5. Default value in generate mode: 1. In rewrite mode, if manually specified, it must match the number of non-empty paragraphs in sourceText. This parameter is ignored for other copy types.
        self.bullet_point_count = bullet_point_count
        # The copy type. Valid values: title, highlight, keywords, bulletPoint, and description. When a platform is specified, you must select a type supported by the platform.
        # 
        # This parameter is required.
        self.content_type = content_type
        # Specifies whether to enable translation. Default value: false. Valid values: true and false.
        self.enable_translation = enable_translation
        # The maximum number of characters for the final complete output text. If specified, it must be an integer greater than or equal to 30. If a platform is specified and this parameter is not passed, the configured upper limit for the type on the platform is used. Example: 60.
        self.max_length = max_length
        # The minimum number of characters for the final complete output text. If specified, it must be an integer greater than or equal to 10. If a platform is specified and this parameter is not passed, the configured lower limit for the type on the platform is used.
        self.min_length = min_length
        # The operation type. Valid values: generate and rewrite.
        # 
        # This parameter is required.
        self.operation = operation
        # The target platform. Valid values: amazon, temu, tiktok, shopify, Wildberries, and tmall. If this parameter is not passed, the general scenario is used. Enum values are case-sensitive.
        self.platform = platform
        # The product attribute materials. Default value: empty. The length is 0 to 500 characters.
        self.product_attributes = product_attributes
        # The product category. Default value: an empty string. The length is 0 to 100 characters. It helps understand the category during generation and eliminates ambiguity during rewriting.
        self.product_category = product_category
        # The source language. Valid values: zh and en. Automatic language identification is not supported. Supported source languages: Chinese (zh) and English (en).
        # 
        # This parameter is required.
        self.source_language = source_language
        # The product materials or copy to be rewritten. The length is 20 to 3,000 characters.
        # 
        # This parameter is required.
        self.source_text = source_text
        # Required when enableTranslation is set to true. For valid values, see Multilingual processing. If translation is disabled, this parameter is optional. If specified, it must be the same as sourceLanguage. Supported target languages: Chinese (zh), English (en), Russian (ru), German (de), French (fr), Korean (ko), Italian (it), Thai (th), Arabic (ar), Turkish (tr), Hebrew (he), Ukrainian (uk), Polish (pl), Japanese (ja), Dutch (nl), Portuguese (pt), Spanish (es), Malay (ms), Bulgarian (bg), Indonesian (id), and Vietnamese (vi).
        self.target_language = target_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bullet_point_count is not None:
            result['BulletPointCount'] = self.bullet_point_count

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.enable_translation is not None:
            result['EnableTranslation'] = self.enable_translation

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_attributes is not None:
            result['ProductAttributes'] = self.product_attributes

        if self.product_category is not None:
            result['ProductCategory'] = self.product_category

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.source_text is not None:
            result['SourceText'] = self.source_text

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BulletPointCount') is not None:
            self.bullet_point_count = m.get('BulletPointCount')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('EnableTranslation') is not None:
            self.enable_translation = m.get('EnableTranslation')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductAttributes') is not None:
            self.product_attributes = m.get('ProductAttributes')

        if m.get('ProductCategory') is not None:
            self.product_category = m.get('ProductCategory')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('SourceText') is not None:
            self.source_text = m.get('SourceText')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        return self

