# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class EcomVideoRecreationRequest(DaraModel):
    def __init__(
        self,
        input: main_models.EcomVideoRecreationRequestInput = None,
        output: main_models.EcomVideoRecreationRequestOutput = None,
    ):
        # The input parameters for video remix.
        # 
        # This parameter is required.
        self.input = input
        # The output specifications for the final video.
        self.output = output

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.output is not None:
            result['Output'] = self.output.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.EcomVideoRecreationRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Output') is not None:
            temp_model = main_models.EcomVideoRecreationRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        return self

class EcomVideoRecreationRequestOutput(DaraModel):
    def __init__(
        self,
        duration: int = None,
        quality: str = None,
        ratio: str = None,
    ):
        # The target duration in seconds. `"auto"` (default): determined by the system. For product replacement, an integer from 5 to 60 can be specified. For person replacement, only `"auto"` is supported.
        self.duration = duration
        # The output resolution. Default value: `720p`.
        self.quality = quality
        # The output aspect ratio. Default value: `auto` (automatically matches the original video).
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        return self

class EcomVideoRecreationRequestInput(DaraModel):
    def __init__(
        self,
        change_description: str = None,
        mode: str = None,
        person_reference_image_urls: List[str] = None,
        product_image_urls: List[str] = None,
        product_info: main_models.EcomVideoRecreationRequestInputProductInfo = None,
        source_video_url: str = None,
    ):
        # The description or supplementary constraints for the target person in person replacement mode. 1 to 500 characters. Required when PersonReferenceImageUrls is not provided.   
        # Example: The target person is an adult male. Retain the original clothing and actions.
        self.change_description = change_description
        # The replacement mode. Valid values: `product_replacement` (default) and `person_replacement`.
        self.mode = mode
        # The URLs of target person reference images for person replacement. 1 to 5 images of the same person are supported. Arrange images in the following order: face close-up, front view, 45-degree angle, side view, and back view.  
        # Example: ["https://example.com/person.jpg"]
        self.person_reference_image_urls = person_reference_image_urls
        # The URL of the target product image. Required for product replacement. Exactly one image must be provided. A clear subject with no occlusion and a clean background is recommended.  
        # Example: ["https://example.com/product.png"]
        self.product_image_urls = product_image_urls
        # The target product information. Provide this parameter to improve voiceover accuracy.
        self.product_info = product_info
        # The HTTP(S) URL of the reference video. The video duration must be in the range of 2 to 360 seconds. The URL must remain accessible during task execution. Set the URL validity period to at least 24 hours.
        # 
        # This parameter is required.
        self.source_video_url = source_video_url

    def validate(self):
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_description is not None:
            result['ChangeDescription'] = self.change_description

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.person_reference_image_urls is not None:
            result['PersonReferenceImageUrls'] = self.person_reference_image_urls

        if self.product_image_urls is not None:
            result['ProductImageUrls'] = self.product_image_urls

        if self.product_info is not None:
            result['ProductInfo'] = self.product_info.to_map()

        if self.source_video_url is not None:
            result['SourceVideoUrl'] = self.source_video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeDescription') is not None:
            self.change_description = m.get('ChangeDescription')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PersonReferenceImageUrls') is not None:
            self.person_reference_image_urls = m.get('PersonReferenceImageUrls')

        if m.get('ProductImageUrls') is not None:
            self.product_image_urls = m.get('ProductImageUrls')

        if m.get('ProductInfo') is not None:
            temp_model = main_models.EcomVideoRecreationRequestInputProductInfo()
            self.product_info = temp_model.from_map(m.get('ProductInfo'))

        if m.get('SourceVideoUrl') is not None:
            self.source_video_url = m.get('SourceVideoUrl')

        return self

class EcomVideoRecreationRequestInputProductInfo(DaraModel):
    def __init__(
        self,
        category: str = None,
        detail: str = None,
        title: str = None,
    ):
        # The product category.  
        # Example: Women\\"s Clothing/Sun Protection Jacket
        self.category = category
        # The actual product information (SKU, brand, color, material, size, specifications, logo, and usage), used to constrain voiceover facts.  
        # Example: Light moon yellow, cool-touch fabric, sun protection to the back of the hand, UPF50+
        self.detail = detail
        # Required for product replacement. The name of the target product. Maximum length: 200 characters.  
        # Example: Light Moon Yellow Cool-touch Sun Protection Jacket
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

