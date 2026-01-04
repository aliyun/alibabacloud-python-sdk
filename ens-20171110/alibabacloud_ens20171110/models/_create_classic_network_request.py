# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClassicNetworkRequest(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        ens_region_id: str = None,
        network_name: str = None,
    ):
        # The CIDR block of the network. You can use one of the following CIDR blocks or their subnets as the CIDR block of the network:
        # 
        # *   10.0.0.0/8 (default)
        # *   172.16.0.0/12
        # *   192.168.0.0/16
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # The description of the network. The name must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https://.
        self.description = description
        # The ID of the edge node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The name of the network. The name must meet the following requirements:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name must start with a letter but cannot start with http:// or https://.
        # *   The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.network_name = network_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.network_name is not None:
            result['NetworkName'] = self.network_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')

        return self

