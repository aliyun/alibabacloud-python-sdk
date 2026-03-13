# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BtripBillInfoAdjustRequest(DaraModel):
    def __init__(
        self,
        primary_id: int = None,
        third_part_cost_center_id: str = None,
        third_part_department_id: str = None,
        third_part_invoice_id: str = None,
        third_part_project_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.primary_id = primary_id
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_department_id = third_part_department_id
        self.third_part_invoice_id = third_part_invoice_id
        self.third_part_project_id = third_part_project_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.primary_id is not None:
            result['primary_id'] = self.primary_id

        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id

        if self.third_part_department_id is not None:
            result['third_part_department_id'] = self.third_part_department_id

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.third_part_project_id is not None:
            result['third_part_project_id'] = self.third_part_project_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')

        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')

        if m.get('third_part_department_id') is not None:
            self.third_part_department_id = m.get('third_part_department_id')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('third_part_project_id') is not None:
            self.third_part_project_id = m.get('third_part_project_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

