# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddWatermarkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        file_url: str = None,
        name: str = None,
        type: str = None,
        watermark_config: str = None,
    ):
        # The application ID. Default value: **app-1000000**. If you have activated the multi-application service, specify the application ID to add the watermark template to the specified application. For more information, see [Multi-application service](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The Object Storage Service (OSS) URL of the watermark image file (without authentication).
        # >- Request parameter is required when you set an image watermark template (`Type` is `Image`).
        # >- You can call [CreateUploadAttachedMedia](~~CreateUploadAttachedMedia~~) to upload the watermark image to ApsaraVideo VOD. The value of the `FileURL` parameter returned after the upload can be used as the value of request parameter.
        self.file_url = file_url
        # The name of the watermark template.
        # - Only Chinese characters, letters, and digits are supported.
        # - The name can be up to 128 bytes in length.
        # - UTF-8 encoding.
        # 
        # This parameter is required.
        self.name = name
        # The templatetype of the watermark. Valid values:
        # - **Image** (default): image watermark template.
        # - **Text**: text watermark template.
        # 
        # This parameter is required.
        self.type = type
        # The configuration information of the watermark (JSON string), including the display position and effect of the watermark. The configuration parameters differ between image watermarks and text watermarks. For more information about the parameter structure, see [WatermarkConfig](~~98618#section-h01-44s-2lr~~).
        # 
        # This parameter is required.
        self.watermark_config = watermark_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')

        return self

