# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class DiskConstraints(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        count_constraint: main_models.ValueConstraints = None,
        size_constraint: main_models.ValueConstraints = None,
    ):
        # 支持的磁盘类型。
        self.categories = categories
        # 磁盘数量最小值。
        self.count_constraint = count_constraint
        # 磁盘容量限制。
        self.size_constraint = size_constraint

    def validate(self):
        if self.count_constraint:
            self.count_constraint.validate()
        if self.size_constraint:
            self.size_constraint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.count_constraint is not None:
            result['CountConstraint'] = self.count_constraint.to_map()

        if self.size_constraint is not None:
            result['SizeConstraint'] = self.size_constraint.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('CountConstraint') is not None:
            temp_model = main_models.ValueConstraints()
            self.count_constraint = temp_model.from_map(m.get('CountConstraint'))

        if m.get('SizeConstraint') is not None:
            temp_model = main_models.ValueConstraints()
            self.size_constraint = temp_model.from_map(m.get('SizeConstraint'))

        return self

