# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySubscriptionDetailRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_no_x: str = None,
        pool_key: str = None,
        product_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subs_id: str = None,
    ):
        self.owner_id = owner_id
        # The privacy number in the binding relationship, which is the X number.
        # 
        # Logon to the privacy protection console and go to the [Number Management](https://dyplsnext.console.aliyun.com/number/list) page to obtain the X number. Alternatively, check the **SecretNo** in the response parameters when you invoke number binding API operations such as [BindAxb](https://www.alibabacloud.com/help/en/pnp/developer-reference/api-dyplsapi-2017-05-25-bindaxb).
        # 
        # > When specifying the X number, make sure it is associated with the **SubsId** parameter.
        # 
        # This parameter is required.
        self.phone_no_x = phone_no_x
        # The key of the number pool.
        # 
        # Log on to the privacy protection console and go to the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool?spm=a2c4g.11186623.0.0.7e6449bbtiHP8m) page to obtain the **Number Pool Key**.
        # 
        # > This parameter is required when **ProductType** is left empty.
        self.pool_key = pool_key
        # The product type. Valid values:
        # - **AXB_170**
        # - **AXN_170**
        # - **AXN_95**
        # - **AXN_EXTENSION_REUSE**
        # 
        # > - This parameter is applicable to former Alibaba Dayu users. Alibaba Cloud users can ignore this parameter.
        # > - This parameter is required when **PoolKey** is left empty.
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The binding relationship ID.
        # 
        # Logon to the privacy protection console, go to the [Number Management](https://dyplsnext.console.aliyun.com/number/list) page, filter the numbers, and click **Details** to view the binding relationship ID. Alternatively, check the **SubsId** in the response parameters when you invoke number binding API operations such as [BindAxb](https://www.alibabacloud.com/help/en/pnp/developer-reference/api-dyplsapi-2017-05-25-bindaxb).
        # 
        # > When specifying the binding relationship ID, make sure it is associated with the **PhoneNoX** parameter.
        # 
        # This parameter is required.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.subs_id is not None:
            result['SubsId'] = self.subs_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')

        return self

