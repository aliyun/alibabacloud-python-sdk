# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDepartmentRequest(DaraModel):
    def __init__(
        self,
        out_dept_id: str = None,
    ):
        # This parameter is required.
        self.out_dept_id = out_dept_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_dept_id is not None:
            result['out_dept_id'] = self.out_dept_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('out_dept_id') is not None:
            self.out_dept_id = m.get('out_dept_id')

        return self

