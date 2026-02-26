# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class AddImageMosaicRequest(DaraModel):
    def __init__(
        self,
        credential_config: main_models.CredentialConfig = None,
        image_format: str = None,
        project_name: str = None,
        quality: int = None,
        source_uri: str = None,
        target_uri: str = None,
        targets: List[main_models.AddImageMosaicRequestTargets] = None,
    ):
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The encoding of the output image. By default, the output image uses the same encoding as the input image. Valid values: jpg, png, and webp.
        self.image_format = image_format
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The quality of the output image. This parameter applies only to JPG and WebP images. Valid values: 0 to 100. Default value: 80.
        self.quality = quality
        # The OSS URI of the input image.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # Supported formats of input images include JPG, PNG, TIFF, JP2, and BMP.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The OSS URI of the output image.
        # 
        # Specify the OSS URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # The bounding boxes and processing parameters.
        # 
        # This parameter is required.
        self.targets = targets

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.image_format is not None:
            result['ImageFormat'] = self.image_format

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.AddImageMosaicRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        return self

class AddImageMosaicRequestTargets(DaraModel):
    def __init__(
        self,
        blur_radius: int = None,
        boundary: main_models.AddImageMosaicRequestTargetsBoundary = None,
        color: str = None,
        mosaic_radius: int = None,
        sigma: int = None,
        type: str = None,
    ):
        # The radius of the Gaussian blur. Valid values: 1 to 50. Default value: 3. Unit: pixels.
        # 
        # >  This parameter takes effect only for a Gaussian blur.
        self.blur_radius = blur_radius
        # The position of the bounding box.
        # 
        # This parameter is required.
        self.boundary = boundary
        # The color of the color shape. You can specify a color by using a color code such as`#RRGGBB` or preset color names such as `red` and `white`. The default value is #FFFFFF, which is white.
        # 
        # >  This parameter takes effect only for solid color shapes.
        self.color = color
        # The radius of the mosaic. Default value: 5. Unit: pixels.
        # 
        # >  This parameter does not take effect for Gaussian blurs and solid color shapes.
        self.mosaic_radius = mosaic_radius
        # The standard deviation of the Gaussian blur. The value must be greater than 0. Default value: 5.
        # 
        # >  This parameter takes effect only for a Gaussian blur.
        self.sigma = sigma
        # The type of the mosaic effect. Valid values:
        # 
        # *   square: squares.
        # *   diamond: diamonds.
        # *   hexagon: hexagons.
        # *   blur: Gaussian blurs.
        # *   pure: solid color shapes.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blur_radius is not None:
            result['BlurRadius'] = self.blur_radius

        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()

        if self.color is not None:
            result['Color'] = self.color

        if self.mosaic_radius is not None:
            result['MosaicRadius'] = self.mosaic_radius

        if self.sigma is not None:
            result['Sigma'] = self.sigma

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlurRadius') is not None:
            self.blur_radius = m.get('BlurRadius')

        if m.get('Boundary') is not None:
            temp_model = main_models.AddImageMosaicRequestTargetsBoundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('MosaicRadius') is not None:
            self.mosaic_radius = m.get('MosaicRadius')

        if m.get('Sigma') is not None:
            self.sigma = m.get('Sigma')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AddImageMosaicRequestTargetsBoundary(DaraModel):
    def __init__(
        self,
        height: float = None,
        refer_pos: str = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        # The height of the bounding box. The value can be an integer greater than or equal to 0 or a decimal within the range of [0,1):
        # 
        # *   An integer value greater than or equal to 0 indicates the height of the bounding box in pixels.
        # *   A decimal value within the range of [0,1) indicates the height of the bounding box as a ratio of its height to the image height.
        # 
        # This parameter is required.
        self.height = height
        # The reference position of the bounding box on the image. Valid values:
        # 
        # *   topright: the upper-right corner.
        # *   topleft: the upper-left corner. This is the default value.
        # *   bottomright: the lower-right corner.
        # *   bottomleft: the lower-left corner.
        self.refer_pos = refer_pos
        # The width of the bounding box. The value can be an integer greater than or equal to 0 or a decimal within the range of [0,1):
        # 
        # *   An integer value greater than or equal to 0 indicates the width of the bounding box in pixels.
        # *   A decimal value within the range of [0,1) indicates the width of the bounding box as a ratio of its width to the image width.
        # 
        # This parameter is required.
        self.width = width
        # The horizontal offset relative to the reference position. The value can be an integer greater than or equal to 0 or a decimal within the range of [0,1):
        # 
        # *   An integer value greater than or equal to 0 indicates the horizontal offset in pixels.
        # *   A decimal value within the range of [0,1) indicates the horizontal offset as a ratio of the offset to the image width.
        # 
        # This parameter is required.
        self.x = x
        # The vertical offset relative to the reference position. The value can be an integer greater than or equal to 0 or a decimal within the range of [0,1):
        # 
        # *   An integer value greater than or equal to 0 indicates the vertical offset in pixels.
        # *   A decimal value within the range of [0,1) indicates the vertical offset as a ratio of the offset to the image height.
        # 
        # This parameter is required.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

