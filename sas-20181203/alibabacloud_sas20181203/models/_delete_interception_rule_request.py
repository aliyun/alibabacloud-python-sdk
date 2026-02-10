# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteInterceptionRuleRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        rule_ids: List[int] = None,
    ):
        # The ID of the cluster that you want to query.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The IDs of the rules that you want to delete.
        self.rule_ids = rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        return self

