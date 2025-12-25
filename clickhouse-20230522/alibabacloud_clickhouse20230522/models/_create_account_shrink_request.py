# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountShrinkRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        account_type: str = None,
        dbinstance_id: str = None,
        description: str = None,
        dml_auth_setting_shrink: str = None,
        password: str = None,
        product: str = None,
        region_id: str = None,
    ):
        # The name of the account.
        # 
        # This parameter is required.
        self.account = account
        # The type of the database account. Valid values:
        # 
        # *   **NormalAccount**: standard account
        # *   **SuperAccount**: privileged account
        # 
        # This parameter is required.
        self.account_type = account_type
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The description of the account.
        self.description = description
        # The information about permissions.
        self.dml_auth_setting_shrink = dml_auth_setting_shrink
        # The password of the database account. The password must meet the following requirements:
        # 
        # - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - The following special characters are supported: ! @ # $ % ^ & * ( ) _ + - =
        # - The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.password = password
        # The code of the cloud service.
        self.product = product
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dml_auth_setting_shrink is not None:
            result['DmlAuthSetting'] = self.dml_auth_setting_shrink

        if self.password is not None:
            result['Password'] = self.password

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DmlAuthSetting') is not None:
            self.dml_auth_setting_shrink = m.get('DmlAuthSetting')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

