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
        # The rule conditions. The value is in the JSON format. Valid values of keys:
        # 
        # *   **condition**: the matching condition.
        # *   **type**: the matching type.
        # *   **value**: the matching value.
        self.conditions = conditions
        # The keyword of the alert item.
        self.event_key = event_key
        # The name of the alert item.
        self.event_name = event_name
        # The alert type.
        # 
        # *   Set the value to **sensitiveFile**.
        self.event_type = event_type
        # The remarks that you want to add.
        self.note = note
        # The operation code.
        # 
        # *   Set the value to **whitelist** to add the alert item to the whitelist.
        self.operation_code = operation_code
        # The application scope of the rule. The value is in the JSON format. Valid values of keys:
        # 
        # *   **type**
        # *   **value**
        self.scenarios = scenarios
        # The source of the whitelist. Valid values:
        # 
        # *   **image**: image.
        # *   **agentless**: agentless detection.
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

