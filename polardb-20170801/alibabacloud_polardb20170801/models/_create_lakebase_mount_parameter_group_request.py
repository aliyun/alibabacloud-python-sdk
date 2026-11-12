# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLakebaseMountParameterGroupRequest(DaraModel):
    def __init__(
        self,
        param_group_category: str = None,
        parameter_group_desc: str = None,
        parameter_group_name: str = None,
        parameters: str = None,
        polar_fs_instance_id: str = None,
        region_id: str = None,
    ):
        # The instance edition. Valid values:
        # - basic: Basic Edition.
        # - high_performance: High-performance Edition.
        # 
        # This parameter is required.
        self.param_group_category = param_group_category
        # The description of the parameter template.
        self.parameter_group_desc = parameter_group_desc
        # The name of the parameter template.
        # 
        # This parameter is required.
        self.parameter_group_name = parameter_group_name
        # The JSON string of parameters and their values.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The PolarFS instance ID.
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
        if self.param_group_category is not None:
            result['ParamGroupCategory'] = self.param_group_category

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamGroupCategory') is not None:
            self.param_group_category = m.get('ParamGroupCategory')

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

