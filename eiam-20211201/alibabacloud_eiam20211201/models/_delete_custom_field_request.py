# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCustomFieldRequest(DaraModel):
    def __init__(
        self,
        field_id: str = None,
        instance_id: str = None,
    ):
        # fieldId
        # 
        # This parameter is required.
        self.field_id = field_id
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_id is not None:
            result['FieldId'] = self.field_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldId') is not None:
            self.field_id = m.get('FieldId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

