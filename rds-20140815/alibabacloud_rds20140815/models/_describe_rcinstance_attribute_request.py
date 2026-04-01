# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        max_disks_results: int = None,
        private_ip_address: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.max_disks_results = max_disks_results
        self.private_ip_address = private_ip_address
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.max_disks_results is not None:
            result['MaxDisksResults'] = self.max_disks_results

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaxDisksResults') is not None:
            self.max_disks_results = m.get('MaxDisksResults')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

