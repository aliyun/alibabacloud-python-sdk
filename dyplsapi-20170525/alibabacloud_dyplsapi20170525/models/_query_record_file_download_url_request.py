# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecordFileDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        call_time: str = None,
        owner_id: int = None,
        pool_key: str = None,
        product_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the call record. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view **Call Record ID** on the **Call Record Query** page.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The call initiation time in the call record. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). View **Call Initiated At** on the **Call Record Query** page, or view the call_time field in the Call Detail Record (CDR) receipt.
        self.call_time = call_time
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # >  This parameter is required when **ProductType** is left empty.
        self.pool_key = pool_key
        # The product type. Valid values:
        # 
        # *   **AXB_170**.
        # *   **AXN_170**.
        # *   **AXN_95**.
        # *   **AXN_EXTENSION_REUSE**
        # 
        # > 
        # 
        # *   This parameter is applicable to the original key accounts of Alibaba Cloud. This parameter can be ignored for Alibaba Cloud users.
        # 
        # *   This parameter is required when **PoolKey** is left empty.
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.call_time is not None:
            result['CallTime'] = self.call_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

