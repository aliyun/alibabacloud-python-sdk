# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeLakebaseMountParameterGroupsResponseBody(DaraModel):
    def __init__(
        self,
        parameter_groups: List[main_models.DescribeLakebaseMountParameterGroupsResponseBodyParameterGroups] = None,
        request_id: str = None,
    ):
        # The parameter templates.
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
                temp_model = main_models.DescribeLakebaseMountParameterGroupsResponseBodyParameterGroups()
                self.parameter_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLakebaseMountParameterGroupsResponseBodyParameterGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        is_apply: str = None,
        modify_time: str = None,
        parameter_counts: int = None,
        parameter_group_desc: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameter_group_type: str = None,
    ):
        # The creation time in UTC.
        self.create_time = create_time
        # Indicates whether the parameter template is applied. Valid values:
        # - 0: No.
        # - 1: Yes.
        self.is_apply = is_apply
        # The modification time in UTC.
        self.modify_time = modify_time
        # The number of parameters.
        self.parameter_counts = parameter_counts
        # The description of the parameter template.
        self.parameter_group_desc = parameter_group_desc
        # The ID of the parameter template.
        self.parameter_group_id = parameter_group_id
        # The name of the parameter template.
        self.parameter_group_name = parameter_group_name
        # The templatetype. Valid values:
        # - 0: System.
        # - 1: User.
        self.parameter_group_type = parameter_group_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.is_apply is not None:
            result['IsApply'] = self.is_apply

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.parameter_counts is not None:
            result['ParameterCounts'] = self.parameter_counts

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameter_group_type is not None:
            result['ParameterGroupType'] = self.parameter_group_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IsApply') is not None:
            self.is_apply = m.get('IsApply')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ParameterCounts') is not None:
            self.parameter_counts = m.get('ParameterCounts')

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('ParameterGroupType') is not None:
            self.parameter_group_type = m.get('ParameterGroupType')

        return self

