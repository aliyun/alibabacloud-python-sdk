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
        # The URL of the garment image. Only one image is supported. The URL must be a publicly accessible `http` or `https` address. The image must be in JPG, JPEG, PNG, BMP, or WEBP format. The resolution must be between 256×256 and 2049×2049 pixels, and the file size cannot exceed 10 MB.<br>
        self.cloth_image_url = cloth_image_url
        # The clothing type. If specified, valid values are tops, bottoms, dresses, tops_and_bottoms, shoes, and hats. If this parameter is not specified, the clothing type is automatically identified.
        self.cloth_type = cloth_type
        # The model tier. Set the value to lite. This parameter is required.
        self.mode = mode
        # The URL of the model image. Only one image is supported. The URL must be a publicly accessible `http` or `https` address. The image must be in JPG, JPEG, PNG, BMP, or WEBP format. The resolution must be between 256×256 and 2049×2049 pixels, and the file size cannot exceed 10 MB.<br>
        # 
        # This parameter is required.
        self.model_image_url = model_image_url
        # The URL of the identity template image. Only one image is supported. This parameter is mutually exclusive with PoseTemplateUrl.
        self.model_template_url = model_template_url
        # The URL of the pose template image. Only one image is supported. This parameter is mutually exclusive with ModelTemplateUrl.
        self.pose_template_url = pose_template_url
        # The aspect ratio of the output image. Valid values: 1:1, 2:3, 3:4, and 9:16. This parameter is optional. If this parameter is not specified, the aspect ratio of the original model image is used.
        self.ratio = ratio
        # The resolution of the output image. Synchronous API operations only support 1K resolution.
        # 
        # This parameter is required.
        self.resolution = resolution
        # The try-on type. Valid values: singletryon and multitryon. This parameter is optional. If this parameter is not specified, the workflow defaults to singletryon based on whether a product image is provided.
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

