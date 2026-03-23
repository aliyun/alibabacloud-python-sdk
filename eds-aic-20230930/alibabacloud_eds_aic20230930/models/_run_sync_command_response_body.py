# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class RunSyncCommandResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.RunSyncCommandResponseBodyData] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.RunSyncCommandResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class RunSyncCommandResponseBodyData(DaraModel):
    def __init__(
        self,
        finish_time: str = None,
        instance_id: str = None,
        invocation_id: str = None,
        invocation_status: str = None,
        output: str = None,
        start_time: str = None,
    ):
        self.finish_time = finish_time
        self.instance_id = instance_id
        self.invocation_id = invocation_id
        self.invocation_status = invocation_status
        self.output = output
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id

        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status

        if self.output is not None:
            result['Output'] = self.output

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')

        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

