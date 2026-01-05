# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetProjectRoleResponseBody(DaraModel):
    def __init__(
        self,
        project_role: main_models.GetProjectRoleResponseBodyProjectRole = None,
        request_id: str = None,
    ):
        # The role in the DataWorks workspace.
        self.project_role = project_role
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.project_role:
            self.project_role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_role is not None:
            result['ProjectRole'] = self.project_role.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectRole') is not None:
            temp_model = main_models.GetProjectRoleResponseBodyProjectRole()
            self.project_role = temp_model.from_map(m.get('ProjectRole'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProjectRoleResponseBodyProjectRole(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # The code of the role in the DataWorks workspace.
        self.code = code
        # The name of the role in the DataWorks workspace.
        self.name = name
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The type of the role in the DataWorks workspace. Valid values:
        # 
        # *   UserCustom: user-defined role
        # *   System: system role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

