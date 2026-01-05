# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupsResponseBody(DaraModel):
    def __init__(
        self,
        parameter_groups: List[main_models.DescribeParameterGroupsResponseBodyParameterGroups] = None,
        request_id: str = None,
    ):
        # The details of parameter templates.
        self.parameter_groups = parameter_groups
        # The ID of the request.
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
        create_time: str = None,
        dbtype: str = None,
        dbversion: str = None,
        force_restart: str = None,
        parameter_counts: int = None,
        parameter_group_desc: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameter_group_type: str = None,
    ):
        # The time when the parameter template was created. The time is in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.create_time = create_time
        # The type of the engine.
        self.dbtype = dbtype
        # The version of the database engine
        self.dbversion = dbversion
        # Indicates whether to restart the cluster when this parameter template is applied. Valid values:
        # 
        # *   **0**: A restart is not required.
        # *   **1**: A restart is required.
        self.force_restart = force_restart
        # The number of parameters in the parameter template.
        self.parameter_counts = parameter_counts
        # The description of the parameter template.
        self.parameter_group_desc = parameter_group_desc
        # The ID of the parameter template.
        self.parameter_group_id = parameter_group_id
        # The name of the parameter template.
        self.parameter_group_name = parameter_group_name
        # The type of the parameter template. Valid values:
        # 
        # *   **0**: the default parameter template.
        # *   **1**: a custom parameter template.
        # *   **2**: an automatic backup parameter template. After you apply this type of template, the system automatically backs up the original parameter settings and saves the backup as a template.
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

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

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

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

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

