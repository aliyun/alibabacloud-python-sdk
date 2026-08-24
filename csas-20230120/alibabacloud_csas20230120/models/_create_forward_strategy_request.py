# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateForwardStrategyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_id: str = None,
        destination_type: str = None,
        name: str = None,
        priority: int = None,
        status: str = None,
    ):
        # The description. The description must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), hyphens (-), and spaces. The description can also contain Chinese characters.
        self.description = description
        # The target instance ID.
        # 
        # This parameter is required.
        self.destination_id = destination_id
        # The destination type. Valid values:
        # - **Connector**: connector.
        # 
        # This parameter is required.
        self.destination_type = destination_type
        # The name. The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name can also contain Chinese characters.
        # 
        # This parameter is required.
        self.name = name
        # The policy priority. A value of 1 indicates the highest priority. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.priority = priority
        # The policy status. Valid values:
        # - **Enabled**: enabled.
        # - **Disabled**: disabled.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

