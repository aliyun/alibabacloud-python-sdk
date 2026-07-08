# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePhoneNumberOnlineTimeRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The authorization code.
        # > Log on to the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), go to the **My Applications** page, and obtain the authorization ID, which is the authorization code.
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The external carrier. Valid values:
        # 
        # - **MOBILE**: China Mobile.
        # - **UNICOM**: China Unicom.
        # - **TELECOM**: China Telecom.
        # 
        # >Notice: This parameter is optional. Alibaba Cloud automatically determines the carrier type based on the phone number. The value of this field has no impact on the query result.
        self.carrier = carrier
        # The phone number to be queried.
        # 
        # - If Mask is set to NORMAL, this field is an 11-digit phone number.
        # - If Mask is set to MD5, this field is a 32-character encrypted string.
        # - If Mask is set to SHA256, this field is a 64-character encrypted string.
        # 
        # >Notice: Letters in the encrypted string are case-insensitive.
        # 
        # This parameter is required.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # - **NORMAL**: no encryption
        # - **MD5**
        # - **SHA256**
        # 
        # This parameter is required.
        self.mask = mask
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

        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.input_number is not None:
            result['InputNumber'] = self.input_number

        if self.mask is not None:
            result['Mask'] = self.mask

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

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

