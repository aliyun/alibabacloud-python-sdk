# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteResponseRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        response_rule_id: str = None,
    ):
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token used to retrieve the next page of results. If you do not specify this parameter, the service returns the first page of results.
        self.next_token = next_token
        # The region ID of the data management center for threat analysis. This must be the region where your assets are located. Valid values:
        # 
        # - `cn-hangzhou`: for assets in the Chinese mainland or Hong Kong (China).
        # 
        # - `ap-southeast-1`: for assets in international regions.
        self.region_id = region_id
        # The ID of the automatic response rule to delete.
        self.response_rule_id = response_rule_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.response_rule_id is not None:
            result['ResponseRuleId'] = self.response_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResponseRuleId') is not None:
            self.response_rule_id = m.get('ResponseRuleId')

        return self

