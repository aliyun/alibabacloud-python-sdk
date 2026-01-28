# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListComponentAssetsRequest(DaraModel):
    def __init__(
        self,
        component_asset_uuid: str = None,
        component_name: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        role_for: int = None,
    ):
        # Asset UUID.
        self.component_asset_uuid = component_asset_uuid
        # The name of the component.
        self.component_name = component_name
        # The language type for requests and responses. Values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # Maximum number of results to return. Range: 0~100.
        self.max_results = max_results
        # Token for the next query. Value: Not required for the first query or if there is no next query. For subsequent queries, use the NextToken value returned from the previous API call.
        self.next_token = next_token
        # Page number for paginated queries, with a default value of 1.
        self.page_number = page_number
        # Number of items per page for paginated queries. Range: 1~100.
        self.page_size = page_size
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_asset_uuid is not None:
            result['ComponentAssetUuid'] = self.component_asset_uuid

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetUuid') is not None:
            self.component_asset_uuid = m.get('ComponentAssetUuid')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

