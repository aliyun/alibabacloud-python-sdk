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
        # - **zh** (default): Chinese.
        # - **en**: English.
        # This parameter is required in practice. If you do not specify this parameter or pass an empty string, the API returns a 400 error (The specified Lang can not be empty.).
        self.lang = lang
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The pagination token for the next query. You do not need to specify this parameter for the first query or if no more results exist. If more results exist, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The normalization rule ID.
        self.normalization_rule_id = normalization_rule_id
        # The list of normalization rule IDs.
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        # The region where the threat analysis data management center resides. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: The assets reside in the Chinese mainland.
        # - ap-southeast-1: The assets reside outside China.
        self.region_id = region_id
        # The user ID that the administrator uses to switch to the view of another member.
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

