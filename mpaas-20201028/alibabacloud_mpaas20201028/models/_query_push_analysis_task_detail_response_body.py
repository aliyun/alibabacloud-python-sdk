# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryPushAnalysisTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.QueryPushAnalysisTaskDetailResponseBodyResultContent = None,
        result_message: str = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.QueryPushAnalysisTaskDetailResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class QueryPushAnalysisTaskDetailResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        data: main_models.QueryPushAnalysisTaskDetailResponseBodyResultContentData = None,
    ):
        self.data = data

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryPushAnalysisTaskDetailResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        return self

class QueryPushAnalysisTaskDetailResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        duration: str = None,
        end_time: int = None,
        push_arrival_num: float = None,
        push_num: float = None,
        push_success_num: float = None,
        start_time: int = None,
        task_id: int = None,
    ):
        self.duration = duration
        self.end_time = end_time
        self.push_arrival_num = push_arrival_num
        self.push_num = push_num
        self.push_success_num = push_success_num
        self.start_time = start_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.push_arrival_num is not None:
            result['PushArrivalNum'] = self.push_arrival_num

        if self.push_num is not None:
            result['PushNum'] = self.push_num

        if self.push_success_num is not None:
            result['PushSuccessNum'] = self.push_success_num

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PushArrivalNum') is not None:
            self.push_arrival_num = m.get('PushArrivalNum')

        if m.get('PushNum') is not None:
            self.push_num = m.get('PushNum')

        if m.get('PushSuccessNum') is not None:
            self.push_success_num = m.get('PushSuccessNum')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

