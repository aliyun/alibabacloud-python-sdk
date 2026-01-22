# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyColumnarClassRequest(DaraModel):
    def __init__(
        self,
        columnar_class: str = None,
        columnar_node_count: str = None,
        instance_name: str = None,
        region_id: str = None,
        switch_mode: str = None,
    ):
        # This parameter is required.
        self.columnar_class = columnar_class
        self.columnar_node_count = columnar_node_count
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.region_id = region_id
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columnar_class is not None:
            result['ColumnarClass'] = self.columnar_class

        if self.columnar_node_count is not None:
            result['ColumnarNodeCount'] = self.columnar_node_count

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnarClass') is not None:
            self.columnar_class = m.get('ColumnarClass')

        if m.get('ColumnarNodeCount') is not None:
            self.columnar_node_count = m.get('ColumnarNodeCount')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

