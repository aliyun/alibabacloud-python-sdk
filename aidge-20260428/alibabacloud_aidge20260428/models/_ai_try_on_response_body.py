# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class AiTryOnResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.AiTryOnResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.AiTryOnResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AiTryOnResponseBodyData(DaraModel):
    def __init__(
        self,
        image_height: str = None,
        image_url: str = None,
        image_width: str = None,
        usage_map: main_models.AiTryOnResponseBodyDataUsageMap = None,
    ):
        self.image_height = image_height
        self.image_url = image_url
        self.image_width = image_width
        self.usage_map = usage_map

    def validate(self):
        if self.usage_map:
            self.usage_map.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.image_width is not None:
            result['ImageWidth'] = self.image_width

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')

        if m.get('UsageMap') is not None:
            temp_model = main_models.AiTryOnResponseBodyDataUsageMap()
            self.usage_map = temp_model.from_map(m.get('UsageMap'))

        return self



class AiTryOnResponseBodyDataUsageMap(DaraModel):
    def __init__(
        self,
        processed_image_count: int = None,
        resolution: str = None,
    ):
        self.processed_image_count = processed_image_count
        self.resolution = resolution

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.processed_image_count is not None:
            result['ProcessedImageCount'] = self.processed_image_count

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessedImageCount') is not None:
            self.processed_image_count = m.get('ProcessedImageCount')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        return self

