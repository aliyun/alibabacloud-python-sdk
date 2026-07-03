# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        target_relation: str = None,
        target_type: str = None,
        target_uuid: str = None,
    ):
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of results to return when using NextToken-based pagination. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token for the next query. Leave this parameter empty for the first query or if no more results exist. If a next query is available, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The region where the threat analysis data management center is located. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: the asset is in the Chinese mainland.
        # - ap-southeast-1: the asset is outside China.
        self.region_id = region_id
        # The user ID that the administrator switches to when viewing as another member.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: the view of the current Alibaba Cloud account.
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type
        # The target relationship.
        self.target_relation = target_relation
        # The scan object type. Valid values:
        # 
        # - **1**: snapshot 
        # - **2**: image
        self.target_type = target_type
        # The UUID of the target asset.
        self.target_uuid = target_uuid

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

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.target_relation is not None:
            result['TargetRelation'] = self.target_relation

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.target_uuid is not None:
            result['TargetUuid'] = self.target_uuid

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

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('TargetRelation') is not None:
            self.target_relation = m.get('TargetRelation')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TargetUuid') is not None:
            self.target_uuid = m.get('TargetUuid')

        return self

