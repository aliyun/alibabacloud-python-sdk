# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateImageSplicingTaskRequest(DaraModel):
    def __init__(
        self,
        align: int = None,
        background_color: str = None,
        credential_config: main_models.CredentialConfig = None,
        direction: str = None,
        image_format: str = None,
        margin: int = None,
        notification: main_models.Notification = None,
        padding: int = None,
        project_name: str = None,
        quality: int = None,
        scale_type: str = None,
        sources: List[main_models.CreateImageSplicingTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # The alignment value, in pixels, for the width or height of the images to be stitched. The value can range from 1 to 4096.
        # 
        # - If you set **Direction** to `vertical`, this parameter specifies the width alignment.
        # 
        # - If you set **Direction** to `horizontal`, this parameter specifies the height alignment.
        # 
        # > If you do not specify this parameter, the width or height of the first image is used for alignment by default.
        self.align = align
        # The fill color for the areas specified by `Padding` and `Margin`. The value can be in the `#FFFFFF` format or a keyword such as `red` or `alpha`.
        self.background_color = background_color
        # The chained authorization configuration. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The image stitching method. Valid values:
        # 
        # - vertical (default): Stitches images vertically. The widths of all images must be the same.
        # 
        # - horizontal: Stitches images horizontally. The heights of all images must be the same.
        self.direction = direction
        # The compression format of the output image. Valid values:
        # 
        # - jpg (default)
        # 
        # - png
        # 
        # - webp
        self.image_format = image_format
        # The blank margin, in pixels, of the stitched image. The default value is 0.
        self.margin = margin
        # The message notification configuration. For information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The space, in pixels, between sub-images in the stitched image. The default value is 0.
        self.padding = padding
        # The project name. For more information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The compression quality of the output image. This parameter is valid only for JPG and WebP images. The value range is 0 to 100. The default value is 80.
        self.quality = quality
        # The scaling method used when the width or height of an image is aligned. Valid values:
        # 
        # - fit (default): Scales the image without adding black bars. Only proportional scaling is supported.
        # 
        # - stretch: Stretches the image to fill the space.
        self.scale_type = scale_type
        # The list of input images. The images are stitched in the order of their URIs in the list.
        # 
        # This parameter is required.
        self.sources = sources
        # Custom tags used to search for and filter asynchronous tasks.
        self.tags = tags
        # The OSS URI where the output image is stored.
        # 
        # The URI must be in the oss\\://${bucketname}/${objectname} format. ${bucketname} is the name of the OSS bucket that is in the same region as the project. ${objectname} is the path of the file, including the file name.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # The custom information. This information is returned in the asynchronous notification message. Use this information to associate the notification message with your system. The maximum length is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.align is not None:
            result['Align'] = self.align

        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.image_format is not None:
            result['ImageFormat'] = self.image_format

        if self.margin is not None:
            result['Margin'] = self.margin

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.padding is not None:
            result['Padding'] = self.padding

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Align') is not None:
            self.align = m.get('Align')

        if m.get('BackgroundColor') is not None:
            self.background_color = m.get('BackgroundColor')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')

        if m.get('Margin') is not None:
            self.margin = m.get('Margin')

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('Padding') is not None:
            self.padding = m.get('Padding')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.CreateImageSplicingTaskRequestSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class CreateImageSplicingTaskRequestSources(DaraModel):
    def __init__(
        self,
        rotate: int = None,
        uri: str = None,
    ):
        # The rotation angle of the image. Valid values:
        # 
        # - 0 (default)
        # 
        # - 90
        # 
        # - 180
        # 
        # - 270
        self.rotate = rotate
        # The OSS URI of the source image.
        # 
        # The URI must be in the oss\\://${Bucket}/${Object} format. `${Bucket}` is the name of the OSS bucket that is in the same region as the project. `${Object}` is the full path of the file, including the file name extension.
        # 
        # Supported image formats: JPG and PNG.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

