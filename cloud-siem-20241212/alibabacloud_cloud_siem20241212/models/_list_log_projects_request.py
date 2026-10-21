# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogProjectsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_region_id: str = None,
        log_user_id: int = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # Note: Although this parameter is marked as optional in the schema, the API returns a 400 error if it is not provided. Therefore, this parameter is required in practice. Set the value to zh (Chinese) or en (English).
        self.lang = lang
        # The log storage region ID.
        self.log_region_id = log_region_id
        # The ID of the data access user.
        self.log_user_id = log_user_id
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The pagination token for the next query. You do not need to specify this parameter for the first query or if no more results exist. If more results exist, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The region where the threat detection and response data management center resides. Specify the management center region based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The ID of the member accounts in the resource folder.
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

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

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

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

