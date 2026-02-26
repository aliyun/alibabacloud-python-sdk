# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddImageMosaicShrinkRequest(DaraModel):
    def __init__(
        self,
        credential_config_shrink: str = None,
        image_format: str = None,
        project_name: str = None,
        quality: int = None,
        source_uri: str = None,
        target_uri: str = None,
        targets_shrink: str = None,
    ):
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
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
        self.targets_shrink = targets_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

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

        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

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

        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')

        return self

