# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSnatTableEntriesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snat_table_entries: List[main_models.DescribeSnatTableEntriesResponseBodySnatTableEntries] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The details of the SNAT entries.
        self.snat_table_entries = snat_table_entries
        # The number of SNAT entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.snat_table_entries:
            for v1 in self.snat_table_entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SnatTableEntries'] = []
        if self.snat_table_entries is not None:
            for k1 in self.snat_table_entries:
                result['SnatTableEntries'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.snat_table_entries = []
        if m.get('SnatTableEntries') is not None:
            for k1 in m.get('SnatTableEntries'):
                temp_model = main_models.DescribeSnatTableEntriesResponseBodySnatTableEntries()
                self.snat_table_entries.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSnatTableEntriesResponseBodySnatTableEntries(DaraModel):
    def __init__(
        self,
        eip_affinity: bool = None,
        idle_timeout: int = None,
        isp_affinity: bool = None,
        nat_gateway_id: str = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        source_cidr: str = None,
        standby_snat_ip: str = None,
        standby_status: str = None,
        status: str = None,
    ):
        # Specifies whether to enable EIP affinity. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # **
        # 
        # **Description** After you enable EIP affinity, if multiple EIPs are associated with an SNAT entry, each client uses one EIP to access the Internet. If EIP affinity is disabled, each client uses a random EIP to access the Internet.
        self.eip_affinity = eip_affinity
        # The timeout period for idle connections. Valid values: **1** to **86400**. Unit: seconds.
        self.idle_timeout = idle_timeout
        # Whether to enable operator affinity. Value taking:
        # 
        # - false:Do not open.
        # 
        # - true:Open.
        self.isp_affinity = isp_affinity
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The ID of the SNAT entry.
        self.snat_entry_id = snat_entry_id
        # The name of the SNAT entry.
        self.snat_entry_name = snat_entry_name
        # The EIP specified in the SNAT entry.
        self.snat_ip = snat_ip
        # The source CIDR block specified in the SNAT entry.
        self.source_cidr = source_cidr
        # The secondary EIP. Multiple EIPs are separated by commas (,).
        self.standby_snat_ip = standby_snat_ip
        # The status of the secondary EIP. Valid values:
        # 
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Starting
        self.standby_status = standby_status
        # The status of the SNAT entry. Valid values:
        # 
        # *   Pending: The SNAT entry is being created or modified.
        # *   Available: The SNAT entry is available.
        # *   Deleting: The SNAT entry is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_affinity is not None:
            result['EipAffinity'] = self.eip_affinity

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.isp_affinity is not None:
            result['IspAffinity'] = self.isp_affinity

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        if self.standby_snat_ip is not None:
            result['StandbySnatIp'] = self.standby_snat_ip

        if self.standby_status is not None:
            result['StandbyStatus'] = self.standby_status

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('IspAffinity') is not None:
            self.isp_affinity = m.get('IspAffinity')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        if m.get('StandbySnatIp') is not None:
            self.standby_snat_ip = m.get('StandbySnatIp')

        if m.get('StandbyStatus') is not None:
            self.standby_status = m.get('StandbyStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

