# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryWorkspaceRoleConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryWorkspaceRoleConfigResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the query result of the interface.
        self.result = result
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryWorkspaceRoleConfigResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryWorkspaceRoleConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_config_list: List[main_models.QueryWorkspaceRoleConfigResponseBodyResultAuthConfigList] = None,
        is_system_role: bool = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # List of role permission configurations.
        self.auth_config_list = auth_config_list
        # Whether it is a predefined role. Value range:
        # 
        # - true: Yes
        # - false: No
        self.is_system_role = is_system_role
        # Workspace role ID, including predefined roles and custom roles:
        # 
        # - 25: Workspace Administrator (predefined role)
        # - 26: Developer (predefined role)
        # - 27: Analyst (predefined role)
        # - 30: Viewer (predefined role)
        # - Custom role: The corresponding role ID for the custom role
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
                temp_model = main_models.QueryWorkspaceRoleConfigResponseBodyResultAuthConfigList()
                self.auth_config_list.append(temp_model.from_map(k1))

        if m.get('IsSystemRole') is not None:
            self.is_system_role = m.get('IsSystemRole')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class QueryWorkspaceRoleConfigResponseBodyResultAuthConfigList(DaraModel):
    def __init__(
        self,
        action_auth_keys: List[str] = None,
        auth_key: str = None,
    ):
        # Permission scope.
        self.action_auth_keys = action_auth_keys
        # Permission type:
        # - portal_create: Data Portal
        # - dashboard_create: Dashboard
        # - report_create: Spreadsheet
        # - screen_create: Data Screen
        # - analysis: Ad-hoc Analysis
        # - offline_download: Self-service Data Retrieval
        # - data_form: Data Entry
        # - quick_etl: Data Preparation
        # - cube: Dataset
        # - datasource: Data Source
        self.auth_key = auth_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_auth_keys is not None:
            result['ActionAuthKeys'] = self.action_auth_keys

        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionAuthKeys') is not None:
            self.action_auth_keys = m.get('ActionAuthKeys')

        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        return self

