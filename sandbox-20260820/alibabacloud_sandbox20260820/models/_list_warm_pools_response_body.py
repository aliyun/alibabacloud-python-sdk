# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class ListWarmPoolsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        warm_pools: List[main_models.PublicWarmPoolConfig] = None,
    ):
        # The business code in the response.
        self.code = code
        # The actual maximum number of results returned per page.
        self.max_results = max_results
        # The response message.
        self.message = message
        # The pagination token. An empty value indicates that no more results are available.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The list of warm pools.
        self.warm_pools = warm_pools

    def validate(self):
        if self.warm_pools:
            for v1 in self.warm_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.warm_pools is not None:
            result['warmPools'] = []
            for k1 in self.warm_pools:
                result['warmPools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('warmPools') is not None:
            self.warm_pools = []
            for k1 in m.get('warmPools'):
                temp_model = main_models.PublicWarmPoolConfig()
                self.warm_pools.append(temp_model.from_map(k1))

        return self

