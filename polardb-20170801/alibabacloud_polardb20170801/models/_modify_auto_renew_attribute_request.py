# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAutoRenewAttributeRequest(DaraModel):
    def __init__(
        self,
        cloud_provider: str = None,
        dbcluster_ids: str = None,
        duration: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period_unit: str = None,
        region_id: str = None,
        renewal_status: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.cloud_provider = cloud_provider
        # The cluster ID. If you need to specify multiple cluster IDs, separate the cluster IDs with commas (,).
        # 
        # This parameter is required.
        self.dbcluster_ids = dbcluster_ids
        # The automatic renewal period.
        # 
        # *   Valid values when you set the **PeriodUnit** parameter to **Month**: `1, 2, 3, 6, and 12`.
        # *   Valid values when you set the **PeriodUnit** parameter to **Year**: `1, 2, and 3`.
        # 
        # Default value: **1**.
        self.duration = duration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unit of the renewal period. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        # 
        # Default value: **Month**.
        self.period_unit = period_unit
        # The ID of the region. The region ID can be up to 50 characters in length.
        # cn-hangzhou
        #  
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The auto-renewal status of the cluster. Valid values:
        # 
        # *   **AutoRenewal:** The cluster is automatically renewed.
        # *   **Normal**: The cluster is manually renewed.
        # *   **NotRenewal:** The cluster is not renewed after expiration.
        # 
        # Default value: **AutoRenewal**.
        # 
        # >  If you set this parameter to **NotRenewal**, the system sends a notification that indicates the cluster is not renewed three days before the cluster expires. After the cluster expires, the system no longer sends a notification.
        self.renewal_status = renewal_status
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.dbcluster_ids is not None:
            result['DBClusterIds'] = self.dbcluster_ids

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('DBClusterIds') is not None:
            self.dbcluster_ids = m.get('DBClusterIds')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

