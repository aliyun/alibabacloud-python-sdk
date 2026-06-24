# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DataAgentBillingInstance(DaraModel):
    def __init__(
        self,
        agent_seats: int = None,
        billing_instance_id: str = None,
        bound_workspace_ids: List[str] = None,
        charge_type: str = None,
        commodity_code: str = None,
        expire_time: int = None,
        free_agent_seats: int = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        is_default: bool = None,
        llm: int = None,
        pay_level: str = None,
        session_available_duration_quota: int = None,
        session_seats: int = None,
        token_limit: int = None,
    ):
        self.agent_seats = agent_seats
        self.billing_instance_id = billing_instance_id
        self.bound_workspace_ids = bound_workspace_ids
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.expire_time = expire_time
        self.free_agent_seats = free_agent_seats
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.is_default = is_default
        self.llm = llm
        self.pay_level = pay_level
        self.session_available_duration_quota = session_available_duration_quota
        self.session_seats = session_seats
        self.token_limit = token_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_seats is not None:
            result['AgentSeats'] = self.agent_seats

        if self.billing_instance_id is not None:
            result['BillingInstanceId'] = self.billing_instance_id

        if self.bound_workspace_ids is not None:
            result['BoundWorkspaceIds'] = self.bound_workspace_ids

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.free_agent_seats is not None:
            result['FreeAgentSeats'] = self.free_agent_seats

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.llm is not None:
            result['LLM'] = self.llm

        if self.pay_level is not None:
            result['PayLevel'] = self.pay_level

        if self.session_available_duration_quota is not None:
            result['SessionAvailableDurationQuota'] = self.session_available_duration_quota

        if self.session_seats is not None:
            result['SessionSeats'] = self.session_seats

        if self.token_limit is not None:
            result['TokenLimit'] = self.token_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentSeats') is not None:
            self.agent_seats = m.get('AgentSeats')

        if m.get('BillingInstanceId') is not None:
            self.billing_instance_id = m.get('BillingInstanceId')

        if m.get('BoundWorkspaceIds') is not None:
            self.bound_workspace_ids = m.get('BoundWorkspaceIds')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FreeAgentSeats') is not None:
            self.free_agent_seats = m.get('FreeAgentSeats')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('LLM') is not None:
            self.llm = m.get('LLM')

        if m.get('PayLevel') is not None:
            self.pay_level = m.get('PayLevel')

        if m.get('SessionAvailableDurationQuota') is not None:
            self.session_available_duration_quota = m.get('SessionAvailableDurationQuota')

        if m.get('SessionSeats') is not None:
            self.session_seats = m.get('SessionSeats')

        if m.get('TokenLimit') is not None:
            self.token_limit = m.get('TokenLimit')

        return self

