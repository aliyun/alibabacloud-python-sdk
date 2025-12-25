# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupResponseBody(DaraModel):
    def __init__(
        self,
        param_group: main_models.DescribeParameterGroupResponseBodyParamGroup = None,
        related_custins_info: main_models.DescribeParameterGroupResponseBodyRelatedCustinsInfo = None,
        request_id: str = None,
    ):
        # The information about the parameter template.
        self.param_group = param_group
        # The information about the instance to which the parameter template is applied.
        # 
        # >  This parameter is available only for ApsaraDB RDS for PostgreSQL instances.
        self.related_custins_info = related_custins_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.param_group:
            self.param_group.validate()
        if self.related_custins_info:
            self.related_custins_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_group is not None:
            result['ParamGroup'] = self.param_group.to_map()

        if self.related_custins_info is not None:
            result['RelatedCustinsInfo'] = self.related_custins_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamGroup') is not None:
            temp_model = main_models.DescribeParameterGroupResponseBodyParamGroup()
            self.param_group = temp_model.from_map(m.get('ParamGroup'))

        if m.get('RelatedCustinsInfo') is not None:
            temp_model = main_models.DescribeParameterGroupResponseBodyRelatedCustinsInfo()
            self.related_custins_info = temp_model.from_map(m.get('RelatedCustinsInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterGroupResponseBodyRelatedCustinsInfo(DaraModel):
    def __init__(
        self,
        related_custins_info: List[main_models.DescribeParameterGroupResponseBodyRelatedCustinsInfoRelatedCustinsInfo] = None,
    ):
        self.related_custins_info = related_custins_info

    def validate(self):
        if self.related_custins_info:
            for v1 in self.related_custins_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RelatedCustinsInfo'] = []
        if self.related_custins_info is not None:
            for k1 in self.related_custins_info:
                result['RelatedCustinsInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_custins_info = []
        if m.get('RelatedCustinsInfo') is not None:
            for k1 in m.get('RelatedCustinsInfo'):
                temp_model = main_models.DescribeParameterGroupResponseBodyRelatedCustinsInfoRelatedCustinsInfo()
                self.related_custins_info.append(temp_model.from_map(k1))

        return self

class DescribeParameterGroupResponseBodyRelatedCustinsInfoRelatedCustinsInfo(DaraModel):
    def __init__(
        self,
        applied_time: str = None,
        dbinstance_name: str = None,
    ):
        # The time when the parameter template was applied.
        self.applied_time = applied_time
        # The instance ID.
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_time is not None:
            result['AppliedTime'] = self.applied_time

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedTime') is not None:
            self.applied_time = m.get('AppliedTime')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        return self

class DescribeParameterGroupResponseBodyParamGroup(DaraModel):
    def __init__(
        self,
        parameter_group: List[main_models.DescribeParameterGroupResponseBodyParamGroupParameterGroup] = None,
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
                temp_model = main_models.DescribeParameterGroupResponseBodyParamGroupParameterGroup()
                self.parameter_group.append(temp_model.from_map(k1))

        return self

class DescribeParameterGroupResponseBodyParamGroupParameterGroup(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        engine: str = None,
        engine_version: str = None,
        force_restart: int = None,
        param_counts: int = None,
        param_detail: main_models.DescribeParameterGroupResponseBodyParamGroupParameterGroupParamDetail = None,
        parameter_group_desc: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameter_group_type: int = None,
        update_time: str = None,
    ):
        # The time when the parameter template was created.
        self.create_time = create_time
        # The database engine of the instance.
        self.engine = engine
        # The database engine version of the instance.
        self.engine_version = engine_version
        # Indicates whether the restart of an instance is required for the parameter template to take effect. Valid values:
        # 
        # *   **0**: A restart is not required.
        # *   **1**: A restart is required.
        self.force_restart = force_restart
        # The number of parameters in the parameter template.
        self.param_counts = param_counts
        # The details of the parameters.
        self.param_detail = param_detail
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
        # The time when the parameter template was last updated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        if self.param_detail:
            self.param_detail.validate()

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

        if self.param_detail is not None:
            result['ParamDetail'] = self.param_detail.to_map()

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

        if m.get('ParamDetail') is not None:
            temp_model = main_models.DescribeParameterGroupResponseBodyParamGroupParameterGroupParamDetail()
            self.param_detail = temp_model.from_map(m.get('ParamDetail'))

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

class DescribeParameterGroupResponseBodyParamGroupParameterGroupParamDetail(DaraModel):
    def __init__(
        self,
        parameter_detail: List[main_models.DescribeParameterGroupResponseBodyParamGroupParameterGroupParamDetailParameterDetail] = None,
    ):
        self.parameter_detail = parameter_detail

    def validate(self):
        if self.parameter_detail:
            for v1 in self.parameter_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ParameterDetail'] = []
        if self.parameter_detail is not None:
            for k1 in self.parameter_detail:
                result['ParameterDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_detail = []
        if m.get('ParameterDetail') is not None:
            for k1 in m.get('ParameterDetail'):
                temp_model = main_models.DescribeParameterGroupResponseBodyParamGroupParameterGroupParamDetailParameterDetail()
                self.parameter_detail.append(temp_model.from_map(k1))

        return self

class DescribeParameterGroupResponseBodyParamGroupParameterGroupParamDetailParameterDetail(DaraModel):
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

