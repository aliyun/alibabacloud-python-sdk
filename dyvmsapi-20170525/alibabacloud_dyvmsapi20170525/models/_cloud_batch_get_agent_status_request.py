# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudBatchGetAgentStatusRequest(DaraModel):
    def __init__(
        self,
        cnos: str = None,
        enterprise_id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 座席号列表；座席号之间用`,`分隔，如：cnos=2000,20001 最多支持100个座席
        # 
        # This parameter is required.
        self.cnos = cnos
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
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
        if self.cnos is not None:
            result['Cnos'] = self.cnos

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cnos') is not None:
            self.cnos = m.get('Cnos')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

