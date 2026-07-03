# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUpgradeItemsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. Leave this parameter empty for the first request. To retrieve the next page, set this parameter to the NextToken value from the previous response.
        self.next_token = next_token
        # The region where the Data Management center is located. Select a region based on where your assets are. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: Your assets are outside China.
        self.region_id = region_id
        # The user ID of the member. An administrator can use this parameter to switch to the member\\"s view.
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

