# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAutoRenewalAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_renewal_period: str = None,
        auto_renewal_period_unit: str = None,
        auto_renewal_status: str = None,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The duration of the auto-renewal. Default value: 1. Valid values:
        # 
        # *   When **AutoRenewalPeriod** is set to **Month**, the value ranges from 1 to 11 (integer).
        # *   When **AutoRenewalPeriod** is set to **Month**, the valid values are 1, 2, 3, and 5 (integer).
        # 
        # >  Longer renewal periods offer better pricing. Renewing for 1 year is more cost-effective than renewing for 10 or 11 months.
        self.auto_renewal_period = auto_renewal_period
        # Auto-renewal duration. Valid values:
        # 
        # *   Year.
        # *   Month.
        self.auto_renewal_period_unit = auto_renewal_period_unit
        # The renewal method. Valid values:
        # 
        # *   **AutoRenewal**: The cluster is automatically renewed.
        # *   **Normal**: The cluster is manually renewed. Before the cluster expires, the system sends you a reminder by SMS message.
        # *   **NotRenewal**: The cluster is not renewed. Reminders are only sent three days before cluster expiration.
        self.auto_renewal_status = auto_renewal_status
        # The ID of cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
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
        if self.auto_renewal_period is not None:
            result['AutoRenewalPeriod'] = self.auto_renewal_period

        if self.auto_renewal_period_unit is not None:
            result['AutoRenewalPeriodUnit'] = self.auto_renewal_period_unit

        if self.auto_renewal_status is not None:
            result['AutoRenewalStatus'] = self.auto_renewal_status

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

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
        if m.get('AutoRenewalPeriod') is not None:
            self.auto_renewal_period = m.get('AutoRenewalPeriod')

        if m.get('AutoRenewalPeriodUnit') is not None:
            self.auto_renewal_period_unit = m.get('AutoRenewalPeriodUnit')

        if m.get('AutoRenewalStatus') is not None:
            self.auto_renewal_status = m.get('AutoRenewalStatus')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

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

