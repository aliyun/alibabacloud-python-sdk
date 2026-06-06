# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class GetTaskExecutionStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTaskExecutionStatisticsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetTaskExecutionStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetTaskExecutionStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        completed_count: int = None,
        running_count: int = None,
        tpm_per_minute: List[main_models.GetTaskExecutionStatisticsResponseBodyDataTpmPerMinute] = None,
        waiting_count: int = None,
    ):
        self.completed_count = completed_count
        self.running_count = running_count
        self.tpm_per_minute = tpm_per_minute
        self.waiting_count = waiting_count

    def validate(self):
        if self.tpm_per_minute:
            for v1 in self.tpm_per_minute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_count is not None:
            result['completedCount'] = self.completed_count

        if self.running_count is not None:
            result['runningCount'] = self.running_count

        result['tpmPerMinute'] = []
        if self.tpm_per_minute is not None:
            for k1 in self.tpm_per_minute:
                result['tpmPerMinute'].append(k1.to_map() if k1 else None)

        if self.waiting_count is not None:
            result['waitingCount'] = self.waiting_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedCount') is not None:
            self.completed_count = m.get('completedCount')

        if m.get('runningCount') is not None:
            self.running_count = m.get('runningCount')

        self.tpm_per_minute = []
        if m.get('tpmPerMinute') is not None:
            for k1 in m.get('tpmPerMinute'):
                temp_model = main_models.GetTaskExecutionStatisticsResponseBodyDataTpmPerMinute()
                self.tpm_per_minute.append(temp_model.from_map(k1))

        if m.get('waitingCount') is not None:
            self.waiting_count = m.get('waitingCount')

        return self

class GetTaskExecutionStatisticsResponseBodyDataTpmPerMinute(DaraModel):
    def __init__(
        self,
        count: int = None,
        time: str = None,
    ):
        self.count = count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

