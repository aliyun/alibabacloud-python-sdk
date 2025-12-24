# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeForwardTableEntriesResponseBody(DaraModel):
    def __init__(
        self,
        forward_table_entries: List[main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntries] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.forward_table_entries = forward_table_entries
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.forward_table_entries:
            for v1 in self.forward_table_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ForwardTableEntries'] = []
        if self.forward_table_entries is not None:
            for k1 in self.forward_table_entries:
                result['ForwardTableEntries'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forward_table_entries = []
        if m.get('ForwardTableEntries') is not None:
            for k1 in m.get('ForwardTableEntries'):
                temp_model = main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntries()
                self.forward_table_entries.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeForwardTableEntriesResponseBodyForwardTableEntries(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_id: str = None,
        forward_entry_name: str = None,
        forward_table_id: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
        status: str = None,
    ):
        self.external_ip = external_ip
        self.external_port = external_port
        self.forward_entry_id = forward_entry_id
        self.forward_entry_name = forward_entry_name
        self.forward_table_id = forward_table_id
        self.internal_ip = internal_ip
        self.internal_port = internal_port
        self.ip_protocol = ip_protocol
        self.nat_gateway_id = nat_gateway_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_ip is not None:
            result['ExternalIp'] = self.external_ip

        if self.external_port is not None:
            result['ExternalPort'] = self.external_port

        if self.forward_entry_id is not None:
            result['ForwardEntryId'] = self.forward_entry_id

        if self.forward_entry_name is not None:
            result['ForwardEntryName'] = self.forward_entry_name

        if self.forward_table_id is not None:
            result['ForwardTableId'] = self.forward_table_id

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalIp') is not None:
            self.external_ip = m.get('ExternalIp')

        if m.get('ExternalPort') is not None:
            self.external_port = m.get('ExternalPort')

        if m.get('ForwardEntryId') is not None:
            self.forward_entry_id = m.get('ForwardEntryId')

        if m.get('ForwardEntryName') is not None:
            self.forward_entry_name = m.get('ForwardEntryName')

        if m.get('ForwardTableId') is not None:
            self.forward_table_id = m.get('ForwardTableId')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

