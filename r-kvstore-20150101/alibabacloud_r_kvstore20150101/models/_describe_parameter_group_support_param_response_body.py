# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupSupportParamResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_list: List[main_models.DescribeParameterGroupSupportParamResponseBodyResourceList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The parameters.
        self.resource_list = resource_list

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.DescribeParameterGroupSupportParamResponseBodyResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        return self

class DescribeParameterGroupSupportParamResponseBodyResourceList(DaraModel):
    def __init__(
        self,
        category: str = None,
        db_type: str = None,
        db_version: str = None,
        param_name: str = None,
    ):
        # The service category.
        self.category = category
        # The engine type.
        self.db_type = db_type
        # The engine version.
        self.db_version = db_version
        # The name of the parameter.
        self.param_name = param_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        return self

