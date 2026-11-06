# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSandboxSessionsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        service_endpoint_id: str = None,
    ):
        # The maximum number of entries to return per page. Default value: 20. Valid values: 1 to 100.
        self.max_results = max_results
        # The token for the next page. Omit this parameter in the first request. For subsequent requests, use the returned token as is, and keep the workspace, agent, instance, and maxResults unchanged. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # 必须与查出该 sandboxId 时使用的 ListSandboxes 入参一致。省略或传空白时查询智能体 latest 运行单元；传入时该服务端点必须属于本智能体且目标类型为 AGENT_VERSION，否则返回 Resource.NotFound；非 DEFAULT 且未独立运行时返回 ServiceEndpointTargetNotReady。sandboxId 不属于所指运行单元时返回 Sandbox.NotFound，不返回空列表。
        self.service_endpoint_id = service_endpoint_id

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

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        return self

