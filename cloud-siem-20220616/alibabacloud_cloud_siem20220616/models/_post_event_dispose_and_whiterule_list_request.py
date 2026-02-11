# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostEventDisposeAndWhiteruleListRequest(DaraModel):
    def __init__(
        self,
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
        self.dispose_strategy_ids = dispose_strategy_ids
        # The configuration of event handling. The value is a JSON object.
        self.event_dispose = event_dispose
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        self.owner = owner
        # The configuration of the alert recipient. The value is a JSON object.
        self.receiver_info = receiver_info
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The remarks of the event.
        self.remark = remark
        self.response_source = response_source
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type
        # The status of the event. Valid values:
        # 
        # *   0: unhandled
        # *   1: handing
        # *   5: handling failed
        # *   10: handled
        self.status = status
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

