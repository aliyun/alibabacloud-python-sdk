# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSimilarSecurityEventsQueryTaskRequest(DaraModel):
    def __init__(
        self,
        resource_owner_id: int = None,
        security_event_id: int = None,
        similar_event_scenario_code: str = None,
        source_ip: str = None,
    ):
        self.resource_owner_id = resource_owner_id
        # The ID of the alert event.
        # 
        # >  You must specify at least one of the SecurityEventId and SimilarEventScenarioCode parameters.
        # 
        # This parameter is required.
        self.security_event_id = security_event_id
        # The codes of alert events that are triggered by the same rule or of the same alert type.
        # 
        # >  You must specify at least one of the SecurityEventId and SimilarEventScenarioCode parameters.
        self.similar_event_scenario_code = similar_event_scenario_code
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.similar_event_scenario_code is not None:
            result['SimilarEventScenarioCode'] = self.similar_event_scenario_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('SimilarEventScenarioCode') is not None:
            self.similar_event_scenario_code = m.get('SimilarEventScenarioCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

