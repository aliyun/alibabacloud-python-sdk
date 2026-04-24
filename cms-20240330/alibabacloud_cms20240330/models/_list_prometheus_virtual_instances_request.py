# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPrometheusVirtualInstancesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        namespace: str = None,
        next_token: str = None,
        tenant_id: str = None,
    ):
        self.max_results = max_results
        # Optional cloud product
        self.namespace = namespace
        self.next_token = next_token
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

