# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListTraceTasksResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        list: List[main_models.ListTraceTasksResponseBodyList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The number of pages.
        self.count = count
        # The returned list information.
        self.list = list
        # The page number, starting from 1.
        self.page_number = page_number
        # The page size. Valid values: any integer from 1 to 1000.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListTraceTasksResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTraceTasksResponseBodyList(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        client_addr: str = None,
        client_ip: str = None,
        create_time: str = None,
        diagnose_id: str = None,
        diagnose_url: str = None,
        domain: str = None,
        expire_time: int = None,
        remain_diagnose_times: int = None,
        state: str = None,
        status: int = None,
        task_id: str = None,
        time_consuming: int = None,
        trace_id: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.aliuid = aliuid
        # The IP address of the local DNS server.
        self.client_addr = client_addr
        # The client IP address.
        self.client_ip = client_ip
        # The time when the report was created. Format: yyyy-MM-dd HH:mm:ss. Time zone: UTC+8.
        self.create_time = create_time
        # The diagnose ID.
        self.diagnose_id = diagnose_id
        # The diagnostic URL.
        self.diagnose_url = diagnose_url
        # The domain name to diagnose.
        self.domain = domain
        # The expiration time. The value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time
        # The remaining number of available diagnostic attempts.
        self.remain_diagnose_times = remain_diagnose_times
        # The report generation status. Valid values:
        # 
        # - 0: Succeeded.
        # - 1: Failed.
        # - 2: Timed out.
        # - 3: Running.
        # - 4: Waiting.
        self.state = state
        # The status of the diagnostic URL. Valid values:
        # 
        # - 1: active
        # - 0: expired.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The time consumed to generate the report.
        self.time_consuming = time_consuming
        # The diagnostic trace ID.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.diagnose_url is not None:
            result['DiagnoseUrl'] = self.diagnose_url

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.remain_diagnose_times is not None:
            result['RemainDiagnoseTimes'] = self.remain_diagnose_times

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.time_consuming is not None:
            result['TimeConsuming'] = self.time_consuming

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('DiagnoseUrl') is not None:
            self.diagnose_url = m.get('DiagnoseUrl')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RemainDiagnoseTimes') is not None:
            self.remain_diagnose_times = m.get('RemainDiagnoseTimes')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TimeConsuming') is not None:
            self.time_consuming = m.get('TimeConsuming')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

