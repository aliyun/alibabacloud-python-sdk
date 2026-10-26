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
        # Specifies the auto-renewal duration for the instance.
        # 
        # - If `PeriodUnit` is set to `Year`, valid values are 1, 3, and 5.
        # 
        # - If `PeriodUnit` is set to `Month`, the valid value is 1.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the renewal duration. Valid values:
        # 
        # - Month
        # 
        # - Year
        # 
        # Default value: Month.
        self.period_unit = period_unit
        # The region ID of the elasticity assurance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The auto-renewal status of the instance. Valid values:
        # 
        # - AutoRenewal: enables auto-renewal.
        # 
        # - Normal: disables auto-renewal.
        # 
        # - NotRenewal: does not renew the instance. If you set this parameter to NotRenewal, the system no longer sends expiration reminders and sends a non-renewal reminder only three days before expiration. You can change the status of an elasticity assurance that is set to NotRenewal to Normal, and then manually renew it or enable auto-renewal.
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
        # The IDs of the elasticity assurances to be modified. This parameter is required. If this parameter is not specified, the MissingParameter.PrivatePoolOptionsId error is returned.
        # 
        # > You can modify up to 50 elasticity assurances at a time.
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

