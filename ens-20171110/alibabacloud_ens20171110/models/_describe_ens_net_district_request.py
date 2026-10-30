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
        # The region code.
        # 
        # If this parameter is left empty, only the edge zones under the specified NetLevelCode are queried.
        # 
        # If this parameter is specified, only the child edge zones under the specified NetDistrictCode are queried.
        self.net_district_code = net_district_code
        # The region code.
        self.net_district_code_node = net_district_code_node
        # The region level. Valid values:
        # 
        # - **Big**: Area.
        # 
        # - **Middle**: Province.
        # 
        # - **Small**: City.
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

