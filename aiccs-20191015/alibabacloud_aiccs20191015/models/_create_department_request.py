# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDepartmentRequest(DaraModel):
    def __init__(
        self,
        department_name: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.department_name = department_name
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_name is not None:
            result['DepartmentName'] = self.department_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

