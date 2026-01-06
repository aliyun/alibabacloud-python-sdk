# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOrgTodoTasksShrinkRequest(DaraModel):
    def __init__(
        self,
        tenant_context_shrink: str = None,
        is_done: bool = None,
        next_token: str = None,
    ):
        self.tenant_context_shrink = tenant_context_shrink
        self.is_done = is_done
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.is_done is not None:
            result['isDone'] = self.is_done

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('isDone') is not None:
            self.is_done = m.get('isDone')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

