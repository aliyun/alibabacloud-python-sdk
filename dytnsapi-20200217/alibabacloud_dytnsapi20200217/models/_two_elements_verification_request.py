# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TwoElementsVerificationRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        mask: str = None,
        name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The authorization code.
        # 
        # > On the **My Applications** page of the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), obtain the authorization ID, which is the authorization code.
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The phone number to be verified.
        # 
        # - If Mask is set to NORMAL, this field is in plaintext.
        # - If Mask is set to MD5, encrypt this field with MD5.
        # - If Mask is set to SHA256, encrypt this field with SHA256.
        # 
        # >Notice: Letters in the encrypted string are not case-sensitive.
        # 
        # This parameter is required.
        self.input_number = input_number
        # The encryption method. Valid values:
        # 
        # - **NORMAL**: No encryption.
        # 
        # - **MD5**
        # 
        # - **SHA256**
        # 
        # This parameter is required.
        self.mask = mask
        # The name to be verified.
        # 
        # - If Mask is set to NORMAL, this field is in plaintext.
        # - If Mask is set to MD5, encrypt this field with MD5.
        # - If Mask is set to SHA256, encrypt this field with SHA256.
        # 
        # >Notice: Letters in the encrypted string are not case-sensitive.
        # 
        # This parameter is required.
        self.name = name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.input_number is not None:
            result['InputNumber'] = self.input_number

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

