# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCampaignRequest(DaraModel):
    def __init__(
        self,
        callable_time: str = None,
        campaign_id: str = None,
        contact_flow_id: str = None,
        end_time: str = None,
        instance_id: str = None,
        name: str = None,
        start_time: str = None,
        strategy_parameters: str = None,
    ):
        self.callable_time = callable_time
        # This parameter is required.
        self.campaign_id = campaign_id
        self.contact_flow_id = contact_flow_id
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.name = name
        self.start_time = start_time
        self.strategy_parameters = strategy_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callable_time is not None:
            result['CallableTime'] = self.callable_time

        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.strategy_parameters is not None:
            result['StrategyParameters'] = self.strategy_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallableTime') is not None:
            self.callable_time = m.get('CallableTime')

        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StrategyParameters') is not None:
            self.strategy_parameters = m.get('StrategyParameters')

        return self

