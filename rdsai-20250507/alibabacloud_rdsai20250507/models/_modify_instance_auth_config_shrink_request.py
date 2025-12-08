# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceAuthConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        config_list_shrink: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.config_list_shrink = config_list_shrink
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_list_shrink is not None:
            result['ConfigList'] = self.config_list_shrink

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigList') is not None:
            self.config_list_shrink = m.get('ConfigList')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

