# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBucUserEnterpriseRequest(DaraModel):
    def __init__(
        self,
        emp_id: str = None,
    ):
        self.emp_id = emp_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.emp_id is not None:
            result['empId'] = self.emp_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('empId') is not None:
            self.emp_id = m.get('empId')

        return self

