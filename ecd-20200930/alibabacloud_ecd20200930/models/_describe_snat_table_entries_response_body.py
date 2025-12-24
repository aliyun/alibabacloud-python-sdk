# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeSnatTableEntriesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        snat_table_entries: List[main_models.DescribeSnatTableEntriesResponseBodySnatTableEntries] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.snat_table_entries = snat_table_entries

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SnatTableEntries'] = []
        if self.snat_table_entries is not None:
            for k1 in self.snat_table_entries:
                result['SnatTableEntries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.snat_table_entries = []
        if m.get('SnatTableEntries') is not None:
            for k1 in m.get('SnatTableEntries'):
                temp_model = main_models.DescribeSnatTableEntriesResponseBodySnatTableEntries()
                self.snat_table_entries.append(temp_model.from_map(k1))

        return self

class DescribeSnatTableEntriesResponseBodySnatTableEntries(DaraModel):
    def __init__(
        self,
        eip_affinity: str = None,
        nat_gateway_id: str = None,
        snat_entry_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        snat_table_id: str = None,
        source_cidr: str = None,
        source_vswitch_id: str = None,
        status: str = None,
    ):
        self.eip_affinity = eip_affinity
        self.nat_gateway_id = nat_gateway_id
        self.snat_entry_id = snat_entry_id
        self.snat_entry_name = snat_entry_name
        self.snat_ip = snat_ip
        self.snat_table_id = snat_table_id
        self.source_cidr = source_cidr
        self.source_vswitch_id = source_vswitch_id
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

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.snat_entry_id is not None:
            result['SnatEntryId'] = self.snat_entry_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        if self.source_vswitch_id is not None:
            result['SourceVSwitchId'] = self.source_vswitch_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SnatEntryId') is not None:
            self.snat_entry_id = m.get('SnatEntryId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        if m.get('SourceVSwitchId') is not None:
            self.source_vswitch_id = m.get('SourceVSwitchId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

