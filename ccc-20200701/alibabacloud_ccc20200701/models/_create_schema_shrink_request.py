# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSchemaShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        instance_id: str = None,
        properties_shrink: str = None,
        request_id: str = None,
    ):
        self.description = description
        # schema id
        self.id = id
        # This parameter is required.
        self.instance_id = instance_id
        self.properties_shrink = properties_shrink
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

