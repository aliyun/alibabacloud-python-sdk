# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNormalizationCategoriesRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_category_type: str = None,
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
        # The token that is used to retrieve the next page of results. Set this parameter to the NextToken value returned in the previous API call to retrieve the next page of results. You do not need to specify this parameter for the first query.
        self.next_token = next_token
        # The type of the normalization rule category. Valid values:
        # 
        # - log
        # 
        # - entity
        self.normalization_category_type = normalization_category_type
        # The region of the Data Management center for threat analysis. Select the region for the Data Management center based on the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Assets are in the Chinese mainland.
        # 
        # - ap-southeast-1: Assets are in a region outside China.
        self.region_id = region_id
        # The user ID of the member. An administrator can use this parameter to switch to the perspective of this member.
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

        if self.normalization_category_type is not None:
            result['NormalizationCategoryType'] = self.normalization_category_type

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

        if m.get('NormalizationCategoryType') is not None:
            self.normalization_category_type = m.get('NormalizationCategoryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

