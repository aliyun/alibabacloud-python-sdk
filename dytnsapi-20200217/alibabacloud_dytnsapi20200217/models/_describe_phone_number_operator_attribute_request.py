# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePhoneNumberOperatorAttributeRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        flow_name: str = None,
        input_number: str = None,
        mask: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        result_count: str = None,
    ):
        # The authorization code.
        # 
        # > On the **My Applications** page of the [Cell Phone Number Service console](https://dytns.console.aliyun.com/analysis/apply), obtain the authorization ID, which is the authorization code.
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # A system parameter. You do not need to specify this parameter.
        self.flow_name = flow_name
        # The phone number that you want to query.
        # 
        # - If Mask is set to NORMAL, this field is an 11-digit phone number.
        # - If Mask is set to MD5, this field is a 32-character encrypted string.
        # - If Mask is set to SHA256, this field is a 64-character encrypted string.
        # - If Mask is set to SM3, this field is a 64-character encrypted string.
        # 
        # >Notice: The letters in the encrypted string are not case-sensitive.</notice>
        # 
        # This parameter is required.
        self.input_number = input_number
        # The encryption method of the phone number. Valid values:
        # 
        # - **NORMAL**: no encryption
        # - **MD5**: MD5 encryption
        # - **SHA256**: SHA256 encryption
        # - **SM3**: SM3 encryption
        # 
        # >Notice: All letters in the string must be uppercase.</notice>
        # 
        # This parameter is required.
        self.mask = mask
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A system parameter. You do not need to specify this parameter.
        self.result_count = result_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

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

        if self.result_count is not None:
            result['ResultCount'] = self.result_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

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

        if m.get('ResultCount') is not None:
            self.result_count = m.get('ResultCount')

        return self

