# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class GetFunctionDefaultInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        function_name: str = None,
        http_code: int = None,
        instance_name: str = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetFunctionDefaultInstanceResponseBodyResult = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The name of the feature.
        self.function_name = function_name
        # The HTTP status code.
        self.http_code = http_code
        # The name of the instance.
        self.instance_name = instance_name
        # The default running time.
        self.latency = latency
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result of the request.
        self.result = result
        # The status of the request.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.latency is not None:
            result['Latency'] = self.latency

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Latency') is not None:
            self.latency = m.get('Latency')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetFunctionDefaultInstanceResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetFunctionDefaultInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        # The default instance name.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

