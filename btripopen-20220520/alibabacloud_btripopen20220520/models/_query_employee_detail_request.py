# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryEmployeeDetailRequest(DaraModel):
    def __init__(
        self,
        out_employee_id: str = None,
    ):
        # This parameter is required.
        self.out_employee_id = out_employee_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_employee_id is not None:
            result['out_employee_id'] = self.out_employee_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('out_employee_id') is not None:
            self.out_employee_id = m.get('out_employee_id')

        return self

