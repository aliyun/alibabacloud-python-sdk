# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetListenerHealthStatusRequest(DaraModel):
    def __init__(
        self,
        include_rule: bool = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # Specifies whether to return the health check results of forwarding rules. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.include_rule = include_rule
        # The listener ID.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The number of entries to return on each page. Valid values: **1** to **30**. Default value: **20**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query or no next queries are to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_rule is not None:
            result['IncludeRule'] = self.include_rule

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeRule') is not None:
            self.include_rule = m.get('IncludeRule')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

