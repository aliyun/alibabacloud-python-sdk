# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunEvaluationRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        metric_ids: List[str] = None,
        region_id: str = None,
        scope: str = None,
    ):
        # The Alibaba Cloud account ID of the member. This parameter takes effect only when a multi-account governance maturity check is performed.
        self.account_id = account_id
        # The IDs of the check items to be checked.
        self.metric_ids = metric_ids
        # The region ID.
        self.region_id = region_id
        # The check range of the governance maturity check. Valid values:
        # 
        # *   Account (default): A single-account governance maturity check is performed to check only the Alibaba Cloud account that you use to access Cloud Governance Center.
        # *   ResourceDirectory: A multi-account governance maturity check is performed to check all members within a resource directory. Before you perform a multi-account governance maturity check, you must enable the multi-account governance maturity check feature.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.metric_ids is not None:
            result['MetricIds'] = self.metric_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('MetricIds') is not None:
            self.metric_ids = m.get('MetricIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

