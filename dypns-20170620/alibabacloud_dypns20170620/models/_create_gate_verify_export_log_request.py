# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGateVerifyExportLogRequest(DaraModel):
    def __init__(
        self,
        authentication_type: int = None,
        os_type: str = None,
        owner_id: int = None,
        query_month: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_code: str = None,
    ):
        # This parameter is required.
        self.authentication_type = authentication_type
        self.os_type = os_type
        self.owner_id = owner_id
        # This parameter is required.
        self.query_month = query_month
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.scene_code = scene_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_type is not None:
            result['AuthenticationType'] = self.authentication_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.query_month is not None:
            result['QueryMonth'] = self.query_month

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationType') is not None:
            self.authentication_type = m.get('AuthenticationType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QueryMonth') is not None:
            self.query_month = m.get('QueryMonth')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        return self

