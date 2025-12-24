# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLdpsResourceCostResponseBody(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        job_id: str = None,
        request_id: str = None,
        start_time: int = None,
        total_resource: int = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.job_id = job_id
        self.request_id = request_id
        self.start_time = start_time
        self.total_resource = total_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_resource is not None:
            result['TotalResource'] = self.total_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalResource') is not None:
            self.total_resource = m.get('TotalResource')

        return self

