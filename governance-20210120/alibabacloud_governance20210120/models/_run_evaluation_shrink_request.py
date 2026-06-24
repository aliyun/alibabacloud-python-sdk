# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunEvaluationShrinkRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        evaluation_domain: str = None,
        metric_ids_shrink: str = None,
        region_id: str = None,
        scope: str = None,
    ):
        # The ID of the member account. This parameter is applicable only to the multi-account check pattern.
        self.account_id = account_id
        self.evaluation_domain = evaluation_domain
        # The list of check item IDs to check.
        self.metric_ids_shrink = metric_ids_shrink
        # The region ID.
        self.region_id = region_id
        # The scope of the governance maturity check. Valid values:
        # 
        # - Account (default): runs a single-account governance maturity check that checks only the current account.
        # - ResourceDirectory: runs a multi-account governance maturity check that checks all member accounts in the resource directory. Before you perform this operation, upgrade to the multi-account governance maturity check.
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

        if self.evaluation_domain is not None:
            result['EvaluationDomain'] = self.evaluation_domain

        if self.metric_ids_shrink is not None:
            result['MetricIds'] = self.metric_ids_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('EvaluationDomain') is not None:
            self.evaluation_domain = m.get('EvaluationDomain')

        if m.get('MetricIds') is not None:
            self.metric_ids_shrink = m.get('MetricIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

