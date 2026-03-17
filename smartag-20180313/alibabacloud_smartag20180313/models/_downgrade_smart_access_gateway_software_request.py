# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DowngradeSmartAccessGatewaySoftwareRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        data_plan: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agid: str = None,
        user_count: int = None,
    ):
        # Specify whether the bill belongs to a subscription instance that has auto renewal enabled. Valid values:
        # 
        # *   **false** (default): no
        # *   **true**: yes
        # 
        # This parameter is required.
        self.auto_pay = auto_pay
        # The amount of free data transfer allocated to each client account per month, which is 5 GB.
        # 
        # This parameter is required.
        self.data_plan = data_plan
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the SAG app instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the SAG app instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The quota of client accounts that can be connected to an SAG app instance. Typically, you need to create an account for each user that needs to log on to the SAG app.
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

        if self.data_plan is not None:
            result['DataPlan'] = self.data_plan

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

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('DataPlan') is not None:
            self.data_plan = m.get('DataPlan')

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

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

