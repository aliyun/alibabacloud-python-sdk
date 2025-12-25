# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupsResponseBody(DaraModel):
    def __init__(
        self,
        parameter_groups: main_models.DescribeParameterGroupsResponseBodyParameterGroups = None,
        request_id: str = None,
        signal_for_optimize_params: bool = None,
    ):
        # The details of the parameter templates.
        self.parameter_groups = parameter_groups
        # The request ID.
        self.request_id = request_id
        # Indicates whether parameter templates exist in the specified region. Valid values:
        # *   true
        # *   false
        # >Notice: This parameter is deprecated.
        self.signal_for_optimize_params = signal_for_optimize_params

    def validate(self):
        if self.parameter_groups:
            self.parameter_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_groups is not None:
            result['ParameterGroups'] = self.parameter_groups.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signal_for_optimize_params is not None:
            result['SignalForOptimizeParams'] = self.signal_for_optimize_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterGroups') is not None:
            temp_model = main_models.DescribeParameterGroupsResponseBodyParameterGroups()
            self.parameter_groups = temp_model.from_map(m.get('ParameterGroups'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignalForOptimizeParams') is not None:
            self.signal_for_optimize_params = m.get('SignalForOptimizeParams')

        return self

class DescribeParameterGroupsResponseBodyParameterGroups(DaraModel):
    def __init__(
        self,
        parameter_group: List[main_models.DescribeParameterGroupsResponseBodyParameterGroupsParameterGroup] = None,
    ):
        self.parameter_group = parameter_group

    def validate(self):
        if self.parameter_group:
            for v1 in self.parameter_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ParameterGroup'] = []
        if self.parameter_group is not None:
            for k1 in self.parameter_group:
                result['ParameterGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_group = []
        if m.get('ParameterGroup') is not None:
            for k1 in m.get('ParameterGroup'):
                temp_model = main_models.DescribeParameterGroupsResponseBodyParameterGroupsParameterGroup()
                self.parameter_group.append(temp_model.from_map(k1))

        return self

class DescribeParameterGroupsResponseBodyParameterGroupsParameterGroup(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        engine: str = None,
        engine_version: str = None,
        force_restart: int = None,
        param_counts: int = None,
        parameter_group_desc: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameter_group_type: int = None,
        update_time: str = None,
    ):
        # The time when the parameter template was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The database engine of the instance.
        self.engine = engine
        # The database engine version.
        self.engine_version = engine_version
        # Indicates whether the restart of an instance is required for the parameter template to take effect. Valid values:
        # 
        # *   0: A restart is not required.
        # *   1: A restart is required.
        self.force_restart = force_restart
        # The number of parameters in the parameter template.
        self.param_counts = param_counts
        # The type of the parameter template. Valid values:
        # 
        # *   0: the default parameter template.
        # *   1: a custom parameter template.
        # *   2: an automatic backup parameter template. After you apply this type of template, the system automatically backs up the original parameter settings and saves the backup as a template.
        self.parameter_group_desc = parameter_group_desc
        # The ID of the parameter template.
        self.parameter_group_id = parameter_group_id
        # The name of the parameter template.
        self.parameter_group_name = parameter_group_name
        # The type of the parameter template. Valid values:
        # 
        # *   0: the default parameter template.
        # *   1: a custom parameter template.
        # *   2: an automatic backup parameter template. After you apply this type of template, the system automatically backs up the original parameter settings and saves the backup as a template.
        self.parameter_group_type = parameter_group_type
        # The time when the parameter template was last updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.param_counts is not None:
            result['ParamCounts'] = self.param_counts

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameter_group_type is not None:
            result['ParameterGroupType'] = self.parameter_group_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('ParamCounts') is not None:
            self.param_counts = m.get('ParamCounts')

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('ParameterGroupType') is not None:
            self.parameter_group_type = m.get('ParameterGroupType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

