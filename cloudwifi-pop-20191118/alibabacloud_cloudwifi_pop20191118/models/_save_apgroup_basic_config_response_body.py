# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudwifi_pop20191118 import models as main_models
from darabonba.model import DaraModel

class SaveApgroupBasicConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SaveApgroupBasicConfigResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

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

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SaveApgroupBasicConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SaveApgroupBasicConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        id: int = None,
        task_id: str = None,
    ):
        self.id = id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

