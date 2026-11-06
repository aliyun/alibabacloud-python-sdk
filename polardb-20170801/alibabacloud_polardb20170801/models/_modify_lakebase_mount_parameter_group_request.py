# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLakebaseMountParameterGroupRequest(DaraModel):
    def __init__(
        self,
        delete_parameters: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameters: str = None,
        polar_fs_instance_id: str = None,
        region_id: str = None,
    ):
        # The names of the parameters to delete, separated by commas.
        self.delete_parameters = delete_parameters
        # The parameter template ID.
        # 
        # This parameter is required.
        self.parameter_group_id = parameter_group_id
        # The new parameter template name.
        self.parameter_group_name = parameter_group_name
        # The JSON string of added or modified parameter key-value pairs.
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
        if self.delete_parameters is not None:
            result['DeleteParameters'] = self.delete_parameters

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

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
        if m.get('DeleteParameters') is not None:
            self.delete_parameters = m.get('DeleteParameters')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

