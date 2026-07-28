# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DlfInstance(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The unique ID of the DLF instance.
        self.instance_id = instance_id
        # The name of the DLF instance.
        self.instance_name = instance_name
        # The type of the DLF instance.
        self.instance_type = instance_type
        # The ID of the region where the DLF instance is located.
        self.region_id = region_id
        # The current status of the DLF instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

