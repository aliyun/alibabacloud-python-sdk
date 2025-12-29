# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceAutoRenewalAttributeRequest(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        dbinstance_id: str = None,
        duration: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If this parameter is set to **true**, you must set the **Duration** parameter.
        # 
        # This parameter is required.
        self.auto_renew = auto_renew
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The auto-renewal period. Valid values: **1** to **12**. Unit: month.
        # 
        # >  This parameter is valid only when **AutoRenew** is set to **true**.
        self.duration = duration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to query the region ID of the instance.
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
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.duration is not None:
            result['Duration'] = self.duration

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
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

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

