# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySecretNoDetailRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        # The key of the number pool.
        # 
        # Log on to the Phone Number Protection console and obtain the **Number Pool Key** on the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool) page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The privacy number, which is the X number.
        # 
        # Log on to the Phone Number Protection console and obtain the X number on the [Number Management](https://dyplsnext.console.aliyun.com/number/list) page. Alternatively, view the **SecretNo** parameter in the response when you call a number binding operation such as [BindAxb](https://www.alibabacloud.com/help/en/pnp/developer-reference/api-dyplsapi-2017-05-25-bindaxb).
        # 
        # This parameter is required.
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')

        return self

