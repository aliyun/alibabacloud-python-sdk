# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateImageEventOperationRequest(DaraModel):
    def __init__(
        self,
        conditions: str = None,
        id: int = None,
        note: str = None,
        scenarios: str = None,
        source: str = None,
    ):
        # The rule conditions. Specify a value in the JSON format. You can specify the following keys:
        # 
        # *   **condition**: the matching condition.
        # *   **type**: the matching type.
        # *   **value**: the matching value.
        self.conditions = conditions
        # The ID of the alert handling rule. 
        # > You can call the [DescribeImageEventOperationPage](~~DescribeImageEventOperationPage~~) operation to query the ID.
        self.id = id
        # The remarks that you want to add.
        self.note = note
        # The application scope of the rule. The value is in the JSON format. Valid values:
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

        if self.id is not None:
            result['Id'] = self.id

        if self.note is not None:
            result['Note'] = self.note

        if self.scenarios is not None:
            result['Scenarios'] = self.scenarios

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('Scenarios') is not None:
            self.scenarios = m.get('Scenarios')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

