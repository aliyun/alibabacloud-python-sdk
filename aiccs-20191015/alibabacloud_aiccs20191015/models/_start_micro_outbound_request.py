# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartMicroOutboundRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_type: str = None,
        app_name: str = None,
        called_number: str = None,
        calling_number: str = None,
        command_code: str = None,
        ext_info: str = None,
        owner_id: int = None,
        prod_code: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.account_id = account_id
        self.account_type = account_type
        self.app_name = app_name
        self.called_number = called_number
        self.calling_number = calling_number
        self.command_code = command_code
        self.ext_info = ext_info
        self.owner_id = owner_id
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.command_code is not None:
            result['CommandCode'] = self.command_code

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('CommandCode') is not None:
            self.command_code = m.get('CommandCode')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

