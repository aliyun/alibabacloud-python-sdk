# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecurityIPGroupRequest(DaraModel):
    def __init__(
        self,
        gip_list: str = None,
        global_ig_name: str = None,
        region_name: str = None,
    ):
        # This parameter is required.
        self.gip_list = gip_list
        # This parameter is required.
        self.global_ig_name = global_ig_name
        # This parameter is required.
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gip_list is not None:
            result['GIpList'] = self.gip_list

        if self.global_ig_name is not None:
            result['GlobalIgName'] = self.global_ig_name

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GIpList') is not None:
            self.gip_list = m.get('GIpList')

        if m.get('GlobalIgName') is not None:
            self.global_ig_name = m.get('GlobalIgName')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        return self

