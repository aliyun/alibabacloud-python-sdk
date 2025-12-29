# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUAIDApplyTokenSignRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        client_type: str = None,
        format: str = None,
        out_id: str = None,
        owner_id: int = None,
        param_key: str = None,
        param_str: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        time: str = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.carrier = carrier
        # This parameter is required.
        self.client_type = client_type
        self.format = format
        # This parameter is required.
        self.out_id = out_id
        self.owner_id = owner_id
        self.param_key = param_key
        self.param_str = param_str
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.time = time

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

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.format is not None:
            result['Format'] = self.format

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param_key is not None:
            result['ParamKey'] = self.param_key

        if self.param_str is not None:
            result['ParamStr'] = self.param_str

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParamKey') is not None:
            self.param_key = m.get('ParamKey')

        if m.get('ParamStr') is not None:
            self.param_str = m.get('ParamStr')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

