# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSecurityEventOperationStatusRequest(DaraModel):
    def __init__(
        self,
        resource_owner_id: int = None,
        security_event_ids: List[str] = None,
        source_ip: str = None,
        task_id: int = None,
    ):
        self.resource_owner_id = resource_owner_id
        # The IDs of the alert events.
        # 
        # >  You must specify at least one of the TaskId and SecurityEventIds parameters.
        # 
        # This parameter is required.
        self.security_event_ids = security_event_ids
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the task that handles the alert events.
        # 
        # >  You must specify at least one of the TaskId and SecurityEventIds parameters.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

