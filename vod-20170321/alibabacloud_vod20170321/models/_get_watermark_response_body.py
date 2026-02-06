# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetWatermarkResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        watermark_info: main_models.GetWatermarkResponseBodyWatermarkInfo = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the watermark template.
        self.watermark_info = watermark_info

    def validate(self):
        if self.watermark_info:
            self.watermark_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.watermark_info is not None:
            result['WatermarkInfo'] = self.watermark_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WatermarkInfo') is not None:
            temp_model = main_models.GetWatermarkResponseBodyWatermarkInfo()
            self.watermark_info = temp_model.from_map(m.get('WatermarkInfo'))

        return self

class GetWatermarkResponseBodyWatermarkInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        creation_time: str = None,
        file_url: str = None,
        is_default: str = None,
        name: str = None,
        type: str = None,
        watermark_config: str = None,
        watermark_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The time when the watermark template was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The URL of the watermark file. The URL is an Object Storage Service (OSS) URL or an Alibaba Cloud CDN URL.
        # 
        # >  This parameter is returned only for image watermark templates.
        self.file_url = file_url
        # Indicates whether the watermark template is the default one. Valid values:
        # 
        # *   **Default**
        # *   **NotDefault**
        self.is_default = is_default
        # The name of the watermark template.
        self.name = name
        # The type of the watermark template. Valid values:
        # 
        # *   **Image**: image watermark template
        # *   **Text**: text watermark template
        self.type = type
        # The configuration information of the watermark such as the display position and special effects. The value is a JSON string. The configuration parameters for image and text watermarks are different. For more information about the parameter structure, see [WatermarkConfig](~~98618#section-h01-44s-2lr~~).
        self.watermark_config = watermark_config
        # The ID of the watermark template.
        self.watermark_id = watermark_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.watermark_config is not None:
            result['WatermarkConfig'] = self.watermark_config

        if self.watermark_id is not None:
            result['WatermarkId'] = self.watermark_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WatermarkConfig') is not None:
            self.watermark_config = m.get('WatermarkConfig')

        if m.get('WatermarkId') is not None:
            self.watermark_id = m.get('WatermarkId')

        return self

