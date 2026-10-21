# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIncidentInvestigationRequest(DaraModel):
    def __init__(
        self,
        incident_investigation_display_id: str = None,
        incident_investigation_id: str = None,
        incident_uuid: str = None,
        lang: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        # The display ID of the AI investigation report. You can obtain this value from the IncidentInvestigationDisplayId field returned by ListIncidentInvestigations. This parameter takes effect only when IncidentInvestigationId is not specified. If neither identifier is specified, the most recent successfully completed investigation result for the specified incident is returned.
        self.incident_investigation_display_id = incident_investigation_display_id
        # The AI investigation report ID. You can obtain this value from the IncidentInvestigationId field returned by ListIncidentInvestigations. If both this parameter and IncidentInvestigationDisplayId are specified, this parameter takes precedence.
        self.incident_investigation_id = incident_investigation_id
        # The globally unique identity of the event. If neither the report ID nor the display ID is specified, the most recent successfully completed investigation result for this event is returned via event query.
        # 
        # This parameter is required.
        self.incident_uuid = incident_uuid
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The region where the threat analysis data management center resides. Specify the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Chinese mainland.
        # - ap-southeast-1: Outside the Chinese mainland.
        self.region_id = region_id
        # The user ID that the administrator uses to switch to the view of another member.
        self.role_for = role_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.incident_investigation_display_id is not None:
            result['IncidentInvestigationDisplayId'] = self.incident_investigation_display_id

        if self.incident_investigation_id is not None:
            result['IncidentInvestigationId'] = self.incident_investigation_id

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncidentInvestigationDisplayId') is not None:
            self.incident_investigation_display_id = m.get('IncidentInvestigationDisplayId')

        if m.get('IncidentInvestigationId') is not None:
            self.incident_investigation_id = m.get('IncidentInvestigationId')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

