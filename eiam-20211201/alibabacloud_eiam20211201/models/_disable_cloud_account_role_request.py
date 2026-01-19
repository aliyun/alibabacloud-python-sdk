# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableCloudAccountRoleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cloud_account_id: str = None,
        cloud_account_role_id: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.cloud_account_id = cloud_account_id
        # 云账号角色ID
        # 
        # This parameter is required.
        self.cloud_account_role_id = cloud_account_role_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_account_role_id is not None:
            result['CloudAccountRoleId'] = self.cloud_account_role_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudAccountRoleId') is not None:
            self.cloud_account_role_id = m.get('CloudAccountRoleId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

