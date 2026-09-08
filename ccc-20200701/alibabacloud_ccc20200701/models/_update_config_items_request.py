# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConfigItemsRequest(DaraModel):
    def __init__(
        self,
        config_items: str = None,
        instance_id: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # A JSON-formatted string representing an array of configuration items. Each object in the array must contain a name to identify the configuration item and its value. You can use system-defined items (which have fixed names and customizable values, such as agent permissions to hang up or the ring no answer timeout) or create custom items.
        # 
        # This parameter is required.
        self.config_items = config_items
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the object to be configured.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The type of the object to be configured.
        # 
        # This parameter is required.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_items is not None:
            result['ConfigItems'] = self.config_items

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigItems') is not None:
            self.config_items = m.get('ConfigItems')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

