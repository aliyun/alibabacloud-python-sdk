# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListProjectRolesResponseBody(DaraModel):
    def __init__(
        self,
        project_role_list: List[main_models.ListProjectRolesResponseBodyProjectRoleList] = None,
        request_id: str = None,
    ):
        # The roles in the DataWorks workspace.
        self.project_role_list = project_role_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.project_role_list:
            for v1 in self.project_role_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProjectRoleList'] = []
        if self.project_role_list is not None:
            for k1 in self.project_role_list:
                result['ProjectRoleList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.project_role_list = []
        if m.get('ProjectRoleList') is not None:
            for k1 in m.get('ProjectRoleList'):
                temp_model = main_models.ListProjectRolesResponseBodyProjectRoleList()
                self.project_role_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectRolesResponseBodyProjectRoleList(DaraModel):
    def __init__(
        self,
        project_role_code: str = None,
        project_role_id: int = None,
        project_role_name: str = None,
        project_role_type: str = None,
    ):
        # The code of the role in the DataWorks workspace.
        self.project_role_code = project_role_code
        # The ID of the role in the DataWorks workspace.
        self.project_role_id = project_role_id
        # The name of the role in the DataWorks workspace.
        self.project_role_name = project_role_name
        # The type of the role in the DataWorks workspace.
        self.project_role_type = project_role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_role_code is not None:
            result['ProjectRoleCode'] = self.project_role_code

        if self.project_role_id is not None:
            result['ProjectRoleId'] = self.project_role_id

        if self.project_role_name is not None:
            result['ProjectRoleName'] = self.project_role_name

        if self.project_role_type is not None:
            result['ProjectRoleType'] = self.project_role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectRoleCode') is not None:
            self.project_role_code = m.get('ProjectRoleCode')

        if m.get('ProjectRoleId') is not None:
            self.project_role_id = m.get('ProjectRoleId')

        if m.get('ProjectRoleName') is not None:
            self.project_role_name = m.get('ProjectRoleName')

        if m.get('ProjectRoleType') is not None:
            self.project_role_type = m.get('ProjectRoleType')

        return self

