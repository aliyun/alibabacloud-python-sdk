# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCreditPackageAgentsRequest(DaraModel):
    def __init__(
        self,
        agent_ids: List[str] = None,
        agent_type: str = None,
        biz_type: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # An array of agent IDs to query. Example: `["agent-1","agent-2"]`.
        self.agent_ids = agent_ids
        # The agent type. Valid values: `CREDIT_PACKAGE`, `JVS_CLAW`, `OPEN_CLAW`, and `JVS_COPILOT`.
        self.agent_type = agent_type
        # The business type.
        self.biz_type = biz_type
        # The maximum number of results to return per page.
        self.max_results = max_results
        # The token to retrieve the next page of results. Obtain this value from the `NextToken` parameter of the previous response. For the first request, set this parameter to an empty string.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

