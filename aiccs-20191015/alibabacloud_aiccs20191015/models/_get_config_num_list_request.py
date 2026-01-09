# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConfigNumListRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        department_id: int = None,
        instance_id: str = None,
    ):
        self.account_name = account_name
        self.department_id = department_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

