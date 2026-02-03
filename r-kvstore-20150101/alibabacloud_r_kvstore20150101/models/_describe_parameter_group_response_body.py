# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupResponseBody(DaraModel):
    def __init__(
        self,
        parameter_group: main_models.DescribeParameterGroupResponseBodyParameterGroup = None,
        request_id: str = None,
    ):
        # The information about the parameter template.
        self.parameter_group = parameter_group
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameter_group:
            self.parameter_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_group is not None:
            result['ParameterGroup'] = self.parameter_group.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterGroup') is not None:
            temp_model = main_models.DescribeParameterGroupResponseBodyParameterGroup()
            self.parameter_group = temp_model.from_map(m.get('ParameterGroup'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterGroupResponseBodyParameterGroup(DaraModel):
    def __init__(
        self,
        category: int = None,
        created: str = None,
        engine: str = None,
        engine_version: str = None,
        modified: str = None,
        param_group_id: str = None,
        param_groups_details: List[main_models.DescribeParameterGroupResponseBodyParameterGroupParamGroupsDetails] = None,
        parameter_group_desc: str = None,
        parameter_group_name: str = None,
    ):
        # The service category. Valid values:
        # 
        # *   **0**: Redis Open-Source Edition
        # *   **1**: Tair (Enterprise Edition)
        self.category = category
        # The time when the parameter template was created.
        self.created = created
        # The engine type. Valid values:
        # 
        # * *redis*: Redis or Tair DRAM-based instance
        # * *tair_pena*: Tair persistent memory-optimized instance
        # * *tair_pdb*: Tair ESSD-based instance
        self.engine = engine
        # The compatible engine version.
        self.engine_version = engine_version
        # The time when the parameter template was last modified.
        self.modified = modified
        # The parameter template ID, which is globally unique.
        self.param_group_id = param_group_id
        # The parameter details of the parameter template.
        self.param_groups_details = param_groups_details
        # The description of the parameter template.
        self.parameter_group_desc = parameter_group_desc
        # The name of the parameter template.
        self.parameter_group_name = parameter_group_name

    def validate(self):
        if self.param_groups_details:
            for v1 in self.param_groups_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.created is not None:
            result['Created'] = self.created

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.modified is not None:
            result['Modified'] = self.modified

        if self.param_group_id is not None:
            result['ParamGroupId'] = self.param_group_id

        result['ParamGroupsDetails'] = []
        if self.param_groups_details is not None:
            for k1 in self.param_groups_details:
                result['ParamGroupsDetails'].append(k1.to_map() if k1 else None)

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('Modified') is not None:
            self.modified = m.get('Modified')

        if m.get('ParamGroupId') is not None:
            self.param_group_id = m.get('ParamGroupId')

        self.param_groups_details = []
        if m.get('ParamGroupsDetails') is not None:
            for k1 in m.get('ParamGroupsDetails'):
                temp_model = main_models.DescribeParameterGroupResponseBodyParameterGroupParamGroupsDetails()
                self.param_groups_details.append(temp_model.from_map(k1))

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        return self

class DescribeParameterGroupResponseBodyParameterGroupParamGroupsDetails(DaraModel):
    def __init__(
        self,
        param_name: str = None,
        param_value: str = None,
    ):
        # The name of the parameter.
        self.param_name = param_name
        # The value of the parameter.
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_value is not None:
            result['ParamValue'] = self.param_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')

        return self

