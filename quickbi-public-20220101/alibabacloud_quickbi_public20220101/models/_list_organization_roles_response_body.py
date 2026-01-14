# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListOrganizationRolesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListOrganizationRolesResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the list of organization roles.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListOrganizationRolesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListOrganizationRolesResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_config_list: List[main_models.ListOrganizationRolesResponseBodyResultAuthConfigList] = None,
        is_system_role: bool = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # List of role permission configurations.
        self.auth_config_list = auth_config_list
        # Whether it is a predefined role. Possible values:
        # - true: Yes
        # - false: No
        self.is_system_role = is_system_role
        # Role ID.
        self.role_id = role_id
        # Role name.
        self.role_name = role_name

    def validate(self):
        if self.auth_config_list:
            for v1 in self.auth_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthConfigList'] = []
        if self.auth_config_list is not None:
            for k1 in self.auth_config_list:
                result['AuthConfigList'].append(k1.to_map() if k1 else None)

        if self.is_system_role is not None:
            result['IsSystemRole'] = self.is_system_role

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_config_list = []
        if m.get('AuthConfigList') is not None:
            for k1 in m.get('AuthConfigList'):
                temp_model = main_models.ListOrganizationRolesResponseBodyResultAuthConfigList()
                self.auth_config_list.append(temp_model.from_map(k1))

        if m.get('IsSystemRole') is not None:
            self.is_system_role = m.get('IsSystemRole')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class ListOrganizationRolesResponseBodyResultAuthConfigList(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
    ):
        # Permission type:
        # - quick_monitor: Metric monitoring
        # - subscription: Subscription management
        # - offline_download: Self-service data retrieval
        # - resource_package: Resource package management
        # - organization_ask: Organization identification code (AK/SK)
        # - developer_openapi: OpenAPI
        # - data_service: Data service
        # - admin_authorize3rd: Embedded analysis
        # - component_manage: Custom component
        # - template_open: Custom template
        # - custom_driver: Custom driver (supported only in standalone deployment)
        # - open_platform_custom_plugin: Custom plugin (supported only in standalone deployment)
        # - enterprise_safety: Enterprise security
        self.auth_key = auth_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        return self

