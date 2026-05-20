# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTraceTasksRequest(DaraModel):
    def __init__(
        self,
        client_ip: str = None,
        diagnose_id: str = None,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.client_ip = client_ip
        self.diagnose_id = diagnose_id
        self.domain_name = domain_name
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

