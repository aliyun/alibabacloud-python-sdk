# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAnalysisColumnListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeAnalysisColumnListResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returned object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeAnalysisColumnListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeAnalysisColumnListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
        is_default: bool = None,
        variable_name: str = None,
        variable_title: str = None,
        variable_type: str = None,
    ):
        # Event code
        self.event_code = event_code
        # Event name.
        self.event_name = event_name
        # Whether it is a default column.
        self.is_default = is_default
        # Variable name.
        self.variable_name = variable_name
        # Variable title.
        self.variable_title = variable_title
        # Variable type.
        self.variable_type = variable_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.event_name is not None:
            result['eventName'] = self.event_name

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.variable_name is not None:
            result['variableName'] = self.variable_name

        if self.variable_title is not None:
            result['variableTitle'] = self.variable_title

        if self.variable_type is not None:
            result['variableType'] = self.variable_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('variableName') is not None:
            self.variable_name = m.get('variableName')

        if m.get('variableTitle') is not None:
            self.variable_title = m.get('variableTitle')

        if m.get('variableType') is not None:
            self.variable_type = m.get('variableType')

        return self

