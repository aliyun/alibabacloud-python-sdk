# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushBindRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        delivery_token: str = None,
        os_type: int = None,
        phone_number: str = None,
        tenant_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.delivery_token = delivery_token
        # This parameter is required.
        self.os_type = os_type
        self.phone_number = phone_number
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.delivery_token is not None:
            result['DeliveryToken'] = self.delivery_token

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeliveryToken') is not None:
            self.delivery_token = m.get('DeliveryToken')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

