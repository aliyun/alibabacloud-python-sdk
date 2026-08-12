# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrometheusSimpleExpression(DaraModel):
    def __init__(
        self,
        operator: str = None,
        query_name: str = None,
        threshold: float = None,
    ):
        # The comparison operator. Valid values:
        # - GT: greater than
        # - GE: greater than or equal to
        # - LT: less than
        # - LE: less than or equal to
        # - EQ: equal to
        # - NE: not equal to
        self.operator = operator
        # The referenced query name, corresponding to QueryConfigUnified.queries[].name.
        self.query_name = query_name
        # The comparison threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['operator'] = self.operator

        if self.query_name is not None:
            result['queryName'] = self.query_name

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

