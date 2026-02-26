# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EncodeBlindWatermarkRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        image_quality: int = None,
        project_name: str = None,
        source_uri: str = None,
        strength_level: str = None,
        target_uri: str = None,
    ):
        # The text content of watermarks. It can be up to 256 characters in length.
        self.content = content
        # This parameter takes effect only if the input image format is JPG.
        # 
        # The storage quality of the output image that carries the watermarks. Default value: 90. Valid values: 70 to 100. The higher the quality, the larger the image size and the higher the watermark resolution quality.
        self.image_quality = image_quality
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The Object Storage Service (OSS) URI of the image.
        # 
        # Specify the value in the oss://${Bucket}/${Object} format. `${Bucket}` specifies the name of the OSS bucket that resides in the same region with the current project. `${Object}` specifies the path of the object with the extension included.
        # 
        # Supported image formats: JPG, PNG, BMP, TIFF, and WebP.
        # 
        # Image size limit: 10,000 px maximum and 80 px x 80 px minimum.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The watermark strength level. The higher the strength, the more resistant the watermarked image is to attacks, but the more the image is distorted. Default value: low. Valid values: [low, medium, high].
        self.strength_level = strength_level
        # The URI of the output image in OSS.
        # 
        # Specify the URI in the oss://${Bucket}/${Object} format, where `${Bucket}` is the name of the bucket in the same region as the current project and `${Object}` is the path of the object with the extension included.
        # 
        # > 
        # 
        # *   The format of the output image is the same as that of the input image.
        # 
        # This parameter is required.
        self.target_uri = target_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.strength_level is not None:
            result['StrengthLevel'] = self.strength_level

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('StrengthLevel') is not None:
            self.strength_level = m.get('StrengthLevel')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        return self

