# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class ImageMattingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ImageMattingResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The matting result.
        self.data = data
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: Successful.
        # - false: Failed.
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
            temp_model = main_models.ImageMattingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImageMattingResponseBodyData(DaraModel):
    def __init__(
        self,
        height: int = None,
        image_url: str = None,
        score: float = None,
        usage_map: Dict[str, int] = None,
        width: int = None,
    ):
        # The height of the result image in pixels.
        self.height = height
        # The URL of the matting result image.
        self.image_url = image_url
        # The quality score of the matting result.
        self.score = score
        # The usage information.
        self.usage_map = usage_map
        # The width of the result image in pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.score is not None:
            result['Score'] = self.score

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

