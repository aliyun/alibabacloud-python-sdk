# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidPhoneCodeRequest(DaraModel):
    def __init__(
        self,
        certify_code: str = None,
        owner_id: int = None,
        phone_no: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 验证码
        # 
        # This parameter is required.
        self.certify_code = certify_code
        self.owner_id = owner_id
        # 手机号
        # 
        # This parameter is required.
        self.phone_no = phone_no
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_code is not None:
            result['CertifyCode'] = self.certify_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyCode') is not None:
            self.certify_code = m.get('CertifyCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

