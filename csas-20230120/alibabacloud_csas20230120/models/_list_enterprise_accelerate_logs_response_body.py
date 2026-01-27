# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListEnterpriseAccelerateLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[main_models.ListEnterpriseAccelerateLogsResponseBodyLogs] = None,
        request_id: str = None,
        total_number: int = None,
    ):
        self.logs = logs
        self.request_id = request_id
        self.total_number = total_number

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.ListEnterpriseAccelerateLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

class ListEnterpriseAccelerateLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        department: str = None,
        device_type: str = None,
        dst_addr: str = None,
        in_bytes: str = None,
        out_bytes: str = None,
        policy_name: str = None,
        proxy_addr: str = None,
        unix_time: str = None,
        username: str = None,
    ):
        self.department = department
        self.device_type = device_type
        self.dst_addr = dst_addr
        self.in_bytes = in_bytes
        self.out_bytes = out_bytes
        self.policy_name = policy_name
        self.proxy_addr = proxy_addr
        self.unix_time = unix_time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department is not None:
            result['Department'] = self.department

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.dst_addr is not None:
            result['DstAddr'] = self.dst_addr

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.proxy_addr is not None:
            result['ProxyAddr'] = self.proxy_addr

        if self.unix_time is not None:
            result['UnixTime'] = self.unix_time

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('DstAddr') is not None:
            self.dst_addr = m.get('DstAddr')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('ProxyAddr') is not None:
            self.proxy_addr = m.get('ProxyAddr')

        if m.get('UnixTime') is not None:
            self.unix_time = m.get('UnixTime')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

