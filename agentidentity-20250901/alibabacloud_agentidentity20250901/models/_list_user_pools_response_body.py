# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListUserPoolsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        user_pools: List[main_models.ListUserPoolsResponseBodyUserPools] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.user_pools = user_pools

    def validate(self):
        if self.user_pools:
            for v1 in self.user_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserPools'] = []
        if self.user_pools is not None:
            for k1 in self.user_pools:
                result['UserPools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_pools = []
        if m.get('UserPools') is not None:
            for k1 in m.get('UserPools'):
                temp_model = main_models.ListUserPoolsResponseBodyUserPools()
                self.user_pools.append(temp_model.from_map(k1))

        return self

class ListUserPoolsResponseBodyUserPools(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        update_time: str = None,
        user_pool_id: str = None,
        user_pool_name: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.update_time = update_time
        self.user_pool_id = user_pool_id
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_pool_id is not None:
            result['UserPoolId'] = self.user_pool_id

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserPoolId') is not None:
            self.user_pool_id = m.get('UserPoolId')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

