# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnBindXBRequest(DaraModel):
    def __init__(
        self,
        auth_id: str = None,
        caller_parent_id: int = None,
        customer_pool_key: str = None,
        owner_id: int = None,
        req_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tel_x: str = None,
    ):
        # The unique ID of the XB binding relationship.
        # 
        # This parameter is required.
        self.auth_id = auth_id
        # The customer UID. This parameter is automatically obtained by the system and does not need to be specified.
        self.caller_parent_id = caller_parent_id
        # The number pool key.
        # 
        # This parameter is required.
        self.customer_pool_key = customer_pool_key
        self.owner_id = owner_id
        # The request deduplication ID. The maximum length is 20 characters. Ensure the atomicity of the request ID.
        # 
        # This parameter is required.
        self.req_id = req_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The number X.
        # 
        # This parameter is required.
        self.tel_x = tel_x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id

        if self.customer_pool_key is not None:
            result['CustomerPoolKey'] = self.customer_pool_key

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tel_x is not None:
            result['TelX'] = self.tel_x

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')

        if m.get('CustomerPoolKey') is not None:
            self.customer_pool_key = m.get('CustomerPoolKey')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        return self

