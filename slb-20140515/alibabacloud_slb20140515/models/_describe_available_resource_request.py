# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableResourceRequest(DaraModel):
    def __init__(
        self,
        address_ipversion: str = None,
        address_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The type of the IP address.
        # 
        # Valid values: **ipv4 and ipv6**.
        self.address_ipversion = address_ipversion
        # The network type.
        # 
        # Valid values: **vpc, classic-internet, and classic-intranet**.
        # 
        # vpc: an internal Classic Load Balancer (CLB) instance that is deployed in a virtual private cloud (VPC).
        # 
        # classic_internet: a public-facing CLB instance.
        # 
        # classic_intranet: an internal CLB instance that is deployed in a classic network.
        self.address_type = address_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

