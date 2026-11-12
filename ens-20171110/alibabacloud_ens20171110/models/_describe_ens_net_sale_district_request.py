# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEnsNetSaleDistrictRequest(DaraModel):
    def __init__(
        self,
        net_district_code: str = None,
        net_level_code: str = None,
    ):
        # The district code.
        # 
        # - If this parameter is left empty, only the nodes under the network level specified by NetLevelCode are queried.
        # 
        # - If this parameter is specified, only the child nodes under the district specified by NetDistrictCode are queried.
        self.net_district_code = net_district_code
        # The network level. Valid values:
        # 
        # - **Big**: Major region.
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

        if self.net_level_code is not None:
            result['NetLevelCode'] = self.net_level_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')

        if m.get('NetLevelCode') is not None:
            self.net_level_code = m.get('NetLevelCode')

        return self

