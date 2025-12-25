# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceConfigResponseBodyData = None,
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
            temp_model = main_models.DescribeDBInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        params: List[main_models.DescribeDBInstanceConfigResponseBodyDataParams] = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.params = params

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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.DescribeDBInstanceConfigResponseBodyDataParams()
                self.params.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceConfigResponseBodyDataParams(DaraModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        is_dynamic: int = None,
        is_user_modifiable: int = None,
        name: str = None,
        optional: str = None,
        param_rely_rule: str = None,
        value: str = None,
    ):
        self.comment = comment
        self.default_value = default_value
        self.is_dynamic = is_dynamic
        self.is_user_modifiable = is_user_modifiable
        self.name = name
        self.optional = optional
        self.param_rely_rule = param_rely_rule
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

        if self.param_rely_rule is not None:
            result['ParamRelyRule'] = self.param_rely_rule

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

        if m.get('ParamRelyRule') is not None:
            self.param_rely_rule = m.get('ParamRelyRule')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

