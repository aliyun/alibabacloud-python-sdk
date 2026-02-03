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
        product: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  The default value is **false**.
        self.auto_renew = auto_renew
        # The ID of the instance. Separate multiple instance IDs with commas (,).
        # 
        # > You can specify up to 30 instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The auto-renewal period. Valid values: **1** to **12**. Unit: months. When the instance is about to expire, the instance is automatically renewed based on the number of months specified by this parameter.
        # 
        # > This parameter is available and required only if the **AutoRenew** parameter is set to **true**.
        self.duration = duration
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The service. Set the value to kvstore.
        self.product = product
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

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

        if self.product is not None:
            result['Product'] = self.product

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

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

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

