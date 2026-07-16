# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TaskAssginConfig(DaraModel):
    def __init__(
        self,
        assign_count: int = None,
        assign_field: str = None,
        assign_sub_task_count: str = None,
        assign_type: str = None,
    ):
        # Allocation quantity.
        self.assign_count = assign_count
        # Assign by field.
        self.assign_field = assign_field
        # If average allocation is selected, specify the number of job packages.
        self.assign_sub_task_count = assign_sub_task_count
        # The allocation rule for job packages. Valid values:
        # - FIXED_SIZE: Assign by fixed size.
        # - AVG_SIZE: Assign by average quantity.
        # - FIELD_BASE: Assign by imported field.
        self.assign_type = assign_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assign_count is not None:
            result['AssignCount'] = self.assign_count

        if self.assign_field is not None:
            result['AssignField'] = self.assign_field

        if self.assign_sub_task_count is not None:
            result['AssignSubTaskCount'] = self.assign_sub_task_count

        if self.assign_type is not None:
            result['AssignType'] = self.assign_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignCount') is not None:
            self.assign_count = m.get('AssignCount')

        if m.get('AssignField') is not None:
            self.assign_field = m.get('AssignField')

        if m.get('AssignSubTaskCount') is not None:
            self.assign_sub_task_count = m.get('AssignSubTaskCount')

        if m.get('AssignType') is not None:
            self.assign_type = m.get('AssignType')

        return self

