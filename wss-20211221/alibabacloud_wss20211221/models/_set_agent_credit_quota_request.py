# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetAgentCreditQuotaRequest(DaraModel):
    def __init__(
        self,
        agent_ids: List[str] = None,
        agent_type: str = None,
        biz_type: str = None,
        credit_quota: int = None,
    ):
        self.agent_ids = agent_ids
        self.agent_type = agent_type
        self.biz_type = biz_type
        self.credit_quota = credit_quota

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

        if self.credit_quota is not None:
            result['CreditQuota'] = self.credit_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('CreditQuota') is not None:
            self.credit_quota = m.get('CreditQuota')

        return self

