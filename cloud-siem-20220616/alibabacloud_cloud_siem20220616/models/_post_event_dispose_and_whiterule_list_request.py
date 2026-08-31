# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostEventDisposeAndWhiteruleListRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dispose_strategy_ids: str = None,
        event_dispose: str = None,
        incident_uuid: str = None,
        owner: str = None,
        receiver_info: str = None,
        region_id: str = None,
        remark: str = None,
        response_source: str = None,
        role_for: int = None,
        role_type: int = None,
        status: int = None,
        threat_level: str = None,
    ):
        # 幂等令牌。
        self.client_token = client_token
        # A comma-separated list of response strategy IDs.
        self.dispose_strategy_ids = dispose_strategy_ids
        # A JSON object that defines the incident response configuration.
        self.event_dispose = event_dispose
        # The globally unique UUID of the incident.
        self.incident_uuid = incident_uuid
        # The UID of the incident owner.
        self.owner = owner
        # A JSON object that defines the alert recipient configuration.
        self.receiver_info = receiver_info
        # The region where the Data Management service for threat analysis is deployed. Select a region based on where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Assets in the Chinese mainland or Hong Kong (China)
        # 
        # - ap-southeast-1: Assets outside China
        self.region_id = region_id
        # A note about the incident.
        self.remark = remark
        # The source of the response policy.
        self.response_source = response_source
        # The UID of the member whose perspective an administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0: Current Alibaba Cloud account view
        # 
        # - 1: View for all accounts in your enterprise
        self.role_type = role_type
        # The incident status. Valid values:
        # 
        # - 0: Not handled
        # 
        # - 1: Handling
        # 
        # - 5: Failed
        # 
        # - 10: Handled
        self.status = status
        # The threat level. Valid values:
        # 
        # - serious: Important
        # 
        # - suspicious: Medium
        # 
        # - remind: Low
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dispose_strategy_ids is not None:
            result['DisposeStrategyIds'] = self.dispose_strategy_ids

        if self.event_dispose is not None:
            result['EventDispose'] = self.event_dispose

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.receiver_info is not None:
            result['ReceiverInfo'] = self.receiver_info

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.response_source is not None:
            result['ResponseSource'] = self.response_source

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.status is not None:
            result['Status'] = self.status

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DisposeStrategyIds') is not None:
            self.dispose_strategy_ids = m.get('DisposeStrategyIds')

        if m.get('EventDispose') is not None:
            self.event_dispose = m.get('EventDispose')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ReceiverInfo') is not None:
            self.receiver_info = m.get('ReceiverInfo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResponseSource') is not None:
            self.response_source = m.get('ResponseSource')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        return self

