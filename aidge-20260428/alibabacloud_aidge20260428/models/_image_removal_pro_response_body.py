# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class ImageRemovalProResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ImageRemovalProResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is not returned if the call is successful.
        self.code = code
        # The intelligent removal Pro result.
        self.data = data
        # The error message. This parameter is not returned if the call is successful.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed.
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
            temp_model = main_models.ImageRemovalProResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImageRemovalProResponseBodyData(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        task_id: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The URL of the result image. This parameter is returned in synchronous mode.
        self.image_url = image_url
        # The asynchronous task ID. This parameter is returned in asynchronous mode and is used to query the task result.
        self.task_id = task_id
        # The usage details. This parameter is returned in synchronous mode.
        self.usage_map = usage_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

