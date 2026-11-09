# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeRuleHitsTopTuleTypeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_hits_top_tule_type: List[main_models.DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The top 10 protection types with the most rule hits.
        self.rule_hits_top_tule_type = rule_hits_top_tule_type

    def validate(self):
        if self.rule_hits_top_tule_type:
            for v1 in self.rule_hits_top_tule_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RuleHitsTopTuleType'] = []
        if self.rule_hits_top_tule_type is not None:
            for k1 in self.rule_hits_top_tule_type:
                result['RuleHitsTopTuleType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule_hits_top_tule_type = []
        if m.get('RuleHitsTopTuleType') is not None:
            for k1 in m.get('RuleHitsTopTuleType'):
                temp_model = main_models.DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType()
                self.rule_hits_top_tule_type.append(temp_model.from_map(k1))

        return self

class DescribeRuleHitsTopTuleTypeResponseBodyRuleHitsTopTuleType(DaraModel):
    def __init__(
        self,
        count: int = None,
        rule_type: str = None,
    ):
        # The number of requests that hit the rule.
        self.count = count
        # The type of the rule hit by the protected object. By default, this parameter is not returned, which indicates that all rules are displayed. Valid values:
        # 
        # - **waf**: basic protection rule.
        # 
        # - **blacklist**: IP blacklist.
        # 
        # - **custom**: custom rule.
        # 
        # - **antiscan**: scan protection rule.
        # 
        # - **cc_system**: HTTP flood protection rule.
        # 
        # - **region_block**: area blocking.
        # 
        # - **scene**: bot management.
        # 
        # - **dlp**: data leak prevention.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

