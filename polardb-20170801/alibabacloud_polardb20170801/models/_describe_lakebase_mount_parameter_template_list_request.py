# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLakebaseMountParameterTemplateListRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        param_group_category: str = None,
        polar_fs_instance_id: str = None,
        region_id: str = None,
    ):
        # The engine. Set the value to polar_3fs.
        # 
        # This parameter is required.
        self.engine = engine
        # The instance category. Valid values: basic (Basic Edition) and high_performance (High-performance Edition).
        self.param_group_category = param_group_category
        # The PolarFS instance ID. You can call DescribePolarFs to query available PolarFS instances and use the returned PolarFsInstanceId.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.param_group_category is not None:
            result['ParamGroupCategory'] = self.param_group_category

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ParamGroupCategory') is not None:
            self.param_group_category = m.get('ParamGroupCategory')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

