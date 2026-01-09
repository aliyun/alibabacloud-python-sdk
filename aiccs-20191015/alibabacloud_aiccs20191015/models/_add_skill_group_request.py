# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSkillGroupRequest(DaraModel):
    def __init__(
        self,
        outer_department_id: str = None,
        outer_department_type: str = None,
        outer_group_id: str = None,
        outer_group_name: str = None,
        outer_group_type: str = None,
    ):
        self.outer_department_id = outer_department_id
        self.outer_department_type = outer_department_type
        # This parameter is required.
        self.outer_group_id = outer_group_id
        # This parameter is required.
        self.outer_group_name = outer_group_name
        # This parameter is required.
        self.outer_group_type = outer_group_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id

        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type

        if self.outer_group_id is not None:
            result['OuterGroupId'] = self.outer_group_id

        if self.outer_group_name is not None:
            result['OuterGroupName'] = self.outer_group_name

        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')

        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')

        if m.get('OuterGroupId') is not None:
            self.outer_group_id = m.get('OuterGroupId')

        if m.get('OuterGroupName') is not None:
            self.outer_group_name = m.get('OuterGroupName')

        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')

        return self

