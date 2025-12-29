# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerExecutionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content: str = None,
        execution_id: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The message body to be sent to the trigger task.
        self.content = content
        # The ID of the event-, alert-, or timer-triggered execution.
        # 
        # This parameter is required.
        self.execution_id = execution_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the trigger. Valid values:
        # 
        # *   Event
        # *   Alarm
        # *   Timer
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content is not None:
            result['Content'] = self.content

        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

