# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class InitializeServiceLinkRoleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InitializeServiceLinkRoleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.InitializeServiceLinkRoleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InitializeServiceLinkRoleResponseBodyData(DaraModel):
    def __init__(
        self,
        required_permission: str = None,
        role_name: str = None,
        service_name: str = None,
    ):
        self.required_permission = required_permission
        self.role_name = role_name
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.required_permission is not None:
            result['RequiredPermission'] = self.required_permission

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequiredPermission') is not None:
            self.required_permission = m.get('RequiredPermission')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

