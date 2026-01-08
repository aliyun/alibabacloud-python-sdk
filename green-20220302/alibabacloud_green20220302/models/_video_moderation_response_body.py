# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class VideoModerationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.VideoModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.VideoModerationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class VideoModerationResponseBodyData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        task_id: str = None,
    ):
        # The ID of the moderated object.
        self.data_id = data_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

