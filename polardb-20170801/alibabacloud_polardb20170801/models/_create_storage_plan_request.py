# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStoragePlanRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: str = None,
        promotion_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_class: str = None,
        storage_type: str = None,
        used_time: str = None,
    ):
        self.auto_use_coupon = auto_use_coupon
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value. Make sure that the value is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unit of the subscription duration for the storage plan. Valid values:
        # 
        # *   **Month**
        # *   **Year**
        # 
        # This parameter is required.
        self.period = period
        self.promotion_code = promotion_code
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The capacity of the storage plan. Unit: GB. Valid values: 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000, 15000, 20000, 25000, 30000, 50000, 100000, and 200000
        # 
        # This parameter is required.
        self.storage_class = storage_class
        # The type of the storage plan. Valid values:
        # 
        # *   **Mainland**: The storage plan is used inside the Chinese mainland.
        # *   **Overseas**: The storage plan is used outside the Chinese mainland.
        # 
        # This parameter is required.
        self.storage_type = storage_type
        # The subscription duration of the storage plan.
        # 
        # *   If **Period** is set to **Month**, the value ranges from 1 to 9.
        # *   If **Period** is set to **Year**, the value can be 1, 2, 3, or 5.
        # 
        # This parameter is required.
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        return self

