# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAnalyticdbByPrimaryDBInstanceResponseBody(DaraModel):
    def __init__(
        self,
        analytic_dbcount: int = None,
        request_id: str = None,
    ):
        # The number of associated analytic instances.
        self.analytic_dbcount = analytic_dbcount
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analytic_dbcount is not None:
            result['AnalyticDBCount'] = self.analytic_dbcount

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyticDBCount') is not None:
            self.analytic_dbcount = m.get('AnalyticDBCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

