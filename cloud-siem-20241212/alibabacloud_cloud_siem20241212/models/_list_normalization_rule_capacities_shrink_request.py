# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNormalizationRuleCapacitiesShrinkRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_rule_id: str = None,
        normalization_rule_ids_shrink: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token to start the next query. Leave this parameter empty for the first query. If the response is truncated, use the \\`NextToken\\` value from the previous response.
        self.next_token = next_token
        # The ID of the normalization rule.
        self.normalization_rule_id = normalization_rule_id
        # A list of normalization rule IDs.
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        # The region of the threat analysis Data Management Center. Select the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: Your assets are outside the Chinese mainland.
        self.region_id = region_id
        # The user ID that an administrator uses to switch to a member\\"s perspective.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.normalization_rule_ids_shrink is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids_shrink = m.get('NormalizationRuleIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

