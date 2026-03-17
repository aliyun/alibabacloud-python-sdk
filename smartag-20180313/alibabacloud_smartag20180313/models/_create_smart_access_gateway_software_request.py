# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmartAccessGatewaySoftwareRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        charge_type: str = None,
        data_plan: int = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_count: int = None,
    ):
        # Specifies whether to automatically complete the payment of the order. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # If you set the parameter to false, go to Billing Management to complete the payment after you call this operation. The instance is created only after you complete the payment.
        # 
        # This parameter is required.
        self.auto_pay = auto_pay
        # The billing method of the SAG app instance. Set the value to **PREPAY**. This value indicates that the SAG app instance is a subscription resource.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The size of the free data plan that is allocated to each client account per month. Unit: GB. Valid value: **5**.
        # 
        # >  This value specifies that a free data plan of 5 GB is allocated to each client account per month.
        # 
        # This parameter is required.
        self.data_plan = data_plan
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the SAG app instance. Unit: months.
        # 
        # Valid values: **1** to **9**, **12**, **24**, and **36**.
        # 
        # This parameter is required.
        self.period = period
        # The ID of the region where you want to create the SAG app instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum number of client accounts that can be created on the SAG app instance.
        # 
        # This parameter is required.
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.data_plan is not None:
            result['DataPlan'] = self.data_plan

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DataPlan') is not None:
            self.data_plan = m.get('DataPlan')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

