# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class ImageUpscaleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ImageUpscaleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code, such as success.
        self.code = code
        # The returned result struct.
        self.data = data
        # The returned message or error prompt.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the API call is successful. Valid values: true and false.
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
            temp_model = main_models.ImageUpscaleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImageUpscaleResponseBodyData(DaraModel):
    def __init__(
        self,
        data: main_models.ImageUpscaleResponseBodyDataData = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
        task_id: str = None,
        usage_map: main_models.ImageUpscaleResponseBodyDataUsageMap = None,
    ):
        # The high-definition upscaling result data.
        self.data = data
        # The error code returned when the request fails, such as InvalidParameter or DownstreamUnavailable.
        self.error_code = error_code
        # The error message returned when the request fails.
        self.error_message = error_message
        # Indicates whether the request is successful. Valid values: true and false.
        self.success = success
        # The ID of the downstream task. This parameter is left empty for synchronous API operations.
        self.task_id = task_id
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        if self.data:
            self.data.validate()
        if self.usage_map:
            self.usage_map.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ImageUpscaleResponseBodyDataData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UsageMap') is not None:
            temp_model = main_models.ImageUpscaleResponseBodyDataUsageMap()
            self.usage_map = temp_model.from_map(m.get('UsageMap'))

        return self

class ImageUpscaleResponseBodyDataUsageMap(DaraModel):
    def __init__(
        self,
        processed_image_count: int = None,
    ):
        # The number of processed images.
        self.processed_image_count = processed_image_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.processed_image_count is not None:
            result['ProcessedImageCount'] = self.processed_image_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessedImageCount') is not None:
            self.processed_image_count = m.get('ProcessedImageCount')

        return self

class ImageUpscaleResponseBodyDataData(DaraModel):
    def __init__(
        self,
        image_height: int = None,
        image_url: str = None,
        image_width: int = None,
    ):
        # The actual height of the generated image.
        self.image_height = image_height
        # The result information of the upscaled image.
        self.image_url = image_url
        # The actual width of the generated image.
        self.image_width = image_width

    def validate(self):
        pass

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')

        return self

