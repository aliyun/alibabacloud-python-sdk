# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeModifyParameterLogResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        items: List[main_models.DescribeModifyParameterLogResponseBodyItems] = None,
        request_id: str = None,
    ):
        self.engine = engine
        self.engine_version = engine_version
        self.items = items
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeModifyParameterLogResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeModifyParameterLogResponseBodyItems(DaraModel):
    def __init__(
        self,
        modify_time: str = None,
        new_parameter_value: str = None,
        old_parameter_value: str = None,
        parameter_name: str = None,
        status: str = None,
    ):
        self.modify_time = modify_time
        self.new_parameter_value = new_parameter_value
        self.old_parameter_value = old_parameter_value
        self.parameter_name = parameter_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.new_parameter_value is not None:
            result['NewParameterValue'] = self.new_parameter_value

        if self.old_parameter_value is not None:
            result['OldParameterValue'] = self.old_parameter_value

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NewParameterValue') is not None:
            self.new_parameter_value = m.get('NewParameterValue')

        if m.get('OldParameterValue') is not None:
            self.old_parameter_value = m.get('OldParameterValue')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

