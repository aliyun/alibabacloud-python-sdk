# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UAIDVerificationRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        ip: str = None,
        out_id: str = None,
        owner_id: int = None,
        province: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        token: str = None,
        user_grant_id: str = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.carrier = carrier
        self.ip = ip
        self.out_id = out_id
        self.owner_id = owner_id
        self.province = province
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.token = token
        self.user_grant_id = user_grant_id

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

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.province is not None:
            result['Province'] = self.province

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.token is not None:
            result['Token'] = self.token

        if self.user_grant_id is not None:
            result['UserGrantId'] = self.user_grant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserGrantId') is not None:
            self.user_grant_id = m.get('UserGrantId')

        return self

