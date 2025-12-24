# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyElasticityAssuranceAutoRenewAttributeRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.ModifyElasticityAssuranceAutoRenewAttributeRequestPrivatePoolOptions = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        renewal_status: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.private_pool_options = private_pool_options
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The auto-renewal period for the elasticity assurance.
        # 
        # *   Valid values when `PeriodUnit` is set to `Year`: 1, 3, and 5.
        # *   Valid values when `PeriodUnit` is set to `Month`: 1.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the renewal duration. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # Default value: Month.
        self.period_unit = period_unit
        # The ID of the region to which the elasticity assurance belongs. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The auto-renewal status of the elasticity assurance. Valid values:
        # 
        # *   AutoRenewal: Auto-renewal is enabled for the elasticity assurance.
        # *   Normal: Auto-renewal is disabled for the elasticity assurance.
        # *   NotRenewal: The elasticity assurance is not renewed. The system no longer sends an expiration notification but sends only a renewal notification three days before the elasticity assurance expires. You can change the value of this parameter from NotRenewal to `Normal` for an elasticity assurance, and then manually renew the elasticity assurance. Alternatively, you can set the RenewalStatus parameter to AutoRenewal.
        self.renewal_status = renewal_status
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.private_pool_options:
            self.private_pool_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.ModifyElasticityAssuranceAutoRenewAttributeRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyElasticityAssuranceAutoRenewAttributeRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: List[str] = None,
    ):
        # The IDs of elasticity assurances.
        # 
        # >  You can renew up to 50 elasticity assurances at a time.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

