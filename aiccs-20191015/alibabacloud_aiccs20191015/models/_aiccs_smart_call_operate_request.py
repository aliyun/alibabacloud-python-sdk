# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiccsSmartCallOperateRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        command: str = None,
        owner_id: int = None,
        param: str = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.call_id = call_id
        self.command = command
        self.owner_id = owner_id
        self.param = param
        self.prod_code = prod_code
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

        if self.command is not None:
            result['Command'] = self.command

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param is not None:
            result['Param'] = self.param

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

