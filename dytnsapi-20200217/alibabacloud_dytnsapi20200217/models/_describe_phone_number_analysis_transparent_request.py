# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePhoneNumberAnalysisTransparentRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        ip: str = None,
        number_type: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.input_number = input_number
        self.ip = ip
        # This parameter is required.
        self.number_type = number_type
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

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.number_type is not None:
            result['NumberType'] = self.number_type

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

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NumberType') is not None:
            self.number_type = m.get('NumberType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

