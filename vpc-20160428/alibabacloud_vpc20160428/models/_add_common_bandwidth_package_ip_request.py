# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCommonBandwidthPackageIpRequest(DaraModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        ip_instance_id: str = None,
        ip_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.bandwidth_package_id = bandwidth_package_id
        self.client_token = client_token
        self.dry_run = dry_run
        # This parameter is required.
        self.ip_instance_id = ip_instance_id
        self.ip_type = ip_type
        self.owner_account = owner_account
        self.owner_id = owner_id
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
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.ip_instance_id is not None:
            result['IpInstanceId'] = self.ip_instance_id

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

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
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpInstanceId') is not None:
            self.ip_instance_id = m.get('IpInstanceId')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

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

