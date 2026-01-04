# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeForwardTableEntriesResponseBody(DaraModel):
    def __init__(
        self,
        forward_table_entries: List[main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntries] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # Details of DNAT entries.
        self.forward_table_entries = forward_table_entries
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forward_table_entries = []
        if m.get('ForwardTableEntries') is not None:
            for k1 in m.get('ForwardTableEntries'):
                temp_model = main_models.DescribeForwardTableEntriesResponseBodyForwardTableEntries()
                self.forward_table_entries.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeForwardTableEntriesResponseBodyForwardTableEntries(DaraModel):
    def __init__(
        self,
        external_ip: str = None,
        external_port: str = None,
        forward_entry_id: str = None,
        forward_entry_name: str = None,
        health_check_port: str = None,
        internal_ip: str = None,
        internal_port: str = None,
        ip_protocol: str = None,
        nat_gateway_id: str = None,
        standby_external_ip: str = None,
        standby_status: str = None,
        status: str = None,
    ):
        # The EIP in the DNAT entry. The public IP address is used to access the Internet.
        self.external_ip = external_ip
        # The external port or port range that is used in port forwarding.
        self.external_port = external_port
        # The ID of the DNAT entry.
        self.forward_entry_id = forward_entry_id
        # The name of the DNAT entry.
        self.forward_entry_name = forward_entry_name
        # The probe port of DNAT.
        self.health_check_port = health_check_port
        # The private IP address of the instance that uses the DNAT entry for Internet communication.
        self.internal_ip = internal_ip
        # The internal port or port range that is used for port forwarding.
        self.internal_port = internal_port
        # The protocol. Valid values:
        # 
        # *   **TCP**: forwards TCP packets.
        # *   **UDP**: forwards UDP packets.
        # *   **Any**: forwards all packets.
        self.ip_protocol = ip_protocol
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The secondary EIP that is used to access the Internet.
        self.standby_external_ip = standby_external_ip
        # The status of the secondary EIP. Valid values:
        # 
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Starting
        self.standby_status = standby_status
        # The status of the DNAT entry. Valid values:
        # 
        # *   Pending: The DNAT entry is being created or modified.
        # *   Available: The DNAT entry is available.
        # *   Deleting: The DNAT entry is being deleted.
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

        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port

        if self.internal_ip is not None:
            result['InternalIp'] = self.internal_ip

        if self.internal_port is not None:
            result['InternalPort'] = self.internal_port

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.standby_external_ip is not None:
            result['StandbyExternalIp'] = self.standby_external_ip

        if self.standby_status is not None:
            result['StandbyStatus'] = self.standby_status

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

        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')

        if m.get('InternalIp') is not None:
            self.internal_ip = m.get('InternalIp')

        if m.get('InternalPort') is not None:
            self.internal_port = m.get('InternalPort')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('StandbyExternalIp') is not None:
            self.standby_external_ip = m.get('StandbyExternalIp')

        if m.get('StandbyStatus') is not None:
            self.standby_status = m.get('StandbyStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

