# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSnatEntryRequest(DaraModel):
    def __init__(
        self,
        eip_affinity: int = None,
        region_id: str = None,
        snat_entry_name: str = None,
        snat_ip: str = None,
        snat_table_id: str = None,
        source_cidr: str = None,
    ):
        self.eip_affinity = eip_affinity
        # This parameter is required.
        self.region_id = region_id
        self.snat_entry_name = snat_entry_name
        # This parameter is required.
        self.snat_ip = snat_ip
        # This parameter is required.
        self.snat_table_id = snat_table_id
        # This parameter is required.
        self.source_cidr = source_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_affinity is not None:
            result['EipAffinity'] = self.eip_affinity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snat_entry_name is not None:
            result['SnatEntryName'] = self.snat_entry_name

        if self.snat_ip is not None:
            result['SnatIp'] = self.snat_ip

        if self.snat_table_id is not None:
            result['SnatTableId'] = self.snat_table_id

        if self.source_cidr is not None:
            result['SourceCIDR'] = self.source_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAffinity') is not None:
            self.eip_affinity = m.get('EipAffinity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnatEntryName') is not None:
            self.snat_entry_name = m.get('SnatEntryName')

        if m.get('SnatIp') is not None:
            self.snat_ip = m.get('SnatIp')

        if m.get('SnatTableId') is not None:
            self.snat_table_id = m.get('SnatTableId')

        if m.get('SourceCIDR') is not None:
            self.source_cidr = m.get('SourceCIDR')

        return self

