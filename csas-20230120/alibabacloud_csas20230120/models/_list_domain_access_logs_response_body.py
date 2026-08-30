# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListDomainAccessLogsResponseBody(DaraModel):
    def __init__(
        self,
        access_logs: List[main_models.ListDomainAccessLogsResponseBodyAccessLogs] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of access log records.
        self.access_logs = access_logs
        # Id of the request
        self.request_id = request_id
        # The total number of records that match the query conditions.
        self.total_num = total_num

    def validate(self):
        if self.access_logs:
            for v1 in self.access_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessLogs'] = []
        if self.access_logs is not None:
            for k1 in self.access_logs:
                result['AccessLogs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_logs = []
        if m.get('AccessLogs') is not None:
            for k1 in m.get('AccessLogs'):
                temp_model = main_models.ListDomainAccessLogsResponseBodyAccessLogs()
                self.access_logs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListDomainAccessLogsResponseBodyAccessLogs(DaraModel):
    def __init__(
        self,
        block_action: str = None,
        department: str = None,
        dest_address: str = None,
        event_time: str = None,
        l_4protocol_type: str = None,
        process_name: str = None,
        remote_address: str = None,
        remote_host: str = None,
        remote_port: str = None,
        src_address: str = None,
        username: str = None,
    ):
        # The action taken upon a rule hit.
        self.block_action = block_action
        # The department.
        self.department = department
        # The destination URL accessed.
        self.dest_address = dest_address
        # The event time.
        self.event_time = event_time
        # The Layer 4 protocol type.
        self.l_4protocol_type = l_4protocol_type
        # The name of the client process that initiated the access.
        self.process_name = process_name
        # The destination IP address.
        self.remote_address = remote_address
        # The destination domain name.
        self.remote_host = remote_host
        # The destination port.
        self.remote_port = remote_port
        # The source address of the client.
        self.src_address = src_address
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_action is not None:
            result['BlockAction'] = self.block_action

        if self.department is not None:
            result['Department'] = self.department

        if self.dest_address is not None:
            result['DestAddress'] = self.dest_address

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.l_4protocol_type is not None:
            result['L4ProtocolType'] = self.l_4protocol_type

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.remote_address is not None:
            result['RemoteAddress'] = self.remote_address

        if self.remote_host is not None:
            result['RemoteHost'] = self.remote_host

        if self.remote_port is not None:
            result['RemotePort'] = self.remote_port

        if self.src_address is not None:
            result['SrcAddress'] = self.src_address

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockAction') is not None:
            self.block_action = m.get('BlockAction')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DestAddress') is not None:
            self.dest_address = m.get('DestAddress')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('L4ProtocolType') is not None:
            self.l_4protocol_type = m.get('L4ProtocolType')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('RemoteAddress') is not None:
            self.remote_address = m.get('RemoteAddress')

        if m.get('RemoteHost') is not None:
            self.remote_host = m.get('RemoteHost')

        if m.get('RemotePort') is not None:
            self.remote_port = m.get('RemotePort')

        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

