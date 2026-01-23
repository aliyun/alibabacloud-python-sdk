# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStandardStatisticsShrinkRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        statistics_query_shrink: str = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.statistics_query_shrink = statistics_query_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.statistics_query_shrink is not None:
            result['StatisticsQuery'] = self.statistics_query_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('StatisticsQuery') is not None:
            self.statistics_query_shrink = m.get('StatisticsQuery')

        return self

