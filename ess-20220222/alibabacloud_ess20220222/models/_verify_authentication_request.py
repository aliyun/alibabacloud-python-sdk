# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyAuthenticationRequest(DaraModel):
    def __init__(
        self,
        only_check: bool = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        uid: int = None,
    ):
        # Specifies whether to check only the authorization status. Valid values:
        # 
        # *   true: checks only the authorization status. The service-linked role is not created.
        # *   false (default): checks the authorization status and resource usage.
        self.only_check = only_check
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of your Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.only_check is not None:
            result['OnlyCheck'] = self.only_check

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlyCheck') is not None:
            self.only_check = m.get('OnlyCheck')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

