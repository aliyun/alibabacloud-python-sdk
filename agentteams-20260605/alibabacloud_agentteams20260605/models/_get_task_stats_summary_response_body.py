# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetTaskStatsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTaskStatsSummaryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetTaskStatsSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTaskStatsSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        average_task_duration: float = None,
        status_distribution: List[main_models.GetTaskStatsSummaryResponseBodyDataStatusDistribution] = None,
        task_token_consumption: int = None,
        total_tasks: int = None,
    ):
        self.average_task_duration = average_task_duration
        self.status_distribution = status_distribution
        self.task_token_consumption = task_token_consumption
        self.total_tasks = total_tasks

    def validate(self):
        if self.status_distribution:
            for v1 in self.status_distribution:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_task_duration is not None:
            result['AverageTaskDuration'] = self.average_task_duration

        result['StatusDistribution'] = []
        if self.status_distribution is not None:
            for k1 in self.status_distribution:
                result['StatusDistribution'].append(k1.to_map() if k1 else None)

        if self.task_token_consumption is not None:
            result['TaskTokenConsumption'] = self.task_token_consumption

        if self.total_tasks is not None:
            result['TotalTasks'] = self.total_tasks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageTaskDuration') is not None:
            self.average_task_duration = m.get('AverageTaskDuration')

        self.status_distribution = []
        if m.get('StatusDistribution') is not None:
            for k1 in m.get('StatusDistribution'):
                temp_model = main_models.GetTaskStatsSummaryResponseBodyDataStatusDistribution()
                self.status_distribution.append(temp_model.from_map(k1))

        if m.get('TaskTokenConsumption') is not None:
            self.task_token_consumption = m.get('TaskTokenConsumption')

        if m.get('TotalTasks') is not None:
            self.total_tasks = m.get('TotalTasks')

        return self

class GetTaskStatsSummaryResponseBodyDataStatusDistribution(DaraModel):
    def __init__(
        self,
        count: int = None,
        status: str = None,
    ):
        self.count = count
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

