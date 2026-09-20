# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkLayerInterceptsResponseBody(DaraModel):
    def __init__(
        self,
        interception_record_count: int = None,
        interception_records: List[main_models.DescribeNetworkLayerInterceptsResponseBodyInterceptionRecords] = None,
        request_id: str = None,
        total_cnt: str = None,
    ):
        # The number of interception log records.
        self.interception_record_count = interception_record_count
        # The interception record details.
        self.interception_records = interception_records
        # Id of the request
        self.request_id = request_id
        # The total number of interception log entries that match the current filter conditions.
        self.total_cnt = total_cnt

    def validate(self):
        if self.interception_records:
            for v1 in self.interception_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interception_record_count is not None:
            result['InterceptionRecordCount'] = self.interception_record_count

        result['InterceptionRecords'] = []
        if self.interception_records is not None:
            for k1 in self.interception_records:
                result['InterceptionRecords'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InterceptionRecordCount') is not None:
            self.interception_record_count = m.get('InterceptionRecordCount')

        self.interception_records = []
        if m.get('InterceptionRecords') is not None:
            for k1 in m.get('InterceptionRecords'):
                temp_model = main_models.DescribeNetworkLayerInterceptsResponseBodyInterceptionRecords()
                self.interception_records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

class DescribeNetworkLayerInterceptsResponseBodyInterceptionRecords(DaraModel):
    def __init__(
        self,
        destination_ip: str = None,
        destination_port: str = None,
        intercept_action: str = None,
        intercept_count: int = None,
        intercept_end_time: int = None,
        intercept_module: str = None,
        intercept_start_time: int = None,
        network_protocol: str = None,
        protocol_number: str = None,
        source_ip: str = None,
        source_port: str = None,
    ):
        # The destination IP address.
        self.destination_ip = destination_ip
        # The destination port in the interception log.
        self.destination_port = destination_port
        # The interception action.
        self.intercept_action = intercept_action
        # The number of interceptions within the specified time range.
        self.intercept_count = intercept_count
        # The interception end time.
        #  > The value is a Unix/POSIX timestamp. Unit: seconds.
        self.intercept_end_time = intercept_end_time
        # The packet interception module.
        self.intercept_module = intercept_module
        # The interception start time.
        # > The value is a Unix/POSIX timestamp. Unit: seconds.
        self.intercept_start_time = intercept_start_time
        # The network protocol.
        self.network_protocol = network_protocol
        # The network protocol number. This is a standard network protocol number.
        self.protocol_number = protocol_number
        # The source IP address.
        self.source_ip = source_ip
        # The source port in the interception log.
        self.source_port = source_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_ip is not None:
            result['DestinationIp'] = self.destination_ip

        if self.destination_port is not None:
            result['DestinationPort'] = self.destination_port

        if self.intercept_action is not None:
            result['InterceptAction'] = self.intercept_action

        if self.intercept_count is not None:
            result['InterceptCount'] = self.intercept_count

        if self.intercept_end_time is not None:
            result['InterceptEndTime'] = self.intercept_end_time

        if self.intercept_module is not None:
            result['InterceptModule'] = self.intercept_module

        if self.intercept_start_time is not None:
            result['InterceptStartTime'] = self.intercept_start_time

        if self.network_protocol is not None:
            result['NetworkProtocol'] = self.network_protocol

        if self.protocol_number is not None:
            result['ProtocolNumber'] = self.protocol_number

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_port is not None:
            result['SourcePort'] = self.source_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationIp') is not None:
            self.destination_ip = m.get('DestinationIp')

        if m.get('DestinationPort') is not None:
            self.destination_port = m.get('DestinationPort')

        if m.get('InterceptAction') is not None:
            self.intercept_action = m.get('InterceptAction')

        if m.get('InterceptCount') is not None:
            self.intercept_count = m.get('InterceptCount')

        if m.get('InterceptEndTime') is not None:
            self.intercept_end_time = m.get('InterceptEndTime')

        if m.get('InterceptModule') is not None:
            self.intercept_module = m.get('InterceptModule')

        if m.get('InterceptStartTime') is not None:
            self.intercept_start_time = m.get('InterceptStartTime')

        if m.get('NetworkProtocol') is not None:
            self.network_protocol = m.get('NetworkProtocol')

        if m.get('ProtocolNumber') is not None:
            self.protocol_number = m.get('ProtocolNumber')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourcePort') is not None:
            self.source_port = m.get('SourcePort')

        return self

