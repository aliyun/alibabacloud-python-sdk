# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPrivateDnsEndpointRequest(DaraModel):
    def __init__(
        self,
        access_instance_id: str = None,
        access_instance_name: str = None,
        primary_dns: str = None,
        private_dns_type: str = None,
        region_no: str = None,
        standby_dns: str = None,
    ):
        # This parameter is required.
        self.access_instance_id = access_instance_id
        # This parameter is required.
        self.access_instance_name = access_instance_name
        self.primary_dns = primary_dns
        # This parameter is required.
        self.private_dns_type = private_dns_type
        # This parameter is required.
        self.region_no = region_no
        self.standby_dns = standby_dns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_id is not None:
            result['AccessInstanceId'] = self.access_instance_id

        if self.access_instance_name is not None:
            result['AccessInstanceName'] = self.access_instance_name

        if self.primary_dns is not None:
            result['PrimaryDns'] = self.primary_dns

        if self.private_dns_type is not None:
            result['PrivateDnsType'] = self.private_dns_type

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.standby_dns is not None:
            result['StandbyDns'] = self.standby_dns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceId') is not None:
            self.access_instance_id = m.get('AccessInstanceId')

        if m.get('AccessInstanceName') is not None:
            self.access_instance_name = m.get('AccessInstanceName')

        if m.get('PrimaryDns') is not None:
            self.primary_dns = m.get('PrimaryDns')

        if m.get('PrivateDnsType') is not None:
            self.private_dns_type = m.get('PrivateDnsType')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('StandbyDns') is not None:
            self.standby_dns = m.get('StandbyDns')

        return self

