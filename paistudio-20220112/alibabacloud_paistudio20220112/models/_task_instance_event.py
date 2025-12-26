# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TaskInstanceEvent(DaraModel):
    def __init__(
        self,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        message: str = None,
        pod_name: str = None,
        status: str = None,
        workload_type: str = None,
    ):
        self.gmt_end_time = gmt_end_time
        self.gmt_start_time = gmt_start_time
        self.message = message
        self.pod_name = pod_name
        self.status = status
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.message is not None:
            result['Message'] = self.message

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.status is not None:
            result['Status'] = self.status

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self

