# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeLakebaseMountParameterGroupResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        is_apply: int = None,
        modify_time: str = None,
        parameter_detail: List[main_models.DescribeLakebaseMountParameterGroupResponseBodyParameterDetail] = None,
        parameter_group_desc: str = None,
        parameter_group_id: str = None,
        parameter_group_name: str = None,
        parameter_group_type: int = None,
        request_id: str = None,
    ):
        # The creation time in UTC.
        self.create_time = create_time
        # Indicates whether the parameter template is applied. Valid values: 0: No. 1: Yes.
        self.is_apply = is_apply
        # The modification time in UTC.
        self.modify_time = modify_time
        # The details of the parameters in the template. An empty array is returned if no data is available.
        self.parameter_detail = parameter_detail
        # The description of the parameter template.
        self.parameter_group_desc = parameter_group_desc
        # The parameter template ID.
        self.parameter_group_id = parameter_group_id
        # The name of the parameter template.
        self.parameter_group_name = parameter_group_name
        # The parameter templatetype. Valid values: 0: System. 1: User.
        self.parameter_group_type = parameter_group_type
        # The request ID.
        self.request_id = request_id

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.is_apply is not None:
            result['IsApply'] = self.is_apply

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        result['ParameterDetail'] = []
        if self.parameter_detail is not None:
            for k1 in self.parameter_detail:
                result['ParameterDetail'].append(k1.to_map() if k1 else None)

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameter_group_type is not None:
            result['ParameterGroupType'] = self.parameter_group_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IsApply') is not None:
            self.is_apply = m.get('IsApply')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        self.parameter_detail = []
        if m.get('ParameterDetail') is not None:
            for k1 in m.get('ParameterDetail'):
                temp_model = main_models.DescribeLakebaseMountParameterGroupResponseBodyParameterDetail()
                self.parameter_detail.append(temp_model.from_map(k1))

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('ParameterGroupType') is not None:
            self.parameter_group_type = m.get('ParameterGroupType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLakebaseMountParameterGroupResponseBodyParameterDetail(DaraModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The parameter name.
        self.parameter_name = parameter_name
        # The parameter value.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

