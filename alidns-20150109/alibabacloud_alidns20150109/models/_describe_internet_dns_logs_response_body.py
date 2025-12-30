# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeInternetDnsLogsResponseBody(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        cur_page: int = None,
        logs: main_models.DescribeInternetDnsLogsResponseBodyLogs = None,
        page_size: int = None,
        request_id: str = None,
        total_page: int = None,
        total_size: int = None,
    ):
        # Indicates whether the log query is precise.
        self.complete = complete
        # Current page number.
        self.cur_page = cur_page
        # The queried logs.
        self.logs = logs
        # Page size for query.
        self.page_size = page_size
        # Unique request identifier.
        self.request_id = request_id
        # Total number of pages.
        self.total_page = total_page
        # Total quantity.
        self.total_size = total_size

    def validate(self):
        if self.logs:
            self.logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete is not None:
            result['Complete'] = self.complete

        if self.cur_page is not None:
            result['CurPage'] = self.cur_page

        if self.logs is not None:
            result['Logs'] = self.logs.to_map()

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')

        if m.get('CurPage') is not None:
            self.cur_page = m.get('CurPage')

        if m.get('Logs') is not None:
            temp_model = main_models.DescribeInternetDnsLogsResponseBodyLogs()
            self.logs = temp_model.from_map(m.get('Logs'))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeInternetDnsLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        log: List[main_models.DescribeInternetDnsLogsResponseBodyLogsLog] = None,
    ):
        self.log = log

    def validate(self):
        if self.log:
            for v1 in self.log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Log'] = []
        if self.log is not None:
            for k1 in self.log:
                result['Log'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log = []
        if m.get('Log') is not None:
            for k1 in m.get('Log'):
                temp_model = main_models.DescribeInternetDnsLogsResponseBodyLogsLog()
                self.log.append(temp_model.from_map(k1))

        return self

class DescribeInternetDnsLogsResponseBodyLogsLog(DaraModel):
    def __init__(
        self,
        dns_msg_id: str = None,
        log_time: int = None,
        protocol: str = None,
        query_name: str = None,
        query_type: str = None,
        rt: int = None,
        server_ip: str = None,
        source_ip: str = None,
        status: str = None,
        subnet_ip: str = None,
        value: main_models.DescribeInternetDnsLogsResponseBodyLogsLogValue = None,
        zone_name: str = None,
    ):
        # Parse log ID (can be duplicated).
        self.dns_msg_id = dns_msg_id
        # Parse timestamp.
        self.log_time = log_time
        # The protocol type of the domain name resolution query request:
        # - UDP
        # - TCP
        # - HTTP
        # - HTTPS
        # - DOH
        self.protocol = protocol
        # The domain name for which you want to query Domain Name System (DNS) records.
        self.query_name = query_name
        # Record type.
        self.query_type = query_type
        # Parse response time.
        self.rt = rt
        # Parse server IP.
        self.server_ip = server_ip
        # Source IP address.
        self.source_ip = source_ip
        # Response status.
        self.status = status
        # The value set for the edns-client-subnet option.
        self.subnet_ip = subnet_ip
        # Array of parsing results.
        self.value = value
        # The zone name.
        self.zone_name = zone_name

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_msg_id is not None:
            result['DnsMsgId'] = self.dns_msg_id

        if self.log_time is not None:
            result['LogTime'] = self.log_time

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.query_name is not None:
            result['QueryName'] = self.query_name

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.subnet_ip is not None:
            result['SubnetIp'] = self.subnet_ip

        if self.value is not None:
            result['Value'] = self.value.to_map()

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsMsgId') is not None:
            self.dns_msg_id = m.get('DnsMsgId')

        if m.get('LogTime') is not None:
            self.log_time = m.get('LogTime')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('QueryName') is not None:
            self.query_name = m.get('QueryName')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubnetIp') is not None:
            self.subnet_ip = m.get('SubnetIp')

        if m.get('Value') is not None:
            temp_model = main_models.DescribeInternetDnsLogsResponseBodyLogsLogValue()
            self.value = temp_model.from_map(m.get('Value'))

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class DescribeInternetDnsLogsResponseBodyLogsLogValue(DaraModel):
    def __init__(
        self,
        value: List[str] = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

