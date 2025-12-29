# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePhoneNumberAnalysisPaiRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        input_number: str = None,
        model_config: str = None,
        owner_id: int = None,
        rate: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.input_number = input_number
        # This parameter is required.
        self.model_config = model_config
        self.owner_id = owner_id
        self.rate = rate
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

        if self.model_config is not None:
            result['ModelConfig'] = self.model_config

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.rate is not None:
            result['Rate'] = self.rate

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

        if m.get('ModelConfig') is not None:
            self.model_config = m.get('ModelConfig')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

