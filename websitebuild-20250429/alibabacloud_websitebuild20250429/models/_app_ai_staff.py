# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppAiStaff(DaraModel):
    def __init__(
        self,
        staff_id: str = None,
        staff_name: str = None,
        staff_type: str = None,
        status: str = None,
    ):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_type = staff_type
        # 可能的值：unknown, init, testing, online
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.staff_id is not None:
            result['StaffId'] = self.staff_id

        if self.staff_name is not None:
            result['StaffName'] = self.staff_name

        if self.staff_type is not None:
            result['StaffType'] = self.staff_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StaffId') is not None:
            self.staff_id = m.get('StaffId')

        if m.get('StaffName') is not None:
            self.staff_name = m.get('StaffName')

        if m.get('StaffType') is not None:
            self.staff_type = m.get('StaffType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

