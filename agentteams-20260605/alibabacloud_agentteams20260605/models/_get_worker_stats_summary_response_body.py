# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetWorkerStatsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetWorkerStatsSummaryResponseBodyData = None,
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
            temp_model = main_models.GetWorkerStatsSummaryResponseBodyData()
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

class GetWorkerStatsSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        other_workers: int = None,
        running_workers: int = None,
        stopped_workers: int = None,
        total_workers: int = None,
    ):
        self.other_workers = other_workers
        self.running_workers = running_workers
        self.stopped_workers = stopped_workers
        self.total_workers = total_workers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.other_workers is not None:
            result['OtherWorkers'] = self.other_workers

        if self.running_workers is not None:
            result['RunningWorkers'] = self.running_workers

        if self.stopped_workers is not None:
            result['StoppedWorkers'] = self.stopped_workers

        if self.total_workers is not None:
            result['TotalWorkers'] = self.total_workers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OtherWorkers') is not None:
            self.other_workers = m.get('OtherWorkers')

        if m.get('RunningWorkers') is not None:
            self.running_workers = m.get('RunningWorkers')

        if m.get('StoppedWorkers') is not None:
            self.stopped_workers = m.get('StoppedWorkers')

        if m.get('TotalWorkers') is not None:
            self.total_workers = m.get('TotalWorkers')

        return self

