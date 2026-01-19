# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class ModifyCustVariableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.ModifyCustVariableResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
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
                temp_model = main_models.ModifyCustVariableResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class ModifyCustVariableResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        fail_type: str = None,
        message: str = None,
        success: bool = None,
    ):
        # Failure type
        self.fail_type = fail_type
        # Detailed information.
        self.message = message
        # Whether the operation was successful
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_type is not None:
            result['failType'] = self.fail_type

        if self.message is not None:
            result['message'] = self.message

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failType') is not None:
            self.fail_type = m.get('failType')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

