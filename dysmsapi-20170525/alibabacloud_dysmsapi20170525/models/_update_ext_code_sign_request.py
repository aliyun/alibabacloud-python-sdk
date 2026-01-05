# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateExtCodeSignRequest(DaraModel):
    def __init__(
        self,
        exist_ext_code: str = None,
        new_ext_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
    ):
        # 要修改的扩展码A3
        # 
        # This parameter is required.
        self.exist_ext_code = exist_ext_code
        # 修改后的扩展码A3
        # 
        # This parameter is required.
        self.new_ext_code = new_ext_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        # 
        # This parameter is required.
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exist_ext_code is not None:
            result['ExistExtCode'] = self.exist_ext_code

        if self.new_ext_code is not None:
            result['NewExtCode'] = self.new_ext_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistExtCode') is not None:
            self.exist_ext_code = m.get('ExistExtCode')

        if m.get('NewExtCode') is not None:
            self.new_ext_code = m.get('NewExtCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        return self

