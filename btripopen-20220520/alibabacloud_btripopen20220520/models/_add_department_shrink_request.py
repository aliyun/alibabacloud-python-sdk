# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDepartmentShrinkRequest(DaraModel):
    def __init__(
        self,
        dept_name: str = None,
        manager_employee_id_list_shrink: str = None,
        out_dept_id: str = None,
        out_dept_pid: str = None,
    ):
        # This parameter is required.
        self.dept_name = dept_name
        self.manager_employee_id_list_shrink = manager_employee_id_list_shrink
        # This parameter is required.
        self.out_dept_id = out_dept_id
        self.out_dept_pid = out_dept_pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dept_name is not None:
            result['dept_name'] = self.dept_name

        if self.manager_employee_id_list_shrink is not None:
            result['manager_employee_id_list'] = self.manager_employee_id_list_shrink

        if self.out_dept_id is not None:
            result['out_dept_id'] = self.out_dept_id

        if self.out_dept_pid is not None:
            result['out_dept_pid'] = self.out_dept_pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dept_name') is not None:
            self.dept_name = m.get('dept_name')

        if m.get('manager_employee_id_list') is not None:
            self.manager_employee_id_list_shrink = m.get('manager_employee_id_list')

        if m.get('out_dept_id') is not None:
            self.out_dept_id = m.get('out_dept_id')

        if m.get('out_dept_pid') is not None:
            self.out_dept_pid = m.get('out_dept_pid')

        return self

