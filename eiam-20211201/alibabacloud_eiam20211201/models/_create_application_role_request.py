# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationRoleRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_role_name: str = None,
        application_role_value: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        # 应用角色名称
        # 
        # This parameter is required.
        self.application_role_name = application_role_name
        # This parameter is required.
        self.application_role_value = application_role_value
        # This parameter is required.
        self.client_token = client_token
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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_role_name is not None:
            result['ApplicationRoleName'] = self.application_role_name

        if self.application_role_value is not None:
            result['ApplicationRoleValue'] = self.application_role_value

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationRoleName') is not None:
            self.application_role_name = m.get('ApplicationRoleName')

        if m.get('ApplicationRoleValue') is not None:
            self.application_role_value = m.get('ApplicationRoleValue')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

