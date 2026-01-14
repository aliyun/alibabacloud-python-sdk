# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListDataLevelPermissionWhiteListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListDataLevelPermissionWhiteListResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Whitelist for the specified row-level permission type.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: Request succeeded
        # - false: Request failed
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
            temp_model = main_models.ListDataLevelPermissionWhiteListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataLevelPermissionWhiteListResponseBodyResult(DaraModel):
    def __init__(
        self,
        cube_id: str = None,
        rule_type: str = None,
        users_model: main_models.ListDataLevelPermissionWhiteListResponseBodyResultUsersModel = None,
    ):
        # Dataset ID.
        self.cube_id = cube_id
        # Type of dataset row and column permissions. Possible values:
        # 
        # - ROW_LEVEL: Row-level permission
        # - COLUMN_LEVEL: Column-level permission
        self.rule_type = rule_type
        # Whitelist information.
        self.users_model = users_model

    def validate(self):
        if self.users_model:
            self.users_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cube_id is not None:
            result['CubeId'] = self.cube_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.users_model is not None:
            result['UsersModel'] = self.users_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CubeId') is not None:
            self.cube_id = m.get('CubeId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('UsersModel') is not None:
            temp_model = main_models.ListDataLevelPermissionWhiteListResponseBodyResultUsersModel()
            self.users_model = temp_model.from_map(m.get('UsersModel'))

        return self

class ListDataLevelPermissionWhiteListResponseBodyResultUsersModel(DaraModel):
    def __init__(
        self,
        user_groups: List[str] = None,
        users: List[str] = None,
    ):
        # UserGroups.
        self.user_groups = user_groups
        # Users.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_groups is not None:
            result['UserGroups'] = self.user_groups

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroups') is not None:
            self.user_groups = m.get('UserGroups')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

