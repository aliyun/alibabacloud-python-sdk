# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateHttpApiOperationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateHttpApiOperationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Operation information.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.CreateHttpApiOperationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateHttpApiOperationResponseBodyData(DaraModel):
    def __init__(
        self,
        operations: List[main_models.CreateHttpApiOperationResponseBodyDataOperations] = None,
    ):
        # Operation information.
        self.operations = operations

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['operations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operations = []
        if m.get('operations') is not None:
            for k1 in m.get('operations'):
                temp_model = main_models.CreateHttpApiOperationResponseBodyDataOperations()
                self.operations.append(temp_model.from_map(k1))

        return self

class CreateHttpApiOperationResponseBodyDataOperations(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
    ):
        # Operation ID.
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        return self

