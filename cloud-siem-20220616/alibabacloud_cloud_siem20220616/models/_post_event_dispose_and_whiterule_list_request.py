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
        sync_alert_status: bool = None,
        threat_level: str = None,
    ):
        # The idempotency token.
        self.client_token = client_token
        # The list of handling policy IDs.
        self.dispose_strategy_ids = dispose_strategy_ids
        # The incident handling configuration as a JSON object.
        self.event_dispose = event_dispose
        # The globally unique UUID of the incident.
        self.incident_uuid = incident_uuid
        # The account UID of the incident owner.
        self.owner = owner
        # The alert recipient configuration as a JSON object.
        self.receiver_info = receiver_info
        # The region where the threat analysis data management center resides. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets reside in regions in the Chinese mainland or China (Hong Kong).
        # - ap-southeast-1: Your assets reside in regions outside the Chinese mainland.
        self.region_id = region_id
        # The remarks for the incident.
        self.remark = remark
        # The source of the handling policy.
        self.response_source = response_source
        # The ID of the user for whom the administrator switches to a member view.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0: the China account view.
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type
        # The incident status. Valid values:
        # 
        # - 0: unhandled  
        # - 1: handling 
        # - 5: handling failed 
        # - 10: handled
        self.status = status
        # Specifies whether to restore associated handled alerts to unhandled status when reopening the incident.
        self.sync_alert_status = sync_alert_status
        # The threat level. Valid values:
        # - serious: high
        # - suspicious: medium
        # - remind: low
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

        if self.sync_alert_status is not None:
            result['SyncAlertStatus'] = self.sync_alert_status

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

        if m.get('SyncAlertStatus') is not None:
            self.sync_alert_status = m.get('SyncAlertStatus')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        return self

