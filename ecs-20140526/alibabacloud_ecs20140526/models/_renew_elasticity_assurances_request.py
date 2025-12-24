# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RenewElasticityAssurancesRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.RenewElasticityAssurancesRequestPrivatePoolOptions = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.private_pool_options = private_pool_options
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the elasticity assurance. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Unit: month. Valid values: 1, 2, 3, 6, 12, 24, and 36.
        # 
        # *   If you set `PeriodUnit` to Month, the default value is 1.
        # *   If you set `PeriodUnit` to Year, the default value is 12.
        # 
        # >  This parameter is required if you set `AutoRenew` to `true`.
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests.
        # 
        # The `token` can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The renewal duration. The unit of the renewal duration is determined by the `PeriodUnit` value. Valid values:
        # 
        # *   Valid values if you set `PeriodUnit` to `Month`: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # *   Valid values if you set `PeriodUnit` to `Year`: 1, 2, and 3.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the renewal duration. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # Default value: Year.
        self.period_unit = period_unit
        # The region ID of the elasticity assurance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/2680071.html) operation to query the most recent region list.
        self.region_id = region_id
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

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.RenewElasticityAssurancesRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class RenewElasticityAssurancesRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: List[str] = None,
    ):
        # The IDs of elasticity assurances.
        # 
        # **Limits**: You can renew up to 20 elasticity assurances at a time.
        # 
        # You can call the [DescribeElasticityAssurances](https://help.aliyun.com/document_detail/2679748.html) operation to query the elasticity assurances that you purchased.
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

