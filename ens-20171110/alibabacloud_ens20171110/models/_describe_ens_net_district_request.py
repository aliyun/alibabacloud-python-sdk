# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnsNetDistrictRequest(DaraModel):
    def __init__(
        self,
        net_district_code: str = None,
        net_district_code_node: bool = None,
        net_level_code: str = None,
    ):
        # The code of the region.
        # 
        # If you do not specify this parameter, only nodes in the regions of the level that is specified by the NetLevelCode parameter are queried.
        # 
        # If you specify this parameter, only nodes in the regions of the level that is specified by this parameter are queried.
        self.net_district_code = net_district_code
        self.net_district_code_node = net_district_code_node
        # The level of the region.
        # 
        # *   **Big**: area
        # *   **Middle**: province
        # *   **Small**: city
        # 
        # This parameter is required.
        self.net_level_code = net_level_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code

        if self.net_district_code_node is not None:
            result['NetDistrictCodeNode'] = self.net_district_code_node

        if self.net_level_code is not None:
            result['NetLevelCode'] = self.net_level_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')

        if m.get('NetDistrictCodeNode') is not None:
            self.net_district_code_node = m.get('NetDistrictCodeNode')

        if m.get('NetLevelCode') is not None:
            self.net_level_code = m.get('NetLevelCode')

        return self

