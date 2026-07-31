# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class PurchaseElasticityAssuranceRequest(DaraModel):
    def __init__(
        self,
        private_pool_options: main_models.PurchaseElasticityAssuranceRequestPrivatePoolOptions = None,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        self.private_pool_options = private_pool_options
        # Ensures the idempotence of the request. The value is generated from your client and must be unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The purchase duration. The unit of the duration is determined by the PeriodUnit parameter. Valid values:
        # 
        # - If PeriodUnit is set to Month: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
        # - If PeriodUnit is set to Year: 1, 2, 3, 4, and 5.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the purchase duration. Valid values:
        # 
        # - Month: month.
        # - Year: year.
        # 
        # Default value: Year.
        self.period_unit = period_unit
        # The region ID of the elastic capacity reservation service. You can call [DescribeRegions](https://help.aliyun.com/document_detail/2679950.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The effective period of the elastic capacity reservation service. By default, the service takes effect when this operation is invoked. Specify the time in the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        self.start_time = start_time

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.PurchaseElasticityAssuranceRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class PurchaseElasticityAssuranceRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the elastic capacity reservation service.
        # 
        # This parameter is required.
        self.id = id
        # The matching mode of the elastic capacity reservation service. Valid values:
        # 
        # - Open: open mode. The system automatically matches the capacity of open private pools when instances are started. If no matching private pool capacity is available, public pool resources are used to start the instances.
        # - Target: targeted mode. Instances are started by using the capacity of the specified private pool. If the specified private pool capacity is unavailable, the instances fail to start.
        # 
        # Default value: Open.
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')

        return self

