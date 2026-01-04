# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSnatAttributeResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        dest_cidr: str = None,
        eip_affinity: bool = None,
        idle_timeout: int = None,
        isp_affinity: bool = None,
        nat_gateway_id: str = None,
        request_id: str = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        snat_ips: List[main_models.DescribeSnatAttributeResponseBodySnatIps] = None,
        source_cidr: str = None,
        standby_snat_ip: str = None,
        standby_status: str = None,
        status: str = None,
        type: str = None,
    ):
        # The time when the entry was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The destination CIDR block. The rule takes effect only on requests that access the destination CIDR block.
        self.dest_cidr = dest_cidr
        # Specifies whether to enable IP affinity. Valid values:
        # 
        # *   **false**
        # *   **true**
        # 
        # >  After you enable IP affinity, if multiple EIPs are associated with an SNAT entry, one client uses the same EIP to for communication. If IP affinity is disabled, the client uses a random EIP for communication.
        self.eip_affinity = eip_affinity
        # The timeout period. Unit: seconds.
        self.idle_timeout = idle_timeout
        # Whether to enable operator affinity. Value taking:
        # - false:Do not open.
        # - true:Open.
        self.isp_affinity = isp_affinity
        # The ID of the Network Address Translation (NAT) gateway.
        self.nat_gateway_id = nat_gateway_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the SNAT entry.
        self.snat_entry_id = snat_entry_id
        # The name of the SNAT entry.
        self.snat_entry_name = snat_entry_name
        # The EIP specified in the SNAT entry. Multiple EIPs are separated by commas (,).
        self.snat_ip = snat_ip
        # The information about the EIP specified in the SNAT entry.
        self.snat_ips = snat_ips
        # The source CIDR block specified in the SNAT entry.
        self.source_cidr = source_cidr
        # The secondary EIP specified in the SNAT entry. Multiple secondary EIPs are separated by commas (,).
        self.standby_snat_ip = standby_snat_ip
        # The status of the secondary EIP.
        # 
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Starting
        self.standby_status = standby_status
        # The status of the SNAT entry.
        # 
        # *   Pending: The SNAT entry is being created or modified.
        # *   Available: The SNAT entry is available.
        # *   Deleting: The SNAT entry is being deleted.
        self.status = status
        # The type of the NAT.
        # 
        # *   Empty: symmetric NAT.
        # *   FullCone: full cone NAT.
        self.type = type

    def validate(self):
        if self.snat_ips:
            for v1 in self.snat_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dest_cidr is not None:
            result['DestCIDR'] = self.dest_cidr

        if self.eip_affinity is not None:
            result['EipAffinity'] = self.eip_affinity

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.isp_affinity is not None:
            result['IspAffinity'] = self.isp_affinity

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        result['SnatIps'] = []
        if self.snat_ips is not None:
            for k1 in self.snat_ips:
                result['SnatIps'].append(k1.to_map() if k1 else None)

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        if self.standby_snat_ip is not None:
            result['StandbySnatIp'] = self.standby_snat_ip

        if self.standby_status is not None:
            result['StandbyStatus'] = self.standby_status

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DestCIDR') is not None:
            self.dest_cidr = m.get('DestCIDR')

        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('IspAffinity') is not None:
            self.isp_affinity = m.get('IspAffinity')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        self.snat_ips = []
        if m.get('SnatIps') is not None:
            for k1 in m.get('SnatIps'):
                temp_model = main_models.DescribeSnatAttributeResponseBodySnatIps()
                self.snat_ips.append(temp_model.from_map(k1))

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        if m.get('StandbySnatIp') is not None:
            self.standby_snat_ip = m.get('StandbySnatIp')

        if m.get('StandbyStatus') is not None:
            self.standby_status = m.get('StandbyStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeSnatAttributeResponseBodySnatIps(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        ip: str = None,
        status: str = None,
    ):
        # The time when the IP address was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The IP address.
        self.ip = ip
        # The status of the IP address.
        # 
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Starting
        # *   Releasing
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

