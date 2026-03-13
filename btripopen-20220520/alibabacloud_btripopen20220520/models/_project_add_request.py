# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProjectAddRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        project_name: str = None,
        third_part_cost_center_id: str = None,
        third_part_id: str = None,
        third_part_invoice_id: str = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.project_name = project_name
        self.third_part_cost_center_id = third_part_cost_center_id
        # This parameter is required.
        self.third_part_id = third_part_id
        self.third_part_invoice_id = third_part_invoice_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.project_name is not None:
            result['project_name'] = self.project_name

        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id

        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')

        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')

        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        return self

