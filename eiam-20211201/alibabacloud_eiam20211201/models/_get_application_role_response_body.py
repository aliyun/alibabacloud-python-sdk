# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetApplicationRoleResponseBody(DaraModel):
    def __init__(
        self,
        application_role: main_models.GetApplicationRoleResponseBodyApplicationRole = None,
        request_id: str = None,
    ):
        self.application_role = application_role
        self.request_id = request_id

    def validate(self):
        if self.application_role:
            self.application_role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_role is not None:
            result['ApplicationRole'] = self.application_role.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationRole') is not None:
            temp_model = main_models.GetApplicationRoleResponseBodyApplicationRole()
            self.application_role = temp_model.from_map(m.get('ApplicationRole'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationRoleResponseBodyApplicationRole(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_role_id: str = None,
        application_role_name: str = None,
        application_role_value: str = None,
        description: str = None,
        instance_id: str = None,
    ):
        # 应用唯一标识
        self.application_id = application_id
        # 应用角色的唯一标识
        self.application_role_id = application_role_id
        # 应用角色名称
        self.application_role_name = application_role_name
        # 应用角色值
        self.application_role_value = application_role_value
        # 应用角色描述
        self.description = description
        # EIAM 实例唯一标识
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

        if self.application_role_id is not None:
            result['ApplicationRoleId'] = self.application_role_id

        if self.application_role_name is not None:
            result['ApplicationRoleName'] = self.application_role_name

        if self.application_role_value is not None:
            result['ApplicationRoleValue'] = self.application_role_value

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationRoleId') is not None:
            self.application_role_id = m.get('ApplicationRoleId')

        if m.get('ApplicationRoleName') is not None:
            self.application_role_name = m.get('ApplicationRoleName')

        if m.get('ApplicationRoleValue') is not None:
            self.application_role_value = m.get('ApplicationRoleValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

