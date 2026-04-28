# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class GetInspectProgressResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInspectProgressResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            temp_model = main_models.GetInspectProgressResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInspectProgressResponseBodyData(DaraModel):
    def __init__(
        self,
        all_subtask_count: int = None,
        finish: bool = None,
        finish_rate: float = None,
        finish_subtask_count: int = None,
        last_inspect_date: int = None,
        task_id: int = None,
        used_time: int = None,
    ):
        self.all_subtask_count = all_subtask_count
        self.finish = finish
        self.finish_rate = finish_rate
        self.finish_subtask_count = finish_subtask_count
        self.last_inspect_date = last_inspect_date
        self.task_id = task_id
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_subtask_count is not None:
            result['AllSubtaskCount'] = self.all_subtask_count

        if self.finish is not None:
            result['Finish'] = self.finish

        if self.finish_rate is not None:
            result['FinishRate'] = self.finish_rate

        if self.finish_subtask_count is not None:
            result['FinishSubtaskCount'] = self.finish_subtask_count

        if self.last_inspect_date is not None:
            result['LastInspectDate'] = self.last_inspect_date

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllSubtaskCount') is not None:
            self.all_subtask_count = m.get('AllSubtaskCount')

        if m.get('Finish') is not None:
            self.finish = m.get('Finish')

        if m.get('FinishRate') is not None:
            self.finish_rate = m.get('FinishRate')

        if m.get('FinishSubtaskCount') is not None:
            self.finish_subtask_count = m.get('FinishSubtaskCount')

        if m.get('LastInspectDate') is not None:
            self.last_inspect_date = m.get('LastInspectDate')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

