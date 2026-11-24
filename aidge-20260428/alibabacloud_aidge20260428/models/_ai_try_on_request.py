# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiTryOnRequest(DaraModel):
    def __init__(
        self,
        cloth_image_url: str = None,
        cloth_type: str = None,
        mode: str = None,
        model_image_url: str = None,
        model_template_url: str = None,
        pose_template_url: str = None,
        ratio: str = None,
        resolution: str = None,
        tryon_type: str = None,
    ):
        # The list of product image URLs. This parameter is required for single-item and multi-item outfit scenarios.   
        # * Single-item try-on: Pass images of the same product from different angles. The standard edition supports up to two product images, but requires that all images contain one and only one main product. We recommend that you use product images with a white background.   
        # * Multi-item outfit: Pass images of all products to be worn. The standard edition supports up to two product images (each image can contain multiple products). A single outfit can include up to six clothing items and accessories.   
        # Note: For the clothing replacement, face replacement, and posture replacement modes, specify only one mode per call. Do not upload parameters for multiple modes at the same time.
        self.cloth_image_url = cloth_image_url
        # Specifies the types of products to try on. You can specify multiple types at a time. If you do not specify this parameter, the system automatically identifies all supported categories in the product image.   
        # Valid values: tops, outwear, bottoms, dresses, tops and bottoms, socks, shoes, hats, earrings, necklaces, braceles, scarves, bags, and glasses.
        self.cloth_type = cloth_type
        # The try-on mode, which determines the maximum number of product images and outfit items. Currently, only `lite` is supported.
        self.mode = mode
        # The URL of the model scene image. You can specify only one image.   
        # * The image must support public network access over HTTP or HTTPS.   
        # * Supported formats: JPG, JPEG, PNG, BMP, and WEBP.   
        # * The width and height must be between 256 and 2049 pixels.   
        # * The size of a single file cannot exceed 10 MB.
        # 
        # This parameter is required.
        self.model_image_url = model_image_url
        # The URL of the model template image. You can specify only one image. This image provides reference identity information such as gender, skin color, age, and body type.   
        # This parameter is required for the model skin replacement scenario. Do not specify this parameter for the clothing replacement or posture replacement scenarios. For the clothing replacement, face replacement, and posture replacement modes, specify only one mode per call. Do not upload parameters for multiple modes at the same time.    
        # We recommend that you use the official model templates. Experience URL: [E-commerce Operation Assistant Aidge console](https://ecoa.console.aliyun.com/translate?category=assetOptimize&apiType=VirtualTryOn)
        self.model_template_url = model_template_url
        # The URL of the posture template image. You can specify only one image. This image provides a reference for the person\\"s posture.
        # This parameter is required for the posture fission scenario.
        # If this parameter is specified, the image is generated based on the template posture.
        # If this parameter is not specified, the posture in the scene image is used if a model scene image is provided. Otherwise, the posture in the model source image is preserved.
        # Note: For the clothing replacement, face replacement, and posture replacement modes, specify only one mode per call. Do not upload parameters for multiple modes at the same time.
        # We recommend that you use the official posture templates. Experience URL: [E-commerce Operation Assistant Aidge console](https://ecoa.console.aliyun.com/translate?category=assetOptimize&apiType=VirtualTryOn)
        self.pose_template_url = pose_template_url
        # The aspect ratio of the output image. By default, the aspect ratio is the same as that of the original image specified by ModelImageUrl. Valid values: 1:1, 2:3, 3:4, and 9:16.
        self.ratio = ratio
        # The resolution of the output image.
        # * Synchronous API: supports 1K.
        # * Asynchronous API: supports 1K and 2K. The asynchronous API only supports single-item outfit scenarios.
        # 
        # This parameter is required.
        self.resolution = resolution
        # This parameter takes effect only in try-on scenarios and specifies the number of products to try on. Default value: `singletryon`.   
        # Valid values:   
        # * `singletryon`: single-item try-on.   
        # * `multitryon`: multi-item outfit.
        self.tryon_type = tryon_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloth_image_url is not None:
            result['ClothImageUrl'] = self.cloth_image_url

        if self.cloth_type is not None:
            result['ClothType'] = self.cloth_type

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.model_image_url is not None:
            result['ModelImageUrl'] = self.model_image_url

        if self.model_template_url is not None:
            result['ModelTemplateUrl'] = self.model_template_url

        if self.pose_template_url is not None:
            result['PoseTemplateUrl'] = self.pose_template_url

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.tryon_type is not None:
            result['TryonType'] = self.tryon_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClothImageUrl') is not None:
            self.cloth_image_url = m.get('ClothImageUrl')

        if m.get('ClothType') is not None:
            self.cloth_type = m.get('ClothType')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ModelImageUrl') is not None:
            self.model_image_url = m.get('ModelImageUrl')

        if m.get('ModelTemplateUrl') is not None:
            self.model_template_url = m.get('ModelTemplateUrl')

        if m.get('PoseTemplateUrl') is not None:
            self.pose_template_url = m.get('PoseTemplateUrl')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('TryonType') is not None:
            self.tryon_type = m.get('TryonType')

        return self

