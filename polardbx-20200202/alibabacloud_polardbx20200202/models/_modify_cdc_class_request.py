# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCdcClassRequest(DaraModel):
    def __init__(
        self,
        cdcnode_count: str = None,
        cdc_class: str = None,
        instance_name: str = None,
        region_id: str = None,
        switch_mode: str = None,
    ):
        self.cdcnode_count = cdcnode_count
        # This parameter is required.
        self.cdc_class = cdc_class
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
        if self.cdcnode_count is not None:
            result['CDCNodeCount'] = self.cdcnode_count

        if self.cdc_class is not None:
            result['CdcClass'] = self.cdc_class

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CDCNodeCount') is not None:
            self.cdcnode_count = m.get('CDCNodeCount')

        if m.get('CdcClass') is not None:
            self.cdc_class = m.get('CdcClass')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

