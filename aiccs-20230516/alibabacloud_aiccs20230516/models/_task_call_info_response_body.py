# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class TaskCallInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        model: main_models.TaskCallInfoResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
        timestamp: int = None,
    ):
        self.code = code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success
        self.timestamp = timestamp

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.TaskCallInfoResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class TaskCallInfoResponseBodyModel(DaraModel):
    def __init__(
        self,
        finish_total: int = None,
        total: int = None,
        un_call_total: int = None,
    ):
        self.finish_total = finish_total
        self.total = total
        self.un_call_total = un_call_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_total is not None:
            result['FinishTotal'] = self.finish_total

        if self.total is not None:
            result['Total'] = self.total

        if self.un_call_total is not None:
            result['UnCallTotal'] = self.un_call_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTotal') is not None:
            self.finish_total = m.get('FinishTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('UnCallTotal') is not None:
            self.un_call_total = m.get('UnCallTotal')

        return self

