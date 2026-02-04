# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCenInterRegionBandwidthLimitRequest(DaraModel):
    def __init__(
        self,
        bandwidth_limit: int = None,
        bandwidth_type: str = None,
        cen_id: str = None,
        local_region_id: str = None,
        opposite_region_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The maximum bandwidth value of the inter-region connection. Unit: Mbit/s.
        # 
        # This parameter is required.
        self.bandwidth_limit = bandwidth_limit
        # The bandwidth allocation method. Valid values:
        # 
        # **BandwidthPackage**: allocates bandwidth from a bandwidth plan.
        self.bandwidth_type = bandwidth_type
        # The ID of the CEN instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The ID of the local region.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query regions where you can attach network instances to a CEN instance.
        # 
        # This parameter is required.
        self.local_region_id = local_region_id
        # The ID of the peer region.
        # 
        # This parameter is required.
        self.opposite_region_id = opposite_region_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_limit is not None:
            result['BandwidthLimit'] = self.bandwidth_limit

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id

        if self.opposite_region_id is not None:
            result['OppositeRegionId'] = self.opposite_region_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthLimit') is not None:
            self.bandwidth_limit = m.get('BandwidthLimit')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')

        if m.get('OppositeRegionId') is not None:
            self.opposite_region_id = m.get('OppositeRegionId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

