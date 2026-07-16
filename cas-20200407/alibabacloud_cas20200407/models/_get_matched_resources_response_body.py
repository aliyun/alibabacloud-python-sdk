# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetMatchedResourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: Any = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # 请求接口返回的数据。
        self.data = data
        # 分页参数：结果集的最大数量，默认值为 20。
        self.max_results = max_results
        # 下一个查询开始 Token，NextToken 为空说明没有下一个。
        self.next_token = next_token
        # 本次请求的 ID。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

