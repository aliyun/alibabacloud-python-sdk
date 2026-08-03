# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQueryViewsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        query_view_scene: str = None,
        query_view_type: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of results to return when you use the NextToken-based pagination method. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request or if no more results exist. If more results exist, set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The scene to which the query view belongs.
        self.query_view_scene = query_view_scene
        # The view type. If this parameter is left empty, all views are returned.
        self.query_view_type = query_view_type
        # The region where the threat analysis data management center is located. Specify the management center based on the region of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets belong to the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: Your assets belong to regions outside China.
        self.region_id = region_id
        # The user ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # - 1: The view of all accounts in the enterprise.
        self.role_type = role_type

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

        if self.query_view_scene is not None:
            result['QueryViewScene'] = self.query_view_scene

        if self.query_view_type is not None:
            result['QueryViewType'] = self.query_view_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('QueryViewScene') is not None:
            self.query_view_scene = m.get('QueryViewScene')

        if m.get('QueryViewType') is not None:
            self.query_view_type = m.get('QueryViewType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

