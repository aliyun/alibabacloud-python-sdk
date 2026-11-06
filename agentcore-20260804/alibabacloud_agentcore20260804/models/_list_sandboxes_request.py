# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSandboxesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_text: str = None,
        service_endpoint_id: str = None,
        session_id: str = None,
    ):
        # The maximum number of entries to return per page. Default value: 20. Valid values: 1 to 100.
        self.max_results = max_results
        # The cursor for querying the next page. When paginating, keep `workspaceId`, `agentId`, `searchText`, `sessionId`, and `maxResults` unchanged.
        self.next_token = next_token
        # The fragment of the Sandbox ID for a case-insensitive fuzzy search.
        self.search_text = search_text
        # 省略或传空白时查询智能体 latest 运行单元；传入时该服务端点必须属于本智能体且目标类型为 AGENT_VERSION，否则返回 Resource.NotFound。独立运行的服务端点只返回其自身运行单元的 Sandbox；DEFAULT 服务端点尚未接管独立运行时回落到 latest 运行单元；非 DEFAULT 且未独立运行时返回 ServiceEndpointTargetNotReady。运行单元尚未创建时返回空列表且 totalCount 为 0，不报错。
        self.service_endpoint_id = service_endpoint_id
        # The fragment of the current valid session ID for a case-insensitive fuzzy search.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.search_text is not None:
            result['searchText'] = self.search_text

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('searchText') is not None:
            self.search_text = m.get('searchText')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

