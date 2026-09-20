# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetBaselineStatusRequest(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        bizdate: str = None,
        in_group_id: int = None,
    ):
        # The ID of the baseline.
        # 
        # This parameter is required.
        self.baseline_id = baseline_id
        # The business date in UTC format (yyyy-MM-dd\\"T\\"HH:mm:ssZ).
        # 
        # This parameter is required.
        self.bizdate = bizdate
        # The cycle number of the baseline instance. The value is 1 for daily baselines. The value ranges from [1,24\\] for hourly baselines.
        # 
        # This parameter is required.
        self.in_group_id = in_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.in_group_id is not None:
            result['InGroupId'] = self.in_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('InGroupId') is not None:
            self.in_group_id = m.get('InGroupId')

        return self

