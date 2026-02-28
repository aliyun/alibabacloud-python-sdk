# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSchemaPropertyShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        property_shrink: str = None,
        request_id: str = None,
        schema_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.property_shrink = property_shrink
        self.request_id = request_id
        # schema id
        # 
        # This parameter is required.
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.property_shrink is not None:
            result['Property'] = self.property_shrink

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Property') is not None:
            self.property_shrink = m.get('Property')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

