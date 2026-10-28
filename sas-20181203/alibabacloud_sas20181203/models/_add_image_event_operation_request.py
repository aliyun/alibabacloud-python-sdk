# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddImageEventOperationRequest(DaraModel):
    def __init__(
        self,
        conditions: str = None,
        event_key: str = None,
        event_name: str = None,
        event_type: str = None,
        note: str = None,
        operation_code: str = None,
        scenarios: str = None,
        source: str = None,
    ):
        # The rule conditions. The value is in JSON format. Valid keys:
        # - **condition**: The matching condition.
        # - **type**: The matching type.
        # - **value**: The matching value.
        self.conditions = conditions
        # The alert metric keyword.
        self.event_key = event_key
        # The alert metric name.
        self.event_name = event_name
        # The Alarm Metric for alerting. Valid values:
        # - **sensitiveFile**: Sensitive file.
        self.event_type = event_type
        # The note to add.
        self.note = note
        # The operation code. Valid values:
        # - **whitelist**: Whitelist.
        self.operation_code = operation_code
        # The rule scope. The value is in JSON format. Valid keys:
        # - **type**: The scope type.
        # - **value**: The scope value.
        # > This parameter and **Source** cannot be empty at the same time. If **Source** is set to **agentless**, this parameter does not take effect.
        self.scenarios = scenarios
        # The source of the whitelist. Valid values:
        # - **image**: Image.
        # - **agentless**: Agentless detection.
        # > This parameter and **Scenarios** cannot be empty at the same time. If this parameter is set to **agentless**, the **Scenarios** parameter does not take effect.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conditions is not None:
            result['Conditions'] = self.conditions

        if self.event_key is not None:
            result['EventKey'] = self.event_key

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.note is not None:
            result['Note'] = self.note

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.scenarios is not None:
            result['Scenarios'] = self.scenarios

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')

        if m.get('EventKey') is not None:
            self.event_key = m.get('EventKey')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('Scenarios') is not None:
            self.scenarios = m.get('Scenarios')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

