# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeCreditPackageAgentsResponseBody(DaraModel):
    def __init__(
        self,
        agents: List[main_models.DescribeCreditPackageAgentsResponseBodyAgents] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.agents = agents
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.agents:
            for v1 in self.agents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agents'] = []
        if self.agents is not None:
            for k1 in self.agents:
                result['Agents'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agents = []
        if m.get('Agents') is not None:
            for k1 in m.get('Agents'):
                temp_model = main_models.DescribeCreditPackageAgentsResponseBodyAgents()
                self.agents.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCreditPackageAgentsResponseBodyAgents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        created_time: str = None,
        credit_package_id: str = None,
        expired_time: str = None,
        instance_type: str = None,
        total_credit: int = None,
        used_credit: int = None,
        warn_percent: int = None,
    ):
        # Agent ID
        self.agent_id = agent_id
        self.created_time = created_time
        self.credit_package_id = credit_package_id
        self.expired_time = expired_time
        self.instance_type = instance_type
        self.total_credit = total_credit
        self.used_credit = used_credit
        self.warn_percent = warn_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.credit_package_id is not None:
            result['CreditPackageId'] = self.credit_package_id

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.total_credit is not None:
            result['TotalCredit'] = self.total_credit

        if self.used_credit is not None:
            result['UsedCredit'] = self.used_credit

        if self.warn_percent is not None:
            result['WarnPercent'] = self.warn_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreditPackageId') is not None:
            self.credit_package_id = m.get('CreditPackageId')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('TotalCredit') is not None:
            self.total_credit = m.get('TotalCredit')

        if m.get('UsedCredit') is not None:
            self.used_credit = m.get('UsedCredit')

        if m.get('WarnPercent') is not None:
            self.warn_percent = m.get('WarnPercent')

        return self

