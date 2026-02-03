# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupsResponseBody(DaraModel):
    def __init__(
        self,
        parameter_groups: List[main_models.DescribeParameterGroupsResponseBodyParameterGroups] = None,
        request_id: str = None,
    ):
        # The list of parameter templates.
        self.parameter_groups = parameter_groups
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameter_groups:
            for v1 in self.parameter_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ParameterGroups'] = []
        if self.parameter_groups is not None:
            for k1 in self.parameter_groups:
                result['ParameterGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_groups = []
        if m.get('ParameterGroups') is not None:
            for k1 in m.get('ParameterGroups'):
                temp_model = main_models.DescribeParameterGroupsResponseBodyParameterGroups()
                self.parameter_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterGroupsResponseBodyParameterGroups(DaraModel):
    def __init__(
        self,
        category: int = None,
        created: str = None,
        engine: str = None,
        engine_version: str = None,
        modified: str = None,
        param_group_id: str = None,
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
        # *   **redis**: Redis Open-Source Edition or Tair (In-Memory)
        # *   **tair_pena**: Tair (On NVM)
        # *   **tair_pdb**: Tair (On Disk)
        self.engine = engine
        # The compatible engine version.
        self.engine_version = engine_version
        # The time when the parameter template was last modified.
        self.modified = modified
        # The parameter template ID.
        self.param_group_id = param_group_id
        # The description of the parameter template.
        self.parameter_group_desc = parameter_group_desc
        # The name of the parameter template.
        self.parameter_group_name = parameter_group_name

    def validate(self):
        pass

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

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        return self

