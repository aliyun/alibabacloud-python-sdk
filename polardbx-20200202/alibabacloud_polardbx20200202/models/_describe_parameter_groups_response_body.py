# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeParameterGroupsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeParameterGroupsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        parameter_groups: List[main_models.DescribeParameterGroupsResponseBodyDataParameterGroups] = None,
        request_id: str = None,
    ):
        self.parameter_groups = parameter_groups
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
                temp_model = main_models.DescribeParameterGroupsResponseBodyDataParameterGroups()
                self.parameter_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterGroupsResponseBodyDataParameterGroups(DaraModel):
    def __init__(
        self,
        cn_force_restart: bool = None,
        cn_param_count: int = None,
        db_type: str = None,
        db_version: str = None,
        dn_force_restart: bool = None,
        dn_param_count: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameter_group_type: str = None,
        series: str = None,
    ):
        self.cn_force_restart = cn_force_restart
        self.cn_param_count = cn_param_count
        self.db_type = db_type
        self.db_version = db_version
        self.dn_force_restart = dn_force_restart
        self.dn_param_count = dn_param_count
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.parameter_group_id = parameter_group_id
        self.parameter_group_name = parameter_group_name
        self.parameter_group_type = parameter_group_type
        self.series = series

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_force_restart is not None:
            result['CnForceRestart'] = self.cn_force_restart

        if self.cn_param_count is not None:
            result['CnParamCount'] = self.cn_param_count

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.dn_force_restart is not None:
            result['DnForceRestart'] = self.dn_force_restart

        if self.dn_param_count is not None:
            result['DnParamCount'] = self.dn_param_count

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameter_group_type is not None:
            result['ParameterGroupType'] = self.parameter_group_type

        if self.series is not None:
            result['Series'] = self.series

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnForceRestart') is not None:
            self.cn_force_restart = m.get('CnForceRestart')

        if m.get('CnParamCount') is not None:
            self.cn_param_count = m.get('CnParamCount')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('DnForceRestart') is not None:
            self.dn_force_restart = m.get('DnForceRestart')

        if m.get('DnParamCount') is not None:
            self.dn_param_count = m.get('DnParamCount')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('ParameterGroupType') is not None:
            self.parameter_group_type = m.get('ParameterGroupType')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        return self

