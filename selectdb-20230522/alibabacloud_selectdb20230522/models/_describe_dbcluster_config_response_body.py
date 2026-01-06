# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterConfigResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.DescribeDBClusterConfigResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) authentication failed.
        self.access_denied_detail = access_denied_detail
        # The information returned.
        self.data = data
        # The dynamic code. This parameter is not returned.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not returned.
        self.dynamic_message = dynamic_message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBClusterConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        db_instance_id: str = None,
        db_instance_name: str = None,
        params: List[main_models.DescribeDBClusterConfigResponseBodyDataParams] = None,
        task_id: int = None,
    ):
        # The cluster ID.
        self.db_cluster_id = db_cluster_id
        # The numeric ID of the instance.
        self.db_instance_id = db_instance_id
        # The instance ID.
        self.db_instance_name = db_instance_name
        # The details about each parameter returned.
        self.params = params
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.DescribeDBClusterConfigResponseBodyDataParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeDBClusterConfigResponseBodyDataParams(DaraModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        is_dynamic: int = None,
        is_user_modifiable: int = None,
        name: str = None,
        optional: str = None,
        param_category: str = None,
        value: str = None,
    ):
        # The comments on the parameter.
        self.comment = comment
        # The default value of the parameter.
        self.default_value = default_value
        # Indicates whether the parameter immediately takes effect without requiring a restart.
        self.is_dynamic = is_dynamic
        # Indicates whether the parameter is modifiable.
        self.is_user_modifiable = is_user_modifiable
        # The name of the parameter.
        self.name = name
        # The value range of the parameter.
        self.optional = optional
        # The category of the parameter.
        self.param_category = param_category
        # The current value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.is_dynamic is not None:
            result['IsDynamic'] = self.is_dynamic

        if self.is_user_modifiable is not None:
            result['IsUserModifiable'] = self.is_user_modifiable

        if self.name is not None:
            result['Name'] = self.name

        if self.optional is not None:
            result['Optional'] = self.optional

        if self.param_category is not None:
            result['ParamCategory'] = self.param_category

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('IsDynamic') is not None:
            self.is_dynamic = m.get('IsDynamic')

        if m.get('IsUserModifiable') is not None:
            self.is_user_modifiable = m.get('IsUserModifiable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('ParamCategory') is not None:
            self.param_category = m.get('ParamCategory')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

