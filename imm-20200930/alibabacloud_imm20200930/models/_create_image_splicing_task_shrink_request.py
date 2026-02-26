# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageSplicingTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        align: int = None,
        background_color: str = None,
        credential_config_shrink: str = None,
        direction: str = None,
        image_format: str = None,
        margin: int = None,
        notification_shrink: str = None,
        padding: int = None,
        project_name: str = None,
        quality: int = None,
        scale_type: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # The width or height with which the input images must align. Valid values: 1 to 4096. Unit: px.
        # 
        # *   If you set **Direction** to `vertical`, this parameter specifies the width with which the input images must align.
        # *   If you set **Direction** to `horizontal`, this parameter specifies the height with which the input images must align.
        # 
        # >  If you do not specify this parameter, the width or height of the first input image is used.
        self.align = align
        # The padding color of the spaces specified by `Padding` and `Margin`. Colors encoded in the `#FFFFFF` format and colors that are related to preset keywords such as `red` and `alpha` are supported.
        self.background_color = background_color
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The splicing method. Valid values:
        # 
        # *   vertical (default): All input images are vertically aligned and have the same width.
        # *   horizontal: All input images are horizontally aligned and have the same height.
        self.direction = direction
        # The compression format of the output image. Valid values:
        # 
        # *   jpg (default)
        # *   png
        # *   webp
        self.image_format = image_format
        # The empty space or border around the edges of the output image. Default value: 0. Unit: px.
        self.margin = margin
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        self.notification_shrink = notification_shrink
        # The space between component images in the output image. Default value: 0. Unit: px.
        self.padding = padding
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The compression quality of the output image. This parameter takes effect only for JPG and WebP images. Valid values: 0 to 100. Default value: 80.
        self.quality = quality
        # The scaling mode of the input images that are vertically or horizontally aligned. Valid values:
        # 
        # *   fit (default): Input images are scaled proportionally, and black edges are not retained.
        # *   stretch: Input images are stretched to fill the space.
        # *   horizon: Input images are horizontally stretched.
        # *   vertical: Input images are vertically stretched.
        self.scale_type = scale_type
        # The input images. The images are sliced in the order of the input image URIs.
        # 
        # This parameter is required.
        self.sources_shrink = sources_shrink
        # The custom tags. You can search for or filter asynchronous tasks by custom tag.
        self.tags_shrink = tags_shrink
        # The OSS bucket in which you want to store the output image.
        # 
        # Specify the value in the oss://${bucketname}/${objectname} format. ${bucketname} specifies the name of the OSS bucket that resides in the same region as the current project. ${objectname} specifies the path to the output image.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # The user data, which is returned as asynchronous notifications to help manage notifications within your system. The maximum length of the user data is 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.align is not None:
            result['Align'] = self.align

        if self.background_color is not None:
            result['BackgroundColor'] = self.background_color

        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.image_format is not None:
            result['ImageFormat'] = self.image_format

        if self.margin is not None:
            result['Margin'] = self.margin

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.padding is not None:
            result['Padding'] = self.padding

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quality is not None:
            result['Quality'] = self.quality

        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type

        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

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
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')

        if m.get('Margin') is not None:
            self.margin = m.get('Margin')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('Padding') is not None:
            self.padding = m.get('Padding')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quality') is not None:
            self.quality = m.get('Quality')

        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')

        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

