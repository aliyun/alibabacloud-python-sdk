# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyConfigRulesRequest(DaraModel):
    def __init__(
        self,
        des_aggregator_ids: str = None,
        src_aggregator_id: str = None,
        src_config_rule_ids: str = None,
    ):
        # The IDs of the destination account groups into which the rules are replicated. Separate multiple account group IDs with commas (,).
        # 
        # > If you leave this parameter empty, the compliance packages are replicated into the same account group.
        self.des_aggregator_ids = des_aggregator_ids
        # The ID of the account group to which the rules belong.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        self.src_aggregator_id = src_aggregator_id
        # The rule IDs. Separate multiple rule IDs with commas (,).
        # 
        # This parameter is required.
        self.src_config_rule_ids = src_config_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.des_aggregator_ids is not None:
            result['DesAggregatorIds'] = self.des_aggregator_ids

        if self.src_aggregator_id is not None:
            result['SrcAggregatorId'] = self.src_aggregator_id

        if self.src_config_rule_ids is not None:
            result['SrcConfigRuleIds'] = self.src_config_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesAggregatorIds') is not None:
            self.des_aggregator_ids = m.get('DesAggregatorIds')

        if m.get('SrcAggregatorId') is not None:
            self.src_aggregator_id = m.get('SrcAggregatorId')

        if m.get('SrcConfigRuleIds') is not None:
            self.src_config_rule_ids = m.get('SrcConfigRuleIds')

        return self

