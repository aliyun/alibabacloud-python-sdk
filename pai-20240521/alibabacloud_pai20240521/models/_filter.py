# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Filter(DaraModel):
    def __init__(
        self,
        filter_by: str = None,
        filter_condition: str = None,
        filter_operation: str = None,
    ):
        self.filter_by = filter_by
        self.filter_condition = filter_condition
        self.filter_operation = filter_operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_by is not None:
            result['FilterBy'] = self.filter_by

        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition

        if self.filter_operation is not None:
            result['FilterOperation'] = self.filter_operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterBy') is not None:
            self.filter_by = m.get('FilterBy')

        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')

        if m.get('FilterOperation') is not None:
            self.filter_operation = m.get('FilterOperation')

        return self

