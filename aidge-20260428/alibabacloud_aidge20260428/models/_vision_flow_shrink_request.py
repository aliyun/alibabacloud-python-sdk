# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VisionFlowShrinkRequest(DaraModel):
    def __init__(
        self,
        ability_shrink: str = None,
        back_ground_type: str = None,
        glossary: str = None,
        image_url: str = None,
        including_product_area: bool = None,
        is_filter: bool = None,
        mask: str = None,
        nonobject_detect_elements_shrink: str = None,
        nonobject_remove_elements_shrink: str = None,
        object_detect_elements_shrink: str = None,
        object_remove_elements_shrink: str = None,
        source_language: str = None,
        target_height: int = None,
        target_language: str = None,
        target_width: int = None,
        translating_brand_in_the_product: bool = None,
        upscale_factor: int = None,
    ):
        # The AI capabilities to apply (1 = intelligent element detection, 2 = intelligent matting, 3 = intelligent removal, 4 = Image Translation Pro, 5 = intelligent cropping, 6 = HD upscaling). Multiple selections allowed.
        # 
        # This parameter is required.
        self.ability_shrink = ability_shrink
        # The background type of the returned image. Valid values: WHITE_BACKGROUND (white background) and TRANSPARENT (transparent background). Required when the intelligent matting capability is selected.
        self.back_ground_type = back_ground_type
        # The intervention glossary ID. Optional. Create a glossary separately in the console and provide its ID. If left empty, translation results are not modified.
        self.glossary = glossary
        # The URL of the image to process. Required. The resolution must be greater than 256 × 256, the long side must not exceed 1920 pixels, and the short side must not exceed 1080 pixels. The file size must not exceed 5 MB. Supported formats: png, jpeg, jpg, bmp, and webp.
        # 
        # This parameter is required.
        self.image_url = image_url
        # Specifies whether to translate text on the image subject. Optional. Default value: false. Helps protect embedded information such as product names from being translated.
        self.including_product_area = including_product_area
        # Specifies whether images with the detected elements proceed to subsequent processing. A value of true indicates that images containing the elements proceed to subsequent processing. A value of false indicates that they do not. Required when the intelligent element detection capability is selected.
        self.is_filter = is_filter
        # The specific removal area in RLE format. Optional. If provided, this parameter takes priority and the ObjectRemoveElements and NonobjectRemoveElements parameters are ignored.
        self.mask = mask
        # The elements to detect on the non-subject area of the image (1 = watermark, 2 = logo, 3 = text, 4 = text-bearing color block). Multiple selections allowed. When the intelligent element detection capability is selected, at least one of NonobjectDetectElements and ObjectDetectElements is required.
        self.nonobject_detect_elements_shrink = nonobject_detect_elements_shrink
        # The elements to remove from the non-subject area of the image (1 = transparent text block, 2 = specific name, 3 = text, 4 = overlay patch). Multiple selections allowed. When the intelligent removal capability is selected, at least one of NonobjectRemoveElements and ObjectRemoveElements is required.
        self.nonobject_remove_elements_shrink = nonobject_remove_elements_shrink
        # The elements to detect on the image subject (1 = watermark, 2 = logo, 3 = text, 4 = text-bearing color block). Multiple selections allowed. When the intelligent element detection capability is selected, at least one of ObjectDetectElements and NonobjectDetectElements is required.
        self.object_detect_elements_shrink = object_detect_elements_shrink
        # The elements to remove from the image subject (1 = transparent text block, 2 = specific name, 3 = text, 4 = overlay patch). Multiple selections allowed. When the intelligent removal capability is selected, at least one of ObjectRemoveElements and NonobjectRemoveElements is required.
        self.object_remove_elements_shrink = object_remove_elements_shrink
        # The source language code. Optional. For supported language pairs, see the supported translation language pairs list.
        self.source_language = source_language
        # The desired height of the cropped image, in pixels. Valid values: 100 to 5000. Required when the intelligent cropping capability is selected.
        self.target_height = target_height
        # The target language code. Optional. For supported language pairs, see the supported translation language pairs list.
        self.target_language = target_language
        # The desired width of the cropped image, in pixels. Valid values: 100 to 5000. Required when the intelligent cropping capability is selected.
        self.target_width = target_width
        # Specifies whether to translate brand names on the image. Optional. Default value: false. Helps protect brand name information from being translated.
        self.translating_brand_in_the_product = translating_brand_in_the_product
        # The image upscaling factor. Optional. Default value: 2. Valid values: 2 to 4. Required when the HD upscaling capability is selected.
        self.upscale_factor = upscale_factor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ability_shrink is not None:
            result['Ability'] = self.ability_shrink

        if self.back_ground_type is not None:
            result['BackGroundType'] = self.back_ground_type

        if self.glossary is not None:
            result['Glossary'] = self.glossary

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.including_product_area is not None:
            result['IncludingProductArea'] = self.including_product_area

        if self.is_filter is not None:
            result['IsFilter'] = self.is_filter

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.nonobject_detect_elements_shrink is not None:
            result['NonobjectDetectElements'] = self.nonobject_detect_elements_shrink

        if self.nonobject_remove_elements_shrink is not None:
            result['NonobjectRemoveElements'] = self.nonobject_remove_elements_shrink

        if self.object_detect_elements_shrink is not None:
            result['ObjectDetectElements'] = self.object_detect_elements_shrink

        if self.object_remove_elements_shrink is not None:
            result['ObjectRemoveElements'] = self.object_remove_elements_shrink

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.target_height is not None:
            result['TargetHeight'] = self.target_height

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.target_width is not None:
            result['TargetWidth'] = self.target_width

        if self.translating_brand_in_the_product is not None:
            result['TranslatingBrandInTheProduct'] = self.translating_brand_in_the_product

        if self.upscale_factor is not None:
            result['UpscaleFactor'] = self.upscale_factor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ability') is not None:
            self.ability_shrink = m.get('Ability')

        if m.get('BackGroundType') is not None:
            self.back_ground_type = m.get('BackGroundType')

        if m.get('Glossary') is not None:
            self.glossary = m.get('Glossary')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('IncludingProductArea') is not None:
            self.including_product_area = m.get('IncludingProductArea')

        if m.get('IsFilter') is not None:
            self.is_filter = m.get('IsFilter')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('NonobjectDetectElements') is not None:
            self.nonobject_detect_elements_shrink = m.get('NonobjectDetectElements')

        if m.get('NonobjectRemoveElements') is not None:
            self.nonobject_remove_elements_shrink = m.get('NonobjectRemoveElements')

        if m.get('ObjectDetectElements') is not None:
            self.object_detect_elements_shrink = m.get('ObjectDetectElements')

        if m.get('ObjectRemoveElements') is not None:
            self.object_remove_elements_shrink = m.get('ObjectRemoveElements')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('TargetHeight') is not None:
            self.target_height = m.get('TargetHeight')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('TargetWidth') is not None:
            self.target_width = m.get('TargetWidth')

        if m.get('TranslatingBrandInTheProduct') is not None:
            self.translating_brand_in_the_product = m.get('TranslatingBrandInTheProduct')

        if m.get('UpscaleFactor') is not None:
            self.upscale_factor = m.get('UpscaleFactor')

        return self

