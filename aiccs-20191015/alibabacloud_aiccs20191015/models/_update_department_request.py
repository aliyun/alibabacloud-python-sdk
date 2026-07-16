# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDepartmentRequest(DaraModel):
    def __init__(
        self,
        department_id: int = None,
        department_name: str = None,
        instance_id: str = None,
    ):
        # The department ID.
        # 
        # You can invoke the [GetAllDepartment](https://help.aliyun.com/document_detail/2717975.html) API and view the **DepartmentId** field in the response to obtain the department ID.
        # 
        # > This parameter does not support updates.
        # 
        # This parameter is required.
        self.department_id = department_id
        # The department name.
        # 
        # > This parameter supports updates.
        # 
        # This parameter is required.
        self.department_name = department_name
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.department_name is not None:
            result['DepartmentName'] = self.department_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

