# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryUserRoleInfoInWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryUserRoleInfoInWorkspaceResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Preset space role information of the user.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request succeeded.
        # - false: The request failed.
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
            temp_model = main_models.QueryUserRoleInfoInWorkspaceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryUserRoleInfoInWorkspaceResponseBodyResult(DaraModel):
    def __init__(
        self,
        role_code: str = None,
        role_id: int = None,
        role_name: str = None,
    ):
        # Preset role code.
        self.role_code = role_code
        # Preset role ID. Possible values:
        # - 25: Space Administrator
        # - 26: Space Developer
        # - 27: Space Analyst
        # - 30: Space Viewer
        self.role_id = role_id
        # Preset role name.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_code is not None:
            result['RoleCode'] = self.role_code

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

